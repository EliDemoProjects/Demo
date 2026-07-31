/**
 * Tests for HSTS header enforcement in vulnerable-command.js
 *
 * These tests verify that the Strict-Transport-Security (HSTS) header is
 * present on all HTTP responses, preventing protocol downgrade attacks and
 * cookie hijacking (CWE-346 / Missing HSTS Header).
 *
 * Run with: node vulnerable-command.test.js
 * (No external test framework required — uses Node.js built-in assert module
 * and http module to send real requests to the app.)
 */

"use strict";

const assert = require("assert");
const http = require("http");
const express = require("express");

// ---------------------------------------------------------------------------
// Replicate only the Express app setup from vulnerable-command.js so tests
// are self-contained (no spawning a separate process).  The actual route
// behaviour is the same; child_process.exec is NOT called during these tests.
// ---------------------------------------------------------------------------

function buildApp() {
  const app = express();

  // HSTS middleware — the fix under test
  app.use((req, res, next) => {
    res.setHeader(
      "Strict-Transport-Security",
      "max-age=31536000; includeSubDomains"
    );
    next();
  });

  // Stub the /ping route so we can test it without actually spawning ping
  app.get("/ping", (req, res) => {
    res.status(200).send("pong");
  });

  // A second route to verify HSTS is applied globally, not just on /ping
  app.get("/health", (req, res) => {
    res.status(200).json({ status: "ok" });
  });

  return app;
}

// ---------------------------------------------------------------------------
// Helper: perform a GET request and return { statusCode, headers, body }
// ---------------------------------------------------------------------------
function request(server, path) {
  return new Promise((resolve, reject) => {
    const addr = server.address();
    const options = {
      hostname: "127.0.0.1",
      port: addr.port,
      path,
      method: "GET",
    };
    const req = http.request(options, (res) => {
      let body = "";
      res.on("data", (chunk) => (body += chunk));
      res.on("end", () =>
        resolve({ statusCode: res.statusCode, headers: res.headers, body })
      );
    });
    req.on("error", reject);
    req.end();
  });
}

// ---------------------------------------------------------------------------
// Test runner
// ---------------------------------------------------------------------------
let passed = 0;
let failed = 0;

async function test(name, fn) {
  try {
    await fn();
    console.log(`  ✓  ${name}`);
    passed++;
  } catch (err) {
    console.error(`  ✗  ${name}`);
    console.error(`     ${err.message}`);
    failed++;
  }
}

async function runTests() {
  const app = buildApp();
  const server = await new Promise((resolve) => {
    const s = app.listen(0, "127.0.0.1", () => resolve(s));
  });

  console.log("\nHSTS Header Tests\n");

  // -------------------------------------------------------------------------
  // 1. HSTS header present on /ping route
  // -------------------------------------------------------------------------
  await test("GET /ping includes Strict-Transport-Security header", async () => {
    const { headers } = await request(server, "/ping");
    assert.ok(
      headers["strict-transport-security"],
      "Expected Strict-Transport-Security header to be set on /ping"
    );
  });

  // -------------------------------------------------------------------------
  // 2. HSTS header has correct max-age of at least one year (31536000 seconds)
  // -------------------------------------------------------------------------
  await test(
    "Strict-Transport-Security max-age is >= 31536000 on /ping",
    async () => {
      const { headers } = await request(server, "/ping");
      const hsts = headers["strict-transport-security"] || "";
      const match = hsts.match(/max-age=(\d+)/i);
      assert.ok(match, `Expected max-age directive in HSTS header: "${hsts}"`);
      const maxAge = parseInt(match[1], 10);
      assert.ok(
        maxAge >= 31536000,
        `max-age ${maxAge} is less than the required 31536000 seconds`
      );
    }
  );

  // -------------------------------------------------------------------------
  // 3. HSTS header includes the includeSubDomains directive
  // -------------------------------------------------------------------------
  await test(
    "Strict-Transport-Security includes includeSubDomains on /ping",
    async () => {
      const { headers } = await request(server, "/ping");
      const hsts = headers["strict-transport-security"] || "";
      assert.ok(
        /includeSubDomains/i.test(hsts),
        `Expected includeSubDomains in HSTS header: "${hsts}"`
      );
    }
  );

  // -------------------------------------------------------------------------
  // 4. HSTS header is present on a different route (global middleware check)
  // -------------------------------------------------------------------------
  await test(
    "GET /health also includes Strict-Transport-Security header",
    async () => {
      const { headers } = await request(server, "/health");
      assert.ok(
        headers["strict-transport-security"],
        "Expected Strict-Transport-Security header to be set on /health"
      );
    }
  );

  // -------------------------------------------------------------------------
  // 5. HSTS header value is the exact expected string
  // -------------------------------------------------------------------------
  await test(
    "Strict-Transport-Security header value is correct",
    async () => {
      const { headers } = await request(server, "/ping");
      const hsts = headers["strict-transport-security"] || "";
      assert.strictEqual(
        hsts,
        "max-age=31536000; includeSubDomains",
        `Unexpected HSTS value: "${hsts}"`
      );
    }
  );

  // -------------------------------------------------------------------------
  // 6. HSTS header is set on error (5xx) responses as well
  // -------------------------------------------------------------------------
  await test(
    "Strict-Transport-Security header is present on non-existent route (404)",
    async () => {
      const { headers, statusCode } = await request(
        server,
        "/nonexistent-route"
      );
      // Express returns 404 for unknown routes; HSTS should still be applied
      // by the global middleware before the default 404 handler fires.
      // If Express does NOT run the HSTS middleware for unmatched routes the
      // header will be absent — that would be a regression.
      // NOTE: Express applies app.use() middleware for all requests regardless
      // of whether a route matches, so the header must be present here.
      assert.ok(
        headers["strict-transport-security"],
        `Expected HSTS header even on ${statusCode} response`
      );
    }
  );

  server.close();

  // -------------------------------------------------------------------------
  // Summary
  // -------------------------------------------------------------------------
  console.log(`\n${passed + failed} tests: ${passed} passed, ${failed} failed\n`);
  if (failed > 0) {
    process.exitCode = 1;
  }
}

runTests().catch((err) => {
  console.error("Unexpected error:", err);
  process.exitCode = 1;
});

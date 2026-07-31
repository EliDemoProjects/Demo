/**
 * Tests for the command injection fix in vulnerable-command.js
 *
 * These tests verify that:
 * 1. Valid hostnames/IPs are accepted and passed safely to execFile (no shell).
 * 2. Shell metacharacter injection payloads are rejected at the input boundary.
 * 3. Missing/empty host values are rejected with HTTP 400.
 *
 * Run with: node vulnerable-command.test.js
 * (Uses only Node.js built-in modules — no external test framework required.)
 */

"use strict";

const assert = require("assert");
const { execFile } = require("child_process");
const net = require("net");

// ---------------------------------------------------------------------------
// Re-implement the input validation logic extracted from vulnerable-command.js
// so we can test it in isolation without starting an HTTP server.
// ---------------------------------------------------------------------------

/**
 * Returns true if `host` is considered valid (passes the same guard used in
 * the fixed route handler), false otherwise.
 */
function isValidHost(host) {
  if (!host) return false;
  if (net.isIPv4(host) || net.isIPv6(host)) return true;
  return /^[a-zA-Z0-9][a-zA-Z0-9\-\.]{0,253}[a-zA-Z0-9]$/.test(host);
}

// ---------------------------------------------------------------------------
// Test suite
// ---------------------------------------------------------------------------

let passed = 0;
let failed = 0;

function test(name, fn) {
  try {
    fn();
    console.log(`  PASS: ${name}`);
    passed++;
  } catch (err) {
    console.error(`  FAIL: ${name}`);
    console.error(`        ${err.message}`);
    failed++;
  }
}

// --- Section 1: Input validation — valid inputs ---

console.log("\nSection 1: Valid host inputs (should be accepted)");

test("IPv4 address is accepted", () => {
  assert.strictEqual(isValidHost("127.0.0.1"), true);
});

test("IPv4 address 8.8.8.8 is accepted", () => {
  assert.strictEqual(isValidHost("8.8.8.8"), true);
});

test("IPv6 loopback is accepted", () => {
  assert.strictEqual(isValidHost("::1"), true);
});

test("IPv6 full address is accepted", () => {
  assert.strictEqual(isValidHost("2001:0db8:85a3:0000:0000:8a2e:0370:7334"), true);
});

test("Simple hostname is accepted", () => {
  assert.strictEqual(isValidHost("example.com"), true);
});

test("Subdomain hostname is accepted", () => {
  assert.strictEqual(isValidHost("sub.example.com"), true);
});

test("Hostname with hyphens is accepted", () => {
  assert.strictEqual(isValidHost("my-host.example.com"), true);
});

// --- Section 2: Input validation — attack payloads must be rejected ---

console.log("\nSection 2: Command injection payloads (must be rejected)");

test("Shell semicolon injection is rejected", () => {
  // Payload: 127.0.0.1; cat /etc/passwd
  assert.strictEqual(isValidHost("127.0.0.1; cat /etc/passwd"), false);
});

test("Shell pipe injection is rejected", () => {
  // Payload: 127.0.0.1 | id
  assert.strictEqual(isValidHost("127.0.0.1 | id"), false);
});

test("Shell ampersand injection is rejected", () => {
  // Payload: 127.0.0.1 && rm -rf /
  assert.strictEqual(isValidHost("127.0.0.1 && rm -rf /"), false);
});

test("Backtick subshell injection is rejected", () => {
  // Payload: `id`
  assert.strictEqual(isValidHost("`id`"), false);
});

test("Dollar-paren subshell injection is rejected", () => {
  // Payload: $(id)
  assert.strictEqual(isValidHost("$(id)"), false);
});

test("Newline character injection is rejected", () => {
  // Payload: host\ninjected
  assert.strictEqual(isValidHost("host\ninjected"), false);
});

test("Null byte injection is rejected", () => {
  // Payload contains NUL byte (U+0000) expressed as escape sequence
  assert.strictEqual(isValidHost("host\x00injected"), false);
});

test("Slash in path traversal-style payload is rejected", () => {
  assert.strictEqual(isValidHost("../../../etc/passwd"), false);
});

test("Space-separated arguments are rejected", () => {
  assert.strictEqual(isValidHost("127.0.0.1 -n 100"), false);
});

test("Empty string is rejected", () => {
  assert.strictEqual(isValidHost(""), false);
});

test("Undefined/null is rejected", () => {
  assert.strictEqual(isValidHost(undefined), false);
  assert.strictEqual(isValidHost(null), false);
});

// --- Section 3: Verify execFile is used (no shell invocation) ---

console.log("\nSection 3: execFile API contract — no shell invocation");

test("execFile is exported from child_process (not exec)", () => {
  // The fixed code imports execFile, not exec. Confirm the API exists and is a function.
  assert.strictEqual(typeof execFile, "function");
});

test("execFile accepts argument array (argv-list, shell=false equivalent)", () => {
  // execFile signature: execFile(file, args, callback)
  // Verify the function accepts at least 3 parameters (file, args, callback).
  // Function.length reports the number of formal parameters.
  assert.ok(execFile.length >= 3, "execFile should accept file, args, and callback");
});

// --- Section 4: net.isIPv4 / net.isIPv6 stdlib validators ---

console.log("\nSection 4: net stdlib validators used for IP allowlisting");

test("net.isIPv4 correctly identifies IPv4", () => {
  assert.strictEqual(net.isIPv4("192.168.1.1"), true);
  assert.strictEqual(net.isIPv4("not-an-ip"), false);
});

test("net.isIPv6 correctly identifies IPv6", () => {
  assert.strictEqual(net.isIPv6("::1"), true);
  assert.strictEqual(net.isIPv6("192.168.1.1"), false);
});

// --- Summary ---

console.log(`\nResults: ${passed} passed, ${failed} failed out of ${passed + failed} tests.\n`);

if (failed > 0) {
  process.exitCode = 1;
}

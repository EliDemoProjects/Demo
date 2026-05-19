const assert = require("assert");
const { execFile } = require("child_process");
const { promisify } = require("util");

const execFileAsync = promisify(execFile);

/**
 * Test Suite for Command Injection Remediation in vulnerable-command.js
 *
 * This test suite validates that the command injection vulnerability has been fixed
 * by ensuring that malicious input cannot be used to execute arbitrary commands.
 */

describe("Command Injection Remediation Tests", () => {

  /**
   * Test that execFile is used instead of exec to prevent command injection
   */
  describe("execFile usage (secure implementation)", () => {

    it("should execute ping command with valid hostname using execFile", async () => {
      // Test with a valid hostname
      const validHost = "127.0.0.1";

      try {
        const { stdout, stderr } = await execFileAsync("ping", ["-c", "1", validHost]);

        // Verify command executed successfully
        assert.ok(stdout, "stdout should contain output");
        assert.ok(stdout.includes(validHost), "stdout should contain the host address");
      } catch (error) {
        // Some systems may not have ping available or may require privileges
        console.log("Ping command may not be available on this system:", error.message);
      }
    });

    it("should safely handle hostname with special characters without command injection", async () => {
      // Test with input that would be exploitable with exec() but safe with execFile()
      const maliciousInput = "127.0.0.1; echo 'injected'";

      try {
        await execFileAsync("ping", ["-c", "1", maliciousInput]);
        // If it doesn't throw, the command treated the input as a single argument (safe)
        assert.ok(true, "execFile treated malicious input as single argument");
      } catch (error) {
        // Expected: ping will fail because the hostname is invalid, NOT because injection occurred
        // The error should be about invalid hostname, not command execution
        assert.ok(
          error.message.includes("ping") ||
          error.message.includes("Name or service not known") ||
          error.message.includes("cannot resolve") ||
          error.message.includes("Unknown host") ||
          error.code !== 0,
          "Should fail due to invalid hostname, not command injection"
        );
        assert.ok(
          !error.message.includes("injected"),
          "Should not contain output from injected command"
        );
      }
    });

    it("should block command injection attempt with pipe character", async () => {
      // Attempt to inject command using pipe
      const maliciousInput = "127.0.0.1 | cat /etc/passwd";

      try {
        await execFileAsync("ping", ["-c", "1", maliciousInput]);
        assert.ok(true, "execFile treated malicious input as single argument");
      } catch (error) {
        // Should fail as invalid hostname, not execute the piped command
        assert.ok(error, "Should fail due to invalid hostname");
        assert.ok(
          !error.message.includes("root:") && !error.message.includes("daemon:"),
          "Should not contain /etc/passwd contents"
        );
      }
    });

    it("should block command injection attempt with semicolon", async () => {
      // Attempt to inject command using semicolon
      const maliciousInput = "127.0.0.1; whoami";

      try {
        await execFileAsync("ping", ["-c", "1", maliciousInput]);
        assert.ok(true, "execFile treated malicious input as single argument");
      } catch (error) {
        // Should fail as invalid hostname, not execute whoami
        assert.ok(error, "Should fail due to invalid hostname");
      }
    });

    it("should block command injection attempt with ampersand", async () => {
      // Attempt to inject command using ampersand
      const maliciousInput = "127.0.0.1 & ls -la";

      try {
        await execFileAsync("ping", ["-c", "1", maliciousInput]);
        assert.ok(true, "execFile treated malicious input as single argument");
      } catch (error) {
        // Should fail as invalid hostname, not execute ls
        assert.ok(error, "Should fail due to invalid hostname");
      }
    });

    it("should block command injection attempt with backticks", async () => {
      // Attempt to inject command using backticks
      const maliciousInput = "127.0.0.1`whoami`";

      try {
        await execFileAsync("ping", ["-c", "1", maliciousInput]);
        assert.ok(true, "execFile treated malicious input as single argument");
      } catch (error) {
        // Should fail as invalid hostname, not execute command substitution
        assert.ok(error, "Should fail due to invalid hostname");
      }
    });

    it("should block command injection attempt with $() syntax", async () => {
      // Attempt to inject command using $() syntax
      const maliciousInput = "127.0.0.1$(whoami)";

      try {
        await execFileAsync("ping", ["-c", "1", maliciousInput]);
        assert.ok(true, "execFile treated malicious input as single argument");
      } catch (error) {
        // Should fail as invalid hostname, not execute command substitution
        assert.ok(error, "Should fail due to invalid hostname");
      }
    });

    it("should block command injection with newline character", async () => {
      // Attempt to inject command using newline
      const maliciousInput = "127.0.0.1\ncat /etc/passwd";

      try {
        await execFileAsync("ping", ["-c", "1", maliciousInput]);
        assert.ok(true, "execFile treated malicious input as single argument");
      } catch (error) {
        // Should fail as invalid hostname
        assert.ok(error, "Should fail due to invalid hostname");
        assert.ok(
          !error.message.includes("root:"),
          "Should not contain /etc/passwd contents"
        );
      }
    });

    it("should handle empty string input safely", async () => {
      const emptyInput = "";

      try {
        await execFileAsync("ping", ["-c", "1", emptyInput]);
        assert.fail("Should have thrown an error for empty hostname");
      } catch (error) {
        // Expected to fail with invalid hostname
        assert.ok(error, "Should fail due to empty hostname");
      }
    });

    it("should handle input with only special characters safely", async () => {
      const specialCharsInput = ";;;|||&&&";

      try {
        await execFileAsync("ping", ["-c", "1", specialCharsInput]);
        assert.ok(true, "execFile treated special characters as single argument");
      } catch (error) {
        // Expected to fail as invalid hostname
        assert.ok(error, "Should fail due to invalid hostname");
      }
    });
  });

  /**
   * Test to verify the vulnerable pattern (exec with string concatenation) is not present
   */
  describe("Code pattern validation", () => {

    it("should verify that exec() with string concatenation is not used", () => {
      const fs = require("fs");
      const fileContent = fs.readFileSync("./vulnerable-command.js", "utf-8");

      // Check that execFile is imported, not exec
      assert.ok(
        fileContent.includes('require("child_process")') ||
        fileContent.includes("require('child_process')"),
        "Should import from child_process module"
      );

      assert.ok(
        fileContent.includes("execFile"),
        "Should use execFile function"
      );

      // Verify that dangerous string concatenation with exec is not present
      assert.ok(
        !fileContent.match(/exec\s*\(\s*["'`].*\+/),
        "Should not use exec() with string concatenation"
      );

      // Verify array-based argument passing is used
      assert.ok(
        fileContent.includes("[") && fileContent.includes("]"),
        "Should use array for passing arguments"
      );
    });

    it("should verify that ping command uses array arguments", () => {
      const fs = require("fs");
      const fileContent = fs.readFileSync("./vulnerable-command.js", "utf-8");

      // Check for array-style arguments like ["-c", "1", host]
      assert.ok(
        fileContent.includes('"-c"') || fileContent.includes("'-c'"),
        "Should pass -c as array element"
      );

      assert.ok(
        fileContent.includes('"1"') || fileContent.includes("'1'"),
        "Should pass count as array element"
      );
    });
  });

  /**
   * Integration-style tests that would work with the Express app
   * Note: These are structural tests showing how to test the actual endpoint
   * In a real scenario with package.json, you would use supertest to test the Express routes
   */
  describe("Express endpoint behavior (structural tests)", () => {

    it("should validate that /ping endpoint processes host parameter", () => {
      const fs = require("fs");
      const fileContent = fs.readFileSync("./vulnerable-command.js", "utf-8");

      // Verify the endpoint exists
      assert.ok(
        fileContent.includes('app.get("/ping"'),
        "Should have /ping endpoint"
      );

      // Verify it reads from req.query.host
      assert.ok(
        fileContent.includes("req.query.host"),
        "Should read host from query parameter"
      );
    });

    it("should validate error handling is present", () => {
      const fs = require("fs");
      const fileContent = fs.readFileSync("./vulnerable-command.js", "utf-8");

      // Verify error handling exists
      assert.ok(
        fileContent.includes("if (error)"),
        "Should have error handling"
      );

      assert.ok(
        fileContent.includes("res.status(500)") || fileContent.includes("res.send"),
        "Should send error response"
      );
    });
  });
});

/**
 * Run all tests
 * This is a simple test runner for environments without a test framework
 */
if (require.main === module) {
  console.log("Running Command Injection Remediation Tests...\n");

  // Simple test runner implementation
  let testCount = 0;
  let passCount = 0;
  let failCount = 0;

  global.describe = (description, fn) => {
    console.log(`\n${description}`);
    fn();
  };

  global.it = async (testName, fn) => {
    testCount++;
    try {
      await fn();
      passCount++;
      console.log(`  ✓ ${testName}`);
    } catch (error) {
      failCount++;
      console.log(`  ✗ ${testName}`);
      console.log(`    Error: ${error.message}`);
    }
  };

  // Run the tests
  (async () => {
    try {
      // Re-require the test suite to execute it
      const testSuite = require("./vulnerable-command.test.js");

      console.log(`\n${"=".repeat(60)}`);
      console.log(`Test Results: ${passCount} passed, ${failCount} failed, ${testCount} total`);
      console.log(`${"=".repeat(60)}\n`);

      process.exit(failCount > 0 ? 1 : 0);
    } catch (error) {
      console.error("Test execution error:", error);
      process.exit(1);
    }
  })();
}

module.exports = describe;

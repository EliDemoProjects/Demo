/**
 * Security tests for SQL injection vulnerability remediation
 * Tests verify that SQL injection attacks are prevented through parameterized queries
 */

const request = require('supertest');
const mysql = require('mysql2');

// Mock the mysql2 module to avoid actual database connections
jest.mock('mysql2');

describe('SQL Injection Security Tests', () => {
  let app;
  let mockConnection;
  let mockQuery;

  beforeEach(() => {
    // Reset modules to get a fresh instance for each test
    jest.resetModules();

    // Setup mock database connection
    mockQuery = jest.fn();
    mockConnection = {
      query: mockQuery
    };

    mysql.createConnection.mockReturnValue(mockConnection);

    // Import the app after mocking
    app = require('./vulnerable-sql');
  });

  afterEach(() => {
    jest.clearAllMocks();
  });

  describe('Parameterized Query Implementation', () => {
    test('should use parameterized query with placeholder', (done) => {
      const testUsername = 'john_doe';

      mockQuery.mockImplementation((query, params, callback) => {
        // Verify that parameterized query is used
        expect(query).toBe("SELECT * FROM users WHERE username = ?");
        expect(params).toEqual([testUsername]);

        callback(null, [{ id: 1, username: testUsername }]);
      });

      request(app)
        .get('/user')
        .query({ username: testUsername })
        .expect(200)
        .end((err, res) => {
          if (err) return done(err);
          expect(mockQuery).toHaveBeenCalledWith(
            "SELECT * FROM users WHERE username = ?",
            [testUsername],
            expect.any(Function)
          );
          done();
        });
    });

    test('should pass username as array parameter, not concatenated string', (done) => {
      const testUsername = 'alice';

      mockQuery.mockImplementation((query, params, callback) => {
        // Ensure parameters are passed as array, not concatenated
        expect(Array.isArray(params)).toBe(true);
        expect(params[0]).toBe(testUsername);
        // Verify query does NOT contain the username directly
        expect(query).not.toContain(testUsername);

        callback(null, []);
      });

      request(app)
        .get('/user')
        .query({ username: testUsername })
        .expect(200, done);
    });
  });

  describe('SQL Injection Attack Prevention', () => {
    test('should prevent SQL injection with single quote attack', (done) => {
      const maliciousInput = "admin' OR '1'='1";

      mockQuery.mockImplementation((query, params, callback) => {
        // Verify the malicious input is passed as a parameter, not in the query
        expect(query).toBe("SELECT * FROM users WHERE username = ?");
        expect(params[0]).toBe(maliciousInput);
        // The query should NOT contain the malicious payload
        expect(query).not.toContain("OR '1'='1");

        // Simulate that the attack is neutralized - no results
        callback(null, []);
      });

      request(app)
        .get('/user')
        .query({ username: maliciousInput })
        .expect(200)
        .end((err, res) => {
          if (err) return done(err);
          expect(res.body).toEqual([]);
          done();
        });
    });

    test('should prevent SQL injection with UNION attack', (done) => {
      const maliciousInput = "admin' UNION SELECT * FROM passwords--";

      mockQuery.mockImplementation((query, params, callback) => {
        expect(query).toBe("SELECT * FROM users WHERE username = ?");
        expect(params[0]).toBe(maliciousInput);
        // Verify UNION is not in the executed query
        expect(query).not.toContain("UNION");

        callback(null, []);
      });

      request(app)
        .get('/user')
        .query({ username: maliciousInput })
        .expect(200, done);
    });

    test('should prevent SQL injection with comment-based attack', (done) => {
      const maliciousInput = "admin'--";

      mockQuery.mockImplementation((query, params, callback) => {
        expect(query).toBe("SELECT * FROM users WHERE username = ?");
        expect(params[0]).toBe(maliciousInput);
        // Comments should not be in the base query
        expect(query.split('?')[0]).not.toContain("--");

        callback(null, []);
      });

      request(app)
        .get('/user')
        .query({ username: maliciousInput })
        .expect(200, done);
    });

    test('should prevent SQL injection with time-based blind attack', (done) => {
      const maliciousInput = "admin'; WAITFOR DELAY '00:00:05'--";

      mockQuery.mockImplementation((query, params, callback) => {
        expect(query).toBe("SELECT * FROM users WHERE username = ?");
        expect(params[0]).toBe(maliciousInput);
        // Time-based attack commands should not be in query
        expect(query).not.toContain("WAITFOR");
        expect(query).not.toContain("SLEEP");

        callback(null, []);
      });

      request(app)
        .get('/user')
        .query({ username: maliciousInput })
        .expect(200, done);
    });

    test('should prevent SQL injection with stacked queries', (done) => {
      const maliciousInput = "admin'; DROP TABLE users;--";

      mockQuery.mockImplementation((query, params, callback) => {
        expect(query).toBe("SELECT * FROM users WHERE username = ?");
        expect(params[0]).toBe(maliciousInput);
        // DROP command should not be in the executed query
        expect(query).not.toContain("DROP");

        callback(null, []);
      });

      request(app)
        .get('/user')
        .query({ username: maliciousInput })
        .expect(200, done);
    });
  });

  describe('Functional Correctness', () => {
    test('should return user data for valid username', (done) => {
      const testUsername = 'bob';
      const mockUserData = [
        { id: 2, username: 'bob', email: 'bob@example.com' }
      ];

      mockQuery.mockImplementation((query, params, callback) => {
        callback(null, mockUserData);
      });

      request(app)
        .get('/user')
        .query({ username: testUsername })
        .expect(200)
        .end((err, res) => {
          if (err) return done(err);
          expect(res.body).toEqual(mockUserData);
          done();
        });
    });

    test('should return empty array for non-existent user', (done) => {
      const testUsername = 'nonexistent';

      mockQuery.mockImplementation((query, params, callback) => {
        callback(null, []);
      });

      request(app)
        .get('/user')
        .query({ username: testUsername })
        .expect(200)
        .end((err, res) => {
          if (err) return done(err);
          expect(res.body).toEqual([]);
          done();
        });
    });

    test('should handle database errors gracefully', (done) => {
      const testUsername = 'test';

      mockQuery.mockImplementation((query, params, callback) => {
        callback(new Error('Connection lost'), null);
      });

      request(app)
        .get('/user')
        .query({ username: testUsername })
        .expect(500, 'Database error', done);
    });
  });

  describe('Edge Cases', () => {
    test('should handle empty username', (done) => {
      mockQuery.mockImplementation((query, params, callback) => {
        expect(params[0]).toBe('');
        callback(null, []);
      });

      request(app)
        .get('/user')
        .query({ username: '' })
        .expect(200, done);
    });

    test('should handle special characters safely', (done) => {
      const specialUsername = "test@user#123";

      mockQuery.mockImplementation((query, params, callback) => {
        expect(query).toBe("SELECT * FROM users WHERE username = ?");
        expect(params[0]).toBe(specialUsername);
        callback(null, []);
      });

      request(app)
        .get('/user')
        .query({ username: specialUsername })
        .expect(200, done);
    });

    test('should handle unicode characters safely', (done) => {
      const unicodeUsername = "用户名";

      mockQuery.mockImplementation((query, params, callback) => {
        expect(query).toBe("SELECT * FROM users WHERE username = ?");
        expect(params[0]).toBe(unicodeUsername);
        callback(null, []);
      });

      request(app)
        .get('/user')
        .query({ username: unicodeUsername })
        .expect(200, done);
    });

    test('should handle very long usernames safely', (done) => {
      const longUsername = 'a'.repeat(1000);

      mockQuery.mockImplementation((query, params, callback) => {
        expect(query).toBe("SELECT * FROM users WHERE username = ?");
        expect(params[0]).toBe(longUsername);
        callback(null, []);
      });

      request(app)
        .get('/user')
        .query({ username: longUsername })
        .expect(200, done);
    });

    test('should handle undefined username parameter', (done) => {
      mockQuery.mockImplementation((query, params, callback) => {
        expect(params[0]).toBeUndefined();
        callback(null, []);
      });

      request(app)
        .get('/user')
        .expect(200, done);
    });
  });

  describe('Regression Prevention', () => {
    test('should never concatenate user input into SQL query string', (done) => {
      const testUsername = 'test_user';

      mockQuery.mockImplementation((query, params, callback) => {
        // Critical check: query must use placeholder, not concatenation
        expect(query).toMatch(/\?/);
        expect(query).not.toContain(testUsername);
        // Ensure no string interpolation patterns
        expect(query).not.toMatch(/\$\{.*\}/);
        expect(query).not.toMatch(/\+.*username/i);

        callback(null, []);
      });

      request(app)
        .get('/user')
        .query({ username: testUsername })
        .expect(200, done);
    });

    test('should always pass parameters as second argument to db.query', (done) => {
      const testUsername = 'security_test';

      mockQuery.mockImplementation((query, params, callback) => {
        // Ensure parameters are passed as the second argument
        expect(typeof query).toBe('string');
        expect(Array.isArray(params)).toBe(true);
        expect(typeof callback).toBe('function');

        callback(null, []);
      });

      request(app)
        .get('/user')
        .query({ username: testUsername })
        .expect(200)
        .end((err) => {
          if (err) return done(err);
          // Verify the call signature
          expect(mockQuery).toHaveBeenCalledWith(
            expect.any(String),
            expect.any(Array),
            expect.any(Function)
          );
          done();
        });
    });
  });
});

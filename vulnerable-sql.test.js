const request = require("supertest");
const express = require("express");
const mysql = require("mysql2");

// Mock the mysql2 module
jest.mock("mysql2");

describe("SQL Injection Vulnerability Remediation Tests", () => {
  let app;
  let mockQuery;
  let mockConnection;

  beforeEach(() => {
    // Setup mock connection and query function
    mockQuery = jest.fn();
    mockConnection = {
      query: mockQuery
    };

    mysql.createConnection.mockReturnValue(mockConnection);

    // Clear the module cache to get a fresh instance
    jest.resetModules();

    // Re-require the app to get fresh instance with mocks
    const appModule = require("./vulnerable-sql.js");
    app = appModule;
  });

  afterEach(() => {
    jest.clearAllMocks();
  });

  describe("Parameterized Query Implementation", () => {
    test("should use parameterized query with placeholder", (done) => {
      const testUsername = "testuser";

      mockQuery.mockImplementation((query, params, callback) => {
        // Verify parameterized query is used
        expect(query).toBe("SELECT * FROM users WHERE username = ?");
        expect(params).toEqual([testUsername]);
        expect(Array.isArray(params)).toBe(true);

        callback(null, [{ id: 1, username: testUsername }]);
      });

      request(app)
        .get("/user")
        .query({ username: testUsername })
        .expect(200)
        .end((err, res) => {
          if (err) return done(err);
          expect(mockQuery).toHaveBeenCalledTimes(1);
          done();
        });
    });

    test("should properly escape parameters to prevent SQL injection", (done) => {
      const maliciousInput = "' OR '1'='1";

      mockQuery.mockImplementation((query, params, callback) => {
        // Verify the query structure uses parameterization
        expect(query).not.toContain(maliciousInput);
        expect(query).toBe("SELECT * FROM users WHERE username = ?");

        // Verify the malicious input is passed as a parameter (to be escaped by mysql2)
        expect(params).toEqual([maliciousInput]);

        // Simulate database properly handling parameterized query
        // (returns no results since literal string doesn't match)
        callback(null, []);
      });

      request(app)
        .get("/user")
        .query({ username: maliciousInput })
        .expect(200)
        .end((err, res) => {
          if (err) return done(err);
          expect(mockQuery).toHaveBeenCalledTimes(1);
          done();
        });
    });
  });

  describe("SQL Injection Attack Prevention", () => {
    test("should block SQL injection with UNION attack", (done) => {
      const unionAttack = "admin' UNION SELECT * FROM passwords--";

      mockQuery.mockImplementation((query, params, callback) => {
        // Verify query uses parameterization
        expect(query).toBe("SELECT * FROM users WHERE username = ?");
        expect(params[0]).toBe(unionAttack);

        // Attack string is treated as literal parameter value
        callback(null, []);
      });

      request(app)
        .get("/user")
        .query({ username: unionAttack })
        .expect(200)
        .end((err, res) => {
          if (err) return done(err);
          expect(res.body).toEqual([]);
          done();
        });
    });

    test("should block SQL injection with comment-based bypass", (done) => {
      const commentAttack = "admin'--";

      mockQuery.mockImplementation((query, params, callback) => {
        expect(query).toBe("SELECT * FROM users WHERE username = ?");
        expect(params[0]).toBe(commentAttack);
        callback(null, []);
      });

      request(app)
        .get("/user")
        .query({ username: commentAttack })
        .expect(200)
        .end((err, res) => {
          if (err) return done(err);
          expect(res.body).toEqual([]);
          done();
        });
    });

    test("should block SQL injection with boolean-based attack", (done) => {
      const booleanAttack = "' OR 1=1--";

      mockQuery.mockImplementation((query, params, callback) => {
        expect(query).toBe("SELECT * FROM users WHERE username = ?");
        expect(params[0]).toBe(booleanAttack);
        callback(null, []);
      });

      request(app)
        .get("/user")
        .query({ username: booleanAttack })
        .expect(200)
        .end((err, res) => {
          if (err) return done(err);
          expect(res.body).toEqual([]);
          done();
        });
    });

    test("should block SQL injection with time-based blind attack", (done) => {
      const timeBasedAttack = "admin'; WAITFOR DELAY '00:00:05'--";

      mockQuery.mockImplementation((query, params, callback) => {
        expect(query).toBe("SELECT * FROM users WHERE username = ?");
        expect(params[0]).toBe(timeBasedAttack);
        callback(null, []);
      });

      request(app)
        .get("/user")
        .query({ username: timeBasedAttack })
        .expect(200)
        .end((err, res) => {
          if (err) return done(err);
          expect(res.body).toEqual([]);
          done();
        });
    });

    test("should block SQL injection with stacked queries", (done) => {
      const stackedQuery = "admin'; DROP TABLE users;--";

      mockQuery.mockImplementation((query, params, callback) => {
        expect(query).toBe("SELECT * FROM users WHERE username = ?");
        expect(params[0]).toBe(stackedQuery);
        // Parameterized query prevents execution of second statement
        callback(null, []);
      });

      request(app)
        .get("/user")
        .query({ username: stackedQuery })
        .expect(200)
        .end((err, res) => {
          if (err) return done(err);
          expect(res.body).toEqual([]);
          done();
        });
    });
  });

  describe("Legitimate Functionality", () => {
    test("should return user data for valid username", (done) => {
      const validUsername = "john_doe";
      const expectedUser = { id: 1, username: validUsername, email: "john@example.com" };

      mockQuery.mockImplementation((query, params, callback) => {
        expect(query).toBe("SELECT * FROM users WHERE username = ?");
        expect(params[0]).toBe(validUsername);
        callback(null, [expectedUser]);
      });

      request(app)
        .get("/user")
        .query({ username: validUsername })
        .expect(200)
        .end((err, res) => {
          if (err) return done(err);
          expect(res.body).toEqual([expectedUser]);
          done();
        });
    });

    test("should return empty array for non-existent user", (done) => {
      const nonExistentUser = "nonexistent_user";

      mockQuery.mockImplementation((query, params, callback) => {
        expect(query).toBe("SELECT * FROM users WHERE username = ?");
        expect(params[0]).toBe(nonExistentUser);
        callback(null, []);
      });

      request(app)
        .get("/user")
        .query({ username: nonExistentUser })
        .expect(200)
        .end((err, res) => {
          if (err) return done(err);
          expect(res.body).toEqual([]);
          done();
        });
    });

    test("should handle special characters in legitimate usernames", (done) => {
      const specialUsername = "user_name-123.test";

      mockQuery.mockImplementation((query, params, callback) => {
        expect(query).toBe("SELECT * FROM users WHERE username = ?");
        expect(params[0]).toBe(specialUsername);
        callback(null, [{ id: 5, username: specialUsername }]);
      });

      request(app)
        .get("/user")
        .query({ username: specialUsername })
        .expect(200)
        .end((err, res) => {
          if (err) return done(err);
          expect(res.body).toHaveLength(1);
          done();
        });
    });

    test("should handle database errors gracefully", (done) => {
      const testUsername = "testuser";
      const dbError = new Error("Database connection failed");

      mockQuery.mockImplementation((query, params, callback) => {
        callback(dbError, null);
      });

      request(app)
        .get("/user")
        .query({ username: testUsername })
        .expect(500)
        .end((err, res) => {
          if (err) return done(err);
          expect(res.text).toBe("Database error");
          done();
        });
    });
  });

  describe("Edge Cases", () => {
    test("should handle empty username parameter", (done) => {
      mockQuery.mockImplementation((query, params, callback) => {
        expect(query).toBe("SELECT * FROM users WHERE username = ?");
        expect(params[0]).toBe("");
        callback(null, []);
      });

      request(app)
        .get("/user")
        .query({ username: "" })
        .expect(200)
        .end((err, res) => {
          if (err) return done(err);
          expect(res.body).toEqual([]);
          done();
        });
    });

    test("should handle undefined username parameter", (done) => {
      mockQuery.mockImplementation((query, params, callback) => {
        expect(query).toBe("SELECT * FROM users WHERE username = ?");
        expect(params[0]).toBeUndefined();
        callback(null, []);
      });

      request(app)
        .get("/user")
        .expect(200)
        .end((err, res) => {
          if (err) return done(err);
          expect(res.body).toEqual([]);
          done();
        });
    });

    test("should handle very long usernames", (done) => {
      const longUsername = "a".repeat(1000);

      mockQuery.mockImplementation((query, params, callback) => {
        expect(query).toBe("SELECT * FROM users WHERE username = ?");
        expect(params[0]).toBe(longUsername);
        callback(null, []);
      });

      request(app)
        .get("/user")
        .query({ username: longUsername })
        .expect(200)
        .end((err, res) => {
          if (err) return done(err);
          expect(res.body).toEqual([]);
          done();
        });
    });

    test("should handle unicode characters", (done) => {
      const unicodeUsername = "用户名测试";

      mockQuery.mockImplementation((query, params, callback) => {
        expect(query).toBe("SELECT * FROM users WHERE username = ?");
        expect(params[0]).toBe(unicodeUsername);
        callback(null, [{ id: 10, username: unicodeUsername }]);
      });

      request(app)
        .get("/user")
        .query({ username: unicodeUsername })
        .expect(200)
        .end((err, res) => {
          if (err) return done(err);
          expect(res.body).toHaveLength(1);
          done();
        });
    });
  });

  describe("Regression Prevention", () => {
    test("should never concatenate user input directly into SQL query", (done) => {
      const testUsername = "test_user";

      mockQuery.mockImplementation((query, params, callback) => {
        // Ensure the query doesn't contain direct concatenation
        expect(query).not.toMatch(/SELECT.*FROM.*WHERE.*username.*=.*'/);
        expect(query).not.toContain(testUsername);

        // Ensure it uses parameterized query
        expect(query).toMatch(/\?/);
        expect(Array.isArray(params)).toBe(true);
        expect(params[0]).toBe(testUsername);

        callback(null, []);
      });

      request(app)
        .get("/user")
        .query({ username: testUsername })
        .expect(200)
        .end((err, res) => {
          if (err) return done(err);
          done();
        });
    });

    test("should always pass user input as array parameter", (done) => {
      const testUsername = "another_test";

      mockQuery.mockImplementation((query, params, callback) => {
        // Verify parameters are passed as array (second argument)
        expect(Array.isArray(params)).toBe(true);
        expect(params).toHaveLength(1);
        expect(params[0]).toBe(testUsername);

        callback(null, []);
      });

      request(app)
        .get("/user")
        .query({ username: testUsername })
        .expect(200)
        .end((err, res) => {
          if (err) return done(err);
          done();
        });
    });
  });
});

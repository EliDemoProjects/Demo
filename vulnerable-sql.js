const express = require("express");
const mysql = require("mysql2");

const app = express();

const db = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "password",
  database: "demo"
});

app.get("/user", (req, res) => {
  const username = req.query.username;

  // Use parameterized query to prevent SQL injection
  const query = "SELECT * FROM users WHERE username = ?";

  db.query(query, [username], (err, results) => {
    if (err) {
      return res.status(500).send("Database error");
    }

    res.json(results);
  });
});

app.listen(3000);

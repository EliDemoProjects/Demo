const express = require("express");
const { execFile } = require("child_process");

const app = express();

app.get("/ping", (req, res) => {
  const host = req.query.host;

  // Use execFile with arguments array to prevent command injection
  execFile("ping", ["-c", "1", host], (error, stdout, stderr) => {
    if (error) {
      return res.status(500).send(error.message);
    }

    res.send(stdout);
  });
});

app.listen(3000, () => {
  console.log("Server running on port 3000");
});

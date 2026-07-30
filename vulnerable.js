const express = require("express");
const { execFile } = require("child_process");

const app = express();

app.get("/ping", (req, res) => {
  const host = req.query.host;

  // Use execFile with an argument array instead of exec with a shell string.
  // execFile does not invoke a shell, so shell metacharacters in `host`
  // are never interpreted — this prevents command injection (CWE-77).
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

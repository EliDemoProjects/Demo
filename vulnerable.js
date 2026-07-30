const express = require("express");
const { spawn } = require("child_process");

const app = express();

// Allowlist: only permit valid hostname/IP characters to avoid OS command injection.
// Using spawn with shell:false (argv array) ensures user input is passed as a literal
// argument to the OS and is never interpreted by a shell.
const VALID_HOST_PATTERN = /^[a-zA-Z0-9.\-]+$/;

app.get("/ping", (req, res) => {
  const host = req.query.host;

  // Validate host against an allowlist of safe characters before use
  if (!host || !VALID_HOST_PATTERN.test(host)) {
    return res.status(400).send("Invalid host parameter.");
  }

  // Use spawn with an argument array (shell: false by default) so the host value
  // is passed directly to execve() and never interpreted by a shell.
  const proc = spawn("ping", ["-c", "1", host]);

  let stdout = "";
  let stderr = "";

  proc.stdout.on("data", (data) => {
    stdout += data;
  });

  proc.stderr.on("data", (data) => {
    stderr += data;
  });

  proc.on("close", (code) => {
    if (code !== 0) {
      return res.status(500).send("ping failed.");
    }
    res.send(stdout);
  });
});

app.listen(3000, () => {
  console.log("Server running on port 3000");
});

const express = require("express");

const { execFile } = require("child_process");
const net = require("net");

const app = express();

app.get("/ping", (req, res) => {

  const host = req.query.host;

  // Validate that host is a valid IP address or hostname using Node.js stdlib.
  // Only allow IPv4/IPv6 addresses and simple hostnames (alphanumeric + hyphens + dots).
  // This input-boundary validation prevents shell metacharacters from reaching the command.
  if (!host || (!net.isIPv4(host) && !net.isIPv6(host) && !/^[a-zA-Z0-9][a-zA-Z0-9\-\.]{0,253}[a-zA-Z0-9]$/.test(host))) {
    return res.status(400).send("Invalid host");
  }

  // execFile does NOT invoke a shell; arguments are passed as an array (argv list),
  // so shell metacharacter injection is not possible.
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
 

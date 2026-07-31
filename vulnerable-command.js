const express = require("express");

const { exec } = require("child_process");

const app = express();

// Apply HSTS header to all responses to prevent protocol downgrade attacks
// and cookie hijacking (CWE-346). max-age=31536000 = 1 year; includeSubDomains
// ensures all subdomains are also protected.
app.use((req, res, next) => {
  res.setHeader(
    "Strict-Transport-Security",
    "max-age=31536000; includeSubDomains"
  );
  next();
});

app.get("/ping", (req, res) => {

  const host = req.query.host;

  exec("ping -c 1 " + host, (error, stdout, stderr) => {

    if (error) {

      return res.status(500).send(error.message);

    }

    res.send(stdout);

  });

});
 
app.listen(3000, () => {

  console.log("Server running on port 3000");

});
 

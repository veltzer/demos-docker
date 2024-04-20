#!/usr/bin/env node

const express = require("express")
const app = express()

app.get("/", (req, res) => {
  res.send("Hello World from express javascript server inside docker container!")
})

app.listen(() => {
  console.log("Contact me at http://localhost")
})

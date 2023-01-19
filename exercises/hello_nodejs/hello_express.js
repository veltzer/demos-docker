#!/usr/bin/env node

const express = require('express')
const app = express()
const port = 8000

app.get('/', (req, res) => {
  res.send('Hello World from express javascript server inside docker container!')
})

app.listen(port, () => {
  console.log(`Contact me at http://localhost:${port}`)
})

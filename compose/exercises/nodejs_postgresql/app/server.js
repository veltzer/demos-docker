#!/usr/bin/env node

const express = require("express");
const Sequelize = require("sequelize");
const cors = require("cors");

// get environment variables
const env_port = parseInt(process.env.PORT, 10);
const env_host = process.env.HOST;
const env_db_type = process.env.db_type;
const env_db_dialect = process.env.db_dialect;
const env_db_name = process.env.db_name;
const env_db_user = process.env.db_user;
const env_db_password = process.env.db_password;
const env_db_port = process.env.db_port;
const env_db_host = process.env.db_host;

// Initialize Express app
const app = express();

// use CORS
app.use(cors());

// Parse JSON request bodies
app.use(express.json());

// Set up Sequelize connection to PostgreSQL
//const sequelize = new Sequelize("postgres://postgres:db_password@postgres:5432/postgres", {
const sequelize = new Sequelize(`${env_db_type}://${env_db_user}:${env_db_password}@${env_db_host}:${env_db_port}/${env_db_name}`, {
  dialect: env_db_dialect 
});

// Define a model for the "users" table
const User = sequelize.define("user", {
  id: {
    type: Sequelize.INTEGER,
    primaryKey: true,
    autoIncrement: true
  },
  name: {
    type: Sequelize.STRING,
    allowNull: false
  },
  email: {
    type: Sequelize.STRING,
    allowNull: false,
    unique: true
  }
});

// Sync the model with the database (create the table if it doesnt exist)
sequelize.sync();

// GET /users - Retrieve all users
app.get("/users", async (req, res) => {
  try {
    const users = await User.findAll();
    res.json(users);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Something went wrong" });
  }
});

// POST /users - Create a new user
app.post("/users", async (req, res) => {
  try {
    const user = await User.create(req.body);
    res.status(201).json(user);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Something went wrong" });
  }
});

// Start the server
app.listen(env_port, () => {
  console.log(`Server started on http://localhost:${env_port}`);
});

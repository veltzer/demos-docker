#!/usr/bin/env node

const express = require("express");
const Sequelize = require("sequelize");

// Initialize Express app
const app = express();

// Parse JSON request bodies
app.use(express.json());

// Set up Sequelize connection to PostgreSQL
const sequelize = new Sequelize("postgres://postgres:db_password@postgres:5432/postgres", {
  dialect: "postgres"
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
app.listen(3000, () => {
  console.log("Server started on http://localhost:3000");
});

-- Databricks notebook source
CREATE DATABASE IF NOT EXISTS coffee_shop;

-- COMMAND ----------

CREATE OR REPLACE TABLE coffee_shop.users (
  id LONG GENERATED ALWAYS AS IDENTITY,
  name STRING,
  machine_serial_number INT,
  birthdate DATE,
  loyalty_points INT,
  email STRING
)
COMMENT 'Mock table for connection testing purposes';

-- COMMAND ----------

describe coffee_shop.users;

-- COMMAND ----------

INSERT INTO coffee_shop.users(Name, machine_serial_number, birthdate, loyalty_points,email) VALUES ('Luis M Ramirez', 117, DATE'1901-01-20', 2, 'lm@coffee.com')

-- COMMAND ----------

SELECT * FROM coffee_shop.users;

-- COMMAND ----------

INSERT INTO coffee_shop.s

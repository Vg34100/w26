# STA220-DATA | W03-Thu | 2026-01-22

## SQL Joins Overview

- Left join keeps all rows from the left table, adds matching rows from the right
- Right join does the opposite – all rows from the right table, matches from the left
- Inner join returns only rows that exist in **both** tables (intersection)
- Full outer join (mentioned) would merge all rows from both tables, filling gaps with nulls
- Example: combine Summer and Winter Olympic tables to see countries appearing in both

## Querying Medal Data

- Use SUM to total gold medals per country in each games table
- Filter with HAVING to keep only countries with at least one gold medal
- Join the two summed tables on country name to compare Winter vs. Summer performance
- Order results by total medals to rank the most successful nations
- Sample top nations mentioned: USA, China, Germany, France, Italy, Russia, Japan, Australia

## Using Views for Reuse

- Create a view to store the summed gold‑medal query (CREATE VIEW ... AS SELECT ...)
- View provides a virtual table that can be queried like a regular table
- Drop the view when it’s no longer needed (DROP VIEW IF EXISTS view_name)
- Views simplify repeated queries without recreating the same sub‑query each time

## Creating and Managing Tables

- CREATE TABLE to add new entities (e.g., a student list with ID, first/last name)
- INSERT INTO to add rows, e.g., 2022 Olympic host data
- UPDATE with a WHERE clause to modify specific rows (avoid updating everything)
- DELETE FROM with conditions to remove unwanted entries
- ALTER TABLE to add or drop columns (e.g., adding a “capital” column)

## Preventing SQL Injection

- Never concatenate raw user input into SQL strings
- Use placeholders (?) and bind parameters to safely insert user values
- Example: SELECT gold FROM all_medals WHERE country = ? with the country supplied as a parameter
- This protects against malicious input that could drop tables or expose data

## Take‑Home Message

- Always guard against SQL injection when combining user input with SQL commands
- Views and parameterized queries make code cleaner and safer
- Regularly review and drop temporary objects (views, tables) after use to keep the database tidy

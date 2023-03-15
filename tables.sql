DROP SCHEMA IF EXISTS katie_github;

CREATE SCHEMA katie_github;
DROP TABLE IF EXISTS katie_github.stargazers;

CREATE TABLE katie_github.stargazers (
    id SERIAL PRIMARY KEY,
    login VARCHAR(255) NOT NULL,
    name VARCHAR(255),
    email VARCHAR(255)
);

CREATE SCHEMA katie_github;

CREATE TABLE katie_github.stargazers (
    id SERIAL PRIMARY KEY,
    login VARCHAR(255) NOT NULL,
    name VARCHAR(255)
);

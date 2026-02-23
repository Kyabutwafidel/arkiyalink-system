-- PostgreSQL schema placeholder
CREATE TABLE sme (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    revenue NUMERIC,
    expenses NUMERIC
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    sme_id INT REFERENCES sme(id),
    rating INT,
    comment TEXT
);

CREATE TABLE comment (
    id          TEXT PRIMARY KEY NOT NULL,
    body        TEXT NOT NULL,
    author      TEXT NOT NULL,
    subreddit   TEXT NOT NULL,
    create_at   timestamp DEFAULT current_timestamp NOT NULL
);

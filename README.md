# letters

Collects comments from popular Tolkien related subreddits with the hope of running some statistical analysis of references to The Letters of J. R. R. Tolkien. Currently it works as a generic, dockerized comment scraper.

## Configuration

Expects a .env file in the root of the repository contain the following fields:

```
CLIENT_ID=<reddit client id>
CLIENT_SECRET=<reddit client secret>
USER_AGENT=<unique user agent>

DB_NAME=letters
DB_USER=letters
DB_PASS=letters
DB_HOST=postgres

SUBREDDIT=<subreddit name>
```

Multiple subreddits can be scanned at the same time by listing them together seperated by a '+'. E.g. 'games+gaming' will scan both subreddits.

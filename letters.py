"""Collects comments from popular Tolkien related subreddits with the hope of running some statistical analysis of references to The Letters of J. R. R. Tolkien."""
import praw

from pg import DB
from time import sleep
from os import environ as config
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def process_comment(db, comment):
    """Add comment to database."""
    print(comment.subreddit)
    print(comment.author)
    print(comment.body)
    print(comment.id)
    print('-----')

    db.upsert(
        'comment', {
            'id': comment.id,
            'body': comment.body,
            'author': comment.author,
            'subreddit': comment.subreddit
        }
    )


def start_scan(db, reddit, subreddit):
    """Scan subreddit for new comments."""
    for comment in reddit.subreddit(subreddit).stream.comments():
        process_comment(db, comment)


if __name__ == "__main__":
    while(1):
        try:
            print("Connecting to db...")
            db = DB(
                dbname=config.get('DB_NAME'),
                host=config.get('DB_HOST'),
                port=5432,
                user=config.get('DB_USER'),
                passwd=config.get('DB_PASS')
            )

            print("Connecting to reddit...")

            reddit = praw.Reddit(
                client_id=config.get('CLIENT_ID'),
                client_secret=config.get('CLIENT_SECRET'),
                user_agent=config.get('USER_AGENT')
            )
            print("Starting scan")
            start_scan(db, reddit, config.get('SUBREDDIT'))

        except Exception as e:
            print(e)
            sleep(1)

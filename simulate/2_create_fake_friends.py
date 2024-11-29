#!/usr/bin/env python3

import os
import sys
from faker import Faker
import time
import random
import sqlite3
import shutil

DB2 = "db2.sqlite3"
DB_SIM = "db_sim.sqlite3"

# -- CHECKS --

# Check if db_su.sqlite3 exists
if not os.path.isfile(DB2):
    print("db with friends table does not exists")
    print(f"please create {DB2}")
    exit(1)

# Reset database
if os.path.isfile(DB_SIM):
    os.remove(DB_SIM)
shutil.copy(DB2, DB_SIM)

# Check if requirements-sim.txt exists
if not os.path.isfile("requirements-sim.txt"):
    print("requirements-sim.txt missing")
    exit(1)

# If directory venv does not exists, then exit
if not os.path.isdir("venv"):
    help = """
You do not have any venv directory, please run following (cut and paste)

python3 -m venv venv
source venv/bin/activate
pip install -r requirements-sim.txt

And then run this script again!
"""
    print(help)
    exit(1)

# Read Users from db2.sqlite3

conn = sqlite3.connect(DB2)
cursor = conn.cursor()

# Also fetching username, for debug/dev purpose
cursor.execute("SELECT id, username FROM users_user")

members = {}
for member in cursor.fetchall():
    id, name = member
    members[id] = name
N = len(members)

friends = {}
for member in members.keys():
    # 20% chance to be in mood to connect
    if N > 100 and random.random() < 0.8:
        continue

    someone = random.choice([key for key in members.keys() if key != member])
    # user_a < user_b (sorted)
    user_a = min(member, someone)
    user_b = max(member, someone)
    if user_a not in friends:
        friends[user_a] = {}
    
    # Max 40 requests
    if len(friends[user_a]) >= 40:
        continue

    register_time = members[member]["joined"]
    request_friendship_time = register_time + random.randint(1,31)*24*60*60

    if member == user_a:
        friends[user_a][user_b] = [request_friendship_time, None]
    else:
        friends[user_a][user_b] = [None, request_friendship_time]


# FUNCTIONS

# Populate the database with friend requests
def insert_friend_requests():
    for user_a, friend_data in friends.items():
        for user_b in friend_data.keys():
            # Fetch user IDs for user_a and user_b
            cursor.execute("SELECT id FROM users_user WHERE username = ?", (members[user_a]["username"],))
            from_user_id = cursor.fetchone()[0]

            cursor.execute("SELECT id FROM users_user WHERE username = ?", (members[user_b]["username"],))
            to_user_id = cursor.fetchone()[0]

            # Insert friendship into the users_user_friends table
            try:
                cursor.execute("""
                    INSERT INTO users_user_friends (
                        from_user_id, to_user_id
                    ) VALUES (?, ?)
                """, (from_user_id, to_user_id))
            except sqlite3.IntegrityError:
                # Skip duplicates (violating the unique constraint)
                print(f"Friendship between {user_a} and {user_b} already exists.")

    conn.commit()

# MAIN

if __name__ == "__main__":
    insert_friend_requests()

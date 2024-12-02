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

# Check if DB_SIM exists
if not os.path.isfile(DB_SIM):
    print(f"please create {DB_SIM}")
    exit(1)

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

# Check if table users_user_friends exists
conn = sqlite3.connect(DB_SIM)
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users_user_friends'")
if cursor.fetchone() is None:
    print("Table users_user_friends does not exist in db2.sqlite3")
    print("Please create it first")
    exit(1)

# Read Users from db_sim.sqlite3
# fetching username, for debug/dev purpose
cursor.execute("SELECT id, username, date_joined FROM users_user")

members = {}
for member in cursor.fetchall():
    id, name, joined = member
    # joined format 2024-11-28 12:49:17.203966
    # convert into unix timestamp with seconds
    joined = int(time.mktime(time.strptime(joined, "%Y-%m-%d %H:%M:%S.%f")))
    members[id] = {"username": name, "joined": joined}
N = len(members)

# Simulate friend requests
friends = {}
for member_id in range(1, N+1):
    # 20% chance to be in mood to connect
    if N > 100 and random.random() < 0.8:
        continue

    someone_id = random.randint(1, N+1)
    # user_a < user_b (sorted)
    user_a = min(member_id, someone_id)
    user_b = max(member_id, someone_id)
    if user_a not in friends:
        friends[user_a] = {}

    # Max 40 requests
    if len(friends[user_a]) >= 40:
        continue

    register_time = members[member_id]["joined"]
    request_friendship_time = register_time + random.randint(1,31)*24*60*60

    if member_id == user_a:
        friends[user_a][user_b] = [request_friendship_time, None]
    else:
        friends[user_a][user_b] = [None, request_friendship_time]

# Simulate accept friend requests
for user_a in range(1, N+1):
    # 50% chance to accept
    if random.random() < 0.5:
        continue

    if user_a not in friends:
        continue

    for user_b in friends[user_a].keys():
        # 50% chance to accept
        if random.random() < 0.5:
            continue
        if friends[user_a][user_b][0] is None:
            friends[user_a][user_b][0] = friends[user_a][user_b][1] + random.randint(1,31)*24*60*60
        else:
            friends[user_a][user_b][1] = friends[user_a][user_b][0] + random.randint(1,31)*24*60*60

exit(1)

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

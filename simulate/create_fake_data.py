#!/usr/bin/env python3

import os
import sys
from faker import Faker
import time
import random
import sqlite3
import shutil

DB_SU = "db_su.sqlite3"
DB_SIM = "db_sim.sqlite3"

# -- CHECKS --

# Check if db_su.sqlite3 exists
if not os.path.isfile(DB_SU):
    print("db with suåeruser only, does not exists")
    print(f"please create {DB_SU}")
    exit(1)

# Reset database
if os.path.isfile(DB_SIM):
    os.remove(DB_SIM)
shutil.copy(DB_SU, DB_SIM)

# Check if requirements.txt exists
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

# -- START --

fake = Faker()

# Connect to the SQLite database
db_path = "db_sim.sqlite3"  # Update the path if necessary
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# N is amount of person you want to simulate
N = 1000
if len(sys.argv) > 1:
    N = int(sys.argv[1])

# Create fake names in a dictionary
a_year_ago = time.time() - 365*24*60*60
members = {}
for _ in range(N):
    fullname = fake.name()
    names = fullname.split(" ")
    first_name = names[0]
    last_name = names[-1]
    name = f"{first_name} {last_name}"
    members[name] = { 
        "username": f"{first_name.lower()}.{last_name.lower()}",
        "joined": a_year_ago + random.randint(0,300)*365*24*60*60    
    }

# Create workplace, email, and event address to the members
for name in members.keys():
    first_name, last_name = name.split(" ")
    org_name = fake.company()
    domain_name = org_name.split(" ")[0] + ".com"
    email = f"{first_name.lower()}.{last_name.lower()}@{domain_name}"
    members[name]["org"] = org_name
    members[name]["email"] = email
    #members[name]["org_address"] = fake.address()

# Populate the database with members
# username, email, first name, last name
def insert_members(): # <-------------------------------------------- *********
    for name, info in members.items():
        first_name, last_name = name.split(" ")
        username = f"{first_name.lower()}.{last_name.lower()}"
        email = info["email"]
        a_year_ago = time.time() - 365*24*60*60
        date_joined = a_year_ago + random.randint(0,300)*24*60*60
        password = "p@ssw0rd1"
        
        cursor.execute("""
            INSERT INTO users_user (
                password, last_login, is_superuser, username, first_name, last_name,
                is_staff, is_active, date_joined, email
            ) VALUES (?, NULL, 0, ?, ?, ?, 0, 1, ?, ?)
        """, (password, username, first_name, last_name, date_joined, email))

    conn.commit()

# Create friend requests
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

# Accept friend requests
for user_a in members.keys():
    # 50% chance to accept
    if random.random() < 0.5:
        continue

    for user_b in friends[user_a]:
        time_delta = random.randint(0,4)*24*60*60 + 60
        accept_times = friends[user_a][user_b]
        if accept_times[0] is None:
            accept_times[0] = accept_times[1] + time_delta
        else:
            accept_times[1] = accept_times[0] + time_delta

def insert_friend_requests():
    for user_a, friend_data in friends.items():
        for user_b, times in friend_data.items():
            # Fetch user IDs for user_a and user_b
            cursor.execute("SELECT id FROM users_user WHERE username = ?", (members[user_a]["username"],))
            user_a_id = cursor.fetchone()[0]
            cursor.execute("SELECT id FROM users_user WHERE username = ?", (members[user_b]["username"],))
            user_b_id = cursor.fetchone()[0]

            # Unpack friendship request/accept times
            request_time, accept_time = times

            # Insert friendship data into the users_user_friends table
            cursor.execute("""
                INSERT INTO users_user_friends (
                    user_1_id, user_2_id, accepted_time_1, accepted_time_2
                ) VALUES (?, ?, ?, ?)
            """, (user_a_id, user_b_id, request_time, accept_time))

    conn.commit()

insert_members()
insert_friend_requests()

import time
import random
import sqlite3
import os

DB_SIM = "db_sim.sqlite3"

# -- CHECKS --

# Check if DB_SIM exists
if not os.path.isfile(DB_SIM):
    print(f"Please create {DB_SIM}")
    exit(1)

# Connect to the database
conn = sqlite3.connect(DB_SIM)
cursor = conn.cursor()

# Check if table users_user_friends exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users_user_friends'")
if cursor.fetchone() is None:
    print("Table users_user_friends does not exist in db_sim.sqlite3")
    print("Please create it first")
    exit(1)

# Read Users from db_sim.sqlite3
cursor.execute("SELECT id, username, date_joined, is_superuser FROM users_user")

members = {}
for member in cursor.fetchall():
    id, name, joined, is_superuser = member

    # Skip superusers
    if is_superuser:
        continue

    # Convert Django ISO datetime to Unix timestamp
    try:
        joined = int(time.mktime(time.strptime(joined, "%Y-%m-%d %H:%M:%S.%f")))
    except ValueError:
        print(f"Invalid date format for user {name}: {joined}. Skipping.")
        continue

    members[id] = {"username": name, "joined": joined}

N = len(members)

# Simulate friend requests
friends = {}
for member_id in range(1, N + 1):
    # Skip users not in members dictionary
    if member_id not in members:
        continue

    # 20% chance to connect
    if N > 100 and random.random() < 0.8:
        continue

    someone_id = random.randint(1, N)  # Fix range to avoid out-of-bounds
    if someone_id not in members or someone_id == member_id:
        continue

    # Ensure consistent ordering for friendship
    user_a = min(member_id, someone_id)
    user_b = max(member_id, someone_id)

    if user_a not in friends:
        friends[user_a] = {}

    # Max 40 requests per user
    if len(friends[user_a]) >= 40:
        continue

    register_time = members[member_id]["joined"]
    request_friendship_time = register_time + random.randint(1, 31) * 24 * 60 * 60

    if member_id == user_a:
        friends[user_a][user_b] = [request_friendship_time, None]
    else:
        friends[user_a][user_b] = [None, request_friendship_time]

# Simulate accept friend requests
for user_a in range(1, N + 1):
    if user_a not in friends:
        continue

    for user_b in friends[user_a]:
        # 50% chance to accept
        if random.random() < 0.5:
            continue

        time_delta = random.randint(1, 31) * 24 * 60 * 60
        if friends[user_a][user_b][0] is None:
            friends[user_a][user_b][0] = friends[user_a][user_b][1] + time_delta
        else:
            friends[user_a][user_b][1] = friends[user_a][user_b][0] + time_delta

# Populate the database with friend requests
def insert_friend_requests():
    for user_a, friend_data in friends.items():
        for user_b, times in friend_data.items():
            accepted_time_1, accepted_time_2 = times

            try:
                cursor.execute("""
                    INSERT INTO users_user_friends (
                        user_1_id, user_2_id, accepted_time_1, accepted_time_2
                    ) VALUES (?, ?, ?, ?)
                """, (user_a, user_b, accepted_time_1, accepted_time_2))
            except sqlite3.IntegrityError:
                print(f"Friendship between {user_a} and {user_b} already exists.")

    conn.commit()

# MAIN
if __name__ == "__main__":
    insert_friend_requests()
    conn.close()
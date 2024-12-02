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
    print("db with superuser only, does not exists")
    print(f"please create {DB_SU}")
    exit(1)

# Reset database
if os.path.isfile(DB_SIM):
    os.remove(DB_SIM)
shutil.copy(DB_SU, DB_SIM)

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

# -- GENERATE FAKE USERS --

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

# FUNCTIONS

# Populate the database with members
# username, email, first name, last name
def insert_members():
    for name, info in members.items():
        first_name, last_name = name.split(" ")
        username = f"{first_name.lower()}.{last_name.lower()}"
        email = info["email"]
        date_joined = a_year_ago + random.randint(0,300)*24*60*60
        password = "p@ssw0rd1"
        
        cursor.execute("""
            INSERT INTO users_user (
                password, last_login, is_superuser, username, first_name, last_name,
                is_staff, is_active, date_joined, email
            ) VALUES (?, NULL, 0, ?, ?, ?, 0, 1, ?, ?)
        """, (password, username, first_name, last_name, date_joined, email))

    conn.commit()

# MAIN

if __name__ == "__main__":
    insert_members()

#!/usr/bin/env python3

from faker import Faker
from users.models import User

fake = Faker()

N = 10

def create_email(first_name, last_name):
    domain_name = fake.domain_name()
    email = f"{first_name.lower()}.{last_name.lower()}@{domain_name}"
    return email

DEFAULT_PASSWORD="secret"

for i in range(N):
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = create_email(first_name, last_name)    
    username = f"{first_name.lower()}.{last_name.lower()}"
    user = User(
        username=username,
        email=email,
        first_name=first_name,
        last_name=last_name,
    )
    user.set_password(DEFAULT_PASSWORD)
    user.save()

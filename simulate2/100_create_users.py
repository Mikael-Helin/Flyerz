#!/usr/bin/env python3

from faker import Faker
from users.models import User

fake = Faker()

N = 10
DEFAULT_PASSWORD="secret"

for i in range(N):
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.ascii_email()    
    username = f"{first_name.lower()}.{last_name.lower()}"
    user = User(
        username=username,
        email=email,
        first_name=first_name,
        last_name=last_name,
    )
    user.set_password(DEFAULT_PASSWORD)
    user.save()

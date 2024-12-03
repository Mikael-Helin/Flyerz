from faker import Faker
from users.models import User
import random

fake = Faker()

NUM_USER = 30
NUM_FRIEND = 4
DEFAULT_PASSWORD="secret"

#
# Seed Users
#

for i in range(NUM_USER):
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
    try:
        user.save()
    except:
        pass

#
# Seed Friend
#

users = []

for user in User.objects.all():
    users.append(user)

no_users = len(users)

if no_users < 2:
    exit(1)

for user1 in users:
    for _ in range(NUM_FRIEND):
        while True:
            user2 = random.choice(users)
            if user1.id != user2.id:
                break
        user1.friends.add(user2)
        # friend = Friend(
        #     user_1 = user1,
        #     user_2 = user2,
        # ) 
        # try:
        #     friend.save()
        # except:
        #     pass

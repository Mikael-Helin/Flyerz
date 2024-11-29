#
# $ python manage.py shell < simulate/at_test.py
#

from users.models import User
from faker import Faker

fake = Faker()

N = 1

for _ in range(N):
    user_name = fake.user_name()
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    user = User.objects.create(
        username=user_name,
        email=email,
        first_name=first_name, 
        last_name=last_name
    )
    user.set_password('supersecret')
    user.save()

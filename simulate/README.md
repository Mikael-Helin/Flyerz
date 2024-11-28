# Simulate Data

Create superuser if needed

    DJANGO_SUPERUSER_USERNAME=admin \
    DJANGO_SUPERUSER_EMAIL=admin@example.com \
    DJANGO_SUPERUSER_PASSWORD=adminpassword \
    python manage.py createsuperuser --noinput

As seen above... superuser credentials becomes

    superuser name: admin
    superuser pass: adminpassword

Next, let's begin create fake data, but before that deactivate current environment

    deactivate
    conda deactivate # if you use conda

If you don't want to create the superuser, there is one already created

    cp simulate/db_su.sqlite3 simulate/db_bak.sqlite3

Now, cd into the simulation directory and create a temporary environment

    cd simulate
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements-sim.txt

Next, create the fake data and populate the database with 5 persons (default is 1000)

    python3 create_fake_data.py 5

Now all users, have the password

    p@ssw0rd1

As said, the environment is temporary, so clean up and go back to your project

    deactivate
    conda deactivate # if you use conda
    rm -rf venv
    cd ..

And activate your dev environment, with or without conda.. whichever way you prefer...
# Creating Fake users

Populates the table db_sim.sqlite3 which you have to copy manually.

## Creating the Superuser

Here are 2 examples on how you can create the superuser...

1) There us a db_su.sqlite3 that is a clean users database. But if you want to create it by hand, it goes something like this:

Create superuser if needed

    DJANGO_SUPERUSER_USERNAME=admin \
    DJANGO_SUPERUSER_EMAIL=admin@example.com \
    DJANGO_SUPERUSER_PASSWORD=adminpassword \
    python manage.py createsuperuser --noinput

As seen above... superuser credentials becomes

    superuser name: admin
    superuser pass: adminpassword

2) But you have already db_su.sqlite3 which you may want to copy.. since its easier?

## Creating Users

The users are created in the db_sim.sqlite3 file.

### Initiate db_sim.sqlite3

Next, let's begin create fake data, but before that deactivate current environment

    cd simulate
    deactivate
    conda deactivate # if you use conda

If you don't want to create the superuser, there is one already created in db_su.sqlite3

    cp db_su.sqlite3 db_bak.sqlite3

the credetials to this superuser are given in the section above.

Let's create a temporary environment

    cd simulate # if you didn't already
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements-sim.txt

Next, create the fake data and populate the database with 5 persons (default is 1000)

    python3 create_fake_data.py 5

Now all users, have the NSA recommended password

    p@ssw0rd1

As said, the environment is temporary, so clean up and go back to your project

    deactivate
    conda deactivate # if you use conda
    rm -rf venv
    cd ..

And activate your dev environment, with or without conda.. whichever way you prefer...

## BUGS, ISSUES, ERRORS ETC

requrements-sim.txt has a bit more dependencies than needed, they do not however harm.

Some users have coma in their email.... that is OK for me (Mikael). If you want to fix it, then you can do it.

# Flyerz

## First Time Setup (Only Once)

Exit any current environment if active:

    conda deactivate

Then clone this project:

    git clone git@github.com:Mikael-Helin/Flyerz.git

Create the environment:

    cd Flyerz
    conda create -n flyerz_env python=3.12

Now you're ready to follow the steps in "Next Time You Work on the Project."

---

## Next Time You Work on the Project

If you are not in the `Flyerz` folder, then cd into it:

    cd Flyerz

Sync with the latest changes:

    conda activate flyerz_env
    git pull
    pip install -r requirements.txt

Now prepare to start to work on your branch

    git checkout -b feature/my_feature_is_better_than_yours
    python manage.py runserver
    code .

**When ending your day:**

Do never forget to push back your work

    git add .
    git commit -m "My awesome comment"
    git push origin feature/my_feature_is_better_than_yours

Go back to start

    git checkout main
    conda deactivate
    cd ..

---

## Reset Everything

If you need to reset the environment and start over:

1. Deactivate and remove the environment:

        conda deactivate
        conda remove --name flyerz_env --all

2. Delete the `Flyerz` folder.

3. Start over with `First Time Setup (Only Once)`

---

## Links

- [Git Collaboration Guide](https://github.com/NikolettaGr/Git-Collaborative)
- [Django Documentation](https://docs.djangoproject.com)
- [Conda Documentation](https://docs.conda.io/en/latest/)

## Contributors

- [Silvia](https://github.com/Da-Ronja)
# Flyerz

## First Time Setup (Only Once)

Exit any current environment if active:

    conda deactivate

Then clone this project:

    git clone git@github.com:Mikael-Helin/Flyerz.git

Create the environment and activate it:

    cd Flyerz
    conda create -n flyerz_env python=3.12
    conda activate flyerz_env

Install dependencies:

    pip install -r requirements.txt
    conda deactivate

Now you're ready to follow the steps in "Next time you work on the project."

---

## Next Time You Work on the Project

Ensure you're in the Flyerz folder.

**When starting your day:**

    conda activate flyerz_env
    git pull  # Sync with the latest changes
    git checkout -b feature/<your-feature-name>
    python manage.py runserver
    code .  # Open your editor

**When ending your day:**

    git push origin feature/<your-feature-name>
    conda deactivate

---

## Reset Everything

If you need to reset the environment and start over:

1. Deactivate and remove the environment:

        conda deactivate
        conda remove --name flyerz_env --all

2. Delete the `Flyerz` folder.

---

## Links

- [Git Collaboration Guide](https://github.com/NikolettaGr/Git-Collaborative)
- [Django Documentation](https://docs.djangoproject.com)
- [Conda Documentation](https://docs.conda.io/en/latest/)

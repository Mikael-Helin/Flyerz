# Flyerz

## First time you work on the project

Exit from your current environment if needed

    deactivate

Then clone this project

    git clone git@github.com:Mikael-Helin/Flyerz.git

Create the environment and enter it

    cd Flyerz
    conda create -n flyerz_env python=3.12
    conda activate flyerz_env

Install dependencies

    pip install -r requirements.txt
    code .

## Next Time when you work on the project

    conda activate flyerz_env
    code .

## Remove everything

In case you need to start over, this is what you do

Deactivate and remove the environment

    deactivate
    conda env list # To list, if you want to
    conda remove --name flyerz_env --all

Then delete the `Flyerz` folder.

## Links

    https://github.com/NikolettaGr/Git-Collaborative
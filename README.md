# Installation

## After cloning

You should first create a new virtual environment. Activate this virtual environment and install the dependencies.

```cli
# Install virtualenv
pip install virtualenv

# Create environment
virtualenv venv

# Activate environment
source venv/bin/activate

# On windows
# ./venv/Scripts/activate
```

```cli
pip install -r requirements.txt
```

You should now be able to run the server locally.

```cli
python manage.py runserver
```

## Administration Interface

Create a superuser if you haven't, already.
The default one for development is username `admin` with the same word as a password.

```cli
python manage.py createsuperuser
```

It will ask for some information, such as username, e-mail and password.
After creating this user you should be able to log in to the admin interface at route `/admin`.

To run postgresql:

```cli
pip install psycopg2-binary
```

## Heroku Upload

Heroku automatically recognizes it's uploading a django app _only_ if it finds the following files: 
  * requirements.txt: dependencies you specify for that heroku can automatically install them
  * setup.py: file that include sensitive credentials so that heroku can configure environmental variables
  * Procfile: file is used to explicitly declare your application’s process types and entry points. It is located in the root of your repository.
 
### requirements.txt
In here you specify your apps dependencies and their versions so that heroku knows what to install. To get packages version and place them in requirements.txt simply run _pip freeze_ and copy the packages you need inside requirements.txt file

## TODO

As the project goes on, the README will be updated.

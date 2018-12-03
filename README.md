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

## TODO

As the project goes on, the README will be updated.

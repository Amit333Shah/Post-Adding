Create an application that has two apps. 
1. User with user and Post model
    User : first_name, last_name, email, password, username
    Post : user, text, created_at, updated_at
   Foreign key relationship exists between User and Post on Model level not on Database level.
2. Products app with Product model.
    Product : name, weight, price, created_at, updated_at

Both of the apps should use two different databases.

/*-----------------------------------------------------------------------------*/
Installing Django with pip in a Virtual Environment
1 . Update your local package index with apt
apt update

2 . Check which version of Python you have installed. The version currently shipped with Ubuntu 20.04 is Python 3.8.2:
root@Django:~# python3 -V
Python 3.8.2

3 . Install pip from the Ubuntu repositories
apt install python3-pip python3-django

4 . Install the venv package with pip
apt install python3-venv

5 . Once that is done, you can now start a new project in Django. Remember that whenever you start a new project, start by creating and moving into a new project directory.
mkdir ~/newhostA
cd ~/newhostA
6 . Create a virtual environment within the project directory using the python command that’s compatible with your version of Python. We will call our virtual environment my_env

python3.8 -m venv my_env
This will install standalone versions of Python and pip into an isolated directory structure within your project directory. A directory will be created with the name you select, which will hold the file hierarchy where your packages will be installed.

7 . To install packages into the isolated environment, you must activate it by typing:
source my_env/bin/activate

Your prompt should change to reflect that you are now in your virtual environment. It will look something like:

(my_env) root@Django:~/newhostA#

8 . In your environment, install Django with pip
pip install django

9 . Verify the version installed
django-admin --version


/*----------------------------------------------------------------------------------------------*/
Creating a Sample Project
With Django installed, we can now start to create our project and test it on your development server using a virtual environment.

1 . Create a directory for your project

mkdir ~/my-django
cd ~/my-django
2 . Create your virtual environment

python3.8 -m venv my_env
3 . Activate the environment

source my_env/bin/activate
4 . Install django in the environment:
5 . To create your project, use django-admin <command> [options] which is Django’s command-line utility for administrative tasks. In each Django project, a manage.py is automatically created.

The startproject command enables to create a new project. The command creates a directory within your current working directory that includes:

manage.py which you can use to administer various Django-specific tasks.
a directory (with the same name as the project) that includes the actual project code.
6 . Create your project(myDjangoProject). Add a period at the end of the command to place the management script and inner directory in the current directory.

django-admin startproject myDjangoProject .
7 . Migrate the database (this example uses SQLite by default) using the migrate command with manage.py. Migrations apply any changes you’ve made to your Django models to your database schema.

python manage.py migrate
8 . Create an administrative user so that you can use the Djano admin interface using the createsuperuser command

python manage.py createsuperuser
9 . Answers the prompts which will ask for:

A username, an email address, and a password for your user.
An email
A password (containing at least 8 characters)
(my_env) root@Django:~/my-django# python manage.py createsuperuser
Username (leave blank to use 'root'): scaleway
Email address: usertest@example.com
Password:
Password (again):

pip install django

/*----------------Download all project dependencies------------------*/
$ pip install -r requirements.txt

/*-------------------------------For Different Database -----------------------------*/
1.Add in settings.py

# DATABASE_ROUTERS = ['Folder_name.file_name.class_name']

DATABASE_ROUTERS = ['task_project.ProductRouters.ProductRouter']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'product_db': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'Product.db.sqlite3',
    }
}

2.create ProductRouters.py in tesk_project
ProductRouters.py
class ProductRouter:
#route_app_labels = {'model name'}
    route_app_labels = {'Product'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'product_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'product_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'product_db'
        return None



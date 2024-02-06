# Portfolio (Built with Django)

Django project for making a Portfolio website.

### How to use this project

Clone this project:
```
git clone https://github.com/ahmedbatty/portfolio.git
```

Install dependencies (recommended to make new virtual environment for this project):
```
cd portfolio
pip install -r requirements.txt
```

Set Database:
```
python3 manage.py makemigrations
python3 manage.py migrate
```

Create Superuser:
```
python3 manage.py createsuperuser
```

Run server:
```
python3 manage.py runserver
```

#### Built With
- Django
- Bootstrap
- CKEditor
- [Start Bootstrap Clean Blog theme](https://startbootstrap.com/themes/clean-blog/)

#### Things to do
- Complete contact form, use [django-contact-form](https://django-contact-form.readthedocs.io/en/latest/)
- Add CK Editor in project model
- Blog: if image exists, show in header, otherwise show gradient, add color selector for gradient
- re-evaluate models: URLs, admin
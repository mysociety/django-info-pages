# django-info-pages

Simple support for static information pages and blog posts in Django.

## Install

    pip install django-info-pages

Add `'info'` to `INSTALLED_APPS`.

Then run the database migrations:

    python manage.py migrate info

Finally add the following to your `urls.py`:

```python
# ...

urlpatterns += (
    url(r'^info/', include('info.urls.pages')),
    url(r'^blog/', include('info.urls.blog')),
)

# ...
```

## Developing

Assuming you've got a clone of the git repo locally you can install the dependencies and run the tests with the following (you might want to create a new virtualenv or similar first):

    pip install -e '.[test]'
    python runtests.py

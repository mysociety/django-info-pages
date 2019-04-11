import io
from setuptools import setup, find_packages
from os import path


this_directory = path.abspath(path.dirname(__file__))
with io.open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name="django-info-pages",
    version="0.0.5",
    packages=find_packages(),
    author="mySociety developers",
    author_email="modules@mysociety.org",
    url="https://github.com/mysociety/django-info-pages",
    description="Editable info pages and basic blog functionality for Django",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="AGPL",
    keywords="django blog cms",
    include_package_data=True,
    install_requires=[
        'Django>=1.8.12,<2',
        'beautifulsoup4',
        'lxml',
        'Markdown',
        'django-markitup',
        'nose',
        'django-autocomplete-light==2.3.3',
        'django-file-archive==0.0.2',
        'mysociety-django-pagination==1.0.8',
        'django-slug-helpers>=0.0.3',
        'six==1.10.0'
    ],
    extras_require={
        'test': [
            'mock',
        ],
    },
)

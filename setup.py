from setuptools import setup, find_packages
setup(
    name = "django-info-pages",
    version = "0.0.1",
    packages = find_packages(),
    author = "Edmund von der Burg",
    author_email = "evdb@ecclestoad.co.uk",
    description = "Editable info pages and basic blog functionality for Django",
    license = "AGPL",
    keywords = "django blog cms",
    install_requires = [
        'Django>=1.8',
        'beautifulsoup4',
        'lxml',
        'django-markitup',
        'nose',
        'django-slug-helpers',
        'django-autocomplete-light',

        # CommentArchiveMixin from pombola.core.views
        # File from pombola.file_archive.models
    ]
)

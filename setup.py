from os import path
from setuptools import setup, find_packages

with open(path.join(path.dirname(__file__), 'README')) as f:
    readme = f.read()

setup(
    name="django-bbcode",
    version='1.0.2',
    description="Little helper application to parse and render bbcode",
    long_description=readme,
    url="https://github.com/camilleb/django-bbcode",
    author="marcinn (Marcin Nowak)",
    packages=find_packages(),
    include_package_data=True,
)

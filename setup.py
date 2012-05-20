import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-dynamicforms',
    version='0.0.1',
    author='Aleksandr Aibulatov',
    author_email='zap.aibulatov@gmail.com',
    description=('Django application for creating dynmaicforms'),
    license="BSD",
    keywords="django, forms, dynamic, application",
    url='https://github.com/Zapix/django-dynamicforms',
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ]
)

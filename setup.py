#!/usr/bin/env python
from setuptools import setup, find_packages

with open('README.rst', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='locallibs',
    version='0.1.1.dev1',
    description='Local Library Management Tool',
    author='Md. Sabuj Sarker',
    author_email='md.sabuj.sarker@gmail.com',
    url='https://github.com/SabujXi/locallibs',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'locallibs = locallibs:locallibs_cli'
        ]
    },
    data_files=[('', ['README.rst'])],
    package_data={
        '': ['*.txt', '*.rst', '*.md'],
    },
    python_requires='>=2.7',
    long_description=long_description
)

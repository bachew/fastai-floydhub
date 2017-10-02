# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


config = {
    'name': 'fastai-floydhub',
    'version': '0.0.1',
    'description': 'Run fast.ai notebooks on FloydHub',
    'license': 'MIT',
    'author': 'Chew Boon Aik',
    'author_email': 'bachew@gmail.com',
    'url': 'https://github.com/bachew/fastai-floydhub',
    'packages': find_packages(),
    'install_requires': [
        'click>=6.7',
        'floyd-cli>=0.10.11',
        'py>=1.4.34',
    ],
    'entry_points': {
        'console_scripts': [
            'ff=ff.cli:cmd',
        ],
    },
    'zip_safe': False,
    'classifiers': [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7'

    ],
}
setup(**config)

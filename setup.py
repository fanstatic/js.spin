# -*- coding: utf-8 -*-

import os

from setuptools import find_packages
from setuptools import setup

version = '2.0.2'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (read('README.txt')
                    + '\n' +
                    read('js', 'spin', 'test_spin.js.txt')
                    + '\n' +
                    read('CHANGES.txt'))

setup(
    name='js.spin',
    version=version,
    description="Fanstatic packaging of spin.js",
    long_description=long_description,
    classifiers=[],
    keywords='',
    author='Andreas Kaiser',
    author_email='disko@binary-punks.com',
    url='https://github.com/disko/js.spin',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    setup_requires=[],
    install_requires=[
        'fanstatic',
        'js.jquery',
        'setuptools',
    ],
    entry_points={
        'fanstatic.libraries': [
            'spin.js = js.spin:library',
        ],
    },
)

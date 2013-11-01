#!/usr/bin/env python

from setuptools import setup, find_packages
from requirements_utils import parse_dependency_links, parse_requirements

### Fix atexit._run_exitfuncs error raised when running tests.
### See http://bugs.python.org/issue15881#msg170215
try:
    import multiprocessing
except ImportError:
    pass

with open("unknown/version.py") as f:
    exec(f.read())

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    long_description = ''

setup(
    name = 'unknown',
    version = __version__,

    description = 'Lightweight HTTP application',
    long_description = long_description,

    author = 'Jesper Brown',
    author_email = 'jesper.brown@edgeware.tv',

    scripts = ["bin/unknown"],
    zip_safe=False,
    packages = find_packages(),
    include_package_data = True,
    install_requires = parse_requirements('requirements.txt'),
    dependency_links = parse_dependency_links('requirements.txt'),
    setup_requires = ['nose>=1.0'],
    tests_require = parse_requirements('requirements-test.txt'),
    test_suite="nose.collector",
    entry_points = {
        'console_scripts': [
            'unknown = unknown.main:main'
    ]},
)
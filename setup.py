"""
Setup script.
"""
import os
import sys
from setuptools import setup

version = '3.0.0.rc.2'

if sys.argv[-1] == 'tag':
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push origin master --tags")
    sys.exit()

if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    os.system("python setup.py bdist_wheel upload")
    sys.exit()

if sys.argv[-1] == 'test':
    test_requirements = [
        'pytest',
        'flake8',
        'coverage'
    ]
    try:
        modules = map(__import__, test_requirements)
    except ImportError as e:
        err_msg = e.message.replace("No module named ", "")
        msg = "%s is not installed. Install your test requirements." % err_msg
        raise ImportError(msg)
    os.system('py.test')
    sys.exit()

# From docs for pytest-runner
needs_pytest = any(arg in ['pytest', 'test', 'ptr'] for arg in sys.argv)
setup_requires = ['pytest-runner'] if needs_pytest else []

setup(
    author='Josh Wilson',
    author_email='josh.wilson@fivestars.com',
    description='falcon-authentication',
    download_url='',
    setup_requires=setup_requires,
    install_requires=[
        'falcon'
    ],
    extras_require={
        'backend-hawk': ['mohawk~=1.0'],
        'backend-jwt': ['pyjwt~=1.7']
    },
    license='MIT',
    name='falcon-authentication',
    packages=[
        'falcon_authentication',
    ],
    scripts=[],
    test_suite='tests',
    tests_require=[
        'pytest<3.3.0',
        'pytest-cov~=2.4',
        'pytest-mock~=1.6',
        'python-coveralls~=2.9',
    ],
    url='https://github.com/jcwilson/falcon-authentication',
    version=version,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)

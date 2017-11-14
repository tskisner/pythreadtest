#!/usr/bin/env python

import glob
import os
import sys
import re
import subprocess

import numpy as np

from setuptools import find_packages, setup, Extension
from Cython.Build import cythonize

from setuptools.command.install import install



extensions = None

ext_work = Extension (
    'pythreadtest.work',
    include_dirs = [np.get_include()],
    sources = [
        'pythreadtest/work.pyx'
    ]
)

extensions = cythonize([
    ext_work
])


# scripts to install

scripts = glob.glob('bin/*.py')


setup (
    name = 'pythreadtest',
    provides = 'pythreadtest',
    version = '0.0.1',
    description = 'Python Thread Test',
    author = 'Theodore Kisner',
    author_email = 'mail@theodorekisner.com',
    url = 'https://github.com/tskisner/pythreadtest',
    ext_modules = extensions,
    packages = ['pythreadtest'],
    scripts = scripts,
    license = 'BSD',
    requires = ['Python (>3.5.0)']
)

# extra cleanup of cython generated sources

if "clean" in sys.argv:
    # Just in case the build directory was created by accident,
    # note that shell=True should be OK here because the command is constant.
    subprocess.Popen("rm -rf build", shell=True, executable="/bin/bash")
    subprocess.Popen("rm -rf dist", shell=True, executable="/bin/bash")
    subprocess.Popen("rm -rf pythreadtest/*.c", shell=True, executable="/bin/bash")
    subprocess.Popen("rm -rf pythreadtest/*.so", shell=True, executable="/bin/bash")
    subprocess.Popen("rm -rf pythreadtest/*.pyc", shell=True, executable="/bin/bash")


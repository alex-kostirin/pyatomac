# Copyright (c) 2017 VMware, Inc; AO Kaspersky Lab. All Rights Reserved.

# This file is part of ATOMac.

# ATOMac is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by the Free
# Software Foundation version 2 and no later version.

# ATOMac is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License version 2
# for more details.

# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51 Franklin
# St, Fifth Floor, Boston, MA 02110-1301 USA.

from setuptools import setup, Extension
import os


def read(fname):
    """
    Returns the contents of the specified file located in the same dir as
    the script
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


source_files = [
    'atomac/_a11y/a11ymodule.m',
    'atomac/_a11y/conversion.m',
    'atomac/_a11y/axlib.m',
]

_a11y = Extension(
    'atomac._a11y',
    sources=source_files,
    extra_link_args=[
        '-framework', 'ApplicationServices',
        '-framework', 'Carbon',
        '-framework', 'AppKit',
    ],
)

setup(
    name='pyatomac',
    version='2.0.5',
    author='Alexey Kostyrin',
    author_email='Alexey.Kostyrin@kaspersky.com',
    url='https://pypi.python.org/pypi/pyathom/',
    description=("Automated Testing on Mac - test GUI applications "
                 "written in Cocoa by using Apple's Accessibility API"),
    license='GPLv2',
    long_description=read('README.rst'),
    ext_modules=[_a11y],
    packages=['atomac', 'atomac.ldtpd', 'atomac.ldtp', 'atomac.ooldtp'],
    install_requires=['pyobjc>=4.0'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: MacOS X :: Cocoa',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
    ],
    entry_points={
        'console_scripts': ['ldtp = atomac.ldtpd:main'],
    },
)

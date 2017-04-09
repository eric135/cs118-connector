#!/usr/bin/env python
'''Setuptools params'''

import setuptools

setuptools.setup(
    name='riddikulus-connector',
    version='0.0.1',
    description='Network controller to connect to Ridikkulus class project',
    author='Alex Afanasyev',
    author_email='aa@cs.fiu.edu',
    license='GPL3+',
    zip_safe=False,
    classifiers=[
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Topic :: Internet",
    ],
    include_package_data=True,
    packages=setuptools.find_packages(),
    install_requires=[
          'zeroc-ice',
      ],
)


#!/usr/bin/env python

from setuptools import setup

setup(
    name='sns-pipe',
    version='0.1',
    description='Publishes standard input to an Amazon SNS topic.',
    author='Raymond Butcher',
    author_email='ray@bashton.com',
    url='https://github.com/BashtonLtd/sns-pipe',
    license='Apache License 2.0',
    packages=(
        'snspipe',
    ),
    scripts=(
        'bin/sns-pipe',
    ),
    install_requires=(
        'boto3',
    ),
)

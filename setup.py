# -*- coding: utf-8 -*-
"""Setup for aiida-metavo-schedulers python package."""
# please see https://github.com/pzarabadip/aiida-metavo-scheduler/issues/2#issue-804035777
# for reason of limiting the aiida-core version to <1.6
import json
from setuptools import setup, find_packages

if __name__ == '__main__':
    # Provide static information in setup.json
    # such that it can be discovered automatically
    with open('setup.json', 'r') as info:
        KWARGS = json.load(info)
    setup(
        packages=find_packages(),
        long_description=open('README.md').read(),
        long_description_content_type='text/markdown',
        **KWARGS
    )

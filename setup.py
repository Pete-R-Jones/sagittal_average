import argparse
from setuptools import setup, find_packages
setup(
    name="sagittal_average",
    version="0.1.0",
    packages=find_packages(),
    install_requires=['numpy','argparse'],
    entry_points ={
        'console_scripts': [
            'sagittal_average_run = command:run'
        ]
    }
)

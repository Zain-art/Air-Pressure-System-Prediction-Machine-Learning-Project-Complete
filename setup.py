from setuptools import find_packages,setup
from typing import List

# ========================
setup(
    name='ml_project_from_scratch',
    version='0.0.1',
    author='Zian Ahmad',
author_email='zainprogrammers@gmail.com',
packages=find_packages(),
   
    install_requires=[
        "pymongo"
        # Add your project dependencies here
    ],
    # Add other arguments as needed
)
from setuptools import find_packages,setup
from typing import List

# --------------------
def get_requirements()->list[str]:
    requirements_list=list[str] = []
    return requirements_list
# ========================
setup(
    name='ml_project_from_scratch',
    version='0.0.1',
    author='Zian Ahmad',
author_email='zainprogrammers@gmail.com',
packages=find_packages(),
   
    install_requires=get_requirements()
          # Add other arguments as needed
)
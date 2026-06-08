from setuptools import setup, find_packages
from typing import List


def get_requirements() -> List[str]:
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        return []
    return requirement_lst

setup(
    name='ml_project',
    version='0.0.1',
    author='Kunal patil',
    packages=find_packages(),
    install_requires=get_requirements()
    )
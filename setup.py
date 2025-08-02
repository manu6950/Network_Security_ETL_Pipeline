from setuptools import find_packages, setup
# import List from the typing module 
from typing import List

def get_requirements() -> List[str]:
    """This function will return a list of requirements."""
    requirements_list = []
    try:
        with open('requirements.txt', 'r') as file:
            # Read lines from the file
            lines = file.readlines()
            # process each file
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirements_list.append(requirement)
    except FileNotFoundError:
        print('requirements.txt file not found.')
    return requirements_list

print(get_requirements())


setup(
    name='network_security',
    version='0.0.1',
    author='Kreshnik',
    author_email='KrishnaX06@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
)
from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements.txt
    """
    requirement_lst:List[str]=[]
    try:
        with open("requirements.txt", 'r') as file:
            ## Read lines form the file
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                ## Ignore the empty lines and -e.
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("Requirements.txt file not found!")

    return requirement_lst

setup(
    name="NetworkSecurity",
    verison="0.0.1",
    author="Anmol Rana",
    author_email="anmolrana909@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
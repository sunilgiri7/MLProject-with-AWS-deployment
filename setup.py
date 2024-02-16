from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function return a list of requirements
    '''
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "")for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements
setup(
    name="ML-Project-with-AWS" ,
    version="0.0.1",
    author="Sunil",
    author_email="seungiri841@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")
)
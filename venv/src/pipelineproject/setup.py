from setuptools import find_packages, setup
from typing import List 

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)-> List[str]: 
    requirements = []
    with open(file_path) as file_obj: 
        requirements = file_obj.readlines()
        requirements = [req.replace ("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements: 
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name = "PipelineProject", 
    version = "0.0.1", 
    author = "Sagnik Sarkar", 
    description= "A trial End to End ML project created for First batch of LP students",
    author_email= "sagnik.sarkar22-24@bibs.co.in", 
    install_requires = get_requirements("requirements.txt"),
    packages= find_packages()
    )
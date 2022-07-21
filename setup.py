from setuptools import setup, find_packages
from typing import List


# Declaring variables for setup functions
PROJECT_NAME = "housing-predictor"
VERSION="0.0.3"
AUTHOR="Divyanshu Kumar"
DESCRIPTION= "This is a first FSDS Machine Learning Project"
PACKAGES=find_packages()
REQUIREMENT_FILE_NAME="requirements.txt"


def get_requirements_list() ->List[str]:
    """
    Description: Returns list of requirements from requirements.txt file

    Return: List of library names 
    """

    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list= [lib_name.replace("\n","") for lib_name in requirement_file.readlines()]
        if "-e ." in requirement_list:
            requirement_list.remove("-e .")
        return requirement_list


setup(
    name= PROJECT_NAME,
    version=VERSION,
    author = AUTHOR,
    description=DESCRIPTION,
    packages= find_packages(),
    install_requires=get_requirements_list()
)
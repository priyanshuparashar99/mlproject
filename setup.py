from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(filepath) -> List[str]:
    with open(filepath) as file_obj:
        requirements = file_obj.read().splitlines()
        file_obj.close()
        
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    print(requirements)
    return requirements


setup(name="mlproject", version="0.0.1", author="Sujeet Gund", author_email="sujeetgund@gmail.com", packages=find_packages(), install_requires=get_requirements("requirements.txt"))
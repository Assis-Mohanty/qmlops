from setuptools import find_packages,setup
from typing import List
def get_requirments(file_path:str)->List[str]:
    """
    this function will return the list of requirements
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
        return requirements

setup(
    name='qmlops',
    version='0.1',
    author='Assis Mohanty',
    author_email='assis.mohanty.98@gmail.com',
    install_requires=get_requirments('requirements.txt')
)
from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return list of req 
    '''
    requirements=[]
    he='-e .'
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","")for req in requirements]
        if he in requirements:
            requirements.remove(he)
    return requirements
setup(
    name='project',
    version='0.0.1',
    author='hari',
    author_email='hraj488.884@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path) -> List[str]:
    """
        This will return a list of requirements
    """
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name="Agentic recruitement screening scheduler",
    version="0.0.1",
    description="A multi agentic system that takes resumes and matches them to a given JD and schedules a meeting",
    author="Vamshi Adimalla",
    author_email="vamshi.codes@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
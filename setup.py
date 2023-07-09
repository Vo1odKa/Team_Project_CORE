from setuptools import setup, find_namespace_packages

setup(
    name='Personalhelper',
    version='1.0',
    packages=find_namespace_packages(),
    entry_points={"console_scripts": ["personal_helper=personal_helper.personal_helper.personal_helper:main"]}
)
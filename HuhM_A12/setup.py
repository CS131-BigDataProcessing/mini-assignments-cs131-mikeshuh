from setuptools import setup, find_packages

setup(
    name='crime_dataset_test',                      # Package name
    version='1.0',                                  # Package version
    packages=find_packages(),                       # Automatically find modules
    install_requires=[
        'pandas',
        'numpy'
    ],                                              # Dependencies, if any
    description='A simple crime dataset package',   # Short description
    author='Michael Huh',
    author_email='michael.huh@sjsu.edu',
)
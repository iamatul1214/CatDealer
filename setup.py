from setuptools import setup, find_packages

with open('README.md','r') as file:
    long_description=file.read()

setup(
   name='CatDealer',
   version='1.0.1',
   description='A library which can deal with Categorical values in a dataframe',
   license="MIT",
   long_description=long_description,
   author='Atul Rai',
   author_email='iamatul1214@gmail.com',
   url="https://github.com/iamatul1214/catergorical_dataset_handling",
   # packages=['NanDealer'], #same as name
    packages=['CatDealer'],
    #No requirement of external packages as dependencies
    classifiers=['Programming Language :: Python :: 3.8',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License']


)
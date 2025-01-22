# setup.py
from setuptools import setup, find_packages

setup(
    name="read_sourcefile",  
    version="0.1.0",   
    packages=find_packages(),  
    install_requires=[  
        "nbformat",
        "io",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple example library",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/byungil-an/read_sourcefile", 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License", 
        "Operating System :: OS Independent",
    ],
)

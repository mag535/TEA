# setup for package MeTEA (Metagenomic Taxa Evaluation and Assessment)

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as readme_file:
    readme = readme_file.read()

requirements = ["numpy>=1", "pandas>=1", "openpyxl>=3"]

setup(name="MeTEA",
        version="0.0.3",
        author="Melissa Gray",
        author_email="mag535@drexel.edu",
        description="A package to parse, organize, calculate, and save data from metagenomic profile files",
        long_description=readme,
        long_description_content_type="text/markdown",
        url="https://github.com/mag535/MeTEA/",
        packages=find_packages(),
		install_requirements=requirements,
        classifiers=[
            "Operating System :: OS Independent",
            "Intended Audience :: Science/Research",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.7",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"]
        )

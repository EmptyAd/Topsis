from setuptools import setup, find_packages

setup(
    name="topsis",
    version="0.1.0",
    author="Avi Srivastava",
    author_email="asrivastava1_be22@thapar.edu",
    description="A Python package for Topsis implementation.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/EmptyAd/Topsis",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "openpyxl",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

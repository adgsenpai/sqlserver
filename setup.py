from setuptools import setup, find_packages

setup(
    name="sqlserver",
    version="0.0.9",
    author="Ashlin Darius Govindasamy",
    author_email="adgrules@hotmail.com",
    url="https://www.adgstudios.co.za",
    description="A class used to simplify pyodbc",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license='MIT', 
    install_requires=["pyodbc"]
)

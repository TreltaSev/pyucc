from setuptools import setup, find_packages

__longdescription = open("README.md", 'r').read()

setup(
    name="pyucc",
    version="1.5",
    description="A high level, unoptimized, colored console written in python.",
    long_description=__longdescription,
    long_description_content_type="text/markdown",
    author="Trelta",
    author_email="treltasev@gmail.com",
    url="https://github.com/treltasev/pyucc",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    entry_points = {
      "console_scripts": [
        "pyucc = pyucc.cli:main"
      ]
    }
)
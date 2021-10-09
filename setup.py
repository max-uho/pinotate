import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pinotate",
    version="0.0.2",
    packages=setuptools.find_packages(),
)
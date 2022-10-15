from io import open

from setuptools import setup


def read(filename):
    with open(filename, encoding="utf-8") as file:
        return file.read()


def requirements():
    with open("requirements.txt", "r") as req:
        return [r for r in req.read().split("\n") if r]


setup(
    name="keyrt",
    version="0.0.1a4",
    packages=["keyrt", "keyrt.models"],
    url="https://github.com/WhiteApfel/keyrt",
    license="Mozilla Public License 2.0",
    author="WhiteApfel",
    author_email="white@pfel.ru",
    description="KeyRT",
    install_requires=requirements(),
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
)

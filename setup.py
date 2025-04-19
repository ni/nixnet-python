import os
from setuptools import setup


pypi_name = "nixnet"


def read_contents(file_to_read):
    with open(file_to_read, "r") as f:
        return f.read()


def get_version():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    version_path = os.path.join(script_dir, pypi_name, "VERSION")
    return read_contents(version_path).strip()


setup(
    name=pypi_name,
    version=get_version(),
    description="NI-XNET Python API",
    long_description=read_contents("README.rst"),
    author="National Instruments",
    author_email="opensource@ni.com",
    url="https://github.com/ni/nixnet-python",
    keywords=["nixnet"],
    license="MIT",
    include_package_data=True,
    packages=["nixnet"],
    install_requires=["six"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Science/Research",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: System :: Hardware :: Hardware Drivers",
    ],
    package_data={pypi_name: ["VERSION"]},
)

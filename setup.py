from setuptools import setup

with open("README.md", "r") as des:
    long_description=des.read()

setup(
    name="superfluid-finance",
    version="0.0.4",
    description="A python package for interacting with the superfluid-finance protocol in your application",
    py_modules=[
        "superfluid_finance"
    ],
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent"
    ],
    include_package_data=True,
    install_requires= [
        "eth-brownie",
        "web3"
    ],
    extras_require = {
        "dev": [
            "pytest>=3.7"
        ]
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/phydy/superfluidpy",
    author="Phidel Musungu",
    author_email="mphidel@gmail.com",
    maintainer="Phidel Musungu",
    maintainer_email="mphidel@gmail.com"
)
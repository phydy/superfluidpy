from setuptools import setup

with open("README.md", "r") as des:
    long_description=des.read()

setup(
    name="superfluidpy",
    version="0.0.1",
    description="A python package for interacting with the superfluid-finance protocol in your application",
    py_modules=[
        "host",
        "CFAV1",
        "IDAV1",
        "provider",
        "supertoken",
        "supertokenFactory",
        "initializer",
        "provider",
        "token_addresses",
        "account_provider",
        "con_addresses"
    ],
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Development Status :: 3 - Alpha",
        "Operating System :: OS Independent"
    ],
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
from setuptools import setup

setup(
    name="superfluid_finance",
    version="0.0.1",
    description="A python pachage for interacting with the superfluid-finance protocol in your application",
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
        "Lincense :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent"
    ],
    install_requires= [
        "eth-brownie"
    ],
    extras_require = {
        "dev": ["pytest>=3.7"]
    }
)
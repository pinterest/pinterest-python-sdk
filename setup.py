"""
Pinterest Client Package Setup
"""
from pathlib import Path
from setuptools import setup, find_namespace_packages

REQUIRES = [
  "urllib3==1.26.12",
  "python-dateutil",
  "python-dotenv==0.20.0",
  "six==1.16.0",
  "Pinterest-Generated-Client==0.1.3"
]

long_description = (Path(__file__).parent / "README.md").read_text()

setup(
    name="pinterest-api-sdk",
    description="Pinterest SDK",
    version="0.1.1",
    author="pinterest, inc.",
    author_email="sdk@pinterest.com",
    url="https://github.com/pinterest/pinterest-python-sdk",
    install_requires=REQUIRES,
    include_package_data=True,
    packages=find_namespace_packages(
        include=['pinterest.*'],
        exclude=[
            'sample',
            'sample.*',
            'tests',
            'tests.*',
            '.github',
        ]
    ),
    license="MIT",
    long_description=long_description,
    long_description_content_type='text/markdown',
)

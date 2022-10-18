"""
Pinterest Client Package Setup
"""
from setuptools import setup, find_namespace_packages

REQUIRES = [
  "urllib3==1.26.12",
  "python-dateutil",
  "python-dotenv==0.20.0",
  "six==1.16.0",
  "Pinterest-Generated-Client @ git+https://github.com/pinterest/pinterest-python-generated-api-client.git"
]

setup(
    name="pinterest-sdk",
    description="Pinterest SDK",
    version="0.1.0-wip",
    author="pinterest, inc.",
    author_email="pinterest-api@pinterest.com",
    url="https://github.com/pinternal/pinterest-python-sdk",
    install_requires=REQUIRES,
    include_package_data=True,
    packages=find_namespace_packages(
        include=['pinterest.*'],
        exclude=[
            'sample',
            'sample.*',
            'tests',
            'tests.*',
            'integration_tests',
            'integration_tests.*',
            '.github',
        ]
    ),
    license="MIT",
    long_description="""
    Pinterest &#39;s SDK
   """
)

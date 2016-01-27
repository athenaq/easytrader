from setuptools import setup, find_packages

setup(
    name="easytrader",
    version="0.1",
    packages=find_packages(),
    package_data={
        # if any package contains *.json or *.jar files, include them:
        '': ['*.json', '*.jar'],
    },

    # metadata for upload to PyPI
    auther="me",
    auther_email="me@example.com",
    license='GPL',
    description="easytrader is a webtrading program for chinese stocks",
    keywords="China stock trading",
    url="http://me.org",
)

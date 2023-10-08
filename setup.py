from setuptools import setup, find_packages

setup(
	name="databases",
	version="0.1.0",
	packages=find_packages(),
    install_requires=[
        "redis[hiredis]",
        "pymysql",
        "aiomysql"
	],
)
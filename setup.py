from setuptools import setup, find_packages

setup(
	name="databases",
	version="0.1.0",
	packages=find_packages(),
    install_requires=[

    ],
    extras_require={
        "all": ["redis[hiredis]", "pymysql", "aiomysql"],
        "redis": ["redis[hiredis]"],
        "pymysql": ["pymysql"],
        "aiomysql": ["aiomysql"],
    }
)
from setuptools import setup, find_packages

setup(
    name="autointerface",
    version="0.0.1",
    packages=find_packages(exclude=[]),
    python_requires=">=3.4",
    data_files=[
    ],
    entry_points={
        'console_scripts': [
        ]
    },
    install_requires=['peewee', 'flask', 'pymysql', 'click']
)

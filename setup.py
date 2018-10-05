from setuptools import setup, find_packages

requirements = []
with open('requirements.txt') as fp:
    for line in requirements:
        requirement = line.strip()
        if requirement and not requirement.startswith('#'):
            requirements.append(requirement)
print(requirements)

setup(
    name="autointerface",
    version="0.0.1",
    packages=find_packages(exclude=[]),
    python_requires=">=3.4",
    data_files=[
        ('data', ['data/backup.sql'])
    ],
    entry_points={
        'console_scripts': [
        ]
    },
    install_requires=requirements
)

from setuptools import find_packages, setup

dependencies = ['click']

setup(
    name='my_clippings_to_json',
    version='0.1.0',
    url='https://github.com/maximumhallinan/my-clippings-to-json',
    author='Maximum Hallinan',
    description='A command-line tool for converting \'My Clippings.txt\' to JSON',
    platforms='any',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'my_clippings_to_json = my_clippings_to_json.cli:main',
        ],
    }        
)

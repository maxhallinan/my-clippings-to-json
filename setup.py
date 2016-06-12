from setuptools import find_packages, setup

dependencies = ['click']

setup(
    author='Maximum Hallinan',
    author_email='maxhallinan@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Text Processing :: Linguistic',
    ],
    description='Format \'Kindle/documents/My Clippings.txt\' as JSON',
    entry_points={
        'console_scripts': [
            'my_clippings_to_json = my_clippings_to_json.cli:main',
        ],
    },
    include_package_data=True,
    install_requires=dependencies,
    keywords='Kindle My Clippings highlights notes bookmarks',
    license='MIT',
    name='my_clippings_to_json',
    packages=find_packages(exclude=['tests']),
    platforms='any',
    url='https://github.com/maximumhallinan/my-clippings-to-json',
    version='0.1.0',
    zip_safe=False)

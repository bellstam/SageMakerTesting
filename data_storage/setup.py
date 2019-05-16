from setuptools import setup, find_packages

setup(
    name='data_storage',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
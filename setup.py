from setuptools import setup, find_packages

setup(
    name='Oliver',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'console_scripts': [
                'submit = package.scripts.submit:cli',
            ],
        ],
    }
)
from setuptools import setup, find_packages

setup(
    name='BusTransactions',  # Name of your package
    version='0.1.0',  # Version number
    description='A Python package for managing bus transactions.',  # Short description
    url='https://github.com/Uhgtred/BusTransactions',  # URL to the homepage (like a github repo)
    author='Markus Kösters',  # Your name
    author_email='markus_koesters@gmx.de',  # Your email
    license='GPLv3',  # License type
    packages=find_packages(),  # Automatically detect all packages in the current directory
    install_requires=[
        # List of dependencies
    ],
    classifiers=[
        # https://pypi.org/classifiers/
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.6',  # Minimum version of Python required
)
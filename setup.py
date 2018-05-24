"""A setuptools based setup module for functional helpers."""

from setuptools import setup, find_packages

setup(
    name='functional-helpers',
    version='0.1.0',
    description='Helpers for functional-alike integration of computations with I/O into a script',
    url='https://github.com/gmrukwa/functional-helpers',
    author='Grzegorz Mrukwa',
    author_email='g.mrukwa@gmail.com',
    classifiers=[
        # based on https://pypi.python.org/pypi?%3Aaction=list_classifiers
		'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(exclude=['test']),
    # based on https://packaging.python.org/discussions/install-requires-vs-requirements/
    install_requires=[
        'tqdm>=4.11.2',
        'typing>=3.6.2'
    ],
    python_requires='>=3.4',
    package_data={
    }
)

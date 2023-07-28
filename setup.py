from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='evque',
    version='1.0.3',
    description='A simple event queue library with support for topics.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Ahmad Siavashi',
    author_email='siavashi@aut.ac.ir',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)

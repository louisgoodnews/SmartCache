#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from setuptools import setup, find_packages

# Read the README for the long description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

# Read requirements
requirements = [
    "dateutil @ git+https://github.com/louisgoodnews/DateUtil.git#egg=dateutil",
    "logger @ git+https://github.com/louisgoodnews/Logger.git#egg=logger",
]

# Development requirements
extras_require = {
    "dev": [
        "black>=23.0.0",
        "isort>=5.12.0",
        "mypy>=1.0.0",
        "pytest>=7.0.0",
        "pytest-cov>=4.0.0",
        "pre-commit>=2.0.0",
    ],
    "docs": [
        "sphinx>=6.0.0",
        "sphinx-rtd-theme>=1.0.0",
        "sphinx-autodoc-typehints>=1.0.0",
    ],
}

setup(
    name="smartcache",
    version="0.1.0",
    description="An intelligent object caching library for Python applications.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Louis Goodnews",
    author_email="louisgoodnews95@gmail.com",
    url="https://github.com/louisgoodnews/Cacheing",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require=extras_require,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Caching",
        "Typing :: Typed",
    ],
    keywords="cache caching memory-cache object-cache ttl",
    project_urls={
        "Bug Reports": "https://github.com/louisgoodnews/Cacheing/issues",
        "Source": "https://github.com/louisgoodnews/Cacheing",
    },
    include_package_data=True,
    zip_safe=False,
)

# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = ""

setup(
    long_description=readme,
    name="routeros-diff",
    version="0.1.0",
    description="Tools for parsing & diffing RouterOS configuration files. Can produce config file patches.",
    python_requires="==3.*,>=3.6.0",
    project_urls={"repository": "https://github.com/gardunha/routeros-diff"},
    author="Adam Charnock",
    author_email="adam.charnock@gardunha.net",
    license="MIT",
    entry_points={
        "console_scripts": [
            "routeros_diff = routeros_diff.commands.diff:run",
            "ros_diff = routeros_diff.commands.diff:run",
            "routeros_prettify = routeros_diff.commands.prettify:run",
            "ros_prettify = routeros_diff.commands.prettify:run",
        ]
    },
    packages=["routeros_diff", "routeros_diff.commands"],
    package_dir={"": "."},
    package_data={},
    install_requires=["python-dateutil==2.*,>=2.8.1"],
)

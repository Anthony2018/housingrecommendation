import os
from setuptools import setup, find_packages
PACKAGES = find_packages()


opts = dict(name="housingrecommendation",
            description='fisrt version',
            url="https://github.com/adonis-wyc/housingrecommendation",
            license="MIT"
            author="Yucehn Wang,Xintong Xu, Yuhan Gao, Jinlin Xiang",
            author_email="mark96@uw.edu",
            version= "__version__ 1.0",
            packages='PACKAGES',
            install_requires='REQUIRES',
            requires=["numpy", "pandas", "sklearn"])


if __name__ == '__main__':
    setup(**opts)

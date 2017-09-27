'''
Created on 2017年9月27日

@author: Mi
'''
from setuptools import setup

setup(
    name='proxy',
    py_modules=['proxy','regeditor'],
    install_requires=['docopt'],
    entry_points={
        'console_scripts': ['proxy=proxy:cli']
    }
)
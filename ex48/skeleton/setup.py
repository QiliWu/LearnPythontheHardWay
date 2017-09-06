try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Qili Wu',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'wuqili@mail2.sysu.edu.cn',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts':[],
    'name': 'projectname'
}

setup(**config)
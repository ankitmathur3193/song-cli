from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup

def read(fname):
	return open(os.path.join(os.path.dirname(__file__),fname)).read()


setup(
	name = 'song',
	version = '1.0',
	author = 'ankit mathur',
	author_email = 'ankitmathur.dtu@gmail.com',
	license = 'UNLICENSE',
	description = ' A script to download hindi and punjabi songs from internet',
	long_description = 'will include something',
	url = '',
	keywords = 'song download script',
	packages = find_packages(exclude=['docs', 'tests*']),
	install_requires = ['docopt','requests','BeautifulSoup'],
	classifiers = [
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
	entry_points = {
        'console_scripts': [
            'song=song.cli:main',
        ],
    },

	)	
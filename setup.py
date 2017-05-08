from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup

this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()


setup(
	name = 'song',
	version = '1.2',
	author = 'ankit mathur',
	author_email = 'ankitmathur.dtu@gmail.com',
	license = 'UNLICENSE',
	description = ' A script to download hindi and punjabi songs from internet',
	long_description = long_description,
	url = 'https://github.com/ankitmathur3193/song-cli',
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
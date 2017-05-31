from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup
from song import __version__ as VERSION
this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()


setup(
	name = 'song',
	version = VERSION,
	author = 'ankit mathur',
	author_email = 'ankitmathur.dtu@gmail.com',
	license = 'MIT',
	description = ' A script to download hindi and punjabi songs from internet',
	long_description = long_description,
	url = 'https://github.com/ankitmathur3193/song-cli',
	keywords = ['song', 'download', 'script', 'youtube-dl','tqdm','requests','beautiful soup'],
	packages = find_packages(exclude=['docs', 'tests*']),
	install_requires = ['docopt==0.6.2','requests==2.16.4','BeautifulSoup==3.2.1','tqdm==4.11.2','youtube-dl==2017.05.26'],
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
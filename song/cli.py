"""
song

Usage:
  song -d [--download-all] TEXT...
  song -h | --help
  song --version
  song -y TEXT...
  song -t <textfile.txt>

Options:
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  song -d wo lamhe

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/ankitmathur3193/song-cli
"""
from inspect import getmembers, isclass

from docopt import docopt

from __init__ import __version__ as VERSION

def main():
    """Main CLI entrypoint."""
    #print VERSION
    from commands.download import Download
    options = docopt(__doc__, version=VERSION)
    #print "You reached here"
    #print options
    print "working."
    p=Download(options)
    p.run()

main()

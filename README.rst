|PyPI version| |license| # SONG DOWNLOADER # A **command line**
interface for **downloading Bollywood and Punjabi Songs** from Internet
## For Installing ##

::

    pip install song

For Upgrading
-------------

::

    pip install --upgrade song

For Uninstalling
----------------

::

    pip uninstall song

Usage:
------

::

    song -d [ song_name | artist_name | movie_name ]

Example:
--------

-  .. rubric:: For Downloading Song (It will download the file in
      current working directory)
      :name: for-downloading-song-it-will-download-the-file-in-current-working-directory

   ::

       song -d tum hi ho

   .. figure:: https://cloud.githubusercontent.com/assets/15183662/26523026/cdc7d2e6-432a-11e7-941b-76fa9c465093.png
      :alt: song-cli example

      song-cli example

-  .. rubric:: For Listing songs of a Movie
      :name: for-listing-songs-of-a-movie

   ``song -d dangal``

   .. figure:: https://cloud.githubusercontent.com/assets/15183662/26523019/b009e7b2-432a-11e7-8241-919f95c993bf.png
      :alt: after movie name

      after movie name

-  .. rubric:: For Listing Top songs of a Artist
      :name: for-listing-top-songs-of-a-artist

   ::

       song -d sunidhi chauhan     

   .. figure:: https://cloud.githubusercontent.com/assets/15183662/26523023/c1a272dc-432a-11e7-85e7-1757a40da341.png
      :alt: artist\_top\_songs

      artist\_top\_songs

TODO
----

-  [ ] Implement Unit Testing
-  [ ] Add support for Hollywood/English Songs
-  [ ] Option for downloading all songs of a movie
-  [ ] Option for downloading all top songs of a artist

Want to Contribute
------------------

-  Clone the repository

::

    $ git clone https://github.com/ankitmathur3193/song-cli.git

-  Install dependencies

::

    $ pip install -r requirements.txt

--------------

.. |PyPI version| image:: https://badge.fury.io/py/song.svg
   :target: https://badge.fury.io/py/song
.. |license| image:: https://img.shields.io/github/license/mashape/apistatus.svg
   :target: https://github.com/ankitmathur3193/song-cli/blob/master/LICENSE

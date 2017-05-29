|PyPI version| |license|

SONG DOWNLOADER
===============

A **command line** interface for **downloading Songs/mp3** from Internet

Just type the **name of the song** and it will download for you

Features
--------
- song can download music from https://www.youtube.com/ and https://mr-jatt.com/
- song query Google for finding link associated to https://mr-jatt.com/
- It then parses Mr-jatt.com for finding download link of the mp3 file and downloads it.

For Installing
--------------

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
    
    song -y [ song_name ]
    song -d [ song_name | singer_name | movie_name ]
    song -d --download-all [ singer_name | movie_name ]
    song --version
    
Optional arguments are:

- -y : For downloading mp3 from **youtube**

- -d : For downloading mp3 from **mr-jatt**

- --download-all For downloading **all songs** of a **movie or top songs of a singer**

- --version : For printing song version    
    
    

Example:
--------

-  .. rubric:: For Downloading Song From Youtube 
      :name: for-downloading-song-from-youtube
      
   ::

       song -y tum hi ho

   .. figure:: https://cloud.githubusercontent.com/assets/15183662/26529632/28499f54-43e1-11e7-87a6-f4c0c3e2fd0b.png
      :alt: youtube example

     


-  .. rubric:: For Downloading Song from Mr-jatt (It will download the file in
      current working directory)
      :name: for-downloading-song-it-will-download-the-file-in-current-working-directory

   ::

       song -d tum hi ho

   .. figure:: https://cloud.githubusercontent.com/assets/15183662/26523026/cdc7d2e6-432a-11e7-941b-76fa9c465093.png
      :alt: song-cli example



-  .. rubric:: For Downloading **all songs** of a **movie or top songs of a singer**
      :name: For Downloading **all songs** of a **movie or top songs of a singer**

   ::

       song -d --download-all dhoom     

   .. figure:: https://cloud.githubusercontent.com/assets/15183662/26556972/929c1c12-44bb-11e7-8fbc-48b389de7a82.png
      :alt: download all songs

     
     
     

-  .. rubric:: For Listing songs of a Movie
      :name: for-listing-songs-of-a-movie

   ``song -d dangal``

   .. figure:: https://cloud.githubusercontent.com/assets/15183662/26523019/b009e7b2-432a-11e7-8241-919f95c993bf.png
      :alt: after movie name



-  .. rubric:: For Listing Top songs of a Artist
      :name: for-listing-top-songs-of-a-artist

   ::

       song -d sunidhi chauhan     

   .. figure:: https://cloud.githubusercontent.com/assets/15183662/26523023/c1a272dc-432a-11e7-85e7-1757a40da341.png
      :alt: artist\_top\_songs

     

TODO
----

-  [ X ] Add support for Hollywood/English Songs
-  [ ] Implement Unit Testing
-  [ X ] Option for downloading all songs of a movie
-  [ X ] Option for downloading all top songs of a artist

Disclaimer
----------

Downloading copyrighted material may be illegal in your country. Use at your own risk.

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

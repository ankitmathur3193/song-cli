[![PyPI version](https://badge.fury.io/py/song.svg)](https://badge.fury.io/py/song)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/ankitmathur3193/song-cli/blob/master/LICENSE)
# SONG DOWNLOADER #
A **command line** interface for **downloading Songs/mp3** from Internet

Just type the **name of the song** and it will download the song for you

## Features ##
* song can download music from https://www.youtube.com/ and https://mr-jatt.com/
* song query Google for finding link associated to https://mr-jatt.com/
* It then parses Mr-jatt.com for finding download link of the mp3 file and downloads it.
## For Installing ##
```
pip install song
```
## For Upgrading ##
```
pip install --upgrade song
```
## For Uninstalling ##
```
pip uninstall song
```
## Usage: ##
```
song -y [ song_name ]
song -d [ song_name | singer_name | movie_name ]
song -d --download-all [ singer_name | movie_name ]
song --ty [ textfile.txt ]
song --td [ textfile.txt ]
song --version
```
Optional arguments are:
* -y : For downloading mp3 from **youtube**
* -d : For downloading mp3 from **mr-jatt**
* --ty : For downloading all songs in specified text file from **youtube** mp3 format
* --td : For downloading all songs in specified text file from **mr-jatt** mp3 format
* --download-all : For downloading **all songs** of a **movie or top songs of a singer**
* --version : For printing song version

## Example: ##
* ### For Downloading Song From Youtube ###
    ```
    song -y roar
    ```

     ![youtube_example](https://cloud.githubusercontent.com/assets/15183662/26529632/28499f54-43e1-11e7-87a6-f4c0c3e2fd0b.png)

* ### For Downloading Song (It will download the file in current working directory) ###
    ```
    song -d tum hi ho
    ```

    ![song-cli example](https://cloud.githubusercontent.com/assets/15183662/26523026/cdc7d2e6-432a-11e7-941b-76fa9c465093.png)

* For Downloading **all songs** of a **movie or top songs of a singer**
    ```
    song -d --download-all dhoom  
   ```

    ![download_all](https://cloud.githubusercontent.com/assets/15183662/26556972/929c1c12-44bb-11e7-8fbc-48b389de7a82.png)

* ### For Listing songs of a Movie
  ```
     song -d dangal
  ```

    ![after movie name](https://cloud.githubusercontent.com/assets/15183662/26523019/b009e7b2-432a-11e7-8241-919f95c993bf.png)


 * ### For Listing Top songs of an Artist ###
    ```
    song -d sunidhi chauhan     
    ```

    ![artist_top_songs](https://cloud.githubusercontent.com/assets/15183662/26523023/c1a272dc-432a-11e7-85e7-1757a40da341.png)

## TODO ##
- [X] Add support for Hollywood/English Songs
- [ ] Implement Unit Testing
- [X] Option for downloading all songs of a movie
- [X] Option for downloading all top songs of a artist

## Disclaimer ##

Downloading copyrighted material may be illegal in your country. Use at your own risk.

## Want to Contribute ##
- Clone the repository

```
$ git clone https://github.com/ankitmathur3193/song-cli.git
```

 - Build from source

```
$ cd song-cli-master
$ python setup.py develop
```






----------------------------------------------------

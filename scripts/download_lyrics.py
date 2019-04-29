"""Basic script to download lyrics.

Should be abstracted out to something that can dedupe, clean, and save
the songs of a specified artist(s) to a specified directory in a
future PR.
"""
import os
import sys
import shutil
import glob
import lyricsgenius


def download_lyrics(api_key):
    bands = ["Iron Maidendaklfgsakdl;fg"]

    genius = lyricsgenius.Genius(api_key)

    for band in bands:
        # We're using nested try/except blocks here for 2 reasons:
        # 1. the song downloading can fail from a connection error
        #    (could use a library like tenacity for retrying logic)
        # 2. song titles with forward slashes on them will not be saved
        #    (we can figure out how to handle this too)
        try:
            songs = genius.search_artist(band, sort="popularity", max_songs=1)
            try:
                songs.save_lyrics(extension="txt")
            except Exception as song_save_exception:
                print("Couldn't save lyrics", song_save_exception.args)
        except Exception as band_search_exception:
            print("Couldn't find band", band_search_exception.args)
    # Move the lyrics file to lyrics folder
    files = set(glob.glob("./lyrics_*")) - set(glob.glob("./*.py"))
    # Lyrics API saves files as lyrics_$songname.txt
    # Therefore, "files" = anything named lyrics_(something)...
    # ...Except python scripts, to ensure lyrics_frequency.py stays
    try:
        os.mkdir("lyrics")
    except Exception as move_lyricsfile_exception:
        print("Lyrics folder already exists; safe to ignore this exception")
        print(move_lyricsfile_exception)
        # Above line is just here so move_lyricsfile_exception gets used
    for lyricsfile in files:
        shutil.move("{0}".format(lyricsfile), "lyrics/{0}".format(lyricsfile))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please provide the API key as a command line argument.")
        sys.exit(1)
    api_key = sys.argv[1]
    download_lyrics(api_key)

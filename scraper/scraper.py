import os
from pathlib import Path

import lyricsgenius


MAX_SONGS = 500


def download_one_band(band_name: str, out_directory="data", max_songs=MAX_SONGS) -> None:
    """Download all songs for `band_name` available from Genius API."""
    api_key = os.environ["GENIUS_ACCESS_TOKEN"]
    api_client = lyricsgenius.Genius(api_key)
    artist_songs = api_client.search_artist(
        band_name, max_songs=max_songs, sort="popularity"
    )
    Path(out_directory).mkdir()
    output_file_name = f"{out_directory}/{band_name}"
    api_client.save_artists(
        artists=[artist_songs], filename=output_file_name, overwrite=True,
    )

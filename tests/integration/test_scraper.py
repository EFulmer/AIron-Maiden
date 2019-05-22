import os

from scraper.scraper import download_one_band


# TODO monkeypatch MAX_SONGS rather than have as a kwarg
def test_download_one_band():
    # when we run the download one band function
    download_one_band(band_name="Symphony X", out_directory="tests/integration/data", max_songs=1)
    # then there's a file for that one band in tests/integration/data/
    assert os.path.exists("tests/integration/data/Symphony X.json")

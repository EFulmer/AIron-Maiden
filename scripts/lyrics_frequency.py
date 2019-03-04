from collections import Counter
from pathlib import Path

data_dir = Path("./data/")

all_words = []

for song_file in data_dir.glob("lyrics_manowar_*.txt"):
    with open(song_file, "r") as f:
        all_words.extend(f.read().split())

        hist = Counter(all_words)
        print(hist.most_common(50))

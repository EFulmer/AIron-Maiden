from collections import Counter
import glob

all_words = []

for song_file in glob.glob("./lyrics/*"):
    with open(song_file, "r") as f:
        all_words.extend(f.read().split())
        hist = Counter(all_words)
        print(f"Name of file: {song_file}")
        print(hist.most_common(50))

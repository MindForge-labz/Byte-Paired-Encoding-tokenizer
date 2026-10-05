import json
import urllib.request
import time

# Target vocabulary size for text.json
TARGET_VOCAB_SIZE = 300000

vocab = {}
start_time = time.time()


base_tokens = list("<unk><pad><s></s>abcdefghijklmnopqrstuvwxyz0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ \n")
for token in base_tokens:
    if token not in vocab:
        vocab[token] = len(vocab)


print(f"Building {TARGET_VOCAB_SIZE} text.json file...")
url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"

try:
    req = urllib.request.urlopen(url)
    words = req.read().decode('utf-8').splitlines()

    for word in words:
        clean_word = word.strip().lower()
        if clean_word and clean_word not in vocab:
            vocab[clean_word] = len(vocab)
        if len(vocab) >= TARGET_VOCAB_SIZE:
            break
except Exception as e:
    print(f"Error fetching web words: {e}")


idx = 0
while len(vocab) < TARGET_VOCAB_SIZE:
    token = f"tok_{idx}"
    if token not in vocab:
        vocab[token] = len(vocab)
    idx += 1


with open("../Training/text.json", "w", encoding="utf-8") as f:
    json.dump(vocab, f, indent=4)


with open("../Training/merges.json", "w", encoding="utf-8") as f:
    json.dump([], f, indent=4)

print(f"Successfully generated text.json with {len(vocab):,} tokens!")

end_time = time.time()

total_time = end_time - start_time

print(f"TOTAL TIME TAKE {total_time}")

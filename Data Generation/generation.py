import json
import urllib.request

TARGET_VOCAB_SIZE = 300000

vocab = {}


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

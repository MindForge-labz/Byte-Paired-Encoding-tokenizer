import torch
from torch import nn
import random
import math
from collections import Counter
import json

device = "cuda" if torch.cuda.is_available() else "cpu"


class BPE:
    def __init__(self):
        self.merges = []
        try:
            with open("bpe.json", "r") as file:  # THis saves it so it can remember it for next time
                that = json.load(file)
        except:
            that = {}
        self.vocab_list = that

    def merge(self, words):
        self.word_list = []

        if len(words) < 2:  # Ok so this checks if the word list is less than 2, if it is duh there is nothing to compare to so it returns it imdediatly
            return words
        else:  # OTHERWISE
            for i in range(len(words) - 1):  # First it adds every 2 characters together to a list like in banana it would ad ba an na an na like that kind of
                # MINIMAL FIX 1: Save as a tuple pair (words[i], words[i+1]) instead of adding strings
                self.word_list.append((words[i].lower(), words[i + 1].lower()))

            that_stuff = Counter(self.word_list)  # Now we count each one's frequency
            if not that_stuff:  # If there is no count (if our previous check failed)
                return words  # THEN WE RETURNS DA WORDS

            top_1 = that_stuff.most_common(1)[0][0]  # This gets the most common pair of characters in the dictonary
            self.merges.append(top_1)  # And merges is a catagory of most_commmon stuff, saves so we can remember it

            merged_string = top_1[0] + top_1[1]
            if merged_string not in self.vocab_list:
                self.vocab_list[merged_string] = len(self.vocab_list) + 1  # Now vocab_list is a list with all the characters and puncuation in the english alphabet, so we go like hey lets add this as well so
            # We reduce the amount of tokens
            print(self.vocab_list)  # Double checking time just for me!
            new_words = []  # Okay so this is what we are actually returning now
            i = 0  # OK so now we reset (so we don't get confused with the other one)
            while i < len(words):  # Ok so while I is less than our word's lenght its chill
                if i < len(words) - 1 and (words[i].lower(), words[i + 1].lower()) == top_1:
                    # If yes then the new_word adds the top 1 to the list
                    new_words.append(merged_string)
                    i += 2  # ANd then we skip 2 bois
                else:
                    new_words.append(words[i])  # If not it just regularly adds it
                    i += 1  # And then goes into the next one like a little boring this

            return new_words

    def encode(self, text):
        words = list(text.lower())
        for merge in self.merges:
            pair_a, pair_b = merge
            new_words = []
            i = 0
            while i < len(words):
                if i < len(words) - 1 and words[i] == pair_a and words[i + 1] == pair_b:
                    new_words.append(pair_a + pair_b)
                    i += 2
                else:
                    new_words.append(words[i])
                    i += 1
            words = new_words
        return words

    def train(self, text, no_times):
        all_characters = list("abcdefghijklmnopqrstuvwxyz0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ \n")
        for i in all_characters:
            if i not in self.vocab_list:
                self.vocab_list[i] = len(self.vocab_list) + 1
            else:
                continue


        words = list(text.lower())
        for _ in range(no_times):
            words = self.merge(words)
        with open("BPE.json", "w") as file:  # THis saves it so it can remember it for next time
            json.dump(self.vocab_list, file)
        return words

    def decode(self, words):
        return "".join(words)

    def tokenizer(self, words):
        encoded = self.encode(words) if isinstance(words, str) else words
        ret_list = []
        for token in encoded:
            ret_list.append(self.vocab_list[token])

        return ret_list


tokenizer = BPE()
try:
    with open("corpus_clean.txt") as file:
        text = file.read().replace("\n", "")
except Exception:
    text = """
  He watched the dancing piglets with panda bear tummies in the swimming pool.
  I don't respect anybody who can't tell the difference between Pepsi and Coke.
  He stepped gingerly onto the bridge knowing that enchantment awaited on the other side."""

epoches = 20
tokenizer.train(text, epoches)

that = tokenizer.tokenizer(text)
print("Token IDs:", that)

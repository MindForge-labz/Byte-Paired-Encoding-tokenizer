import torch
from torch import nn
import random
import math
from collections import Counter
import json

device = "GPU"


class BPE:
    def __init__(self):
        self.merges = []
        self.vocab_list = {}

    def merge(self, words):
        self.word_list = []
        words = list(words)

        if len(words) < 2: #Ok so this checks if the word list is less than 2, if it is duh there is nothing to compare to so it returns it imdediatly
            return words
        else: #OTHERWISE
            for i in range(len(words) - 1): #First it adds every 2 characters together to a list like in banana it would ad ba an na an na like that kind of
                self.word_list.append(words[i].lower() + words[i + 1].lower())

            that_stuff = Counter(self.word_list) #Now we count each one's frequency
            if not that_stuff: #If there is no count (if our previous check failed)
                return words #THEN WE RETURNS DA WORDS

            top_1 = that_stuff.most_common(1)[0][0] #This gets the most common pair of characters in the dictonary
            self.merges.append(top_1) #And merges is a catagory of most_commmon stuff, saves so we can remember it
            self.vocab_list[top_1] = len(self.vocab_list) + 1 #Now vocab_list is a list with all the characters and puncuation in the english alphabet, so we go like hey lets add this as well so
            #We reduce the amount of tokens
            print(self.vocab_list) #Double checking time just for me!
            new_words = [] #Okay so this is what we are actually returning now
            i = 0 #OK so now we reset (so we don't get confused with the other one)
            while i < len(words): #Ok so while I is less than our word's lenght its chill
                if i < len(words) - 1 and words[i].lower() + words[i + 1].lower() == top_1: #So also checking if we add 1 i it would work and then we check does this letter + this letter is our top 1?
                #If yes then the new_word adds the top 1 to the list
                    new_words.append(top_1)
                    i += 2 #ANd then we skip 2 bois
                else:
                    new_words.append(words[i]) #If not it just regularly adds it
                    i += 1 #And then goes into the next one like a little boring this

            with open("text.json", "w") as file: #THis saves it so it can remember it for next time
                json.dump(self.vocab_list, file)

            return new_words

    def encode(self, text):
        words = list(text.lower())
        for merge in self.merges:
            new_words = []
            i = 0
            while i < len(words):
                if i < len(words) - 1 and words[i] + words[i + 1] == merge:
                    new_words.append(merge)
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
        words = text.lower()
        for _ in range(no_times):
            words = self.merge(words)
        return words

    def decode(self, words):t
        return "".join(words)

    def tokenizer(self, words):
        encoded = self.encode(words)
        ret_list = []
        for token in encoded:
            ret_list.append(self.vocab_list[token])

        return ret_list


tokenizer = BPE()
text = """
He watched the dancing piglets with panda bear tummies in the swimming pool.
I don’t respect anybody who can’t tell the difference between Pepsi and Coke.
He stepped gingerly onto the bridge knowing that enchantment awaited on the other side."""
tokenizer.train(text, 7)

that = tokenizer.tokenizer(text)
print("Token IDs:", that)

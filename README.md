
<div align="center">

# BPE Tokenizer

A lightweight Byte-Pair Encoding tokenizer built from scratch in Python.

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-Supported-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org)
[![Build](https://img.shields.io/badge/Status-Active_Dev-black?style=for-the-badge)]()

</div>

## Overview

Most modern language models rely on Byte-Pair Encoding (BPE) to turn raw text into subwords and numbers. 

Instead of relying on heavy third-party libraries, this project implements a working BPE tokenizer from scratch to show exactly how subword merging, vocabulary creation, and token encoding operate under the hood.
> **Note:** *Built single-handedly with a broken keyboard and a mouse that is actively fighting for its life.*
## Tech Stack

| Technology | Purpose |
| :--- | :--- |
| **Python 3.8+** | Core execution and logic |
| **PyTorch** | Tensor integration |
| **`collections.Counter`** | Pair frequency tracking |
| **`json`** | Vocabulary saving and storage |

## Key Features

- **Dynamic Pair Merging:** Automatically identifies high-frequency character pairs and merges them across iterations.
- **Base Vocabulary Seeding:** Initializes default alphanumeric characters, punctuation, and whitespace.
- **Persistence:** Automatically dumps updated vocabulary mappings to `text.json`.
- **Bidirectional Processing:** Supports encoding raw text to token IDs and decoding IDs back into strings.

## Quick Start

Import the module and run the training pipeline:

```python
from bpe import BPE

tokenizer = BPE()

corpus = """
He watched the dancing piglets with panda bear tummies in the swimming pool.
I don’t respect anybody who can’t tell the difference between Pepsi and Coke.
He stepped gingerly onto the bridge knowing that enchantment awaited on the other side.
"""

# Train for 7 merge cycles
tokenizer.train(corpus, no_times=7)

# Convert text to token IDs
token_ids = tokenizer.tokenizer(corpus)
print("Token IDs:", token_ids)

---


```


<br>


## How It Works
```markdown


1. **Initial Setup:** Loads the base ASCII character set into the vocabulary.
2. **Frequency Counting:** Scans the text for adjacent character pairs.
3. **Merging:** Replaces the most frequent pair with a single combined subword.
4. **Export:** Assigns a unique ID to the new subword and writes the vocabulary to disk.

---

## Roadmap

- [x] Core subword merge algorithm
- [x] Text encoding and decoding
- [x] JSON vocabulary persistence
- [ ] UTF-8 byte-level fallback for out-of-vocabulary handling
- [ ] Configurable target vocabulary size cap

---
```


<div align="center">
  <b>Built by Aarav Sureka</b>
</div>

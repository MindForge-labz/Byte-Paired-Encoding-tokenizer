# Byte-Pair Encoding (BPE) Tokenizer

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Framework](https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=white)
![Status](https://img.shields.io/badge/status-work--in--progress-orange)
![License](https://img.shields.io/badge/license-MIT-green)

A lightweight, from-scratch implementation of a **Byte-Pair Encoding (BPE) Tokenizer** in Python and PyTorch. Designed to demonstrate how subword tokenization models transform raw text into numerical token sequences for Natural Language Processing (NLP) and Large Language Models (LLMs).

> *Built single-handedly with passion, a broken keyboard, and a barely working mouse.* 🚀

---

## Features

- **Custom Vocabulary Building:** Automatically seeds the initial vocabulary with standard alphanumeric characters, punctuation, and whitespace.
- **Iterative Merging Algorithm:** Dynamically identifies and merges the most frequent adjacent character pairs across successive training iterations.
- **Persistent Vocabulary Storage:** Automatically serializes learned vocabulary mappings to JSON (`text.json`) for persistence across runs.
- **Subword Encoding & Decoding:** Maps arbitrary raw text sequences to learned subword tokens and converts token ID lists back into continuous text strings.

---

## Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Language** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) | Core implementation language |
| **Deep Learning** | ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white) | Tensor framework foundation |
| **Data Mappings** | `json` / `collections.Counter` | Vocabulary persistence and frequency counting |

---

## Quick Start

### Prerequisites

Ensure you have Python 3.8+ and PyTorch installed:

```bash
pip install torch

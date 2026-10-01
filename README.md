<div align="center">

# ⚡ Byte-Pair Encoding (BPE) Tokenizer

*A lightweight, zero-dependency subword tokenization engine built from scratch in Python.*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-Supported-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org)
[![Status](https://img.shields.io/badge/Build-Active_Dev-ff69b4?style=for-the-badge)](https://github.com)
[![License](https://img.shields.io/badge/License-MIT-blueviolet?style=for-the-badge)](LICENSE)

<p align="center">
  <a href="#-about-the-project">About</a> •
  <a href="#-key-features">Features</a> •
  <a href="#-tech-stack">Tech Stack</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-roadmap">Roadmap</a>
</p>

</div>

---

## 📌 About The Project

Tokenization is the foundational bedrock of modern Large Language Models (LLMs) like GPT-4, LLaMA, and Claude. Before text enters a Transformer, Byte-Pair Encoding converts raw character strings into dense integer sequences.

This repository hosts a clean, ground-up implementation of a **BPE Tokenizer**. It demonstrates the exact mechanics of subword merging, vocabulary expansion, and token-to-ID mapping without hiding behind heavy black-box abstractions.

> 🛠️ **Developer Note:** *Engineered with 100% manual determination, a broken keyboard, and a barely functional mouse.*

---

## ✨ Key Features

- **📊 Dynamic Frequency Merging:** Scans input corpora to identify and collapse high-frequency token pairs iteratively.
- **🔤 Base Vocabulary Seeding:** Pre-populates standard alphanumeric characters, punctuation, and whitespace tokens automatically.
- **💾 Auto-Persistence:** Exports updated vocabulary indexes to local JSON storage (`text.json`) after every merge step.
- **🔄 Two-Way Conversion:** Full support for `encode()` (Text → Subwords), `tokenizer()` (Subwords → Integer IDs), and `decode()` (Subwords → String).

---

## 🛠️ Tech Stack

# Natural Language Processing with SpaCy and Python

A comprehensive introduction to Natural Language Processing (NLP) using SpaCy, demonstrated through text analysis of Wikipedia articles.

## 📋 Overview

This project explores various NLP concepts and techniques using SpaCy, including:

- Text tokenization and sentence segmentation
- Part-of-speech (POS) tagging
- Named Entity Recognition (NER)
- Dependency parsing
- Morphological analysis
- Lemmatization

## 🚀 Features

- **Text Analysis**: Analyze Wikipedia articles using SpaCy's pre-trained models
- **Token Exploration**: Examine individual tokens and their linguistic properties
- **Entity Recognition**: Identify and classify named entities in text
- **Linguistic Properties**: Extract morphological, syntactic, and semantic information

## 🛠️ Prerequisites

- Python 3.12.3 or higher
- Ubuntu 24.04 (or any Linux distribution)
- pip package manager

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Xtalism/natural-language-spacy-python.git
cd natural-language-spacy-python
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Linux/macOS
# or
# venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies

```bash
# Upgrade pip and install build tools
pip install -U pip setuptools wheel

# Install SpaCy
pip install -U spacy

# Download language models
python -m spacy download en_core_web_sm  # English model
python -m spacy download es_core_news_sm # Spanish model (optional)
```

## 🏃‍♂️ Usage

Run the main analysis script:
```bash
python3 intro.py
```

This will:
1. Load the English language model
2. Process the Wikipedia text about the United States
3. Demonstrate various NLP features including token analysis, entity recognition, and linguistic properties

## 📁 Project Structure

```
natural-language-spacy-python/
├── intro.py          # Main analysis script
├── data/
│   └── wiki_us.txt   # Wikipedia article about the United States
├── README.md         # Project documentation
└── LICENSE           # License file
```

## 🔍 What You'll Learn

The `intro.py` script demonstrates:

- **Text Loading**: Reading and processing text files
- **Document Processing**: Converting raw text into SpaCy document objects
- **Sentence Segmentation**: Breaking text into individual sentences
- **Token Analysis**: Examining individual words and their properties:
  - `.text` - Original text
  - `.lemma_` - Base form of the word
  - `.pos_` - Part-of-speech tag
  - `.dep_` - Syntactic dependency
  - `.ent_type_` - Named entity type
  - `.morph` - Morphological features

## 📚 Resources

- [SpaCy Documentation](https://spacy.io/)
- [SpaCy Installation Guide](https://spacy.io/usage)
- [SpaCy Models](https://spacy.io/models)
- [Natural Language Processing Course](https://course.spacy.io/)

## 🤝 Contributing

Feel free to contribute by:
1. Adding new text analysis examples
2. Implementing additional NLP techniques
3. Improving documentation
4. Adding support for other languages

## 📄 License

This project is licensed under the terms specified in the LICENSE file.
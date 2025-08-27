## 🚀 WordChainBuilder: A Python Tool for Finding Word Chains


[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/)
[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-blue.svg)](https://www.gnu.org/licenses/agpl-3.0.en.html)
[![Issues](https://img.shields.io/github/issues/Behdad-kanaani/WordChainBuilder)](https://github.com/Behdad-kanaani/WordChainBuilder/issues)
[![Stars](https://img.shields.io/github/stars/Behdad-kanaani/WordChainBuilder)](https://github.com/Behdad-kanaani/WordChainBuilder/stargazers)



### 🌟 Overview

**`WordChainBuilder`** is a pure Python tool designed to discover the longest possible chains of words from a given list. It does this by applying two distinct, powerful rules. Whether you're a fan of word games, a computational linguist, or a programmer looking for an interesting challenge, this tool provides an elegant way to explore the relationships between words. Built with simplicity in mind, it's easy to use right out of the box with no external dependencies.

-----

### ⚡ Key Features

  * **Dual-Rule System:** Find chains based on two different logical rules, offering flexibility and deeper analysis.
  * **Substring Rule:** Identifies chains where each word is a **substring** of the next, ensuring a clear, nested relationship.
  * **Character Subset Rule:** Discovers chains where the next word contains all the characters of the previous word, regardless of their order, making it perfect for anagram-style puzzles.
  * **Zero Dependencies:** The entire script is written in **pure Python**, so you can integrate it into your projects without worrying about external packages.
  * **Easy to Use:** The straightforward function call makes it simple to implement in any Python script.

-----

### 🛠 Installation & Setup

Getting started is quick and easy. All you need is **Python 3.7+**.

1.  Clone the repository or download the `wordChainBuilder.py` file.
2.  Navigate to the project directory.

<!-- end list -->

```bash
git clone https://github.com/Behdad-kanaani/WordChainBuilder.git
```

-----

### 🚀 Usage Example

Here’s a practical example demonstrating how to use the main function to find and print word chains.

```python
from wordChainBuilder import find_longest_word_chains

words = ["apple", "ple", "Oapple", "bapple", "capple"]

# Find chains using the substring rule
chains_sub = find_longest_word_chains(words, rule="substring")

# Find chains using the character subset rule
chains_char = find_longest_word_chains(words, rule="char_subset")

# Print the results
def print_chains(chains, rule):
    print(f"Chains using '{rule}' rule:")
    if not chains:
        print("No chains found.")
    else:
        for chain in chains:
            print(" -> ".join(chain))
    print()

print_chains(chains_sub, "substring")
print_chains(chains_char, "char_subset")
```

**Sample Output:**

```
Chains using 'substring' rule:
ple -> apple -> Oapple
ple -> apple -> bapple
ple -> apple -> capple

Chains using 'char_subset' rule:
ple -> apple -> Oapple
ple -> apple -> bapple
ple -> apple -> capple
```

-----

### 📖 Deeper Look into the Rules

#### Substring Rule

This rule requires that a word must be a part of the next word. For example, `ple` is a substring of `apple`. The next word must also be longer to ensure the chain progresses. This creates a clear, hierarchical relationship between words.

#### Character Subset Rule

This rule is more flexible. It checks if the next word contains all the characters from the previous one, including the same or higher counts for each character. This means a word like `apple` can lead to `capple` because all the characters of `apple` are present in `capple`. The order of the characters doesn't matter, which makes it perfect for finding hidden connections.

-----

### ⚖ License

This project is open-source and released under the **AGPL-3.0 License**. You are free to use, modify, and distribute the code under the terms of this license.

### ✨ Author

**Behdad Kanani**

*This tool was born from a simple thought experiment: how to connect words in an interesting way. It started as a quick script to solve a mental puzzle and evolved into a robust, reusable tool for anyone fascinated by words and their structures.*

-----

### 🔗 Contributions

Your feedback and contributions are highly encouraged\! If you find any issues, have a feature request, or want to contribute to the code, please feel free to check out the [issues page](https://github.com/yourusername/WordChainBuilder/issues) and submit a pull request.

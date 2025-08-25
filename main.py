################################################################################
#                                                                              #
#                           WRITTEN BY BEHDAD KANANI                            #
#                                                                              #
#   Description:                                                               #
#       This script finds the longest chains of words based on two rules:      #
#         1. "substring"   -> Each word must be a substring of the next word. #
#         2. "char_subset" -> All characters of the previous word must exist  #
#                             in the next word, respecting character counts.  #
#                                                                              #
################################################################################

import collections
from typing import List

def is_valid_link(word1: str, word2: str, rule: str) -> bool:
    """
    Check if word2 can follow word1 based on the chosen rule.
    """
    if len(word2) <= len(word1):
        return False
    
    if rule == "substring":
        return word1 in word2
    elif rule == "char_subset":
        count1 = collections.Counter(word1)
        count2 = collections.Counter(word2)
        for char, count in count1.items():
            if count2.get(char, 0) < count:
                return False
        return True
    return False

def build_chains(words: List[str], rule: str) -> dict:
    """
    Build chains of words based on the given linking rule.
    
    Returns a dictionary mapping each word to the longest chain ending with it.
    """
    unique_words = sorted(list(set(words)), key=len)
    chains_map = {word: [word] for word in unique_words}

    for i in range(len(unique_words)):
        for j in range(i):
            word1 = unique_words[j]
            word2 = unique_words[i]
            if is_valid_link(word1, word2, rule):
                if len(chains_map[word1]) + 1 > len(chains_map[word2]):
                    chains_map[word2] = chains_map[word1] + [word2]
    
    return chains_map

def find_longest_chains(chains_map: dict) -> List[List[str]]:
    """
    Extract the longest chains from the chains map.
    """
    if not chains_map:
        return []
    
    max_length = max(len(chain) for chain in chains_map.values())
    longest_chains = [chain for chain in chains_map.values() if len(chain) == max_length and len(chain) > 1]
    return longest_chains

def find_longest_word_chains(words: List[str], rule: str = "substring") -> List[List[str]]:
    """
    Find the longest chains of words using the specified rule.
    """
    chains_map = build_chains(words, rule)
    return find_longest_chains(chains_map)


# ======================= Example Usage =======================

example_words = ["apple", "ple", "Oapple", "bapple", "capple"]

def print_chains(chains: List[List[str]], rule: str):
    print(f"Chains using '{rule}' rule:")
    if not chains:
        print("No chains were found.")
    else:
        for chain in chains:
            print(" -> ".join(chain))
    print("\n")

chains_substring = find_longest_word_chains(example_words, rule="substring")
chains_char_subset = find_longest_word_chains(example_words, rule="char_subset")

print_chains(chains_substring, "substring")
print_chains(chains_char_subset, "char_subset")

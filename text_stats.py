#!/usr/bin/env python3
"""Text Statistics - Word count, readability scores, frequency analysis."""
import sys, re, math
from collections import Counter

def analyze(text):
    words = re.findall(r"\b\w+\b", text.lower())
    sentences = re.split(r"[.!?]+", text)
    sentences = [s.strip() for s in sentences if s.strip()]
    syllables = sum(count_syllables(w) for w in words)
    freq = Counter(words)
    chars = len(text); chars_no_space = len(text.replace(" ", ""))
    avg_word = sum(len(w) for w in words) / max(len(words), 1)
    avg_sent = len(words) / max(len(sentences), 1)
    flesch = 206.835 - 1.015 * avg_sent - 84.6 * (syllables / max(len(words), 1))
    return {"chars": chars, "chars_no_space": chars_no_space, "words": len(words),
            "sentences": len(sentences), "syllables": syllables, "avg_word_len": avg_word,
            "avg_sent_len": avg_sent, "flesch": flesch, "top_words": freq.most_common(10),
            "unique_words": len(set(words)), "lexical_density": len(set(words))/max(len(words),1)}

def count_syllables(word):
    word = word.lower(); count = 0; vowels = "aeiouy"; prev_vowel = False
    for c in word:
        is_vowel = c in vowels
        if is_vowel and not prev_vowel: count += 1
        prev_vowel = is_vowel
    if word.endswith("e"): count -= 1
    return max(count, 1)

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f: text = f.read()
    else:
        text = "The quick brown fox jumps over the lazy dog. This is a sample text for analysis. It contains several sentences with varying complexity. Some words are short. Others are considerably longer and more elaborate."
    stats = analyze(text)
    print("=== Text Statistics ===\n")
    print(f"  Characters:      {stats['chars']} ({stats['chars_no_space']} no spaces)")
    print(f"  Words:           {stats['words']} ({stats['unique_words']} unique)")
    print(f"  Sentences:       {stats['sentences']}")
    print(f"  Syllables:       {stats['syllables']}")
    print(f"  Avg word length: {stats['avg_word_len']:.1f}")
    print(f"  Avg sent length: {stats['avg_sent_len']:.1f}")
    print(f"  Lexical density: {stats['lexical_density']:.2%}")
    print(f"  Flesch score:    {stats['flesch']:.1f}")
    print("\n  Top words:")
    for w, c in stats["top_words"]: print(f"    {w:15s} {c}")

if __name__ == "__main__":
    main()

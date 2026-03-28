#!/usr/bin/env python3
"""text_stats - Compute text statistics and readability metrics."""
import sys, re, math

def syllables(word):
    word = word.lower().rstrip("e")
    count = len(re.findall(r"[aeiouy]+", word))
    return max(1, count)

def analyze(text):
    sentences = [s.strip() for s in re.split(r"[.!?]+", text) if s.strip()]
    words = text.split()
    chars = sum(len(w) for w in words)
    sylls = sum(syllables(w) for w in words)
    n_sent = max(1, len(sentences))
    n_words = max(1, len(words))
    # Flesch-Kincaid
    fk_grade = 0.39 * (n_words/n_sent) + 11.8 * (sylls/n_words) - 15.59
    fk_ease = 206.835 - 1.015 * (n_words/n_sent) - 84.6 * (sylls/n_words)
    return {
        "chars": len(text), "words": n_words, "sentences": n_sent,
        "avg_word_len": chars/n_words, "avg_sent_len": n_words/n_sent,
        "syllables": sylls, "fk_grade": fk_grade, "fk_ease": fk_ease
    }

if __name__ == "__main__":
    if len(sys.argv) < 2: print("Usage: text_stats <file>"); sys.exit(1)
    with open(sys.argv[1]) as f: stats = analyze(f.read())
    for k, v in stats.items():
        print(f"{k:20s}: {v:.2f}" if isinstance(v, float) else f"{k:20s}: {v}")

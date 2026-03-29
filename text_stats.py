#!/usr/bin/env python3
"""text_stats - Text statistics and readability metrics."""
import sys, argparse, json, re, math

def syllable_count(word):
    word = word.lower().rstrip("e")
    vowels = "aeiou"
    count = 0; prev_vowel = False
    for ch in word:
        is_vowel = ch in vowels
        if is_vowel and not prev_vowel: count += 1
        prev_vowel = is_vowel
    return max(1, count)

def analyze(text):
    words = re.findall(r"\b\w+\b", text)
    sentences = re.split(r"[.!?]+", text)
    sentences = [s.strip() for s in sentences if s.strip()]
    chars = len(text)
    word_count = len(words)
    sent_count = max(1, len(sentences))
    syllables = sum(syllable_count(w) for w in words)
    avg_word_len = sum(len(w) for w in words) / max(1, word_count)
    flesch = 206.835 - 1.015*(word_count/sent_count) - 84.6*(syllables/max(1,word_count))
    unique = len(set(w.lower() for w in words))
    return {"characters": chars, "words": word_count, "sentences": sent_count, "syllables": syllables, "unique_words": unique, "avg_word_length": round(avg_word_len, 2), "lexical_diversity": round(unique/max(1,word_count), 3), "flesch_reading_ease": round(flesch, 1), "words_per_sentence": round(word_count/sent_count, 1)}

def main():
    p = argparse.ArgumentParser(description="Text statistics")
    p.add_argument("input", help="Text or @filename")
    args = p.parse_args()
    text = args.input
    if text.startswith("@"):
        with open(text[1:]) as f: text = f.read()
    print(json.dumps(analyze(text), indent=2))

if __name__ == "__main__": main()

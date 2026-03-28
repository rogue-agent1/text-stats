#!/usr/bin/env python3
"""Text statistics — word/sentence count, readability scores, frequency."""
import sys, re, math, collections

def analyze(text):
    words = re.findall(r"\b\w+\b", text.lower())
    sentences = re.split(r"[.!?]+", text)
    sentences = [s.strip() for s in sentences if s.strip()]
    syllables = sum(count_syllables(w) for w in words)
    chars = len(re.sub(r"\s", "", text))
    wf = collections.Counter(words).most_common(10)
    avg_word = sum(len(w) for w in words) / max(1, len(words))
    avg_sent = len(words) / max(1, len(sentences))
    fk_grade = 0.39 * avg_sent + 11.8 * syllables / max(1, len(words)) - 15.59
    return {"chars": chars, "words": len(words), "sentences": len(sentences),
            "syllables": syllables, "avg_word_len": avg_word, "avg_sent_len": avg_sent,
            "fk_grade": fk_grade, "top_words": wf}

def count_syllables(word):
    word = word.lower(); count = 0; vowels = "aeiouy"; prev_vowel = False
    for c in word:
        is_vowel = c in vowels
        if is_vowel and not prev_vowel: count += 1
        prev_vowel = is_vowel
    if word.endswith("e"): count -= 1
    return max(1, count)

def cli():
    if len(sys.argv) > 1 and sys.argv[1] == "--file":
        with open(sys.argv[2]) as f: text = f.read()
    else: text = " ".join(sys.argv[1:]) or sys.stdin.read()
    s = analyze(text)
    print(f"  Characters: {s['chars']}"); print(f"  Words: {s['words']}")
    print(f"  Sentences: {s['sentences']}"); print(f"  Syllables: {s['syllables']}")
    print(f"  Avg word length: {s['avg_word_len']:.1f}")
    print(f"  Avg sentence length: {s['avg_sent_len']:.1f}")
    print(f"  FK Grade Level: {s['fk_grade']:.1f}")
    print(f"  Top words: {s['top_words']}")

if __name__ == "__main__": cli()

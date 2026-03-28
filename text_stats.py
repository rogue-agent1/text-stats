#!/usr/bin/env python3
"""Text statistics calculator."""
import sys, re, json

def analyze(text):
    chars = len(text)
    chars_no_space = len(text.replace(' ', '').replace('\n', '').replace('\t', ''))
    words = len(text.split())
    lines = text.count('\n') + (1 if text else 0)
    sentences = len(re.findall(r'[.!?]+', text))
    paragraphs = len([p for p in text.split('\n\n') if p.strip()])
    reading_min = round(words / 238, 1)
    return {'characters': chars, 'characters_no_spaces': chars_no_space, 'words': words,
            'lines': lines, 'sentences': sentences, 'paragraphs': paragraphs,
            'reading_minutes': reading_min}

def main():
    if len(sys.argv) > 1 and sys.argv[1] != '-':
        with open(sys.argv[1]) as f: text = f.read()
    else:
        text = sys.stdin.read()
    fmt = '--json' in sys.argv
    stats = analyze(text)
    if fmt:
        print(json.dumps(stats, indent=2))
    else:
        for k, v in stats.items():
            print(f"{k.replace('_', ' ').title():>25}: {v}")

if __name__ == '__main__':
    main()

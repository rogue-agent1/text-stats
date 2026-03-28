#!/usr/bin/env python3
"""Text statistics — counts, readability, word frequency."""
import sys, re, math, collections
def syllables(w):
    w=w.lower(); c=0; pv=False
    for ch in w:
        iv=ch in "aeiouy"
        if iv and not pv: c+=1
        pv=iv
    if w.endswith("e"): c-=1
    return max(1,c)
def cli():
    if len(sys.argv)>1 and sys.argv[1]=="--file":
        with open(sys.argv[2]) as f: text=f.read()
    else: text=" ".join(sys.argv[1:]) or sys.stdin.read()
    words=re.findall(r"\b\w+\b",text.lower()); sents=re.split(r"[.!?]+",text); sents=[s for s in sents if s.strip()]
    syls=sum(syllables(w) for w in words); wc=len(words); sc=max(1,len(sents))
    fk=0.39*(wc/sc)+11.8*(syls/max(1,wc))-15.59
    print(f"  Words: {wc}  Sentences: {sc}  FK Grade: {fk:.1f}")
    print(f"  Top: {collections.Counter(words).most_common(5)}")
if __name__ == "__main__": cli()

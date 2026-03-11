#!/usr/bin/env python3
"""Text statistics — word count, readability, etc. Zero deps."""
import re
def analyze(text):
    words=text.split(); sents=re.split(r'[.!?]+',text); sents=[s for s in sents if s.strip()]
    chars=len(text); wc=len(words); sc=len(sents)
    avg_wl=sum(len(w.strip('.,!?;:')) for w in words)/wc if wc else 0
    avg_sl=wc/sc if sc else 0
    # Flesch-Kincaid
    syllables=sum(count_syllables(w) for w in words)
    fk=0.39*avg_sl+11.8*(syllables/wc)-15.59 if wc else 0
    return {"chars":chars,"words":wc,"sentences":sc,"avg_word_len":round(avg_wl,1),
            "avg_sent_len":round(avg_sl,1),"syllables":syllables,"fk_grade":round(fk,1)}

def count_syllables(word):
    word=word.lower().strip(".,!?;:")
    if not word: return 0
    vowels="aeiou"; count=0; prev=False
    for c in word:
        if c in vowels:
            if not prev: count+=1
            prev=True
        else: prev=False
    if word.endswith('e') and count>1: count-=1
    return max(1,count)

def test():
    r=analyze("The quick brown fox jumps over the lazy dog. It was a good day.")
    assert r["words"]==13; assert r["sentences"]==2
    assert r["avg_word_len"]>2
    print(r); print("All tests passed!")
if __name__=="__main__":
    import sys
    if len(sys.argv)>1:
        with open(sys.argv[1]) as f: print(analyze(f.read()))
    else: test()

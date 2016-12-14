"""
https://www.hackerrank.com/challenges/from-paragraphs-to-sentences

BRIEF:
Sentence segmentation, means, to split a given paragraph of text into sentences, by identifying the sentence boundaries. In many cases, a full stop is all that is required to identify the end of a sentence, but the task is not all that simple.

This is an open ended challenge to which there are no perfect solutions. Try to break up given paragraphs into text into individual sentences. Even if you don't manage to segment the text perfectly, the more sentences you identify and display correctly, the more you will score.

Achieved Score: 29.38/40
"""

import re 

S = raw_input().strip()

chars = re.findall('\W+|\w+',S)

puncs = ["!", ".", "?"]

print chars 

sent = ""
sentences = []
for char in chars:
    if char.strip() in puncs:
        sent+=char
        sentences.append(sent)
        sent=""
    else:
        sent+=char

for s in sentences:
    print s.strip()

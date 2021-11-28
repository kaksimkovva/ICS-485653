from collections import Counter

import matplotlib.pyplot as plt
import numpy as np
import pylab



def count_sentences(text: str):
    marks = ['.', '?', '!', '...']
    for b in range(0, len(marks)):
        pylab.bar(marks[b], text.count(marks[b]))
      

count_sentences("Python is a programming language with dynamic semantics.")
count_sentences("Let's go for a walk!")
count_sentences("What are you thinking about?")
count_sentences("Here is how it was...")

plt.show()  
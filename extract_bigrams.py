# -*- coding: utf-8 -*-
"""extract bigrams

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eaotNDPtc3Iku0Nt5a-8gGVCrfj4eIjp
"""

#Bigrams are extracted from input corpus
def collect_bigrams(corpus):
  word_bigrams={}
  for doc in corpus:
    tmp= doc.split(' ')
    
    for i in range(1,len(tmp)):
      word=tmp[i]
      prev_word=tmp[i-1]
      
      if not (word in word_bigrams):
        word_bigrams[word]= []
        
      word_bigrams[word].append[prev_word]
   return word_bigrams

#extract bigrams from corpus:

word_bigrams= collect_bigrams(corpus name)
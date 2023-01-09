# -*- coding: utf-8 -*-
"""bigram LM

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lOHyyYA-5D5Q5I44-n64m3g2fG3v88nD
"""

#The Bigram LM probability of the input sentence is calculated
def bigram_LM(sent):
    prob=1
    tmp=sent.split(' ')
    prob=prob*(word_count[tmp[0]]/total_words)
    
    for i in range(1, len(tmp)):
        prob=prob*get_bigram_prob(tmp[i], tmp[i-1])

    return prob

#calculate Prob for two sentences
prob1=bigram_LM('sentence1')
prob2=bigram_LM('sentence2')

#compare prob1 and prob2
if prob1>prob2:
    print ('prob1')
else:
    print('prob2')

"""By Comparing unigram and bigram in your corpus you can see that **"Bigram works better than unigram"**"""
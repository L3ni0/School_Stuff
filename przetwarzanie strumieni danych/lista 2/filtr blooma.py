import nltk
from multiprocessing import Pool
from nltk.corpus import words,movie_reviews
from nltk import edit_distance
from bloom_filter2.bloom_filter import BloomFilter
import time
from collections import Counter
import tracemalloc
import matplotlib.pyplot as plt
import seaborn as sns

words_core = words.words()

# print(movie_reviews.fileids('neg'))
# print(movie_reviews.fileids('pos'))
files = movie_reviews.fileids('neg') + movie_reviews.fileids('pos')
reviews = []
for file in files:
    file =  ' '.join(movie_reviews.words(file)).replace(',','').replace('.','').replace("'",'').replace(':','').replace('?','')\
        .replace('!','').replace(':','').replace('-','').replace(')','').replace('(','').\
        replace('-','').replace('"','').replace(';','').replace('*','').replace('/','').split()
    reviews.extend(file)
#print(len(reviews)) 1338714
reviews = reviews[:402814]
fiter_bloom = BloomFilter(402814)
for w in words_core:
    fiter_bloom.add(w)

def chceck_bloom(who): #function checking using bloom filter, return
    if who in fiter_bloom:
        return None
    return who

def check_naiwe(who):
    if who in words_core:
        return None
    return who

def make_plot():
    sns.set_theme(style='whitegrid')
    plt.bar(['czas naiwny','czas bloom'],[time_naiwe, time_bloom])
    plt.show()
    print([mem_naiwe, mem_bloom])
    plt.bar(['pamiec naiwny','pamiec bloom'],[mem_naiwe, mem_bloom])
    plt.show()

if __name__ ==  '__main__':
    print('start')
    with Pool(processes=7) as pool:
        tracemalloc.start()
        start_bloom = time.time()
        b = list(pool.map(chceck_bloom, reviews))
        mem_bloom = tracemalloc.get_traced_memory()
        mem_bloom = mem_bloom[1]

        tracemalloc.stop()
        words_list = Counter(b)
        words_list = words_list.most_common(11)[1:]
        time_bloom = time.time() - start_bloom


    with Pool(processes=7) as pool:
        start_normal = time.time()
        tracemalloc.start()
        n = list(pool.map(check_naiwe, reviews))
        mem_naiwe = tracemalloc.get_traced_memory()
        mem_naiwe = mem_naiwe[1]
        tracemalloc.stop()
        time_naiwe = time.time() - start_normal

    with Pool(processes=7) as pool:
        make_plot()
        print(words_list)
        for word, number in words_list:
            print(word)
            first = [words_core[0],edit_distance(word,words_core[0])]
            second = [words_core[0],edit_distance(word,words_core[0])]
            third = [words_core[0],edit_distance(word,words_core[0])]
            for chceck_word in words_core:
                if first[1] > edit_distance(word,chceck_word):
                    third = second
                    second = first
                    first = [chceck_word,edit_distance(word,chceck_word)]

                elif second[1] > edit_distance(word,chceck_word):
                    third = second
                    second = [chceck_word,edit_distance(word,chceck_word)]

                elif third[1] > edit_distance(word,chceck_word):
                    third = [chceck_word, edit_distance(word, chceck_word)]

            print(word, first, second, third)




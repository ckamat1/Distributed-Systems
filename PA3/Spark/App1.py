from pyspark import SparkContext, SparkConf
import os
import sys
from nltk.tokenize import RegexpTokenizer
from operator import add


tokenizer = RegexpTokenizer(r'\w+')

def tokenize(text):
    return tokenizer.tokenize(text.lower())


def tokens(text):
    return [line.split() for line in text]

def getListofTuples(text):
    return [(l.split()[0],l.split()[3]) for l in open(text) if l is not None]



# path = "/home/ckamat/PA2_Raft/Distributed-Systems/PA3/Spark/"
path = "/root/source/Distributed-Systems/PA3/Spark/"
# logFile = "n-grams.txt"  # Should be some file on your system
# logFile = path + logFile
logFile = "s3://datasets.elasticmapreduce/ngrams/books/20090715/eng-us-all/1gram/data"
conf = SparkConf().setAppName("Simple App").setMaster("local")
sc = SparkContext(conf=conf)
lines = sc.textFile(logFile)
tuplesRDD = lines.map(lambda line: (line.split()[0],int((line.split()[4]))))
# partitionRDD = sc.parallelize(tuplesRDD.collect())
booksRDD = tuplesRDD.reduceByKey(add)
booksRDD.saveAsTextFile(path+'output2')
counts = booksRDD.collect()

#
# pairs = tokensRDD.map(lambda s: (s, 1))
# counts = pairs.reduceByKey(lambda a, b: a + b)
# counts.saveAsTextFile(path+"output")
print counts


# logData = sc.textFile(logFile).cache()
#
# numAs = logData.filter(lambda s: 'a' in s).count()
# numBs = logData.filter(lambda s: 'b' in s).count()
#
# print("Lines with a: %i, lines with b: %i" % (numAs, numBs))
#
# sc.stop()
from pyspark import SparkContext, SparkConf
import os
import sys
from nltk.tokenize import RegexpTokenizer


tokenizer = RegexpTokenizer(r'\w+')

def tokenize(text):
    return tokenizer.tokenize(text.lower())


def tokens(text):
    return [line.split() for line in text]



path = "/home/ckamat/PA2_Raft/Distributed-Systems/PA3/Spark/"
logFile = "shakespeare.txt"  # Should be some file on your system
logFile = path + logFile
conf = SparkConf().setAppName("Simple App").setMaster("local")
sc = SparkContext(conf=conf)
lines = sc.textFile(logFile)
tokensRDD = lines.flatMap(lambda line: line.split(" "))
pairs = tokensRDD.map(lambda s: (s, 1))
counts = pairs.reduceByKey(lambda a, b: a + b)
counts.saveAsTextFile(path+"output")
print counts


# logData = sc.textFile(logFile).cache()
#
# numAs = logData.filter(lambda s: 'a' in s).count()
# numBs = logData.filter(lambda s: 'b' in s).count()
#
# print("Lines with a: %i, lines with b: %i" % (numAs, numBs))
#
# sc.stop()
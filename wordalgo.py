# coding=utf8
import re

class discretize:
    #self.signRE = re.compile("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+".decode("utf8"))
    
    self.signRE = re.compile("[\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+".decode("utf8"))
    def __init__(self, code='utf8'):
        self.code = 'utf8'

    def removeSign(self, wordline):
        self.signRE.sub(wordline, ' ')
    def word2char(self, word):


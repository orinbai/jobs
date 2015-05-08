# coding=utf8
import re

class discretize:
    #self.signRE = re.compile("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+".decode("utf8"))
    
    def __init__(self, code='utf8', maxchar=6):
        self.code = 'utf8'
        self.maxchar = 6
        self.signRE = re.compile("[\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+".decode(self.code))
        #self.signRE = re.compile("[\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+")

    def removePunctuation(self, wordline):
        return self.signRE.sub(" ".decode(self.code), wordline.decode(self.code))
    def word2char(self, word):

        return False


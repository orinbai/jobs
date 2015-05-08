# coding=utf8
import re

class discretize:
    
    def __init__(self, code='utf8', maxchar=6):
        self.code = 'utf8'
        self.maxchar = 6
        self.enumrate = range(1, maxchar)
        self.signRE = re.compile("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+".decode(self.code))

    def _removePunctuation(self, wordline):
        return self.signRE.sub(" ".decode(self.code), wordline.decode(self.code))

    def _char2line(self, word):
        tmparray = []
        for x in range(len(word)-1):
            for width in self.enumrate:
                if x+width >= len(word):
                    tmparray.append(word[x:])
                    break
                tmparray.append(word[x:x+width])
        return tmparray

    def word2char(self, word):
        ## OutPut a multiple array ##
        tmparray = []
        k = self._removePunctuation(word)
        for sChar in k.split():
            tmparray.append(self._char2line(sChar))
        return tmparray


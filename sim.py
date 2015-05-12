import MatrixComputing as mc
import math

clusterArray = ["cluster-1","cluster-2","cluster-3","cluster-4","cluster-5","cluster-6","cluster-7","cluster-8","cluster-9","cluster-10"]
#clusterArray = ["cluster-1"]
clusterNum = {}
preArray = {}
sigma = {}
epsilon = {}
testgroup = {}
epsilon_test = {}
allArray = []
### Distance ###
d = {}




### 22 Features ###
mc = mc.MatrixComputing(22)

def EpsilonIJ(Array):
    allArray.append(Array)
    tmpEsp = {}
    for cluster in clusterArray:
        preArray[cluster].append(Array)
        tmpEsp[cluster] = mc.Epsilon(mc.Var(allArray), mc.Var(preArray[cluster]),clusterNum[cluster]+1)
        preArray[cluster].pop()
    allArray.pop()
    return tmpEsp

#>>>>>>>> computing Sigma(k), Sigma(vk) <<<<<<<<#
for cluster in clusterArray:
    i = 0
    preArray[cluster] = []
    #f = open('%s.train.txt' % cluster)
    f = open('%s.txt' % cluster)
    f.readline()
    ## matrixes cluster ##
    for line in f:
        i += 1
        aa = line.strip().split(',')
        aa[1:-1] = map(float, aa[1:-1])
        preArray[cluster].append(aa[1:-1])
    f.close()
    ### Sigma(vk) ###
    sigma[cluster] = mc.Var(preArray[cluster])
    clusterNum[cluster] = i
    allArray.extend(preArray[cluster])

### sigma(k) ###
mc.clear()
#sigma['all'] = mc.Var(allArray)

### Computing Cluster Epsiloni(i) ###
#for cluster in clusterArray:
#    epsilon[cluster] = mc.Epsilon(sigma['all'], sigma[cluster], clusterNum[cluster])

### test start ###
num = 0
f = open('cluster-5.test.txt')
for line in f:
    if num > 100: break
    num += 1
    aa = line.strip().split(',')
    testgroup[aa[0]] = map(float, aa[1:-1])
    #break
    #print epsilon_test[aa[0]]
f.close()

### Computing Epsilon(j) of Single record ###
for cookie in testgroup.keys():
    allArray.append(testgroup[cookie])
    epsilon_test[cookie] = mc.Epsilon(mc.Var(allArray), mc.Var([testgroup[cookie]]), 1)
    allArray.pop()

#print epsilon_test
print '-'*8
### Computing Epsilon(i,j) ###
#epsilonIJ = EpsilonIJ([epsilon_test[cookie]])

for cookie in epsilon_test.keys():
    epsilonIJ = EpsilonIJ(testgroup[cookie])
    tmpd = {}
    allArray.append(testgroup[cookie])
    allVar = mc.Var(allArray)
    allArray.pop()
    for cluster in clusterArray:
        epsilon[cluster] = mc.Epsilon(allVar, sigma[cluster], clusterNum[cluster])
        tmpd[cluster] = epsilon[cluster] + epsilon_test[cookie] - epsilonIJ[cluster]
    print cookie, sorted(tmpd, key=lambda x: tmpd[x])
    #print tmpd

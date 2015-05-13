import newSim
i = 0
preArray = {}
m = newSim.ClusterClassify('suv.sample.txt')
f = open('suv.sample.txt')
preArray['suv'] = []
for line in f:
    lines = line.strip().split("\t")
    if not lines[-1].startswith('clus'): continue
    i += 1
    lines = map(lambda x: m.featureOP[x](lines[x]), range(len(lines)))
    preArray['suv'].append(lines)
f.close()


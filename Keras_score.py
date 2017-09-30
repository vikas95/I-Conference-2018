ind2Stance={0: 'disagree', 1: 'unrelated', 2: 'agree', 3: 'discuss'}
Keras_tags=[]
file=open('PredVec_15.txt','r')
for line in file:
    probs=line.split()
    PredTag=probs.index(max(probs))
    Keras_tags.append(ind2Stance[PredTag])
print (len(Keras_tags))
print (Keras_tags)

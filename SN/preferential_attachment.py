import random
import numpy as np

from collections import defaultdict
def deg(edges,node):
    return len([(x,y) for (x,y) in edges if x==node or y==node])

def create_model(m0=5,Nodes=500):
    current_nodes=5
    
    edges=[
    (1,2),
    (1,3),
    (4,3),
    (1,5),
    (4,2),
    ]

    for i in range(int(Nodes/m0)):
        choices=[node for node in range(current_nodes) for x in range(deg(edges,node))]
        print(i)
        current_choosens=[]
        for x in range(m0):
            if (len(choices)==0):
                break
            choosen=random.choice(choices)
            current_nodes+=1
            edges.append((choosen,current_nodes))
            choices=list(filter(lambda a: a != choosen, choices))


    print(len(edges))


    dist=defaultdict(int)
    for x in range(Nodes+5):
        dist[deg(edges,x)]+=1

    s1=sorted(dist.items(), key=lambda item: item[0])
    print(*zip(*s1))
    return s1

def create_random_model(Nodes=500):
    current_nodes=5
    
    edges=[
    (1,2),
    (1,3),
    (4,3),
    (1,5),
    (4,2),
    ]

    for i in range(int(Nodes)):
        choices=[node for node in range(current_nodes) ]
        print(i)

        choosen=random.choice(choices)
        current_nodes+=1
        edges.append((choosen,current_nodes))
        choices=list(filter(lambda a: a != choosen, choices))


    print(len(edges))


    dist=defaultdict(int)
    for x in range(Nodes+5):
        dist[deg(edges,x)]+=1

    s1=sorted(dist.items(), key=lambda item: item[0])
    print(*zip(*s1))
    return s1
import matplotlib.pyplot as plt
f1 = plt.figure()
ax1 = f1.add_subplot(111)
N=800
s1=create_random_model(Nodes=N)
s2=create_model(m0=1,Nodes=N)
s3=create_model(m0=5,Nodes=N)
# plt.xlim(1,65)
# plt.plot(*zip(*s1),label="m0=5",fillstyle="none")
plt.plot(*zip(*s2),'ro',label="m0 = 1",fillstyle="none")
plt.plot(*zip(*s3),'g^',label="m0 = 5",fillstyle="none",linewidth=1.)
plt.plot(*zip(*s1),'b.',label="random",fillstyle="none",linewidth=1.)
plt.xlabel('Degree')
plt.ylabel('[Occurence / Frequence]')
plt.legend(loc=1)
plt.xticks(np.arange(0,max(max(list(zip(*s1))[0]),max(list(zip(*s2))[0]))+5, 5.0))
print(max(max(s1[0]),max(s2[0])))
plt.show()



    




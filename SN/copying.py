import random
import numpy as np

from collections import defaultdict

def degree(edges,node):
    edges_from_node=[y for (x,y) in edges if x==node]
    return len(edges_from_node)

def node_count(edges):
    sources=[x for (x,y) in edges]
    return len(list(set(sources)))


def copying(edges,N=300,m=3,p=.5):

    nodes=3
    for new_node in range(nodes,N+nodes):
        if (new_node%500==0):
            print("node num",new_node)
        rnd_node=random.randrange(0,new_node)
        # node_degree=degree(edges,rnd_node)
        # print(f"chosen deg for {rnd_node} is{node_degree}")

        old_neighbors=set([y for (x,y) in edges if x==rnd_node ])
        # print(all_ref)
        all={y for y in range(new_node)}
        for i in range(m):
            prob=random.uniform(0, 1)
            # print(prob)
            if (prob<p and len(old_neighbors)>0):
                #old neighbor selection

                new_dest=random.choice(list(old_neighbors))
                edges.append((new_node,new_dest))
                edges.append((new_dest,new_node))
                old_neighbors.discard(new_dest) 
                all.discard(new_dest) 
                
                # old_neighbors=[x for x in old_neighbors if x!=new_dest]
                # all=all-set(old_neighbors)
            else:
                if (len(all)==0):
                    continue
                new_dest=random.choice(list(all))
                edges.append((new_node,new_dest))
                edges.append((new_dest,new_node))
                all.discard(new_dest) 
                # all=all-set(old_neighbors)
            # print(edges)
    return edges

def plot_dist(list_of_edges_collection):
    print(len(list_of_edges_collection))
    comm_dist=defaultdict(int)
    counter=0
    import matplotlib.pyplot as plt
    import time
    f1 = plt.figure()
    ax1 = f1.add_subplot(111)
    tic = time.perf_counter()
    colors=['r','g','b','m']
    for (edges_collection,N,p0) in list_of_edges_collection:
        dist=defaultdict(int)
        exps=len(edges_collection)
        for edges in edges_collection:
            # print(f'edges for {N}-{p0}={len(edges)}')
            for x in range(N):
                # print(f'len{(N)}')
                dist[degree(edges,x)]+=1
    # for deg0 in range(N):
    #     comm_dist[deg0]+=sum([freq for (deg,freq) in dist.items() if (deg>=deg0)])
        dist={x:y/exps for (x,y) in dist.items()}
        print("deg 3",dist[3])
        s1=sorted(dist.items(), key=lambda item: item[0])
        print(s1)
        plt.loglog(*zip(*s1),colors[counter]+'.',label=f'p={p0}',fillstyle="none", basex=2, basey=2)
        # plt.plot(*zip(*s1),colors[counter]+'.',label=f'p={p0}',fillstyle="none")
        counter+=1
    plt.xlabel('Degree')
    plt.ylabel('[Occurence / Frequence]')
    plt.legend(loc=1)
    (edges_collection,N,p0)=list_of_edges_collection[0]
    exps=len(list_of_edges_collection[0][0])
    toc = time.perf_counter()

    plt.title(f'{N} nodes   {exps} experiments    {toc - tic:0.0f} seconds')
    # plt.xticks(np.arange(0,max(max(list(zip(*s1))[0]),max(list(zip(*s1))[0]))+5, 5.0))
    print(max(max(s1[0]),max(s1[0])))
    plt.show()


m0=3
N=5000
edges=[
(0,1),
(1,0),
(1,2),
(2,0)
]
list_of_exp_collection=[]
for p0 in [.01,.5,.95]:
    exp_res=[]
    for i in range(20):
        edges=[
        (0,1),
        (1,0),
        (1,2),
        (2,0)
        ]
        print(f'------------------exp num-------------------{i+1}')
        edges=copying(edges,N,m=m0,p=p0)
        exp_res.append(edges)
    list_of_exp_collection.append((exp_res,N,p0))
# print(edges)
plot_dist(list_of_exp_collection)









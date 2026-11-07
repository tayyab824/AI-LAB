"""Lab 4: A* audit and UCS control. Sample campus graph is explicitly assumed.
Undirected weighted graph. Tie-break: lower f, then earlier insertion.
Expansion count includes a valid goal pop; stale entries are skipped.
"""
import heapq
from itertools import count

GRAPH = {
 "S":[("A",2),("B",4)],
 "A":[("S",2),("C",2),("D",5)],
 "B":[("S",4),("D",1),("E",3)],
 "C":[("A",2),("G",5)],
 "D":[("A",5),("B",1),("G",3)],
 "E":[("B",3),("G",2)],
 "G":[("C",5),("D",3),("E",2)],
}
H={"S":7,"A":6,"B":4,"C":5,"D":3,"E":2,"G":0}
H_OVER=dict(H); H_OVER["C"]=10

def path_cost(path):
    return sum(next(w for n,w in GRAPH[u] if n==v) for u,v in zip(path,path[1:]))

def search(heuristic=None, verbose=True):
    h=heuristic or {n:0 for n in GRAPH}
    serial=count()
    heap=[(h["S"],next(serial),0,"S",["S"])]
    best={"S":0}; expanded=[]; stale=[]
    while heap:
        f,_,g,node,path=heapq.heappop(heap)
        if g != best.get(node):
            stale.append((node,g,f))
            if verbose: print(f"SKIP STALE {node}: g={g}, f={f}")
            continue
        expanded.append(node)
        if verbose: print(f"EXPAND {node}: g={g}, h={h[node]}, f={g+h[node]}")
        if node=="G":
            result={"path":path,"cost":g,"sum":path_cost(path),
                    "expanded":expanded,"count":len(expanded),"stale":stale}
            if verbose:
                print("PATH:", " -> ".join(path))
                print("RETURNED COST:",g,"INDEPENDENT SUM:",path_cost(path))
                print("EXPANDED ORDER:",expanded,"COUNT:",len(expanded))
            return result
        for nxt,w in GRAPH[node]:
            ng=g+w
            if ng < best.get(nxt,float("inf")):
                best[nxt]=ng; nf=ng+h[nxt]
                heapq.heappush(heap,(nf,next(serial),ng,nxt,path+[nxt]))
                if verbose: print(f"  INSERT/UPDATE {nxt}: g={ng}, h={h[nxt]}, f={nf}")
        if verbose:
            print("  FRONTIER:",[(x[3],x[2],x[0]) for x in sorted(heap)])
    return None

if __name__=="__main__":
    print("=== A* ORIGINAL HEURISTIC ==="); a=search(H)
    print("\\n=== UCS ZERO HEURISTIC ==="); u=search()
    print("\\n=== A* WITH h(C)=10 ==="); o=search(H_OVER)
    print("\\n=== SUMMARY ===")
    for name,r in [("A*",a),("UCS",u),("A* overestimate",o)]:
        print(name, "path=",r["path"],"cost=",r["cost"],
              "independent_sum=",r["sum"],"expanded=",r["expanded"],"count=",r["count"])

class Solution:
    def mostProfitablePath(self, edges: list[list[int]], bob: int, amount: list[int]) -> int:
        def dfs(graph,s,e, visited, path):
            visited.add(s)
            path = path.copy()
            path.append(s)
            foundPath = False
            tres = False
            for vertex in graph[s]:
                if alicedfs:
                    if(len(graph[vertex]) == 2):
                        path.append(vertex)
                        return [True,path]
                elif(vertex == e):
                    path.append(e)
                    return [True,path]
                if(vertex not in visited):
                    cp = path.copy()
                    y = dfs(graph, vertex, e,visited,cp)
                    [tres,tpath] = y
                if(tres):
                    if(alicedfs):
                        print(path)
                    if(foundPath):
                        if(len(tpath) < len(path)):
                            path = tpath
                    else:
                        foundPath = True
                        path = tpath
            return [foundPath , path]
        graph = []
        for i in range(len(edges) + 1):
            graph.append(set([i]))
        
        for edge in edges:
            [a,b] = edge
            graph[a].add(b)
            graph[b].add(a)

        #dfs Bob
        alicedfs = 0
        res = dfs(graph,bob,0,set(),[])
        bobpath = res[1]
        alicedfs = 1
        def findAlicePath(currSum, node,time,parent):
            if(node not in bobpath or bobpath.index(node) > time):
                currSum += amount[node]
            elif bobpath.index(node) == time:
                currSum += amount[node] //2
            if(len(graph[node]) == 2 and node != 0):
                return currSum
            else:
                return max(findAlicePath(currSum,nei,time+1,node) for nei in graph[node] if (nei is not node and nei is not parent))
        return(findAlicePath(0,0,0,-1))


class Solution1:
    def mostProfitablePath(self, edges: list[list[int]], bob: int, amount: list[int]) -> int:
        graph = {i: [] for i in range(len(amount))}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        bobPath = [-1] * len(amount)
        path = []

        def fillBobPath(node, parent):
            if node == 0:
                return True
            for neighbor in graph[node]:
                if neighbor != parent:
                    path.append(node)
                    if fillBobPath(neighbor, node):
                        return True
                    path.pop()

        fillBobPath(bob, -1)
        print(path)
        for i, node in enumerate(path):
            bobPath[node] = i
        
        def getAliceMaxScore(node, parent, currScore, timestamp):
            if bobPath[node] == -1 or bobPath[node] > timestamp:
                currScore += amount[node]
            elif bobPath[node] == timestamp:
                currScore += amount[node] // 2
            return currScore if len(graph[node]) == 1 and node != 0 else max(getAliceMaxScore(neighbor, node, currScore, timestamp + 1) for neighbor in graph[node] if neighbor != parent)

        return getAliceMaxScore(0, -1, 0, 0)
# print(Solution1().mostProfitablePath([[0,1],[1,2],[1,3],[3,4]],3,[-2,4,2,-4,6]))


class Solution3:
    def equationsPossible(self, equations: list[str]) -> bool:
        def dfs(graph, start, visited):
            visited.append(start)
            for nei in graph[start]:
                if(nei not in visited):
                    visited = dfs(graph, nei, visited)
            return visited
                    
        graph = {}
        nonEqs = []
        for eq in equations:
            if(eq[1] == "!"):
                nonEqs.append(eq)
            else:
                u = eq[0]
                v = eq[3]
                if(u not in graph.keys()):
                    graph[u] = [v]
                else:
                    graph[u].append(v)

                if(v not in graph.keys()):
                    graph[v] = [u]
                else:
                    graph[v].append(u)
        for ne in nonEqs:
            u = eq[0]
            v = eq[3] 
            x = dfs(graph, u,[])
            if(v in x):
                return False
        return(True)
    
# print(Solution3().equationsPossible(["a==b","b!=a"]))

class Solution4:
    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        flat_list = [
                x
                for xs in moveTime
                for x in xs
            ]
        n = len(moveTime)
        m = len(moveTime[0])
        def dfs(i,j, visited, timestamp):
            a1  = (max(flat_list) + 1) *m * n
            visited[tuple([i,j])] = timestamp
            if(i == n-1 and j == m-1):
                return timestamp
            if(i < n-1):
                if(timestamp >= moveTime[i+1][j] ):
                    a1 = min(a1,dfs(i+1,j,visited,timestamp+1))
            if(j < m-1):
                if(timestamp >= moveTime[i][j+1] ):
                    a1 = min(a1,dfs(i,j+1,visited,timestamp+1))

            havegoneright = (i < n-1 and timestamp >= moveTime[i+1][j]) or  i == n-1
            havegoeleft = (j<m-1 and timestamp >= moveTime[i][j+1]) or j == m-1
            if(havegoneright and havegoeleft):
                return a1
            else:
                a1 = min(a1,dfs(i,j,visited,timestamp+1))
                return a1
        return( dfs(0,0,dict(),0))
    
# print(Solution4().minTimeToReach([[3,72,14],[25,81,5]]))

class cheapG:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
            gmin = float("inf")
            graph = {i: [] for i in range(n)}
            weights = {}
            for u, v, w in flights:
                graph[u].append(v)
                weights[tuple([u,v])] = w
            
            def dfs(s,e,leftjumps, visited, current_weight):
                nonlocal gmin
                if(s == e and leftjumps >= 0):
                    gmin = min(gmin,current_weight)
                    return
                if(leftjumps <= 0):
                    return
                visited.add(s)
                for v in graph[s]:
                    if v == e:
                        if leftjumps > 0:
                            rv = current_weight + weights[tuple([s,v])]
                            gmin = min(gmin,rv)
                        continue
                    elif(v not in visited):
                        (dfs(v,e,leftjumps-1,visited,current_weight+weights[tuple([s,v])]))
                        visited.discard(v)
                return
            dfs(src,dst, k+1,set(),0)
            return gmin
arr  = [[0,12,28],[5,6,39],[8,6,59],[13,15,7],[13,12,38],[10,12,35],[15,3,23],[7,11,26],[9,4,65],[10,2,38],[4,7,7],[14,15,31],[2,12,44],[8,10,34],[13,6,29],[5,14,89],[11,16,13],[7,3,46],[10,15,19],[12,4,58],[13,16,11],[16,4,76],[2,0,12],[15,0,22],[16,12,13],[7,1,29],[7,14,100],[16,1,14],[9,6,74],[11,1,73],[2,11,60],[10,11,85],[2,5,49],[3,4,17],[4,9,77],[16,3,47],[15,6,78],[14,1,90],[10,5,95],[1,11,30],[11,0,37],[10,4,86],[0,8,57],[6,14,68],[16,8,3],[13,0,65],[2,13,6],[5,13,5],[8,11,31],[6,10,20],[6,2,33],[9,1,3],[14,9,58],[12,3,19],[11,2,74],[12,14,48],[16,11,100],[3,12,38],[12,13,77],[10,9,99],[15,13,98],[15,12,71],[1,4,28],[7,0,83],[3,5,100],[8,9,14],[15,11,57],[3,6,65],[1,3,45],[14,7,74],[2,10,39],[4,8,73],[13,5,77],[10,0,43],[12,9,92],[8,2,26],[1,7,7],[9,12,10],[13,11,64],[8,13,80],[6,12,74],[9,7,35],[0,15,48],[3,7,87],[16,9,42],[5,16,64],[4,5,65],[15,14,70],[12,0,13],[16,14,52],[3,10,80],[14,11,85],[15,2,77],[4,11,19],[2,7,49],[10,7,78],[14,6,84],[13,7,50],[11,6,75],[5,10,46],[13,8,43],[9,10,49],[7,12,64],[0,10,76],[5,9,77],[8,3,28],[11,9,28],[12,16,87],[12,6,24],[9,15,94],[5,7,77],[4,10,18],[7,2,11],[9,5,41]]
# print(cheapG().findCheapestPrice(17,
#                                  arr ,16,4,13))


class Solution2:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        color = [0] * (n+1)
        graph = {i:[] for i in range(1,n+1)}
        for u,v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        
        def bfs(u):
            if(color[u]):
                return True
            color[u] = 1
            q = [u]
            while q:
                c = q.pop()
                for v in graph[c]:
                    if(color[v] ):
                        if(color[v] == color[c]):
                            return False
                    else:
                        color[v] = color[c] * -1
                        q.append(v)
            return True

        for i in range(1,n+1):
            if( not bfs(i)):
                return False
        print(color)
        return True
# print(Solution2().possibleBipartition(4,[[1,2],[1,3],[2,4]]))

from collections import defaultdict
class Solution7:
    def findRedundantConnection(self, ogedges: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        for u,v in ogedges:
            graph[u].append(v)
            graph[v].append(u)
        q = [(u,-1)]
        visited = set()
        while q:
            top,prev = q.pop()
            foundcycle = False
            for i in graph[top]:
                if(i != prev and i in visited):
                    foundcycle = True
                    break
                else:
                    if i not in visited:
                        q.append((i,top))
            if foundcycle:
                break
            prev = top
            visited.add(top)
        # top and is a part of cycle
        # run dfs from top
        visited = set()
        def dfs(ini,edgestillnow,prev):
            if ini == top and len(edgestillnow):
                return edgestillnow,True
            bol = False
            rv = []
            visited.add(ini)
            for v in graph[ini]:
                if v != prev:
                    cpy = edgestillnow.copy()
                    cpy.append([ini,v])
                    rv,bol = dfs(v,cpy,ini)
                    if(bol):
                        return rv,bol
            return rv,bol

        edges, _ = dfs(top,[],-1)
        nedges = set()
        for e in edges:
            nedges.add(tuple(sorted(e)))
        for u,v in ogedges[::-1]:
            if (u,v) in nedges:
                return[u,v]

# print(Solution7().findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))

class Solution8:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        dp = {i:set() for i in range(0,target+1)}

        def crossprod(i,j):
            if not dp[i] or not dp[j]:
                return set()
            rv = set()
            for a in list(dp[i]):
                for b in list(dp[j]):
                    n = tuple(sorted(list(a) + list(b)))
                    rv.add(n)
            return rv
        for i in range(2,target +1):
            add = set()
            if i in candidates:
                add.add(tuple([i]))
            for j in range(1,(i//2) + 1):
                add = add | crossprod(j , i-j)
            dp[i] = add

        res = list(dp[target])
        res = [ list(x) for x in res ]
        return res

class Solution9:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        fin = []
        def backtrack(remain,currcomb,start):
            if remain == 0:
                fin.append(currcomb.copy())
                return
            if remain < 0:
                return 
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                else:
                    currcomb.append(candidates[i])
                    backtrack(remain - candidates[i], currcomb, i+1)
                    currcomb.pop()
            return
        
        backtrack(target,[],0)
        return fin
        

print(Solution9().combinationSum2([10,1,2,7,6,1,5], 8))






        
        
        





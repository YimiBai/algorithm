 # use two jugs with different capacities to measure a certain amount of water
 # 3 operations are allowed: empty one, fill one, fill one with the other
 # algorithm: BFS, time complexity:  O(m*n)
 
 
def jug_bfs(m, n, target)
  # m,n: int, capacities of jugs
  # target: int, target capacity
  # r: list[int], the path of the process
  que = []    
  que.append((m,n))
  targets = [(0,target),(target,0)]
  status_set = set([(m,n)])     # record of the visited nodes
  pre = {}                      # track the path
  res = []
  while que:
      status = que.pop()
      print status
      if status in target:
          print 'the result is:'
          s = status
          while s in pre:
              res.append(s)
              s = pre[s]
          res.append(s)
          break
      ops = [(status[0],0), (0, status[1]), (min(m,status[0]+status[1]), status[1] - min(status[1], m-status[0])),
             ( status[0]-min(status[0],n-status[1])  ,min( n,status[0] + status[1])),
             (m, status[1]), (status[0], n)]
      for op in ops:
          if op not in status_set:
              que.append(op)
              status_set.add(op)
              pre[op] = status
  return res         

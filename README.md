# DrivingDirectionsAlgo

# dijkstra's algo from textbook

def dijkstra(G, s):
distance = Vector(G.vertex_count(), None)
penultimate = Vector(G.vertex_count(), None)
seen = Vector(G.vertex_count(), False)
distance[s.index] = 0
seen[s.index] = True
done = False
while not done:
<FIND SOME EDGE b={v, u} SUCH THAT v IS SEEN AND u IS UNSEEN, AND
[s, ..., v, u]
IS A CORRECT SHORTEST PATH TO u>
if <NO SUCH b EXISTS>:
done = True
else:
distance[u.index] = distance[v.index] + b.label
penultimate[u.index] = v
seen[u.index] = True
return distance, penultimate
148

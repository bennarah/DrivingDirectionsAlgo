def dijkstra(graph, start):
    shortest_time = {}
    previous_place = {}
    unseen = list(graph.keys())

    for place in unseen:
        shortest_time[place] = float('inf')
    shortest_time[start] = 0

    while unseen:
        current = min(unseen, key=lambda place: shortest_time[place])
        unseen.remove(current)

        for neighbor, time in graph[current]:
            new_time = shortest_time[current] + time
            if new_time < shortest_time[neighbor]:
                shortest_time[neighbor] = new_time
                previous_place[neighbor] = current

    return shortest_time, previous_place

def get_path(previous_place, start, end):
    path = []
    current = end
    while current != start:
        if current is None:
            return ["No path found"]
        path.append(current)
        current = previous_place.get(current)
    path.append(start)
    return path[::-1]

graph = {
    'CSUF': [('57 Freeway', 5), ('Sand Canyon', 60)],
    '57 Freeway': [('5 Freeway', 10)],
    '5 Freeway': [('Sand Canyon', 7)],
    'Sand Canyon': [('Bassma\'s Home', 5)],
    'Bassma\'s Home': []
}

if __name__ == "__main__":
    start = 'CSUF'
    end = 'Bassma\'s Home'

    times, previous = dijkstra(graph, start)
    path = get_path(previous, start, end)

    print("Estimated Travel Time:", times[end], "minutes")
    print("Directions:", " → ".join(path))

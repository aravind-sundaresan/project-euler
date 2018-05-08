import collections

def breadth_first_search(graph, source):

	visited, queue = [], collections.deque([source])
	visited.append(source)

	while queue:
		vertex = queue.popleft()
		for neighbour in graph[vertex]:
			if neighbour not in visited:
				queue.append(neighbour)
				visited.append(neighbour)

	print(visited)


if __name__ == '__main__':
	graph = {0: [1, 3, 2], 1: [4, 6], 2: [3, 5], 3: [4], 4: [], 5: [], 6: []}
	breadth_first_search(graph, 0)
# Python 3 program to count all paths
# from a source to a destination.

# A directed graph using adjacency
# list representation
class Graph:

    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def addEdge(self, u, v):

        # Add v to u’s list.
        self.adj[u].append(v)

        # Returns count of paths from 's' to 'd'

    def countPaths(self, s, d):

        # Mark all the vertices
        # as not visited
        visited = [False] * self.V

        # Call the recursive helper
        # function to print all paths
        pathCount = [0]
        self.countPathsUtil(s, d, visited, pathCount)
        return pathCount[0]

        # A recursive function to print all paths

    # from 'u' to 'd'. visited[] keeps track
    # of vertices in current path. path[]
    # stores actual vertices and path_index
    # is current index in path[]
    def countPathsUtil(self, u, d,
                       visited, pathCount):
        visited[u] = True

        # If current vertex is same as
        # destination, then increment count
        if (u == d):
            pathCount[0] += 1
            print("Count",pathCount)

        # If current vertex is not destination
        else:

            # Recur for all the vertices
            # adjacent to current vertex
            i = 0
            #print("self.adj[u]", len(self.adj[u]))
            while i < len(self.adj[u]):
                if (not visited[self.adj[u][i]]):
                    self.countPathsUtil(self.adj[u][i], d,
                                        visited, pathCount)
                i += 1

        visited[u] = False


# Driver Code
if __name__ == '__main__':
    # Create a graph given in the
    # above diagram
    file = open("easy.txt")
    input = [int(line.strip("\n")) for line in file]
    file.close()
    input.sort()
    print(input)
    g = Graph(input[-1]+1)

    for i in range(len(input)):
        current = input[i]
        for j in range(i + 1, len(input)):
            next = input[j]
            if next - current < 4:
                print(current,next)
                g.addEdge(current, next)
    #print(g)
    total = 0
    d = input[-1]
    for i in range(len(input)):
        if input[i] < 4:
            print("From", input[i], "to", d)
            print(g.countPaths(input[i], d))
            total += g.countPaths(input[i], d)
            print("Total",total)
    print(total)
    #print(g.countPaths(s, d))
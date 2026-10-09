class Graph:
    def __init__(self, vertices):
        self.v = vertices
        
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]
  
        self.adj_list = {i: [] for i in range(vertices)}

    def add_edge(self, u, v):

        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1
        
       
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def display_matrix(self):
        print("\n--- Adjacency Matrix ---")
        for row in self.adj_matrix:
            print(" ".join(map(str, row)))

    def display_list(self):
        print("\n--- Adjacency List ---")
        for node, neighbors in self.adj_list.items():
            print(f"User {node}: {neighbors}")

    def is_connected(self, u, v):
       
        matrix_connected = self.adj_matrix[u][v] == 1
       
        list_connected = v in self.adj_list[u]
        
        print(f"\nChecking connection between User {u} and User {v}:")
        print(f"Matrix Result: {'Connected' if matrix_connected else 'Not Connected'}")
        print(f"List Result: {'Connected' if list_connected else 'Not Connected'}")



if __name__ == "__main__":
    
    num_users = int(input("Enter total number of users (e.g., 6): "))
    graph = Graph(num_users)

    num_edges = int(input("Enter number of connections (friendships): "))

    print("\nEnter each connection as 'user1 user2' (0-indexed, e.g., 0 1):")
    for _ in range(num_edges):
        u, v = map(int, input().split())
        graph.add_edge(u, v)
    graph.display_matrix()
    graph.display_list()
    print("\n--- Check Direct Connection ---")
    u1, u2 = map(int, input("Enter two users to check connection (e.g., 0 2): ").split())
    graph.is_connected(u1, u2)

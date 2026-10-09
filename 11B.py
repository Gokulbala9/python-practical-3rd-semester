from collections import deque


class SocialNetwork:

    def __init__(self, num_users):
        self.num_users = num_users
       
        self.adj_list = {i: [] for i in range(num_users)}

    def add_connection(self, u, v):
    
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def display_direct_friends(self, user):
        print(f"\nDirect friends connected to User {user}: {self.adj_list[user]}")

    def bfs(self, start_node):
        visited = []
        queue = deque([start_node])

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.append(node)
           
                for neighbor in self.adj_list[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        return visited

    def dfs(self, start_node):
        visited = []
        stack = [start_node]

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                
                for neighbor in self.adj_list[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)

        return visited


if __name__ == "__main__":
    
    num_users = int(input("Enter total number of users: "))
    network = SocialNetwork(num_users)

    num_edges = int(input("Enter number of connections (friendships): "))

    print("\nEnter connections as 'user1 user2' (0-indexed, e.g., 0 1):")
    for _ in range(num_edges):
        u, v = map(int, input().split())
        network.add_connection(u, v)

    start_user = int(
        input(
            f"\nEnter starting user ID (0 to {num_users - 1}) to analyze: "
        )
    )

    network.display_direct_friends(start_user)

    bfs_result = network.bfs(start_user)
    dfs_result = network.dfs(start_user)

    print(
        f"\nBFS Traversal (Reachable users level-by-level from User {start_user}):"
    )
    print(" -> ".join(map(str, bfs_result)))

    print(
        f"\nDFS Traversal (Reachable users depth-first from User {start_user}):"
    )
    print(" -> ".join(map(str, dfs_result)))

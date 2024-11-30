class RoundRobinLoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.index = 0

    def get_next_server(self):
        server = self.servers[self.index]
        self.index = (self.index +1) % len(self.servers)
        return server

    def add_server(self, server):
        self.servers.append(server)
        print(f"\n{server} added.")

    def remove_server(self, server):
        self.servers.remove(server)
        print(f"\n{server} removed.")
        if self.index >= len(self.servers):
            self.index = 0

if __name__ == "__main__":
    servers = ["server1", "server2", "server3"]
    load_balancer = RoundRobinLoadBalancer(servers)

    for i in range(5):
        print(f"Request {i+1}: {load_balancer.get_next_server()}")

    # Add a new server
    load_balancer.add_server("server4")
    print("\nAfter adding server4:")
    for i in range(5):
        print(f"Request {i+1}: {load_balancer.get_next_server()}")

    # Remove a server
    load_balancer.remove_server("server2")
    print("\nAfter removing server2:")
    for i in range(5):
        print(f"Request {i+1}: {load_balancer.get_next_server()}")

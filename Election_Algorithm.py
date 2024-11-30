import random
import time
import threading

class Node(threading.Thread):
    def __init__(self, node_id, nodes):
        super().__init__()
        self.node_id = node_id
        self.nodes = nodes
        self.is_coordinator = False

    def run(self):
        time.sleep(random.randint(1, 5))
        if self.is_coordinator:
            print(f"Node {self.node_id} is the coordinator")
        else:
            self.start_election()

    def start_election(self):
        print(f"Node {self.node_id} is starting an election")
        higher_nodes = [node for node in self.nodes if node.node_id > self.node_id]

        if higher_nodes:
            for node in higher_nodes:
                node.receive_election(self.node_id)
        else:
            self.become_coordinator()

    def receive_election(self, sender_id):
        print(f"Node {self.node_id} received election message from Node {sender_id}")

        if sender_id > self.node_id:
            print(f"Node {self.node_id} acknowledges election from Node {sender_id}")
            self.start_election()

    def become_coordinator(self):
        print(f"Node {self.node_id} becomes the coordinator")
        self.is_coordinator = True

        for node in self.nodes:
            if node.node_id != self.node_id:
                node.announce_coordinator(self.node_id)

    def announce_coordinator(self, coordinator_id):
        print(f"Node {self.node_id} acknowledges Node {coordinator_id} as coordinator")

num_nodes = 5
nodes = [Node(i, []) for i in range(num_nodes)]

for node in nodes:
    node.nodes = nodes

for node in nodes:
    node.start()

time.sleep(10)

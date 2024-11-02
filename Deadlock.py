class Resource:
    def __init__(self, name):
        self.name = name
        self.holder = None

class Process:
    def __init__(self, name):
        self.name = name
        self.held_resources = []

    def request_resource(self, resource):
        if resource.holder is None:
            resource.holder = self
            self.held_resources.append(resource)
            print(f"{self.name} acquired {resource.name}.")

        else:
            print(f"{self.name} is waiting for {resource.name} held by {resource.holder.name}.")

def detect_deadlock(processes):
    for process in processes:
        if len(process.held_resources) == 2:
            print(f"Potential deadlock detected with {process.name} holding 2 resources.")

def main():
    r1, r2 = Resource("R1"), Resource("R2")
    p1, p2 = Process("P1"), Process("P2")

    p1.request_resource(r1)
    p1.request_resource(r2)
    p2.request_resource(r1)

    detect_deadlock([p1, p2])

if __name__ == "__main__":
    main()

from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler

# Restrict the server to only handle requests to /RPC2
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create the server
with SimpleXMLRPCServer(('localhost', 9000), requestHandler=RequestHandler) as server:

    # Register some functions
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y == 0:
            return "Error: Division by zero."
        return x / y

    # Register the functions
    server.register_function(add, 'add')
    server.register_function(subtract, 'subtract')
    server.register_function(multiply, 'multiply')
    server.register_function(divide, 'divide')

    print("Server is running on localhost:9000...")
    # Run the server's main loop
    server.serve_forever()

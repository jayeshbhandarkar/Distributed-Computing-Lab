import xmlrpc.client

# Create an XML-RPC client
with xmlrpc.client.ServerProxy("http://localhost:9000/RPC2") as proxy:
    # Example calls to the server
    print("3 + 5 =", proxy.add(3, 5))
    print("10 - 4 =", proxy.subtract(10, 4))
    print("7 * 6 =", proxy.multiply(7, 6))
    print("20 / 4 =", proxy.divide(20, 4))  

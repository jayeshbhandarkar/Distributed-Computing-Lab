import time

cs = False
pro = 0  
run = 5.0  
t1 = time.time() - run  

while True:
    key = input("Press a key (except 'q') to enter a process: ")
    if key == 'q':
        print("Exiting..")
        break

    if cs:
        t2 = time.time()
        if (t2-t1) > run:
            print(f"Process {pro - 1} exited critical section.")
            cs = False
        else:
            print("Error: Another process is currently executing!")
    else:
        print(f"Process {pro} entered critical section")
        cs = True
        pro += 1
        t1 = time.time()
        
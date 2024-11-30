from datetime import datetime, timedelta

def berkeley_algo(server_time, time1, time2):
    print("Server Clock =", server_time)
    print("Client Clock 1=", time1)
    print("Client Clock 2 =", time2)
    
    time_format = "%H:%M"
    try:
        s = datetime.strptime(server_time, time_format)   
        t1 = datetime.strptime(time1, time_format)       
        t2 = datetime.strptime(time2, time_format)
        
        st1 = (t1 - s).total_seconds()
        st2 = (t2 - s).total_seconds()
        print("t1 - s =", st1)
        print("t2 - s =", st2)
        
        avg_offset = (st1 + st2) / 2
        print("(st1 + st2) / 2 =", avg_offset)

        adj_server = s + timedelta(seconds=avg_offset)
        adj_t1 = t1 - timedelta(seconds=st1 - avg_offset)
        adj_t2 = t2 - timedelta(seconds=st2 - avg_offset)
        
        print("Synchronized Server Clock =", adj_server.strftime(time_format))
        print("Synchronized Client 1 Clock =", adj_t1.strftime(time_format))
        print("Synchronized Client 2 Clock =", adj_t2.strftime(time_format))
        
    except ValueError as e:
        print("Error parsing time:", e)

berkeley_algo("10:00", "10:05", "10:03")
        
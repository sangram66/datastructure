import threading 
  
def print_odd(num): 
    """ 
    function to print cube of given num 
    """  
    i=1
    while i <= int(num):
        print ("print_odd : {}".format(i))
        i+=2
  
def print_even(num): 
    """ 
    function to print square of given num 
    """

    i=0
    while i <= int(num):
        print ("print_even : {}".format(i))
        i+=2
  
if __name__ == "__main__": 
    # creating thread 
    x=input()
    t1 = threading.Thread(target=print_even, args=(x,)) 
    t2 = threading.Thread(target=print_odd, args=(x,)) 
  
    # starting thread 1 
    t1.start() 
    # starting thread 2 
    t2.start() 
  
    # wait until thread 1 is completely executed 
    t1.join() 
    # wait until thread 2 is completely executed 
    t2.join() 
  
    # both threads completely executed 
    print("Done!") 
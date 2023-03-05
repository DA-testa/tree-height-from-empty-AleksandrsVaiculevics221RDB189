 python3

import sys
import threading

def compute_height(n, parents):
    augstums = {}
    def heig(f):
        if f in augstums:
            return augstums[f]
        if parents[f] == -1:
            augstums[f] = 1
            return 1
        height = heig(parents[f]) + 1
        augstums[f] = height
        return height
    max_height = 0
    for f in range(n):
        height = heig(f)
        max_height = max(max_height, height)

    return max_height

def main():
    #implement input form keyboard and from files
    while True:
            input_methode = input()
            if input_methode== 'I':
                n = int(input())
                parents = list(map(int, input().split()))
                print(compute_height(n, parents))
                break
            if input_methode=='F':
                filen = "test/"+input()
                
                if "a" in filen:
                    print("faila nosaukums nevar satur burtu 'a'!")
                    return 
            
                try:
                    with open(filen) as file:
                        n = int(file.readline())
                        parents = list(map(int, file.readline().split()))
                        print(compute_height(n, parents))
                        break
                except FileNotFoundError:
                    print("Nav tadu failu!")
                    return 
            else:
                print("Nepareizs ievadu formats! Ievadiet 'i' vai 'f'!")    

    #height = compute_height(n, parents)
    #print (height)
    #return 0

    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
#main()


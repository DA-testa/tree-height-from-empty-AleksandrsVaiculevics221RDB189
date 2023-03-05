# python3

import sys
import threading

def compute_height(n, parents):
    # Write this function
    max_height = 0
    
    for i in range(n):
        root = 0
        while i !=-1:
            root = root+1
            i = parents[i]
            max_height = max(max_height, root)
    return max_height
#         if parents[i] == -1:
#             root = i
#             break
#     if root == -1:
#         return 0
    
#     q = [(root,1)]
#     height = 0
#     while q:
#         node,level = q.pop(0)
#         height = level
#         for i in range(n):
#             if parents[i] == node:
#                 q.append((i, level+1))
#     return height

def main():
    #implement input form keyboard and from files
    while True:
        try:
             input_methode = input()
        except EOFError:
            return
        if input_methode == "I":
            n = int(input())
            parents = list(map(int, input().split()))
            break
        if input_methode=="F":
            filen = "test/"+input()
            if "a" in filen:
                print("faila nosaukums nevar satur burtu 'a'!")
                return 1
            
            try:
                with open(filen) as file:
                    n = int(file.readline())
                    parents = list(map(int, file.readline().split()))
                    break
            except FileNotFoundError:
                print("Nav tadu failu!")
                return 
        #else:
         #   print("Nepareizs ievadu formats! Ievadiet 'i' vai 'f'!")    

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


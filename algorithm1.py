# Recursive Python function to solve the tower of hanoi



def TowerOfHanoi(n, source, destination, auxiliary,originalN):
    if n == 1:
        #print("Move disk 1 from source", source, "to destination", destination+" xd")
        return
    TowerOfHanoi(n - 1, source, auxiliary, destination,originalN)
    #print("Move disk", n, "from source", source, "to destination", destination)
    TowerOfHanoi(n - 1, auxiliary, destination, source,originalN)

    if n == originalN:
        return True




# Driver code
# A, C, B are the name of rods
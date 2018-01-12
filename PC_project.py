def matrix_transitive_check(matrix):
    """
    lst -> bool

    This function checks if matrix is transitive or not and returns the result.

    >>> matrix_transitive_check([0,0,0,0,1,0,0,0,1,1,0,0,1,1,1,0])
    True
    >>> matrix_transitive_check([1,1,0,0,1,1,0,0,0,0,0,1,1,0,0,1])
    False
    >>> matrix_transitive_check([0,1,1,0,1,0,0])
    Invalid matrix inputed. Please try another one.
    >>> matrix_transitive_check([3,5,1,12,9,7,-5])
    Invalid matrix inputed. Please try another one.

    """
    l = len(matrix)**0.5
    result = True
    if l.is_integer() == False:   #checking if matrix was inputed right or not
        print("Invalid matrix inputed. Please try another one.")
        return None
    else:
        l = int(l)
        mtrx = []
        for k in range(l): #Changing matrix form to more comfortable
            t_lst = matrix[k*l:(k+1)*l] 
            mtrx.append(t_lst)

        for i in range(l):
            for j in range(l):
                if mtrx[i][j] < 0 or mtrx[i][j] > 1:
                    print("Invalid matrix inputed. Please try another one.")
                    #checking if matrix was inputed right or not one more time
                    return None
                if mtrx[i][j] == 1:  #cheking if matrix is transitive
                    for k in range(l):
                        if mtrx[j][k] == 1 and mtrx[i][k] == 0:
                            result = False
                        else:
                            continue
    return result
if __name__ == "__main__":
    import doctest
    doctest.testmod()

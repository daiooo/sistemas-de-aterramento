import sys

def projATT_getNumberofRods(path,var):
    import projATT_functions as pat
    C=pat.function_LabviewResults(path,var)
    f = open("ResultProjATT.txt", "w")
    f.write(str(C[0]))
    f.close()
    return C

if __name__ == '__main__':
    # Map command line arguments to function arguments.
    projATT_getNumberofRods(*sys.argv[1:])

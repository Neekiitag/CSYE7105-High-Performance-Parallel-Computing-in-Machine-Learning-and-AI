import multiprocessing as mp

list_c = [[2, 3, 4, 5], [6, 9, 10, 12], [11, 12, 13, 14], [21, 24, 25, 26]]

def normalize(x):
    minimum = min(x)
    maximum = max(x)
    val = [(i - minimum)/(maximum-minimum) for i in x]
    return val

if __name__ == '__main__':
    pool = mp.Pool(mp.cpu_count())
    results = [pool.apply(normalize, args=(l, )) for l in list_c]
    pool.close()
    print("Normalized values of the given 2-D array list is as follows - \n")    
    print(results)
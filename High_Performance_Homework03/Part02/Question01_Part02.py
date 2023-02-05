
#Importing necessary Libraries
import pandas as pd
import numpy as np
import multiprocessing as mp
from multiprocessing import Pool
import time
import matplotlib
import matplotlib.pyplot as plt
import math

#Creating a DataFrame having the shape values with 20000 x 100
df = pd.DataFrame(np.random.randint(3, 10, size=[20000,100]))

speedup = []
cpus = [1, 2, 4, 8]

def sum_squares(x):
    temp = [y*y for y in x]
    return sum(temp)

def plot_speedupvscpus(cpus_nums):
    for i in cpus_nums:
        start = time.perf_counter()
        pool = Pool(processes=i)
        result = pool.map(sum_squares, [df[df.columns[column]]
                                        for column in df.columns])
        pool.close()
        speedup.append(time.perf_counter()-start)
      
    plt.plot(cpus, speedup)
    plt.title('Speedup V/s No of CPUs Used')
    plt.xlabel('No of CPUs Used')
    plt.ylabel('Speedup (in seconds)')
    plt.show()


#function to find the maximum and minimum values of each column, sum the squares of these two numbers, and then find the square root
def sqrt_cal(row):
    res1=list(row)
    res1.pop(0)
    res=math.sqrt(min(res1)*2 + max(res1)*2)
    return res

#Main Function
if __name__ == '__main__':
    
    with mp.Pool(1) as pool:

        start_time_1 = time.time()
        result = pool.imap(sqrt_cal, df.itertuples(name=None), chunksize=10)
        output = [round(x, 2) for x in result]
        end_time_1 = time.time() - start_time_1

    print("\nTime taken to run for cpu = 1 is:",end_time_1)                                              #printing output for cpu = 1
    

    with mp.Pool(2) as pool:

        start_time_2 = time.time()
        result = pool.imap(sqrt_cal, df.itertuples(name=None), chunksize=10)
        output = [round(x, 2) for x in result]
        end_time_2 = time.time() - start_time_2

    print("\nTime taken to run for cpu = 2 is:",end_time_2)                                                  #printing output for cpu = 2

    with mp.Pool(4) as pool:
        start_time_4 = time.time()
        result = pool.imap(sqrt_cal, df.itertuples(name=None), chunksize=10)
        output = [round(x, 2) for x in result]
        end_time_4 = time.time() - start_time_4

    print("\nTime taken to run for cpu = 4 is:",end_time_4)                                                    #printing output for cpu = 4

    with mp.Pool(8) as pool:
        start_time_8 = time.time()
        result = pool.imap(sqrt_cal, df.itertuples(name=None), chunksize=10)
        output = [round(x, 2) for x in result]
        end_time_8 = time.time() - start_time_8

    print("\nTime taken to run for cpu = 8 is:",end_time_8)                                                     #printing output for cpu = 8

    #Calculating the Speedup vs CPUs time and plotting the trend
    plot_speedupvscpus(cpus)
    plt.savefig('plot_speedupvscpus.png', bbox_inches='tight')
    plt.show()


import os  
                                                                    
import multiprocessing as mp

process = ('script1.py', 'script2.py', 'script3.py')        

def parallel(process):                                                             
    os.system('python {}'.format(process))

if __name__ == '__main__':
    pool = mp.Pool(processes=3)                                                     
    pool.map(parallel, process)
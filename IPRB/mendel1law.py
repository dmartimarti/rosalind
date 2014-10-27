### Mendel first law ###

def dominant(k,m,n):

    k = float(k)
    m = float(m)
    n = float(n)
    
    t = k + n + m  # total number of individuals
    
    dom_all = ((k/t) * ((k-1)/(t-1))) + (2 * ((k/t)*(m/(t-1)))) + 2 * ((k/t)*(n/(t-1))) + 0.75 * ((m/t)*((m-1)/(t-1))) + ((m/t)*(n/(t-1)))
    
    print dom_all
    
    #my_dict = {'kxk':1,'kxm':1,'kxn':1,'mxm':0.75,'kxn':0.5,'nxn':0}
    
dominant(21,22,22)
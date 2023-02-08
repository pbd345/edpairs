import math
##########################################################################################
def dist(x,y,n): # distance in Z_n
    d=(x-y)%n
    if d>n//2:
        d=n-d
    return d
##########################################################################################
def checkTuple(k1,k2,k,g2,n):
    mult_dict={}
    for i in range(1,k1): # initialize multiplicities from AP_n(1,k1)
        mult_dict[i]=k1-i
    len_dict=k1-1
    for i in range(1,k2):
        d=dist(0,g2*i,n)
        if d in mult_dict.keys(): # increment existing multiplicity and check it's not too big
            mult_dict[d]+=k2-i
            if mult_dict[d]>k-1:
                return "fails max"
        else: # create new distance and check we don't have too many
            mult_dict[d]=k2-i
            len_dict+=1
            if len_dict>k-1:
                return "fails num"
    if sorted(list(mult_dict.values()))==list(range(1,k)): # check the ED pair condition
        return "solution"
    return "candidate"
##########################################################################################
def search(verbose=False):
    print("Search returns parameter lists k1, k2, k, g2, n such that {AP_n(1,k1),AP_n(g2,k2)}")
    if verbose:
        print("has fewer than k distinct distances, each of multiplicity less than k.")
    else:
        print("forms an ED pair.")
    for t in range(1,30):
        for k2 in range(4,int(t+6*math.sqrt(2*t+40))+37):
            k2=int(k2)
            if k2>=7*t/3+1:
                k1=((k2*(k2-1))/t+1-t)/2
                if k1==int(k1) and k1>=k2:
                    k1=int(k1)
                    k=t+k1
                    for n in range(2*k1,6*k1):
                        beta=n/k1
                        if t<=5*beta-3/4 and (k2-t)**2/4<=n<=18*k2+36:
                            for g2 in range(k2-t,2*k1+1):
                                if math.gcd(g2,n)==1 and g2<=int(n/2):
                                    result=checkTuple(k1,k2,k,g2,n)
                                    if result=='solution' or (verbose and result==''):
                                        print(k1,k2,k,g2,n,result)

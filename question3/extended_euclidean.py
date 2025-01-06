


# computing the extended euclidean inverse i such that i* a mod p = 1

def extended_euclidean_inverse(a, p):
    # keep track of the original p value 
    original_p = p 
    # initialize arrays of quotients to hold all quotients necessary in the backward calculation
    quotients=[]
    
    # perform forward euclidean algorithm to find the  q's 
    
    while( (r:= p % a) != 0 ):
        q = p // a
        quotients.append(q)
        p= a
        a = r
    

    # perform reverse euclidean algorithm by using the computed quotients
    
    # initialize s and t 
    s= 1
    t= -quotients[-1]

    # skip the first value of the list 
    # decrement until the first quotient
    for i in range(len(quotients)-2, -1, -1):
        prev_t = t
        t= s - t*quotients[i]
        s= prev_t
       
    return t % original_p


# compute the needed inverse
a1 = 125681513
p1 = 2057547329

a2 = 2208276616121472267596290626568183546366694495512524718210265634418816822599057950873548490767184192948
p2 = 3125250912230709951372256510072774348164206451981118444862954305561681091773335180100000000000000000537
print(f'The inverse of the first test is: {extended_euclidean_inverse(a1, p1)}')

print(f'The inverse of the second test is: {extended_euclidean_inverse(a2, p2)} ')
        

    


"""
     1     
    212    
   32123   
  4321234
"""
# pattern 14


N = 5
res = ""
for i in range(1,N):
    k = N-i
    if i==1:
        res = str(i)
        print(" "*k,res," "*k)
        k -= 1
    else:

        res = str(i)  + res + str(i)
        print(" "*k,res," "*k)
        k -= 1




    
    
                                 
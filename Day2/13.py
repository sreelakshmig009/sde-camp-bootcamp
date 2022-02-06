"""
      1      
     1 1     
    1 2 1    
   1 3 3 1   
  1 4 6 4 1  
 1 6 1 0 5 1 
"""
# pattern 13
N = 5
for i in range(0,N+1):
    k = N-i
    res = str(11**i)
    res = " ".join(list(res))
    print(" "*k,res," "*k)
    k -= 1

    
    
        


    
        
        
        
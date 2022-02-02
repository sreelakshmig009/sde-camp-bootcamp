# largest among three numbers

# beginner friendly if else conditions
a,b,c = map(int,input().split())
if a>b:
    if a>c:
        print(a,"is greater")
        
    else:
        if c>b:
            print(c,"is greater")
        
else:
    if b>c:
        print(b,"is greater")
        
    else:
        print(c,"is greater")
 
 # legends use three conditions using and
 # max(a,b,c) is boring

def transfer(S,T):
    temp=[]
    
    while S:
        temp.append(S.pop())
    while temp:
        T.append(temp.pop())    

s=[1,2,3]
t=[]
transfer(s,t)
print("t:",t)        

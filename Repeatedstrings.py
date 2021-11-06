def fun(s,n):
    t=0
    new=""
    for i in range(n):
        for j in s:
            new+=j
    # print(new)    
    if len(new)==n: 
      t=1
    else:
      count=0         
      for i in new:
        if i=='a':
            count+=1        
    
    print(count)       
    
string=input("")   
num=int(input(""))
fun(string,num) 

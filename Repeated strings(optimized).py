str = input("")
n = int(input(""))
c=str.count("a")
num=c*(n//len(str))
t=n%len(str)
for i in range(t):
    if(str[i]=="a"):
        num+=1
        
print(num)

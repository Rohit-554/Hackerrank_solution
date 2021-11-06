# Algorithm 2
import time


def fun(s, n):
    count = 0
    if s.count('a') != len(s):
        length = ""
        for j in range(n):
            length = length + s
            if len(length) > 10:
                length = length[0:10]
                break

        print(length)

        for i in length:
            if i == 'a':
                count += 1
    else:
        count = len(s) * n

    print(count)


string = input("")
num = int(input(""))
fun(string, num)
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))


# Algorithm 1
# import time

# def fun(s,n):
#     t=0
#     new=""
#     for i in range(n):
#         for j in s:
#             new+=j
#     # print(new)
#     if len(new)==n:
#       t=1
#     else:
#       count=0
#       for i in new:
#         if i=='a':
#             count+=1

#     print(count)

# string=input("")
# num=int(input(""))

# fun(string,num)
# start_time = time.time()
# print("--- %s seconds ---" % (time.time() - start_time))

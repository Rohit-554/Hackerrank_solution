# Algorithm 2
import time


def fun(s, n):
    count = 0
    if len(s) > n:
        s = s[0:n]
        count = s.count('a')
    else:
        if(len(s) != s.count('a')):
            check = n / len(s)
            # print(check)
            # print(len(s))
            getter = int(check) * len(s)
            # print(s)
            s = s * int(check)
            #  print(s, n)
            # print(getter)
            check = n - getter
            count = s.count('a')
            # print(check)
            if check != 0:
                a = s[0:check]
                count = a.count('a')
                count = count + s.count('a')
            # print(check)r
            #     s = s * 2
            #     print(s)
            # print(count)
            # s = s[0:n]
        else:
            count = n

    print(count)


string = input("")
num = int(input(""))
fun(string, num)
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))


# def fun(s, n):
#     count = 0
#     if s.count('a') != len(s):
#         length = ""
#         for j in range(n):
#             length = length + s
#             if len(length) > 10:
#                 length = length[0:10]
#                 break

#         print(length)å

#         for i in length:
#             if i == 'a':
#                 count += 1
#         count = count * n
#     else:
#         count = len(s) * n

#     print(count)


# string = input("")
# num = int(input(""))
# fun(string, num)
# start_time = time.time()
# print("--- %s seconds ---" % (time.time() - start_time))


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

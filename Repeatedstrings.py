# Algorithm 2
#import time


def fun(s, n):
    if(s.count('a') != 0):
        count = 0
        if len(s) > n:
            s = s[0:n]
            count = s.count('a')
        else:
            if(len(s) != s.count('a')):
                check = n / len(s)
                getter = int(check) * len(s)
                final = s.count('a')
                final = final * int(check)
                check = n - getter
                count = final
                if check != 0:
                    s = s[0:check]
                    final = final + s.count('a')
                    # print(final)
                    count = final
            else:
                count = n
    else:
        count = 0

    print(count)


string = input("")
num = int(input(""))
fun(string, num)
#start_time = time.time()
#print("--- %s seconds ---" % (time.time() - start_time))



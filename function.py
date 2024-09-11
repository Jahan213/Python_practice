# def cal_sum(a, b):
#     sum = a+b 
#     print(sum)
#     return sum

# cal_sum(5,10)
# cal_sum(20,10)

# def cal_avg(a,b,c):
#     avg = (a+b+c)/3
#     print(avg)
#     return avg

# cal_avg(1,2,9)

# def cal_fact(n):
#     fact=1
#     for i in range(1, n+1):
#         fact=fact*i
#     print(fact)

# cal_fact(5)

# def find_num(num):
#     if(num%2 == 0):
#         print("EVEN")
#     else:
#         print("ODD")
       
# find_num(5)

# recursive function

def show(n):
    if(n==0):
        return 
    print(n)
    show(n-1)
show(6)
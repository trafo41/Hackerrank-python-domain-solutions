#-----------------------------------------textwrap---------------------------------
# # string = 'asdfghjklmnbv'
# for i in range(0,len(string),4):
#     print(string[i:i+4])
                      #-----------------OR------------------#

# import textwrap
# def wrap(string, max_width):
#     return textwrap.fill(string,max_width)


# string, max_width = input(), int(input())
# result = wrap(string, max_width)
# print(result)

#-------------------------------------------------------------------------------------------------
         #----------------------Designer Door Mat----------------------#
# n,m = (int(x) for x in input().split())
# z = (m - 7)//2
# x = '.|.'
# if n%2 != 0 and m == 3*n:
#     for i in range(1,n//2+1):
#         y = x*i + x*(i-1)
#         a = len(y)
#         f = '-'*((m-a)//2)
#         print(f + y + f) 

#     print('-'*z + 'WELCOME' + '-'*z)

#     for i in range(1,n//2+1):
#         f = '-'*(3*i)
#         a = len(f)
#         y = x*((m-2*a)//3)
#         print(f + y + f) 

#-------------------------------------------------------------------------------------------
#-----------
n =  int(input())
if n>=1 and n<=99:
    for i in range(n+1):
        print(i,oct(i)[2:],hex(i)[2:].upper(),bin(i)[2:])



printsorted(dict1.items(), key = lambda kv:(kv[1], kv[0])))     # sort dictionaryss
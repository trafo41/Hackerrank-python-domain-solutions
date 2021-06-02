 #-----------------------------------------textwrap---------------------------------
# string = 'asdfghjklmnbv'
# for i in range(0,len(string),4):
#     print(string[i:i+4])
#                     #   -----------------OR------------------#

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
# n =  int(input())
# if n>=1 and n<=99:
#     for i in range(n+1):
#         print(i,oct(i)[2:],hex(i)[2:].upper(),bin(i)[2:])

#------------------------------groupby---------------------------
# from itertools import groupby
# s = input().strip()
# z = groupby(s)
# v = []
# for i,j in z:
#     print(i,list(j))                                      # see what group by returns   , input = 1222331
#     x = (len(list(j)),int(i))
#     v.append(x)

# print("---------------------------")    
# for i in v:
#     print(i,end=' ')

#------------------------------------------IterABLES AND ITERATORS
# from itertools import combinations
# a = int(input())
# b = list(input().split())
# c = int(input())

# all_tuples = list(combinations(b,c))
# print(all_tuples)

# count = 0
# for i in all_tuples:
#     if 'a' in i:
#         count += 1
# print(count)
# print('{:.4f}'.format(count/len(all_tuples)))

# a,b = map(int,input().split())
# N = (list(map(int, input().split())) for i in range(a))
# print(N)

# for i in z:
#     sum += max(i)*max(i)
# print(sum%int(b))

#-------------------------------------------------------Maximize it----------------------------------------
# from itertools import product
# K,M = map(int,input().split())
# N = (list(map(int, input().split()))[1:] for i in range(K))
# results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
# print(max(results))

# from itertools import product
# K,M = map(int,input().split())
# N = list(list(map(int, input().split()))[1:] for i in range(K))
# print(list(product(*N)))

# results = list(map(lambda x: sum(i**2 for i in x)%M, product(*N)))
# print(max(results))

# print('-----------------------------------------------------------------------See this------------------------------------------------------------------')
# print(results,'\n')

# from itertools import product
# K,M = map(int,input().split())
# N = list(list(map(int, input().split())) for i in range(K))
# results = list(map(lambda x: sum(i**2 for i in x)%M, product(*N)))

# print(max(results))
# # print(list(product(*N)))
# print('-----------------------------------------------------------------------See this------------------------------------------------------------------')
# print(results,'\n')

#-----------------------------------------------------Sets Symmetric Difference
# a = int(input())
# set1 = set(map(int, input().split()))
# b = int(input())
# set2 = set(map(int, input().split()))

# z = list((set1 | set2) - (set1 & set2))
# for i in sorted(z):
#     print(i)

#-------------------------------------------------------------------Sets No idea
# faltu, no_list, a, b = list(map(int, input().split())),list(map(int, input().split())), set(map(int, input().split())), set(map(int, input().split()))

# happiness_score = 0

# for i in no_list:
#     if i in a:
#         happiness_score += 1
#     elif i in b:
#         happiness_score -= 1

# print(happiness_score)

#----------------------------------------------------------------------SEt add()
# n = int(input())
# stamps = set(input() for i in range(n))
# print(len(stamps))                                      # OR

# stamps = set()
# for i in range(n):
#     stamps.add(input())
# print(stamps)

#---------------------------------------------------------------------------------------
# .remove(x)
# This operation removes element  from the set.
# If element  does not exist, it raises a KeyError.
# The .remove(x) operation returns None.
# #------------------------------Difeerence--------------------
# .discard(x)
# This operation also removes element  from the set.
# If element  does not exist, it does not raise a KeyError.
 #------------------------------Difeerence--------------------
# .pop()
# This operation removes and return an arbitrary element from the set.
# If there are no elements to remove, it raises a KeyError.
#---------------------------------------------------------------------------------------

#-----------------------------------------------------Set .discard(), .remove() & .pop()

# n = int(input())
# s = set(map(int, input().split()))
# no_of_operations = int(input())

# for i in range(no_of_operations):
#     z = input().split()
#     if z[0] == 'pop':
#         s.pop()
#     elif z[0] == 'remove':
#         s.remove(int(z[1]))
#     elif z[0] == 'discard':
#         s.discard(int(z[1]))

#----------------------------------------------------------------------------------------

#Set is immutable to the .union() operation (or | operation).

#----------------------------------------------------------------------------------------
# >>> s = set("Hacker")
# >>> print s.union("Rank")
# set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

# >>> print s.union(set(['R', 'a', 'n', 'k']))
# set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

# >>> print s.union(['R', 'a', 'n', 'k'])
# set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

# >>> print s.union(enumerate(['R', 'a', 'n', 'k']))
# set(['a', 'c', 'r', 'e', (1, 'a'), (2, 'n'), 'H', 'k', (3, 'k'), (0, 'R')])

# >>> print s.union({"Rank":1})
# set(['a', 'c', 'r', 'e', 'H', 'k', 'Rank'])

# >>> s | set("Rank")
# set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])
#----------------------------------------------------------------------------------------
# A union B = C(elements in atleast  1 set)
#----------------------------------------------------------------------------------------
# >>> H = set("Hacker")
# >>> R = set("Rank")
# >>> H.intersection_update(R)                        #.intersection_update
# >>> print H
# set(['a', 'k'])

# >>> H = set("Hacker")
# >>> R = set("Rank")
# >>> H.update(R)                                    #.update
# >>> print H
# set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])

# >>> H = set("Hacker")
# >>> R = set("Rank")
# >>> H.difference_update(R)                          #.difference_update
# >>> print H
# set(['c', 'e', 'H', 'r'])

# >>> H = set("Hacker")
# >>> R = set("Rank")
# >>> H.symmetric_difference_update(R)                   #.symmetric_difference_update
# >>> print H
# set(['c', 'e', 'H', 'n', 'r', 'R'])

##---------------------------------------------------------------------------------
# -------------------------------------------------------------Set Mutations

# n = int(input())
# s = set(map(int, input().split()))
# no_of_operations = int(input())

# for i in range(no_of_operations):
#     z = input().split()
#     if z[0] == 'intersection_update':
#         k = set(map(int,input().split()))
#         s.intersection_update(k)
#     elif z[0] == 'symmetric_difference_update':
#         l = set(map(int,input().split()))
#         s.symmetric_difference_update(l)
#     elif z[0] == 'difference_update':
#         o = set(map(int,input().split()))
#         s.difference_update(o)
#     elif z[0] == 'update':
#         m = set(map(int,input().split()))
#         s.update(m)

# print(sum(s))

# #-------------------------------or
# n = int(input())
# s = set(map(int, input().split()))
# no_of_operations = int(input())

# for i in range(no_of_operations):
#     z = input().split()
#     if z[0] == 'intersection_update':
#         k = set(map(int,input().split()))
#         s.intersection_update(k)
#     elif z[0] == 'symmetric_difference_update':
#         k = set(map(int,input().split()))
#         s.symmetric_difference_update(k)
#     elif z[0] == 'difference_update':
#         k = set(map(int,input().split()))
#         s.difference_update(k)
#     elif z[0] == 'update':
#         k = set(map(int,input().split()))
#         s.update(k)

# print(sum(s))

#------------------------------------------------------------------OR best
# n = int(input())
# s = set(map(int, input().split()))
# no_of_operations = int(input())

# for i in range(no_of_operations):
#     z = input().split()
#     operation = z[0]
#     k = set(map(int,input().split()))
#     if operation == 'update':
#         s |= k
#     elif operation == 'intersection_update':
#         s &= k                                                                       # In every case updates will we reflected in s only
#     elif operation == 'symmetric_difference_update':
#         s ^= k
#     elif operation == 'difference_update':
#         s -= k
    
# print(sum(s))
# print(sum(k))                                                                      # printing sum of last set bcoz k is not affecting


#------------------------------------------------------namedtuple----------------------------------------------------------------
# from collections import namedtuple
# n = int(input())
# a = input()
# total = 0
# Student = namedtuple('Student', a)
# for _ in range(n):
#     student = Student(*input().split())
#     total += int(student.MARKS)
# print('{:.2f}'.format(total/n))

# from collections import namedtuple

# N = int(input())
# fields = input().split()

# total = 0
# for i in range(N):
#     students = namedtuple('student',fields)
#     field1, field2, field3,field4 = input().split()
#     student = students(field1,field2,field3,field4)
#     total += int(student.MARKS)
# print('{:.2f}'.format(total/N))

#------------------------------------------------------OrderedDict----------------------------------------------------------------
# from collections import OrderedDict

# n = int(input())
# odict = OrderedDict()
# for i in range(n):
#     litem = input().split(' ')
#     price = int(litem[-1])
#     item_name = ' '.join(litem[:-1])                                                    #see this

#     if odict.get(item_name):
#         odict[item_name] += price                                                      # see this
#     else:
#         odict[item_name] = price    
# for i,v in odict.items():
#     print(i,v)

# j = {'a' : 2, 'b' : 4}
# j['c'] = 6
# j['b'] += 6
# print(j)

from collections import Counter
# chars = Counter(input())                                                  # input : aabbbccde
# chars2 = list(Counter(input()).items())
# print(chars2)                                                               #  Counter({'b': 3, 'a': 2, 'c': 2, 'd': 1, 'e': 1})
# # print(chars2)                                                            #  dict_items([('a', 2), ('b', 3), ('c', 2), ('d', 1), ('e', 1)])   giving sorted
# print(chars2[:3])                                                            


# number_of_shoes = int(input())
# sizes_in_stock = Counter(map(int, input().split()))

# total = 0

# for _ in range(int(input())):
#     size, price = map(int, input().split())
#     if sizes_in_stock[size]:
#         total += price
#         sizes_in_stock[size] -= 1
#         print(sizes_in_stock)

# print(total)

from collections import deque

# for _ in range(int(input())):  
#     _, queue =input(), deque(map(int, input().split()))
    
#     for cube in reversed(sorted(queue)):
#         if queue[-1] == cube: queue.pop()
#         elif queue[0] == cube: queue.popleft()
#         else:
#             print('No')
#             break
#     else: print('Yes')

# j = deque(map(int, input().split()))                        
# print(j)                                                      gives deque([4, 3, 2, 1, 3, 4])
# print(sorted(j))                                              gives sorted list
# print(reversed(sorted(j)))


import calendar
# d, m, y = map(int, input().split())
# print(calendar.weekday(y, m, d))
# print(calendar.day_name[calendar.weekday(y, m, d)].upper())

# z = 5
# g = ++z
# print(g)
# def magic(n):
#     l =[]
#     for i in range(n,0,-1):
#         l2 = []
#         for _ in range(i-1):
#             l2.append(1)
#         l2.append(n+1-i)
#         l.append(l2)

#     return l

# def show(n):
#     finallist = []
#     for i in range(n,0,-1):
#         j = magic(i)
#         if i < n:
#             for k in j:
#                 k.append(n-i)
#                 finallist.append(k)
#         else:
#             for k in j:
#                 finallist.append(k)
    
#     yeah = []
#     for i in finallist:
#         i.sort()
#         yeah.append(i)

#     result = []
#     for i in yeah:
#         if i not in result:
#             result.append(i)
#     for i in result:
#         print(*i)
#     return result
    

# n = int(input())
# okay = show(n)
# print(okay)

# from itertools import permutations
# finalOkay = []
# for i in okay[1:]:
#     q = list((permutations(i)))
#     for j in q:
#         finalOkay.append(j)

# finalOkay2 = []
# for i in finalOkay:
#     if i not in finalOkay2:
#         finalOkay2.append(i)
# print(finalOkay2)
# v = (5,7,6,2)
# if v in finalOkay2:
#     print('yes')


# import itertools


# j = 2567
# stuff = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
# flag = False
# for L in range(1, len(stuff)+1):
    
#     for subset in itertools.combinations(stuff, L):
#         if j == sum(subset):
#             s = subset
#             flag = True
#             break
# if flag:
#     print(s)
#     result = ''
#     for i in s:
#         result = result + str(stuff.index(i)+1)
#     print(result)
# else:
#     print("Sorry")

# from itertools import permutations, combinations_with_replacement, combinations

# v = [1,2,3,4,5,6,7,8,9,10]
# list1 = []
# for i in range(2,len(v)):
#     j = combinations(v,i)
#     for k in j:
#         if sum(k) == 10:
#             list1.append(k)
# print(list1)
# list2=[]
# for i in range(2,len(v)+1):
#     j = combinations_with_replacement(v,i)
#     for k in j:
#         if sum(k) == 10:
#             list2.append(k)
# print(list2)
# print(list(permutations(list2)))

# from operator import itemgetter
# j = [(1,2),(9,0),(6,5),(7,6),(3,2),(8,1,6)]
# n = 1
# j.sort(key = itemgetter(n))
# j.sort()
# print(j)

# def sortdict(lst):
#     dct = {}
#     for i, j in lst:
#         dct.setdefault(i,[]).append(j)
    
#     # return [(i,*dict.fromkeys(j)) for i,j in dct.items()]
#     # return [(i,j) for i,j in dct.items()]
#     return [(i,*j) for i,j in dct.items()]

# lst = [(1,'jake'), (2,'bob'), (1,'carl')]
# print(sortdict(lst))


# from collections import OrderedDict

# def sortdict(lst):
#     dct = {}
#     for i, j in lst:
#         dct.setdefault(i,[]).append(j)

#     print([(i,) + tuple(OrderedDict.fromkeys(j)) for i,j in dct.items()])

#     return [(i,) + tuple(OrderedDict.fromkeys(j)) for i,j in dct.items()]

# lst = [(1,'jake'), (2,'bob'), (1,'carl')]



# def findp(v):
#     lst = list(v[i:i+j] for i in range(len(v)) for j in range(i,len(v)) if len(v[i:i+j]) > 1)
#     print(v)

#     flag = False
#     for i in v:
#         if i == i[::-1]:
#             flag = True
    
#     if flag:
#         return 'Yes'
#     else:
#         return 'No'

# v = 'veenaj'
# lst = []
# for i in range(len(v)):
#     for j in range(i,len(v)):
#         if len(v[i:j+1]) > 1:
#             lst.append(v[i:j+1])
# lst.sort(key = lambda x : len(x))
# print(lst)


# lst = list(v[i:i+j] for i in range(len(v)) for j in range(i,len(v)) if len(v[i:i+j]) > 2 )


# print(lst)
# print(findp(lst))

# # print(v[2:6])

# v = 'Palindrome'
# z = [4,0,1]
# c = ['i','l','i']
# ve = []
# for i in range(len(c)):
#     a = z[i]
#     b = c[i]
#     d = v[a]
#     ve.append(v.replace(d,b,a))
#     # ve.append(v)
# for i in ve:
#     print(findp(i))

# v = 'veenaj'
# n = len(v)
# new = []
# for len in range(2,n+1):
#     for i in range(n-len+1):
#         j = i+len-1
#         s = ''
#         for k in range(i,j+1):
#             s+=v[k]
#         new.append(s)
#             # print(v[k],end='')
# print(new)


# for i in range(n):
#     s = ''
#     for j in range(i,n):
#         s += v[j]
#         new.append(s)
# print(new)



# i = 0
# count = 0
# lst = [(2,12),(4,13),(16,18),(6,10),(3,15),(19,20),(4,6)]
# a = lst[0][0]
# while(i<len(lst)):
#     if a < lst[i][0]:
#         b = lst[i][0] - a
#         if b >1:
#             count += b
#         a = lst[i][1]
#         i += 1
#     elif a < lst[i][1]:
#         a = lst[i][1]
#         i += 1
#     else:
#         i += 1
    
# print(count)
#------------------------------------------------------------------------------------------------------

# count = []
# def findp(p):
#     for i in p:
#         if i == i[::-1]:
#             print(i,end=' ')
#             count.append(len(i))                                #  don't what is happening here
#     return count


# v = 'aaaabbbc'
# n = len(v)
# new = []
# for len in range(2,n+1):
#     for i in range(n-len+1):
#         j = i+len-1
#         s = ''
#         for k in range(i,j+1):
#             s+=v[k]
#             new.append(s)
#             print(v[k],end='')

# new = ['bc', 'bb', 'aaaab', 'ab', 'aaabb', 'aaaabbbc', 'aaab', 'aabb', 'bbc', 'aaaabb', 'aabbb', 
# 'abbb', 'aab', 'aaa', 'aaaa', 'aabbbc', 'bbbc', 'aaabbbc',
# 'abbbc', 'aa', 'abb', 'bbb', 'aaabbb', 'aaaabbb']
# print(set(new))
# print(type(new),type(new[5]))
# print(findp(set(new)))

# print(findp(new))

#------------------------------------------------------------------------------------------------------
from itertools import permutations, combinations
# dictionary = ['heater', 'cold', 'clod', 'reheat', 'docl']
# query = ['codl', 'heater', 'abcd']
# ans = []
# # set1 = set(dictionary)

# for i in  query:
#     # lst = []
#     count = 0
#     lst = set(''.join(s) for s in permutations(i))
#     for j in dictionary:
#         if j in lst:
#             count+=1
#     ans.append(count)














# g = 'cold'
# print(list(g))
# g = list(permutations(list(g)))
# # for i in g:
# #     print(''.join(i), end=' ')
# new =  [''.join(i) for i in g]
# # c,d = 0,0
# # for i in new:
# #     if i == 'heater':
# #         c +=1
# #     elif i == 'reheat':
# #         d+=1
# # print(c,d)
# print(new)
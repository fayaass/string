# a='helo'

# print(a[0])
# print(a[-1])



            #string

# collection of characters enclose in '' or ""
# string is immutable(unchangable)

# negative and positive index position
# negative starts from -1,-2....
# positive starts from 0,1,2........


    #slice

# syntax=a[starting index : ending index]


# a='welcome'

# print(a[2:])
# print(a[:1])
# print(a[1:4])
# print(a[::2])
# print(a[::-1])


    #format

#we can add space through {:no}

# print("{:10}{:10}".format("hello","welcome"))


# a='welcome'

# print(a.capitalize())       #to change the first letter into capital letter
# print(a.upper())            #to change all letters to capital letters
# print(a.lower())            #to change all letters to small letters
# print(a.isupper())         
#                             #to check the letters are capital or small letters 
# print(a.islower()) 
# print(a.isalpha()) 
#                             #to check this is letters or numbers  
# print(a.isdigit()) 
# print(a.index('e',0))       #to check the index position
# print(a.index('e'))         #to check how many specified letter
# print(a.center(20))         #to get space 
# print(a.strip())            #to remove white space ,there are lstrip and rstrip
# print(a.startswith('w'))    #to check the starting letter

# b='helo good morning'

# print(b.replace('morning','afternoon'))  #to change word(morning to afternoon)



# a='malayalam'
# rev=''
# for i in a:
#     rev=i+rev
# print(rev)

# if rev==a:
#         print(rev,'its palindrome')
# else:
#         print(rev,'its not palindrome')


b='welcome'
alpha=0
lower=0
caps=0
for i in b:
    if i.isalpha():
        alpha+=1
    elif i.islower():
        lower+=1
    else i.capitalize():
        caps+=1
    
    







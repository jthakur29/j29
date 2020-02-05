def cm(a,b):
    a_set=set(a)
    b_set=set(b)
    if(a_set & b_set):
        return True
    else:
        return False
a=[56,3425,78,2,9]
b=[6764,546,45,9,4]
print(cm(a,b))

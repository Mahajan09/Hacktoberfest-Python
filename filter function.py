def seam(n):
    if(n%2==0):
        return True
    else:
        return False
l2=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
result= list(filter(seam,l2))
print(result)

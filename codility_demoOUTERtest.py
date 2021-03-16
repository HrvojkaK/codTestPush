def solutionWRONG(A):
    Nmax=A.__len__()
    #print(Nmax)
    i=1
    while i <Nmax:
        if A.__contains__(i) == False:
            integer=i
            break
        i=i+1
    return integer


#zakaj ovo ne dela u Py 3.6?
def solutionWrongAgain(A):
    #Nmax=A.__len__()
    #print(Nmax)
    i=1
    while i < 100000:
        if A.__contains__(i) == False:
            integerM=i
            #print(integerM)
            break
        i=i+1
    return integerM

#print(solutionWRONG([3,-2,1]))


#fakit. ovo gore su bili parcijalni pokusaji. ovo dole je OK finally.
##################
#ovo eksueli i prolazi i radi za slucajeve za koje ovi gore ne:
#[1,2,3] treba vratit 4
#[-1,-2] treba vratit 1

#ok je samo kaj je jako spor pa mi ga Codility ubije za Nmax>10 000
def solution(A):
    Nmax=A.__len__()
    #print(Nmax)
    integerM=0
    i=1
    while i <Nmax:
        if A.__contains__(i) == False:
            integerM=i
            break
        i=i+1

    if (Nmax==1 and A[0]>1):
        integerM=A[0]-1 

    if integerM==0:
        j=0
        pos=0
        integerM=0
        while j<Nmax:
            if A[j] >0:
                pos=1
                if A[j]>integerM:
                   integerM=A[j] 
                
            j=j+1
            
        if pos==0:
            integerM=1
        if pos==1:
            integerM=integerM+1
            
#        if pos==1:
#            k=1
#            integerM=A[0]
#            while k<Nmax:
#                if A[k]> integerM:
#                    integerM=A[k]
            
            
            
            
    return integerM

A=[-10,0,1,3,2,4,5,6,8,7,9,10,12]
B=[-3,-1,1,2,4]
C=[5]
integer=solution(C)
print(integer)


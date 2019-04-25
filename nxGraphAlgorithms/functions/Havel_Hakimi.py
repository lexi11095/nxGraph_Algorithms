D = [3,2,2,2,1]

def Havel_Hakimi_Derivative(D):
    for i in range(1,D[0]+1):
        D[i] -= 1
        D.pop(0)
        D.sort(reverse = True)
        return D
    
print(Havel_Hakimi_Derivative(D))
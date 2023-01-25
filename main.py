N = int(input("pin down yhe number of your project:"))
if N == 1:
    N = input("you most pin atleast 2 project :))...pleas try again: ")

method_list = ['NPW', 'EUAC', 'B/C']
method = input("Enter Your method ( NPW , EUAC , B/C) :").upper()


def PA(m, y):
    sorat1 = ((1 + m)**y)
    makhraj1 = m * ((m + 1)**y)
    x1 = (sorat1 -1)/(makhraj1)
    return x1
def PF(m, y):
    makhraj2 = (1 + m)**y
    x2 = 1 / (makhraj2)
    return x2


if method == method_list[0]:
    i = 1
    result_list = []
    n = int(input("pit down your intended time(n): "))
    while i < N + 1:
        print("PROJECT",i)
        P = int(input("pin down your intial capital(P):"))
        OC = int(input("pit down your operation cost(OC): "))
        GI = int(input("pit down your gross income(GI): "))
        MARR = float(input("pit down your minimum attractive range of return(MARR): "))
        SV = int(input("pit down your scrap value(SV): "))
        re1= (GI-OC) * PA(MARR , n)
        re2= SV * PF(MARR , n)
        Res= re1 + re2 - P
        print("result:", Res)
        i += 1
        result_list.append(Res)

    X= result_list.index(max(result_list))
    print("the best choice: PROJECT" , X+1)

def AP(m, y):
    sorat3 = m * ((m + 1) ** y)
    makhraj3 = ((1 + m) ** y)
    x3 = (sorat3)/(makhraj3 - 1)
    print(x3)
    return x3
def AF(m, y):
    sorat4 = m
    makhraj4 = ((1+m) ** y)
    x4 = (sorat4)/(makhraj4 - 1)
    print(x4)
    return  x4


if method == method_list[1]:
    i= 1
    result_list2 = []
    while i < N+1:
        P = int(input("pin down your intial capital(P):"))
        OC = int(input("pit down your operation cost(OC): "))
        GI = int(input("pit down your gross income(GI): "))
        MARR = float(input("pit down your minimum attractive range of return(MARR): "))
        SV = int(input("pit down your scrap value(SV): "))
        n = int(input("pit down your intended time(n): "))
        re1= OC - GI
        re2= P* AP(MARR , n)
        re3= SV* AF(MARR , n)
        Res2= +re1 + re2 - re3
        print("result" , Res2)
        i+=1
        result_list2.append(Res2)
    X= result_list2.index(min(result_list2))
    print("The best choice is:" , X+1)



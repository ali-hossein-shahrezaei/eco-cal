N = int(input("pin down yhe number of your project:"))
if N == 1:
    N = input("you most pin atleast 2 project :))...pleas try again: ")

method_list = ['NPW', 'NEUA', 'B/C']
method = input("Enter Your method ( NPW , EUAC , B/C) :").upper()


def PA(m, y):
    sorat1 = ((1 + m)**y)
    makhraj1 = m * ((m + 1)**y)
    x = (sorat1 -1)/(makhraj1)
    return x
def PF(m, y):
    makhraj2 = (1 + m)**y
    z= 1 / (makhraj2)
    return z



if method == method_list[0]:
    i = 1
    result_list = []
    n = int(input("pit down your intended time(n): "))
    while i < N + 1:
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
        result_list.extend(Res)
        X= result_list.index(max(result_list))
        print("the best choice" , X+1)

#if method == method_list[1]:
   # i= 1
   # result_list[]
   # while i < N+1:
     #   pass


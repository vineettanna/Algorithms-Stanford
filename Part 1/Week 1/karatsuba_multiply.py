def split(n):
    mid = len(n)//2
    if len(n) > 1:
        return n[:mid],n[mid:],len(n)
    return '0',n,1

def mutiply(p,q):
    str_p = str(p)
    str_q = str(q)
    if (len(str_p) < 2) or (len(str_q) < 2):
        return str(int(str_p) * int(str_q))
    a,b,lenp = split(str_p)
    c,d,lenq = split(str_q)
    ac = mutiply(a,c)
    bd = mutiply(b,d)
    step_3 = int(mutiply((int(a)+int(b)),(int(c)+int(d))))
    step_4 = str(int(step_3) - int(ac) - int(bd))
    return str(int(ac)*(10**lenp) + int(step_4)*(10**(lenq/2)) + int(bd))

print(mutiply(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627))
#print(mutiply(1501,1234))
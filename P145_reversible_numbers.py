
def isreversible(n):
    if n%10:
        s   = n + int(str(n)[::-1])
        return all(i%2 for i in (map(int, str(s))))
    else:
        return False


def nreversible(d):
    '''
    # of reversible numbers with n digits
    '''
    n, r    = divmod(d, 4)
    if r == 0 or r == 2:
        n   = d // 2
        return 20*(30**(n-1))       # 2n digit solutions (4n+0 or 4n+2)
    elif r == 1:
        return 0                    # no 4n+1 digits solutions
    else:
        return 5*20*((25*20)**n)    # 4n+3 digits solutions

count = 0
for i in range(1,10):
    print(str(i) + "," + str(nreversible(i)))
    count += nreversible(i)

print(count)
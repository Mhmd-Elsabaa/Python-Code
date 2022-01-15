puzzle = []
count = 0
with open("puzzle.txt", 'r') as file:
    for line in file:
        l = line.strip().split(' ')
        for v in l:
            puzzle.append(v)

def print_puzzle(puzzle):
    str = ""
    for i in range(9):
        if i% 3 == 0:
            str+="\n"
        if puzzle[i] == "0":
            str += "   "
        else:
            str += puzzle[i]
            str+="  "
    print (str)

def m_distance(p):
    res=0
    for i in range(8):
        if int(p[i]) != i+1:
            res +=1
    return res

def num_distance(p):
    res = 0
    for i in range(8):
        res += equal(i,p.index(str(i+1)))
    return res

def equal(n,i):
    res = 0
    while n != i:
        if i-3 >= n:
            res +=1
            i -= 3
        elif i-1 >= n:
            res +=1
            i -= 1
        elif i +3 <= n:
            res +=1
            i += 3
        elif i+1 <= n:
            res +=1
            i += 1
    return res

def moves(p):
    moves = [False,False,False,False]
    left = p.index('0') -1
    right = p.index('0') +1
    up = p.index('0') -3
    down = p.index('0') +3

    if left >= 0 and left < 9 and left != 2 and left != 5 :
        moves[0] = True

    if right >= 0 and right < 9 and right != 3 and right != 6:
        moves[1]= True

    if up >= 0 and up < 9:
        moves[2]= True

    if down >= 0 and down < 9:
        moves[3]= True

    return moves

def swap(p,a,b):
    t=p[a]
    p[a]=p[b]
    p[b] =t
    return p

def move(p):
    m = [False, False, False, False]
    left = 1000
    right = 1000
    up = 1000
    down = 1000
    l = []
    r = []
    u = []
    d = []
    for i in p:
        l.append(i)
        r.append(i)
        u.append(i)
        d.append(i)

    if (m_distance(p)+num_distance(p)) == 0:
        return p

    print_puzzle(p)
    global count
    count+= 1
    m = moves(p)
    if m[0] == True:
        l = swap(l,l.index('0'),l.index('0')-1)
        left = num_distance(l)+m_distance(l)

    if m[1] == True:
        r = swap(r,r.index('0'),r.index('0')+1)
        right =num_distance(r)+m_distance(r)

    if m[2] == True:
        u = swap(u,u.index('0'),u.index('0')-3)
        up = num_distance(u)+m_distance(u)

    if m[3] == True:
        d = swap(d,d.index('0'),d.index('0')+3)
        down = num_distance(d)+m_distance(d)

    if left <= right and left <= up and left <=down :
        p = swap(p, p.index('0'), p.index('0') - 1)

    elif right <= left and right <= up and right <= down:
        p = swap(p, p.index('0'), p.index('0') + 1)

    elif up <= right and up <= left and up <=down:
        p = swap(p, p.index('0'), p.index('0') - 3)

    elif down <= right and down <= up and down <= left :
        p = swap(p, p.index('0'), p.index('0') + 3)

    move(p)
    return p

m=move(puzzle)
print_puzzle(m)
print ("number of iterations ")
print (count)
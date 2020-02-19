N=int(input(''))

for i in range(N*2-1) :
    for j in range(N*2-1) :
        if j>=i :
            print(5-i)
        elif i>j :
            print(5-j)

    print("\n")

def floyd(n, row=1, num=1):
    if row > n:
        return
    
    print(" ".join(str(num + i) for i in range(row)))
    
 
    floyd(n, row + 1, num + row)

floyd(5)

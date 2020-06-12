def josephus(items,k):
    k = int(k)
    u = k-1
    per = []
    def permut(items,u,k):
        if items == []:
            return per
        else:
            if u > len(items) or u == len(items):
                u = u - len(items)
                permut(items,u,k)

            if items != []:
                p = items.pop(u)
                per.append(p)
                u = k + u - 1 
                permut(items,u,k)
            

    permut(items,u,k)
    return per
        
        

obj = []
res = josephus(obj,input())
print(res)
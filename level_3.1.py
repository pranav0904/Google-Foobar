import numpy as np

def solution(N): 
    shape=(N+1,N+1)
    steps = np.zeros(shape,int)

    steps[3][2] = steps[4][2] = 1   

    for y in range (5, N+1) :
        steps[y][2] = steps[y-2][2] + 1  
                                        
        for x in range (3, y + 1) :
            steps[y][x] = steps[y-x][x-1] + steps[y-x][x]
            if steps[y][x]==0: 
                break  

    return np.sum(steps[N])


print(solution(3))
print(solution(200))
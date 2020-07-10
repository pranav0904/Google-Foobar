'''
The challenge specification :
You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny prisoners, but once they're 
free of the prison blocks, the bunnies are going to need to escape Lambda's space station via the escape pods as quickly as possible. 
Unfortunately, the halls of the space station are a maze of corridors and dead ends that will be a deathtrap for the escaping bunnies. 
Fortunately, Commander Lambda has put you in charge of a remodeling project that will give you the opportunity to make things a little 
easier for the bunnies. Unfortunately(again), you can't just remove all obstacles between the bunnies and the escape pods - at most you 
can remove one wall per escape pod path, both to maintain structural integrity of the station and to avoid arousing Commander Lambda's 
suspicions.

You have maps of parts of the space station, each starting at a prison exit and ending at the door to an escape pod. 
The map is represented as a matrix of 0sand 1s, where 0s are passable space and 1s are impassable walls. 
The door out of the prison is at the top left (0,0) and the door into an escape pod is at the bottom right (w-1,h-1).

Write a function answer(map) that generates the length of the shortest path from the prison door to the escape pod,
where you are allowed to remove one wall as part of your remodeling plans. 
The path length is the total number of nodes you pass through, counting both the entrance and exit nodes.
The starting and ending positions are always passable (0).
The map will always be solvable, though you may or may not need to remove a wall. 
The height and width of the map can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.
'''


from collections import deque

def solution(map):
    h= len(map)
    w= len(map[0])
    q = deque([(0, 0, 1, True)])
    map[0][0] = -1

    if h < 2 or h > 20:
      return "Out of Range!!"
    else:
      while (True):
        x, y, step, wall = q.popleft()
        if (x == h-1 and y == w-2 or x == h-2 and y == w-1): 
            return step+1
        for a, b in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if (not (0 <=a < h and 0 <=b < w) or map[a][b] == -1 or map[a][b] == -2 and not wall or map[a][b] == 1 and not wall): 
              continue
            elif (map[a][b] in [0, -2]):
              q.append((a, b, step+1, wall))
            elif (map[a][b] == 1):
              q.append((a, b, step+1, False))
            if wall:
              map[a][b]=-1
            else:
              map[a][b]=-2
    return map[a][b]

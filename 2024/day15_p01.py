import time
import re

def move_piece(pos: tuple[int, int], move: tuple[int, int], boxes: list[tuple[int, int]], walls: list[tuple[int, int]], is_box: bool=False) -> bool:
    (new_x, new_y) = (pos[0]+move[0],pos[1]+move[1])
    if (new_x, new_y) in boxes:
        new_box_pos = move_piece((new_x, new_y), move, boxes, walls, True)  # recursively move boxes
        if new_box_pos != (new_x, new_y):
           if is_box:
               boxes[boxes.index(pos)] = (new_x, new_y)
           return (new_x, new_y)
    elif (new_x, new_y) in walls:
        return pos
    else:
        if is_box:
            boxes[boxes.index(pos)] = (new_x, new_y)
        return (new_x, new_y)
    return pos

def debug_print(pos, boxes, walls, dim_w, dim_h):
    for i in range(dim_h):
        line = []
        for j in range(dim_w):
            if (i,j) == pos:
                line.append('@')
            elif (i,j) in boxes:
                line.append('O')
            elif (i,j) in walls:
                line.append('#')
            else:
                line.append('.')
        print(''.join(line))

if '__main__' == __name__:
    with open('./data/day15.txt') as f:
        map_, moves = f.read().split('\n\n')
    map_ = map_.split('\n')
    moves = moves.replace('\n', '')
    boxes = []
    walls = []
    pos = (-1,-1)
    for i in range(len(map_)):
        for j in range(len(map_[i])):
            obj = map_[i][j]
            if obj == '#':
                walls.append((i,j))
            elif obj == 'O':
                boxes.append((i,j))
            elif obj == '.':
                pass
            else:
                pos = (i,j)

    map = {'^':(-1,0),'>':(0,1),'v':(1,0),'<':(0,-1)}
    for move in moves:
        pos = move_piece(pos, map[move], boxes, walls)
    debug_print(pos, boxes, walls, len(map_), len(map_[0]))
    result = sum([100*box[0]+box[1] for box in boxes])
    print(result)
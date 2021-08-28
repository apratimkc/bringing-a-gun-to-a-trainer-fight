import math

def get_mirror_coordinates(size,pos,rel_cg,layer_count):
    [w,h] = size
    (px,py) = pos
    
    dxR = (w-px)*2
    dxL = px*2
    x= [px-rel_cg[0]]*(layer_count*2+1)
    for i in range(layer_count+1,layer_count*2+1):
        x[i] = x[i-1]+dxR if (i-layer_count-1)%2==0 else x[i-1]+dxL
    for i in range(layer_count-1,-1,-1):
        x[i] = x[i+1]-dxL if (layer_count-1-i)%2==0 else x[i+1]-dxR
        
    dyU = (h-py)*2 #275-100=175*2=350
    dyD = py*2
    y= [py-rel_cg[1]]*(layer_count*2+1)
    for i in range(layer_count+1,layer_count*2+1):
        y[i] = y[i-1]+dyU if (i-layer_count-1)%2==0 else y[i-1]+dyD
    for i in range(layer_count-1,-1,-1):
        y[i] = y[i+1]-dyD if (layer_count-1-i)%2==0 else y[i+1]-dyU

    return x,y

def solution(dimensions, your_position, trainer_position, distance):
    player_pos = (your_position[0],your_position[1])
    trainer_pos = (trainer_position[0], trainer_position[1])
    min_d = min(dimensions)
    layer_count = (distance//min_d)+1 

    px, py = get_mirror_coordinates(dimensions,player_pos,player_pos,layer_count)
    tx, ty = get_mirror_coordinates(dimensions,trainer_pos,player_pos,layer_count)

    angle_dist = {}
    
    for _x in px:
        for _y in py:
            if (_x==0 and _y==0):
                continue
            d = math.hypot(_y,_x)
            if d<=distance:
                beam =  math.atan2(_y, _x)
                if beam in angle_dist:                
                    if d<angle_dist[beam]:
                        angle_dist[beam] = d
                else:
                    angle_dist[beam] = d
    
    res = set()
    for _x in tx:
        for _y in ty:
            d = math.hypot(_y,_x)
            if d<=distance:
                beam =  math.atan2(_y, _x)
                if beam in angle_dist:
                    if d<angle_dist[beam]:
                        angle_dist[beam] = d
                        #res.add((_x,_y))
                        res.add(beam)
                        #print(f'({player_pos[0]+_x},{player_pos[1]+_y})')
                else:
                    angle_dist[beam] = d
                    res.add(beam)
                    #print(f'({player_pos[0]+_x},{player_pos[1]+_y})')
    #print(res)                
    return len(res)

import matplotlib.pyplot as plt
def test_draw():
    dimensions= [300,275]
    player_pos = (150,150)
    trainer_pos = (185,100)
    distance = 500
    layer_count = 2
    px, py = get_mirror_coordinates(dimensions,player_pos,(0,0),layer_count)
    tx, ty = get_mirror_coordinates(dimensions,trainer_pos,(0,0),layer_count)

    for x in range(-900,1201,300):
        plt.plot([x,x],[-550,826])
    for y in range(-550,827,275):
        plt.plot([-900,1200],[y,y])
        
    for _x in px:
        for _y in py:
            plt.scatter(_x,_y,c='blue',s=0.5) 
    for _x in tx:
        for _y in ty:
            plt.scatter(_x,_y,c='red',s=0.5) 
    plt.savefig('plot2.png', dpi=300)
if __name__=='__main__':
    #print(solution([3,2], [1,1], [2,1], 4))
    #print(solution([300,275], [150,150], [185,100], 500))
    #test_draw()
    #print(solution([2,5], [1,2], [1,4], 11))
    print(solution([10,10], [4,4], [3,3], 5000))




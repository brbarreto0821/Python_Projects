from random import randint
  
def security():
    floor = ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
    floor.insert(randint(0, 9), 'G')
    floor.insert(randint(0, 10), '$')
    floor.insert(randint(0, 11), 'T')
    floor.insert(randint(0, 12), 'G')
    floor.insert(randint(0, 13), 'G')
    
    guard = floor.index('G')
    guard2 = floor.index('G')
    money = floor.index('$')
    thief = floor.index('T')
    
    quiet = 0
    pos = (g for g, value in enumerate(floor) if value == 'G')
    for i in pos:
        if (i < money < thief) or (i > thief > money) or (i < thief < money) or (i > money > thief):
            continue
        else:
            quiet += 1
    if quiet > 0:
        print("quiet")
    else:
        print("ALARM")       
        
    floor = "".join(floor)
    
    print(floor)
    
security()
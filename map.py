import matplotlib.pyplot as plt
class Position:
    locs = []
    def __init__(self) -> None:
        self.init_x_co = 0
        self.init_y_co = 0
        self.x_co = 0
        self.y_co = 0
    
    def command(self,distance,direction):
        if direction == "N" :
            self.y_co += distance
        elif direction == "S" :
            self.y_co -= distance
        elif direction == "E" :
            self.x_co += distance
        elif direction == "W" :
            self.x_co -= distance

    def Values(self):
        print(f"({self.x_co},{self.y_co})")

Object = Position()
Position.locs.append((Object.init_x_co,Object.init_y_co))
while True:
    command = input("Enter the command (For ex : 3mm,N) : ")
    if len(command) == 0:
        break
    distance = command.split(",")[0]
    direction = command.split(",")[1]
    if distance[-2] == 'c' and distance[-1] == 'm':
        distance = float(distance[0:-2])
        distance *= 10
    elif distance[-2] == 'm' and distance[-1] == 'm':
        distance = float(distance[0:-2])
    else :
        print("Units should be mm/cm")
        continue
    if len(direction) == 2:
        distance = distance * (1/2**0.5)
    for i in range(len(direction)):
        Object.command(distance,direction[i])
    Position.locs.append((Object.x_co,Object.y_co))
    
flag = 0
print("Final point ",end='')
if Position.locs[0][1] > Position.locs[-1][1]:
    print("is South",end='')
    flag += 1
elif Position.locs[0][1] < Position.locs[-1][1]:
    print("is North",end='')
    flag += 1
if Position.locs[0][0] > Position.locs[-1][0]:
    if flag == 0:
        print("is West",end='')
    else:
        print("west",end='')
    flag += 1
elif Position.locs[0][0] < Position.locs[-1][0]:
    if flag == 0:
        print("is East",end='')
    else:
        print("east",end='')
    flag += 1
if flag != 0:
    print(" of S")
else:
    print("Initial and Final positions are coinciding")

print("The euclidean distance(displacement) between S and final point is ",end='')
print(((Position.locs[0][0] - Position.locs[-1][0])**2 + (Position.locs[0][1] - Position.locs[-1][1])**2)**0.5,"mm")

x_values = [cos[0] for cos in Position.locs]
y_values = [cos[1] for cos in Position.locs]

plt.plot(x_values, y_values, marker='o', linestyle='-')
for i in range(len(Position.locs)):
    plt.scatter(x_values[i], y_values[i])
    plt.text(x_values[i], y_values[i], f"{i+1}", verticalalignment='bottom', horizontalalignment='right')
plt.title('Path Followed')
plt.xlabel('X-coordinate')
plt.ylabel('Y-coordinate')
plt.grid(False)
plt.show()
file = open("input.txt")
input = [line.strip("\n") for line in file]
file.close()
print(input)

directions = []
for i in range(len(input)):
    directions.append([input[i][0],int(input[i][1:])])
print(directions)

ship_NS = 0
ship_EW = 0
waypoint_NS = 1
waypoint_EW = 10
compass = ["N","E","S","W"]
for i in range(len(input)):
    print(input[i])
    if directions[i][0] == "N":
        waypoint_NS += directions[i][1]
    if directions[i][0] == "S":
        waypoint_NS -= directions[i][1]
    if directions[i][0] == "E":
        waypoint_EW += directions[i][1]
    if directions[i][0] == "W":
        waypoint_EW -= directions[i][1]
    if directions[i][0] == "R":
        turn = int(directions[i][1]/90)
        for j in range(turn):
            temp = waypoint_NS
            waypoint_NS = -(waypoint_EW)
            waypoint_EW = temp
    if directions[i][0] == "L":
        turn = int((360 - (directions[i][1]))/90)
        for j in range(turn):
            temp = waypoint_NS
            waypoint_NS = -(waypoint_EW)
            waypoint_EW = temp
    if directions[i][0] == "F":
        ship_NS += directions[i][1] * waypoint_NS
        ship_EW += directions[i][1] * waypoint_EW
    print("Waypoint: ", waypoint_NS, waypoint_EW)
    print("Ship: ", ship_NS, ship_EW)
print(abs(ship_NS)+abs(ship_EW))



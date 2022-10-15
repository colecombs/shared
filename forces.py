import math as m

forces = [429.0, 185.0, 135.0] # Newtons
angles = [233.0, 32.0, 6.0] # Degrees

if len(forces) != len(angles): # Check for equal list length
    print("Your input is missing a force or degree.")
    quit()

xCompSum = 0.0
yCompSum = 0.0

for index, force in enumerate(forces):
    angle = angles[index]
    xCompSum += force * m.cos(m.radians(angle))
    yCompSum += force * m.sin(m.radians(angle))

#print(f"xComponent is {xCompSum}")
#print(f"xComponent is {yCompSum}")

restMag = m.sqrt(xCompSum**2 + yCompSum**2) # Resultant Magnitude of a^2 + b^2
restMag = round(restMag, 3)

#print(f"The magnitude of the resultant force is {restMag}")

restDir = 0.0 # Degrees of resultant angle

if xCompSum == 0.0 and yCompSum == 0.0:
    restDir == 0.0
elif xCompSum == 0.0 and yCompSum > 0.0:
    restDir == 90.0
elif xCompSum == 0.0 and yCompSum < 0.0:
    restDir = -90.0
else:
    restDir = m.atan2(yCompSum, xCompSum) # returns RADIANS
    restDir = m.degrees(restDir) # converts to degrees
    restDir = round(restDir, 2)
if restDir < 180:
    restDir = restDir + 180

print(f"Resultant magnitude: {restMag} Newtons\nDirection: {restDir} Degrees")

import math as m

force1 = float(input("Input first force in N: "))
force2 = float(input("Input second force in N: "))
force3 = float(input("Input third force in N: "))

forces = [force1, force2, force3]

angle1 = float(input("Input first angle in degrees: "))
angle2 = float(input("Input second angle in degrees: "))
angle3 = float(input("Input third angle in degrees: "))

angles = [angle1, angle2, angle3]

#forces = [628.92, 100.0, 736.72] # Newtons
#angles = [165.0, 30.0, 315.0] # Degrees

if len(forces) != len(angles):  # Check for equal list length
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

restMag = m.sqrt(xCompSum**2 + yCompSum**2)  # Resultant Magnitude of a^2 + b^2
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
    restDir = m.atan2(yCompSum, xCompSum)  # returns RADIANS
    restDir = m.degrees(restDir)  # converts to degrees
    restDir = round(restDir, 2)
if restDir < 180:
    restDir = restDir + 180

print(f"Resultant magnitude: {restMag} Newtons\nDirection: {restDir} Degrees")

print("Copyright Cole B. Combs 2022 This code is reusable under the GNU General Public License v3")
print('Press Enter to Exit')
input()

  #This program is free software: you can redistribute it and/or modify it under the terms of the
  # GNU General Public License as published by the Free Software Foundation, either version 3 of the License,
  # or (at your option) any later version. This program is distributed in the hope that it will be useful,
  # but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  # See the GNU General Public License for more details. You should have received a copy of the GNU General Public License
  # along with this program. If not, see <https://www.gnu.org/licenses/>.
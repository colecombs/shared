import math as m

# The inputs all convert into floats, else your compounded rounding errors would be huge.

force1 = float(input("Input first force in N: "))
force2 = float(input("Input second force in N: "))
force3 = float(input("Input third force in N: "))

forces = [force1, force2, force3]  # Making a list.

angle1 = float(input("Input first angle in degrees: "))
angle2 = float(input("Input second angle in degrees: "))
angle3 = float(input("Input third angle in degrees: "))

angles = [angle1, angle2, angle3]  # Checking it twice.

if len(forces) != len(angles):  # Check for equal list length
    print("Your input is missing a force or degree.")
    quit()

# Perfectly balanced, as all things should be.
xCompSum = 0.0
yCompSum = 0.0

# The math to find component parts.
for index, force in enumerate(forces):
    angle = angles[index]
    # Python's "math" functions default to radians.
    # This converts the degree input to radians.
    xCompSum += force * m.cos(m.radians(angle))
    yCompSum += force * m.sin(m.radians(angle))

# print(f"xComponent is {xCompSum}")
# print(f"xComponent is {yCompSum}")

restMag = m.sqrt(xCompSum ** 2 + yCompSum ** 2)  # Resultant Magnitude of a^2 + b^2
restMag = round(restMag, 2)

# Degrees of resultant angle
restDir = 0.0

# Three checks for edge cases which would throw an error.
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
if restDir < 180:  # Use if the forces might be in any quadrant. If all forces are only in + x,y then comment out.
    restDir = restDir + 180

print(f"Resultant magnitude: {restMag} Newtons\nDirection: {restDir} Degrees")

print("Copyright Cole B. Combs 2022 This code is reusable under the GNU General Public License v3")
print('Press Enter to Exit')
input()

# This program is free software: you can redistribute it and/or modify it under the terms of the
# GNU General Public License as published by the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version. This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details. You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

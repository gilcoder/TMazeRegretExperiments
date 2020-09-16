# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 07:01:19 2020
@author: Gilzamir Gomes (gilzamir_gomes@uvanet.br)
"""
from tmaze import TMaze

m = TMaze()
print(m.get_position())
for i in range(20):
    m.forward()
assert m.get_position() == (0, 9), "FAIL: GO TOEND OF MAIN CORRIDOR"
print("PASS: GO TOEND OF MAIN CORRIDOR")

#BEGIN::TEST LEFT CORRIDOR
m.left()
assert m.get_position() == (2, 0), "FAIL: GET LEFT CORRIDOR"
print("PASS: GET LEFT CORRIDOR")

for i in range(2):
    m.forward()
assert m.get_position() == (2, 2), "FAIL: MIDDLE OF LEFT CORRIDOR"
print("PASS: MIDDLE OF LEFT CORRIDOR")

for i in range(4):
    m.forward()
assert m.get_position() == (2, 3), "FAIL: END OF LEFT CORRIDOR"
print("PASS: END OF LEFT CORRIDOR")

for i in range(3):
    m.backward()
assert m.get_position() == (2, 0), "FAIL: BACKWARD TO START OF THE LEFT CORRIDOR"
print("PASS: BACKWARD TO START OF THE LEFT CORRIDOR")

m.backward()
assert m.get_position() == (0, 9), "FAIL: GO BACK TO END OF THE MAIN CORRIDOR"
print("PASS: GO BACK TO END OF THE MAIN CORRIDOR")
#END::TEST LEFT CORRIDOR

#BEGIN TEST RIGHT CORRIDOR
m.right()
assert m.get_position() == (1, 0), "FAIL: GET RIGHT CORRIDOR"
print("PASS: GET RIGHT CORRIDOR")

for i in range(2):
    m.forward()
assert m.get_position() == (1, 2), "FAIL: MIDDLE OF RIGHT CORRIDOR"
print("PASS: MIDDLE OF RIGHT CORRIDOR")

for i in range(4):
    m.forward()
assert m.get_position() == (1, 3), "FAIL: END OF RIGHT CORRIDOR"
print("PASS: END OF RIGHT CORRIDOR")

for i in range(3):
    m.backward()
assert m.get_position() == (1, 0), "FAIL: BACKWARD TO START OF THE RIGHT CORRIDOR"
print("PASS: BACKWARD TO START OF THE RIGHT CORRIDOR")

m.backward()
assert m.get_position() == (0, 9), "FAIL: GO BACK TO END OF THE MAIN CORRIDOR"
print("PASS: GO BACK TO END OF THE MAIN CORRIDOR")
#END::TEST RIGHT CORRIDOR

m.reset()
assert m.get_position() == (0, 0), "FAIL: RESET FAIL"
print("PASS: RESET OK")





# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 06:41:06 2020
@author: Gilzamir F. Gomes
"""
class TMaze:
    def __init__(self, corridor = 10, right = 4, left = 4):
        self.pos = [0, 0]  #pos[0] = corridor, pos[1] = corridor position
        self.corridorLenght = [corridor, right, left]

    def forward(self):
        np = self.pos[1] + 1
        if np < self.corridorLenght[self.pos[0]]:
            self.pos[1] = np

    def backward(self):
        np = self.pos[1] - 1
        if np >= 0:
            self.pos[1] = np
        else:
            if self.pos[0] != 0:
                self.pos[0] = 0
                self.pos[1] = self.corridorLenght[0] - 1

    def right(self):
        if self.pos[0] == 0 and self.pos[1] == self.corridorLenght[0]-1:
            self.pos[0] = 1
            self.pos[1] = 0

    def left(self):
        if self.pos[0] == 0 and self.pos[1] == self.corridorLenght[0]-1:
            self.pos[0] = 2
            self.pos[1] = 0

    def get_position(self):
        return (self.pos[0], self.pos[1])
    
    def reset(self):
        self.pos = [0, 0]



#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  random_screen.py
#  
#  Copyright 2013 notna <anton@kosmonautL>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

#import random
import pygame
import sys
import numpy
import os

def random_generator(screen_size):
    return numpy.random.randint(low=0, high=255, size=(screen_size[0], screen_size[1], 3))

def main():
    #screen_size = [random.randint(200, 1000), random.randint(200, 500)]
    screen_size = [200, 200]
    screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
    #max_frame = random.randint(100, sys.maxint)
    prefix = "~/random_images/"
    frame = 0
    #fps = random.randint(5, 100)
    #clock = pygame.time.Clock()
    # Uncomment this to use Whichman Hill
    #random = random.WichmannHill()
    overlay = pygame.Surface([screen_size[0], 75], pygame.SRCALPHA)
    overlay.fill([50,50,50,60])
    overlay_pos = 0
    run = True
    while run:
        #frame += 1
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
            elif e.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode(e.size, pygame.RESIZABLE)
                screen_size = e.size
                overlay = pygame.Surface([screen_size[0], 75], pygame.SRCALPHA)
                overlay.fill([40,40,40,60])
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    fname = prefix+raw_input("Where do you want to save the image? "+prefix)
                    print "your image has been saved to "+os.path.abspath(fname)
                    pygame.image.save(screen.copy(), fname)
                elif e.key == pygame.K_F11:
                    screen = pygame.display.set_mode(screen.get_size(),pygame.FULLSCREEN|pygame.HWSURFACE|pygame.RESIZABLE)
                elif e.key == pygame.K_ESCAPE:
                    pygame.display.toggle_fullscreen()
        #w, h = screen.get_size()
        w,h = screen_size
        random = random_generator(screen_size)
        pygame.surfarray.blit_array(screen, random)
        #for y in range(0, h):
        #    for x in range(0, w):
        #        screen.set_at([x, y], random[x][y])
        #        #pygame.display.flip()
        #    pygame.display.flip()
        screen.blit(overlay, [0,overlay_pos])
        pygame.display.flip()
        frame += 1
        overlay_pos += 1
        if overlay_pos >= h:
            overlay_pos = -75
    return 0

if __name__ == '__main__':
    main()


#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  random_colors.py
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

import tools

import pygame
pygame.init()

COLOR_FILE = "colors.py"

EVENT_COLOR_CHANGE = pygame.USEREVENT

def main():
    screen = pygame.display.set_mode([100, 100])
    color = tools.random_color()
    paused = False
    pygame.time.set_timer(EVENT_COLOR_CHANGE, 1500)
    clock = pygame.time.Clock()
    color_number = 0
    number_font = pygame.font.Font(None, 20)
    f = open(COLOR_FILE, "a")
    print >> f, "# Start of session at "+tools.time_str()+"."
    run = True
    while run:
        clock.tick(20)
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                run = False
                print >> f, "# End of session at "+tools.time_str()+".\n"
                f.close()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    paused = not paused
                elif e.key == pygame.K_RETURN:
                    name = raw_input("Type a name for the color here: ")
                    print "Color Nr. "+str(color_number)+" with name '"+name+"':"+str(color)
                    print >> f, "colors['"+name+"'] = "+str(color)+""
                    color_number += 1
                    paused = True
            elif e.type == EVENT_COLOR_CHANGE:
                if not paused:
                    color = tools.random_color()
                screen.fill(color)
        screen.fill(color)
        screen.blit(number_font.render(str(color_number), 0, [0, 0, 0]), [0, 0])
        pygame.display.flip()
    return 0

if __name__ == '__main__':
    main()


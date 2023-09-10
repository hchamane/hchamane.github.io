"""
 towers_of_hanoi
 python pygame towers of hanoi simulation attempt
 author Hainadine Chamane
 date Sep 2023
"""

# import the libraries needed
import pygame
import sys

# Initialise Pygame
pygame.init()

# Constants for screen size and colors
window_size = (640, 480)
backgroung_color = (255, 255, 255)
peg_color = (149, 149, 149)
disk_colors = [(252, 51, 61), (252, 106, 7), (255, 255, 11), (69, 255, 60), (64, 146, 255)]
disk_height = 20
peg_width = 20

# Create a Pygame window
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Tower of Hanoi")


# Definition of a grid that can be used to convert between coordinates of larger cells and pixel coordinates
class Grid:
    """
    object-creation pattern
    """
    def __init__(self, left_x, top_y, width, height):
        self.leftX = left_x
        self.topY = top_y
        self.width = width
        self.height = height

    def pixel_x(self, grid_x):
        """
        :param grid_x:
        :return:
        """
        return self.leftX + grid_x * self.width

    def pixel_y(self, grid_y):
        """
        :param grid_y:
        :return:
        """
        return self.topY + grid_y * self.height


# Definition of a disk sprite
class Disk:
    """
    Color the objects
    """
    def __init__(self, number, peg, color):
        self.number = number
        self.peg = peg
        self.color = color
        self.w = peg_width * (number + 1.3)
        self.h = disk_height
        self.x = peg.x - self.w / 2 + peg.w / 2
        self.y = peg.y + peg.h - (disk_height + 0.1) * (peg.countDisks() + 1)
        peg.addDisk(self)

    def move_to_peg(self, dest_peg):
        """
        :param dest_peg:
        """
        self.peg.removeDisk()
        self.peg = dest_peg
        self.peg.addDisk(self)

    def move_to_peg_position(self):
        """
        peg movement
        """
        self.x = self.peg.x + self.peg.w / 2 - self.w / 2
        self.y = self.peg.y + self.peg.h - (self.h + 0.1) * (self.peg.getNumberOfDisksUnder(self) + 1)

    def draw(self):
        """
        pygame
        """
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))
        font = pygame.font.Font(None, 36)
        text = font.render(str(self.number), True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.x + self.w / 2, self.y + self.h / 2))
        screen.blit(text, text_rect)


# Definition of a peg sprite
class Peg:
    """
    peg class
    """
    def __init__(self, letter, number, x1, y1, w, h):
        self.letter = letter
        self.number = number
        self.x = x1
        self.y = y1
        self.w = w
        self.h = h
        self.disks = []

    def removeDisk(self):
        """
        remove disks
        """
        if self.disks:
            self.disks.pop()

    def addDisk(self, disk):
        """
        :param disk:
        """
        self.disks.append(disk)

    def countDisks(self):
        """

        :return:
        """
        return len(self.disks)

    def getTopDisk(self):
        """
        get top disks
        :return:
        """
        if self.disks:
            return self.disks[-1]
        return None

    def getNumberOfDisksUnder(self, disk):
        """

        :param disk:
        :return:
        """
        return self.disks.index(disk)

    def draw(self):
        """
        draw
        """
        pygame.draw.rect(screen, peg_color, (self.x, self.y, self.w, self.h))
        font = pygame.font.Font(None, 36)
        text = font.render(self.letter, True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.x + self.w / 2, self.y + 15))
        screen.blit(text, text_rect)


# Initialise pegs and disks
pegs = []
disks = []
peg_positions = [(window_size[0] / 4, window_size[1] / 5), (2 * window_size[0] / 4, window_size[1] / 5), (3 * window_size[0] / 4, window_size[1] / 5)]

for i in range(3):
    peg = Peg(chr(65 + i), i + 1, peg_positions[i][0] - peg_width / 2, peg_positions[i][1], peg_width,
              3 * window_size[1] / 6)
    pegs.append(peg)

for i in range(5):
    disk = Disk(i + 1, pegs[0], disk_colors[i % len(disk_colors)])
    disks.append(disk)

# Game loop
running = True
dragging_disk = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # Left mouse button clicked
                x, y = event.pos
                for disk in reversed(disks):
                    if disk.x <= x <= disk.x + disk.w and disk.y <= y <= disk.y + disk.h:
                        if disk == disk.peg.getTopDisk():
                            dragging_disk = disk
                            break
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                # Left mouse button released
                if dragging_disk:
                    for peg in pegs:
                        if peg.x <= event.pos[0] <= peg.x + peg.w and peg.y <= event.pos[1] <= peg.y + peg.h:
                            if peg.countDisks() == 0 or dragging_disk.number < peg.getTopDisk().number:
                                dragging_disk.move_to_peg(peg)
                                break
                    dragging_disk = None

    screen.fill(backgroung_color)

    for peg in pegs:
        peg.draw()

    for disk in disks:
        disk.draw()

    if dragging_disk:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dragging_disk.x = mouse_x - dragging_disk.w / 2
        dragging_disk.y = mouse_y - dragging_disk.h / 2

    pygame.display.flip()

pygame.quit()
sys.exit()

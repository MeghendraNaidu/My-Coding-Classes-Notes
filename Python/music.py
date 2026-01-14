import pygame
import math
import sys
import time

# ---------------- INIT ----------------
pygame.init()
pygame.mixer.init()

W, H = 800, 600
S = pygame.display.set_mode((W, H))
pygame.display.set_caption("Shapes with Sound")

clock = pygame.time.Clock()

# ---------------- SOUND ----------------
def tone(f):
    sr = 22050
    n = int(sr * 0.2)
    b = bytearray(n * 2)

    for i in range(n):
        s = int(30000 * math.sin(2 * math.pi * f * i / sr))
        b[2 * i] = s & 255
        b[2 * i + 1] = (s >> 8) & 255

    return pygame.mixer.Sound(buffer=bytes(b))


freq = {
    'C': 261,
    'D': 293,
    'E': 329,
    'F': 349,
    'G': 392,
    'A': 440,
    'B': 493,
    'C2': 523
}

tones = {k: tone(v) for k, v in freq.items()}

# ---------------- SHAPES ----------------
shapes = [
    {"p": [(-100, 0), (100, 0)], "t": ["C", "D"]},

    {"p": [(-80, -80), (80, -80), (80, 80), (-80, 80)],
     "t": ["C", "D", "E", "F"]},

    {"p": [(100 * math.cos(i * 0.78), 100 * math.sin(i * 0.78)) for i in range(8)],
     "t": ["C", "D", "E", "F", "G", "A", "B", "C2"]},

    {"p": [(100 * math.cos(i * 0.39), 100 * math.sin(i * 0.39)) for i in range(16)],
     "t": ["C", "D", "E", "F", "G", "A", "B", "C2"]}
]

# ---------------- STATE ----------------
i_s = 0
i_p = 0
prog = 0.0
line = []
paused = False

# ---------------- LOOP ----------------
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            paused = not paused

    if not paused:
        sh = shapes[i_s]
        cx, cy = W // 2, H // 2

        if i_p < len(sh["p"]):
            if len(line) <= i_p:
                x, y = sh["p"][i_p]
                line.append((cx + x, cy + y))

        prog += 0.02

        if prog >= 1:
            tones[sh["t"][i_p]].play()
            prog = 0
            i_p += 1

            if i_p >= len(sh["p"]):
                time.sleep(0.3)
                i_s = (i_s + 1) % len(shapes)
                i_p = 0
                line = []

    S.fill((20, 20, 30))

    for a, b in zip(line, line[1:]):
        pygame.draw.line(S, (0, 200, 0), a, b, 3)

    pygame.display.flip()
    clock.tick(60)

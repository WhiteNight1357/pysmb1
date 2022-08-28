import resources


def load(pxsize):
    resources.load(pxsize)


def tile_draw(level, campos, surface, pxsize):
    xpos = 0
    ypos = 0
    listxpos = 0
    listypos = 0

    if level == "0x11":
        level = resources.level1_1

    for row in level:
        for _ in row:
            tile = level[listypos][listxpos]
            if tile is None or xpos - campos < -16 * pxsize or xpos - campos > 256 * pxsize:
                xpos += 16 * pxsize
                listxpos += 1
                continue
            surface.blit(resources.tileset[tile], (xpos - campos, ypos))
            xpos += 16 * pxsize
            listxpos += 1
        ypos += 16 * pxsize
        xpos = 0
        listypos += 1
        listxpos = 0
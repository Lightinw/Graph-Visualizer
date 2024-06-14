import pygame
import math
from grid.node import Node
from design_set.global_variables import *
from design_set.text_design import drawText, drawTextcenter

pygame.init()
font = pygame.font.SysFont('arial', GAP)


def make_grid(rows, width):
    grid = []
    gap = 15
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows, [0, 0], math.inf, [-1, -1], -1, -1)
            grid[i].append(node)

    return grid


def draw_grid(win, rows, width):
    # gap = width // rows
    gap = 15
    for i in range(50):
        pygame.draw.line(win, BLACK, (0, i * gap), (GAP * 50 - 1, i * gap))
        for j in range(50):
            pygame.draw.line(win, BLACK, (j * gap, 0), (j * gap, GAP * 50 - 1))

    for i in range(gap):
        pygame.draw.line(win, LIGHT_BLUE, (ROWS * GAP, i), (WIDTH, i))
        pygame.draw.line(win, LIGHT_BLUE, (ROWS * GAP, HEIGHT - GAP + i), (WIDTH, HEIGHT - GAP + i))
        pygame.draw.line(win, LIGHT_BLUE, (ROWS * GAP, (int)(HEIGHT / 2) + 100 + i), (WIDTH, (int)(HEIGHT / 2) + 100 + i))
        pygame.draw.line(win, LIGHT_BLUE, (ROWS * GAP, 7 * GAP + 100 + i), (WIDTH, 7 * GAP + 100 + i))
        pygame.draw.line(win, LIGHT_BLUE, (ROWS * GAP, 14 * GAP + 100 + i), (WIDTH, 14 * GAP + 100 + i))
        pygame.draw.line(win, LIGHT_BLUE, (WIDTH - GAP + i, 0), (WIDTH - GAP + i, GAP * 50 - 1))
        pygame.draw.line(win, LIGHT_BLUE, (ROWS * GAP + i, 0), (ROWS * GAP + i, GAP * 50 - 1))


def draw(win, grid, rows, width, ALG_ID, time):
    win.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw(win)
            if spot.isStart == 1:
                spot.make_start()
                text = font.render(" ", True, BLACK)
                text_rect = text.get_rect(center=(spot.row * GAP + (int)(GAP / 2), spot.col * GAP + (int)(GAP / 2)))
                win.blit(text, text_rect)

            if spot.isEnd == 1:
                spot.make_end()
                text = font.render(" ", True, BLACK)
                text_rect = text.get_rect(center=(spot.row * GAP + (int)(GAP / 2), spot.col * GAP + (int)(GAP / 2)))
                win.blit(text, text_rect)

            if spot.is_barrier():
                text = font.render(" ", True, WHITE)
                text_rect = text.get_rect(center=(spot.row * GAP + (int)(GAP / 2), spot.col * GAP + (int)(GAP / 2)))
                win.blit(text, text_rect)

            if (spot.row == 0 and spot.col <= 49) or (
                    spot.row == 49 and spot.col <= 49) or (
                    spot.col == 0 and spot.row <= 49) or (
                    spot.col == 49 and spot.row <= 49):
                spot.make_barrier()

    draw_grid(win, rows, width)
    font1 = pygame.font.SysFont('script', 22)

    # Draw the topic if no algorithm is selected or reset button is clicked
    if ALG_ID == 0:
        font1 = pygame.font.SysFont('arial', 40)
        drawTextcenter("GRAPH VISUALIZER", font1, win, 965, 50, BLACK)
    else:
        font1 = pygame.font.SysFont('arial', 40)
        drawTextcenter("", font1, win, 965, 50, BLACK)


    # BFS Algorithm Initiate
    if ALG_ID == 1:
        for i in range(len(bfs_string)):
            if i == 0:
                font1 = pygame.font.SysFont('arial', 40)
                drawTextcenter(bfs_string[i], font1, win, 975, 50, BLACK)
            else:
                font1 = pygame.font.SysFont('arial', 22)
                drawText(bfs_string[i], font1, win, 825, 50 + i * 30, BLACK)

    # DFS Algorithm Initiate
    if ALG_ID == 2:
        for i in range(len(dfs_string)):
            if i == 0:
                font1 = pygame.font.SysFont('arial', 40)
                drawTextcenter(dfs_string[i], font1, win, 975, 50, BLACK)
            else:
                font1 = pygame.font.SysFont('arial', 22)
                drawText(dfs_string[i], font1, win, 825, 50 + i * 30, BLACK)

    # Dijkstra's Algorithm Initiate
    if ALG_ID == 3:
        for i in range(len(dijkstra_string)):
            if i == 0:
                font1 = pygame.font.SysFont('arial', 35)
                drawTextcenter(dijkstra_string[i], font1, win, 975, 50, BLACK)
            else:
                font1 = pygame.font.SysFont('arial', 22)
                drawText(dijkstra_string[i], font1, win, 825, 50 + i * 30, BLACK)


    font1 = pygame.font.SysFont('arial', 40)

    # drawTextcenter("GRAPH VISUALIZER",font1,win,965,50,BLACK)
    # drawTextcenter(dfs_string[i], font1, win, 975, 50, BLACK)

    drawTextcenter("Notations", font1, win, 960, 245, BLACK)
    font1 = pygame.font.SysFont('arial', 22)
    drawText("Start node", font1, win, 800, 275, BLACK)
    drawText("End node", font1, win, 925, 275, BLACK)
    drawText("Obstacle node", font1, win, 1050, 275, BLACK)
    drawText("Select Algorithm:", font1, win, 785, 520, BLACK)
    drawText("Elapsed time: " + str(format(time, ".1f")) + "s", font1, win, 825, 350, BLACK)

    total_visited_nodes = 0

    for rows in grid:
        for spot in rows:
            if spot.is_closed():
                total_visited_nodes += 1

    drawText("Visited nodes: " + str(total_visited_nodes), font1, win, 825, 375, BLACK)
    # Draw buttons and legends
    button_bfs.draw(win)
    button_dfs.draw(win)
    button_dijkstra.draw(win)
    button_reset.draw(win)
    button_start.draw(win)
    legend_start.draw(win)
    legend_end.draw(win)
    legend_obstacle.draw(win)
    pygame.display.update()

    # button_bfs.draw(win)
    # button_dfs.draw(win)
    # button_dijkstra.draw(win)
    # button_reset.draw(win)
    # button_start.draw(win)
    # legend_start.draw(win)
    # legend_end.draw(win)
    # legend_obstacle.draw(win)
    # pygame.display.update()


# grid separation between x coordinate and y coordinate
def get_clicked_pos(pos, rows, width):
    gap = 15
    y, x = pos
    row = y // gap
    col = x // gap

    return row, col

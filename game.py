import numpy as np
import random
import pygame
import sys
import math
from functions import *
from draw import *
from Tree import *

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)



def create_board():
	board = np.zeros((ROW_COUNT,COLUMN_COUNT))
	return board

ROW_COUNT = 6
COLUMN_COUNT = 7
WINDOW_LENGTH = 4
EMPTY = 0
SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE
size = (width, height)
RADIUS = int(SQUARESIZE/2 - 5)


def draw_board(board,screen):

	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):
			pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
			pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
	
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):		
			if board[r][c] == player.getPiece():# PLAYER_PIECE:
				pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
			elif board[r][c] == ai.getPiece():#AI_PIECE: 
				pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
	pygame.display.update()


def game(type, depth):
	board = create_board()
	print_board(board)
	game_over = False
	pygame.init()
	screen = pygame.display.set_mode(size)
	draw_board(board,screen)
	pygame.display.update()
	turn = random.randint(0, 1)

	while not game_over:
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.MOUSEMOTION:
				pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
				posx = event.pos[0]
				if turn == player.getTurn():
					pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)

			pygame.display.update()

			if event.type == pygame.MOUSEBUTTONDOWN:
				pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
				# Ask for Player 1 Input
				if turn == player.getTurn():
					posx = event.pos[0]
					col = int(math.floor(posx/SQUARESIZE))

					if is_valid_location(board, col):
						row = get_next_open_row(board, col)
						x = ROW_COUNT - row -1
						while x :
							b_board = board.copy()
							drop_piece(b_board,x,col,player.getPiece())
							draw_board(b_board,screen)
							pygame.time.wait(100)
							x = x-1
						drop_piece(board, row, col, player.getPiece())

						if isEndGame(board):		
							game_over = True

						turn=ai.getTurn()
						print_board(board)
						draw_board(board,screen)
							

						

		# # Ask for Player 2 Input		
		if turn == ai.getTurn() and not game_over:	
			tree.clear()
			root = expandTree(board,depth)
			setScores(depth)			

			if not type:
				col,minimax_score=minimax_withoutpruning(board,depth,True)
				now()
				img = guiTree(tree)
				show(img)
							
			else:
				col, minimax_score = minimax(board, depth, -math.inf, math.inf, True)
			
			
			if is_valid_location(board, col):
				row = get_next_open_row(board, col)
				x = ROW_COUNT - row -1
				while x :
							b_board = board.copy()
							drop_piece(b_board,x,col,ai.getPiece())
							draw_board(b_board,screen)
							pygame.time.wait(100)
							x = x-1
				drop_piece(board, row, col, ai.getPiece())

				if isEndGame(board):
					game_over = True

				turn=player.getTurn()
				print_board(board)
				draw_board(board,screen)
				# now()
				# img = guiTree(tree)
				# show(img)
								
				
	calcScore(board,player.getPiece())
	calcScore(board,ai.getPiece())

	displayScores(ai.getScore(),player.getScore())


import pygame

from setting import gameSetting
import documents
import gameplay

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

FONT_1984 = pygame.font.Font("Literally1984/ShareTechMono-Regular.ttf")

game_state = gameplay.GameState.DESK_VIEW
documents.add_prompt()

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  if game_state == gameplay.GameState.DESK_VIEW:
    gameSetting.draw_setting(screen)

    for paper in documents.papers:
      paper.draw_function(screen, paper.paper_type, paper.click_boundary, paper.paragraph_end, paper.end_line_length)
      paper.drag(0)
      is_clicked = paper.if_click(paper.display_paper, screen, game_state, FONT_1984, button_number=2)
      if is_clicked:
        game_state = gameplay.GameState.PAPER_VIEW
  
  if game_state == gameplay.GameState.PAPER_VIEW:
    print("hello")

  pygame.display.flip()

  clock.tick(60)

pygame.quit()
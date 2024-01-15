import pygame
from setting import gameSetting
import documents

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

FONT_1984 = pygame.font.Font("Literally1984/ShareTechMono-Regular.ttf")

pos = (100, 100)

click_boundary = pygame.rect.Rect(*pos, 100, 100)
def draw(screen):
  pygame.draw.rect(screen, pygame.color.Color(255, 255, 255), click_boundary)
test_paper = documents.Paper(documents.PaperType.NEWSPAPER, (100, 100))

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  gameSetting.draw_setting(screen)

  test_paper.draw_obj(screen, test_paper.paper_type, test_paper.click_boundary, test_paper.paragraph_end, test_paper.end_line_length)
  test_paper.drag(0)

  pygame.display.flip()

  clock.tick(60)

pygame.quit()
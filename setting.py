import pygame

papers = []

class Setting:
  SIDE_WALL_COLOR  = pygame.Color(58 , 58 , 66 )
  DESK_COLOR       = pygame.Color(145, 170, 171)
  FRONT_WALL_COLOR = pygame.Color(98 , 114, 115)
  SLOT_COLOR       = pygame.Color(0  , 0  , 0  )

  WALL_WIDTH  = 300
  WALL_HEIGHT = 300

  SCREEN_WIDTH  = 1280
  SCREEN_HEIGHT = 720

  SLOT_HEIGHT = 50

  DESK_RECT = pygame.rect.Rect(WALL_WIDTH                   ,
                               WALL_HEIGHT                  ,
                               SCREEN_WIDTH - 2 * WALL_WIDTH,
                               SCREEN_HEIGHT - WALL_HEIGHT  )

  MEMORY_HOLE_RECT = pygame.rect.Rect(2 * WALL_WIDTH / 3,
                                      SCREEN_HEIGHT / 2 ,
                                      SLOT_HEIGHT / 2   ,
                                      SLOT_HEIGHT * 3   )

  NEWSPAPER_TUBE = [
    (3 * WALL_WIDTH / 2, 2 * WALL_HEIGHT / 3),
    SLOT_HEIGHT
  ]

  DOCUMENT_TUBE = [
    (SCREEN_WIDTH - 3 * WALL_WIDTH / 2, 2 * WALL_HEIGHT / 3),
    SLOT_HEIGHT / 2
  ]
  

  FRONT_WALL_RECT = pygame.rect.Rect(WALL_WIDTH                   ,
                                     0                            ,
                                     SCREEN_WIDTH - 2 * WALL_WIDTH,
                                     WALL_HEIGHT                  )

  def draw_setting(self, screen : pygame.Surface):
    screen.fill(color=self.SIDE_WALL_COLOR)
    
    pygame.draw.rect(screen, self.FRONT_WALL_COLOR, self.FRONT_WALL_RECT)
    pygame.draw.rect(screen, self.DESK_COLOR, self.DESK_RECT)

    pygame.draw.rect(screen, self.SLOT_COLOR, self.MEMORY_HOLE_RECT)
    pygame.draw.circle(screen, self.SLOT_COLOR, self.DOCUMENT_TUBE[0], self.DOCUMENT_TUBE[1])
    pygame.draw.circle(screen, self.SLOT_COLOR, self.NEWSPAPER_TUBE[0], self.NEWSPAPER_TUBE[1])


gameSetting = Setting()
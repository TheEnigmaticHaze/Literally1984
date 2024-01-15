from random import randint, choice
from enum import Enum
from objs import Clickable, Draggable
import pygame

seen_documents = set()

TRY_COUNT = 100

DOCUMENT_PREFIX = "times $date "

DOCUMENT_PROMPTS = [
  "bb $messageform malreported $malreport rectify",
  "miniplenty malquoted $good rectify"
  "bb $messageform unpersons ref $rewrite",
  "forecasts 3yp $quarter $misprintcount verify issue",
]

GOOD = [
  "shoelaces",
  "chocolate",
  "razors",
  "boots",
  "shoes",
  "coffee",
  "gin"
]

MESSAGE_FORM = [
  "speech",
  "dayorder",
  "quote"
]

MALREPORT = [
  "africa",
  "eastasia",
  "eurasia",
  "oceania"
]

QUARTER = [
  "1st quarter",
  "2nd quarter",
  "3rd quarter",
  "4th quarter"
]

REWRITE = [
  "rewrite fullwise upsub antefiling",
  "rewrite fullwise",
  "reperson"
]

REPLACEMENTS = {
  "$messageform"  : MESSAGE_FORM,
  "$malreport"    : MALREPORT   ,
  "$good"         : GOOD        ,
  "$rewrite"      : REWRITE     ,
  "$quarter"      : QUARTER     ,
  "$misprintcount": range(1, 5) 
}

month_length = {
  1  : 31,
  2  : 28,
  3  : 31,
  4  : 30,
  5  : 31,
  6  : 30,
  7  : 31,
  8  : 31,
  9  : 30,
  10 : 31,
  11 : 30,
  12 : 31
}

def generate_date():
  year = randint(82, 84)
  month = 0
  if year == 84:
    month = randint(1, 3)
  else:
    month = randint(1, 12)
  day = randint(1, month_length(month))

  return f"{day}.{month}.{year}"
  

def generate_random_document():
  prompt = choice(DOCUMENT_PROMPTS)
  for to_replace in REPLACEMENTS.keys():
    prompt.replace(to_replace, str(choice(REPLACEMENTS[to_replace])))
  return prompt

def produce_document(seen_documents):
  for i in range(TRY_COUNT):
    new_document = generate_random_document()
    if new_document in seen_documents:
      continue
    else:
      return new_document
  return

DOCUMENT_WIDTH  = 100
DOCUMENT_HEIGHT = 144

NEWSPAPER_WIDTH  = 200
NEWSPAPER_HEIGHT = 144

SPEAKWRITE_WIDTH  = 75
SPEAKWRITE_HEIGHT = 50

LINE_SPACING   = 5
LINE_THICKNESS = 2

LINE_COLOR       = pygame.color.Color(50,  50,  50 )
DOCUMENT_COLOR   = pygame.color.Color(255, 255, 255)
SPEAKWRITE_COLOR = pygame.color.Color(255, 255, 255)
NEWSPAPER_COLOR  = pygame.color.Color(200, 200, 200)


class PaperType(Enum):
  DOCUMENT        = pygame.rect.Rect(0                ,
                                     0                ,
                                     DOCUMENT_WIDTH   ,
                                     DOCUMENT_HEIGHT)
  NEWSPAPER       = pygame.rect.Rect(0                ,
                                     0                ,
                                     NEWSPAPER_WIDTH  ,
                                     NEWSPAPER_HEIGHT)
  SPEAKWRITE_SLIP = pygame.rect.Rect(0                ,
                                     0                ,
                                     SPEAKWRITE_WIDTH ,
                                     SPEAKWRITE_HEIGHT)

MIN_PARAGRAPH_LENGTH =     DOCUMENT_HEIGHT // (3 * LINE_SPACING)
MAX_PARAGRAPH_LENGTH = 2 * DOCUMENT_HEIGHT // (3 * LINE_SPACING)

def draw_paper(screen : pygame.Surface, paper_type : PaperType, draw_rect : pygame.rect.Rect, paragraph_end : int, end_line_length : int):
  color = pygame.color.Color(0, 0, 0)
  if paper_type == PaperType.DOCUMENT:        color = DOCUMENT_COLOR
  if paper_type == PaperType.NEWSPAPER:       color = NEWSPAPER_COLOR
  if paper_type == PaperType.SPEAKWRITE_SLIP: color = SPEAKWRITE_COLOR

  pygame.draw.rect(screen, color, draw_rect)

  if paper_type == PaperType.SPEAKWRITE_SLIP:
    for line_number in range(1, SPEAKWRITE_HEIGHT // LINE_SPACING):
      left, top = draw_rect.topleft
      right = draw_rect.right
      start = (left + LINE_SPACING, top + line_number * LINE_SPACING)
      end   = (right - LINE_SPACING, top + line_number * LINE_SPACING)

      pygame.draw.line(screen, LINE_COLOR, start, end, LINE_THICKNESS)
  
  if paper_type == PaperType.DOCUMENT:
    for line_number in range(1, DOCUMENT_HEIGHT // LINE_SPACING):
      left, top  = draw_rect.topleft
      right = draw_rect.right
      start = (left + LINE_SPACING, top + line_number * LINE_SPACING)
      end   = (right - LINE_SPACING, top + line_number * LINE_SPACING)
      if line_number == paragraph_end:
        end = (right - LINE_SPACING - end_line_length, top + line_number * LINE_SPACING)
      
      pygame.draw.line(screen, LINE_COLOR, start, end, LINE_THICKNESS)

  if paper_type == PaperType.NEWSPAPER:
    left, top = draw_rect.topleft
    right = draw_rect.right - LINE_SPACING

    for line_number in range(1, NEWSPAPER_HEIGHT // LINE_SPACING):
      start1 = (left + LINE_SPACING                        , top + line_number * LINE_SPACING)
      end1   = (right - LINE_SPACING - NEWSPAPER_WIDTH // 2, top + line_number * LINE_SPACING)
      if line_number == paragraph_end:
        end1 = (right - LINE_SPACING - end_line_length - NEWSPAPER_WIDTH // 2, top + line_number * LINE_SPACING)
      start2 = (left + LINE_SPACING + NEWSPAPER_WIDTH // 2, top + line_number * LINE_SPACING)
      end2   = (right - LINE_SPACING                      , top + line_number * LINE_SPACING)

      pygame.draw.line(screen, LINE_COLOR, start1, end1, LINE_THICKNESS)
      pygame.draw.line(screen, LINE_COLOR, start2, end2, LINE_THICKNESS)

    img_rect = pygame.rect.Rect(left + NEWSPAPER_WIDTH // 2 + LINE_SPACING // 2,
                                top + paragraph_end * LINE_SPACING,
                                NEWSPAPER_WIDTH // 2 - 1.5 * LINE_SPACING,
                                (paragraph_end // 2 + 0.5) * LINE_SPACING),
    pygame.draw.rect(screen, pygame.color.Color(100, 100, 100), img_rect)
    pygame.draw.rect(screen,
                     pygame.color.Color(0, 0, 0),
                     img_rect,
                     LINE_THICKNESS,
                     LINE_THICKNESS,
                     LINE_THICKNESS,
                     LINE_THICKNESS)

class Paper(Draggable):
  def __init__(self, paper_type : PaperType, initial_position):
    self.prompt = produce_document(seen_documents)
    self.position = [0, 0]
    self.paper_type = paper_type

    self.paragraph_end = randint(MIN_PARAGRAPH_LENGTH, MAX_PARAGRAPH_LENGTH)
    self.end_line_length = randint(5, 2 * DOCUMENT_WIDTH // 3)

    self.click_boundary = paper_type.value
    self.draw_function = draw_paper
  

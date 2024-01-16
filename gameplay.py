from enum import Enum, auto
from setting import gameSetting


class GameState(Enum):
  TITLE_SCREEN    = auto()
  DESK_VIEW       = auto()
  PAPER_VIEW      = auto()
  SPEAKWRITE_VIEW = auto()
  GAME_OVER_VIEW  = auto()
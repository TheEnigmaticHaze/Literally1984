from pygame import Rect, mouse

def nothing(*args):
  pass 

class Clickable:
  def __init__(self, draw_function, click_boundary : Rect):
    self.draw_function = draw_function
    self.click_boundary = click_boundary
  
  def in_boundary(self) -> bool:
    x, y = mouse.get_pos()

    if self.click_boundary.left < x < self.click_boundary.right:
      if self.click_boundary.top < y < self.click_boundary.bottom:
        return True
      
    return False
  
  def if_click(self, on_click, *args, button_number : int) -> bool:
    if not mouse.get_pressed(num_buttons=3)[button_number]:
      return False

    if self.in_boundary():
      on_click(*args)
      return True
    
    return False
  
  def draw_obj(self, screen, *args):
    if args: self.draw_function(screen, *args)
    else: self.draw_function(screen)

class Draggable(Clickable):
  def __init__(self, initial_position, draw_function, click_boundary : Rect, on_click):
    self.position = initial_position
    self.draw_function = draw_function
    self.click_boundary = click_boundary
  
  def drag(self, button_number : int):
    if self.in_boundary() and mouse.get_pressed(num_buttons=3)[button_number]:
      self.position = mouse.get_pos()
      self.click_boundary.center = self.position
  
  def draw_obj(self, *args):
    self.draw_function(*args)
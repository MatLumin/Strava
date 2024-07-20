
from nut import Nut;
import nuts_definitions;


class Food:
	def __init__(self, title:str, nuts:List[Nut]):
		self.title = title;
		self.nuts = nuts;
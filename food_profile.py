
from nut import Nut;
import nuts_definitions;


class FoodProfile:
	def __init__(self, title:str, nuts:List[Nut], serving_mass:float):
		self.title = title;
		self.nuts = nuts; #based on serving mass
		self.serving_mass = serving_mass;


	def calcualte_calorie(self):
		sum_of_calories:float = 0.0;

		for i1 in self.nuts:
			sum_of_calories += i1.return_calorie();

		return sum_of_calories;



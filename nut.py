from typing import *;
from nut_tag import NutTag;

class Nut:
	def __init__(self, energy_per_gram:float, title:str, mass:float, tags:List[NutGroup]):
		self.energy_per_gram = energy_per_gram;
		self.title = title;
		self.mass = mass;
		self.tags = tags;


	@classmethod
	def sub_class_decorator(cls, target_sub_class):

		energy_per_gram:flaot = target_sub_class.energy_per_gram;
		title:str = target_sub_class.title;

		class Output(cls):
			def __init__(self, mass, tags):
				cls.__init__(self, energy_per_gram=energy_per_gram, mass=mass, title=title, tags=tags);


		Output.__name__ = target_sub_class.__name__;
		return Output;


	def return_calorie(self)->float:
		return self.mass * self.energy_per_gram;





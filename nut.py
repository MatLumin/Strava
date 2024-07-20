from typing import *;

class Nut:
	def __init__(self, energy_per_gram:float, title:str, mass:float):
		self.energy_per_gram = energy_per_gram;
		self.title = title;
		self.mass = mass;


	@classmethod
	def sub_class_decorator(cls, target_sub_class):

		energy_per_gram:flaot = target_sub_class.energy_per_gram;
		title:str = target_sub_class.title;

		class Output(cls):
			def __init__(self, mass):
				cls.__init__(self, energy_per_gram=energy_per_gram, mass=mass, title=title);


		Output.__name__ = target_sub_class.__name__;
		return Output;





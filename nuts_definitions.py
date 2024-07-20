from nut import *;
from typing import *;

@Nut.sub_class_decorator
class GeneralProtein:
	title:str="general protein";
	energy_per_gram:float=4.5;

@Nut.sub_class_decorator
class GeneralFat:
	title:str="general fat";
	energy_per_gram:float=9;

@Nut.sub_class_decorator
class GeneralCarb:
	title:str="general carb";
	energy_per_gram:float=4.5;
#Батьківський клас
class Product:
    def __init__(self , Quantity , Name):
        self.Quantity = Quantity
        self.Name = Name
#Похідний клас продукти
class Food(Product):
    #Метод на доставку до вичерпання терміну придатності продукту
    def Time_to_live(self , living_time , traveling_time):
        self.living_time = living_time
        self.Transporting_result = self.living_time < traveling_time
        return self.Transporting_result
#Похідний клас матеріали
class Materials(Product):
    #Метод обрахунок загальної ваги
    def Space(self , Weight_of_one_point):
        self.Weight_of_one_point = Space_of_one_point
        All_space = self.Space_of_one_point * Quantity
        return All_space
#Похідний клас меблі
class Furniture(Product):
    #Метод на пошук об'єму та ваги вантажу
    def Weight_and_Space(self , weight_of_one_point , space_of_one_point ):
         self.weight_of_one_point = weight_of_one_point
         self.space_of_one_point = space_of_one_point
         All_space = self.space_of_one_point * Quantity
         All_weight = self.weight_of_one_point * Quantity
         

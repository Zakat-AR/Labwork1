#Створення батьківського класу робота-перевізника
import random
class Robot:
    def __init__(self , Model , Speed , distance_energy_consume , Drone_charge_price):
        self.Drone_charge_price = Drone_charge_price
        self.Model = Model
        self.Speed = Speed
        self.__Price = 1000
        self.__Battery = 100
        self.distance_energy_consume = distance_energy_consume

    def show_info(self):
        print("Модель:",self.Model)
        print("Швидкість: ",self.Speed)
        print("Ціна: ",self.__Price)
        print("Ціна заряджання: ",self.Drone_charge_price)
        print("Ємність батареї: ",self.__Battery)
        print("Споживання заряду на годину",self.distance_energy_consume)
        
    #Метод обрахунку заробітку , витрат на зараджання акумулятора , кількості переходів з точки А в точку Б
    def Calculating_time(self  , Distance_to_client , Weather_impact):
        self.Distance_to_client = Distance_to_client
        self.Speed_all = self.Speed + Weather_impact
        self.Working_time = self.Distance_to_client // self.Speed_all
        return self.Working_time

    def Calculating_number_of_deliveries(self , Weight , One_delivery_weight):
        self.Weight = Weight
        self.Deliveries_for_Deliverying_weight = Weight // One_delivery_weight
        self.Charges_percents = self.Distance_to_client * self.distance_energy_consume * 5
        self.Charges_times = self.Charges_percents // self.__Battery
        self.Charges_times = self.Charges_times *  self.Deliveries_for_Deliverying_weight 
        self.Charges_times = int(self.Charges_times)
        return self.Deliveries_for_Deliverying_weight 

    def Money_for_charging(self ,  Charges):
            
        
        self.Money_charging = Charges  * 10 
        return int(self.Money_charging)

    #Мето на поламку робота
    def Get_broken(self , Broken_robots): 
        Chance_of_getting_broken_random = random.randint(1,10)
        Chance = Chance_of_getting_broken_random % 4 == 0
        if Chance :
            Broken_robots = Broken_robots + 1

        return Broken_robots



    
    #Метод на рух , показує результати обрахунків
    def move(self):
        print("Відбувається рух робота")
        print(f"Робот:{ self.Model} , отримав вагу для перевезень:{Weight} кг.")
        print(f"Буде проведено перевезень:{self.Deliveries_for_Deliverying_weight } , тривалістю: {self.Working_time} год.")
        print(f"Приблизний заробіток становить:{self.Money_of_deliverying}")
        print(f"Буде повних заряджань:{self.Battery_recharging} , що коштує {self.Money_recharging}")
        
pass


#Похідний клас , звичайний дрон
class Fly_Drone(Robot):
    def move(self ,Money_of_deliverying , Charges, all_weight , all_deliveries , all_time ):
        print("Відбувається політ робота")
        print(f"Робот:{ self.Model} , отримав вагу для транспортування повітряними шляхами:{all_weight} кг.")
        print(f"Буде проведено перельотів:{all_deliveries } , тривалістю: {all_time} год.")
        print(f"Приблизний заробіток становить:{Money_of_deliverying}")
        print(f"Буде повних заряджань:{Charges} , що коштує {self.Money_charging}")
pass


#Похідний клас , наземний робот
class Ground_Drone(Robot):
    
    
    #Метод руху , показ результавтів обрахунків    
    def move(self ,Money_of_deliverying , Charges_times , all_weight , all_deliveries , all_time ):
        print("Відбувається поїздка робота")
        print(f"Робот:{ self.Model} , отримав вагу для транспортування наземними шляхами:{all_weight} кг.")
        print(f"Буде проведено поїздок:{all_deliveries } , тривалістю: {all_time} год.")
        print(f"Приблизний заробіток становить:{Money_of_deliverying}")
        print(f"Буде повних заряджань:{Charges_times} , що коштує {self.Money_charging}")
pass


#похідний клас водного робота-перевізника
class Water_Drone(Robot):

    def Calculating_deliveries_space(self, materials_space , normal_space):
        self.normal_space = normal_space
        self.materials_space = materials_space
        self.Deliveries_space = self.materials_space // self.normal_space
        return self.Deliveries_space 



    def Calculating_number_of_deliveries(self , Weight , One_delivery_weight):
        self.Weight = Weight
        self.Deliveries_for_Deliverying_weight = Weight // One_delivery_weight
        self.Charges_percents = self.Distance_to_client * self.distance_energy_consume * 0.1
        self.Charges_times = self.Charges_percents // 100
        return self.Deliveries_for_Deliverying_weight



    
    def move(self, Charges_times , Money_of_deliverying ,all_weight , Deliveries , all_space  , all_time  ,One_delivery_space):
        print("Відбувається подолання водних перешкод роботом")
        print(f"Робот:{ self.Model} , отримав вагу для транспортування морськими шляхами:{all_weight} кг.")
        print(f"Буде проведено водних подорожей:{Deliveries} , тривалістю: {all_time} год.")
        print(f"Приблизний заробіток становить:{Money_of_deliverying}")
        print(f"Буде повних заряджань:{Charges_times*Deliveries} , що коштує {self.Money_charging*Deliveries}")
        print(f"Об'єм вантажу одного перевезення становить:  {One_delivery_space}")
        print(f"Весь об'єм перевезень стаовить:{all_space}")
pass


















        

        

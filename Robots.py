#Створення батьківського класу робота-перевізника
class Robot:
    def __init__(self , Model , Speed , hour_energy_consume , price_of_recharging):
        self.Model = Model
        self.Speed = Speed
        self.__Price = 1000
        self.price_of_recharging = price_of_recharging
        self.__Battery = 100
        self.hour_energy_consume = hour_energy_consume

    def show_info(self):
        print("Модель:",self.Model)
        print("Швидкість: ",self.Speed)
        print("Ціна: ",self.__Price)
        print("Ціна заряджання: ",self.price_of_recharging)
        print("Ємність батареї: ",self.__Battery)
        print("Споживання заряду на годину",self.hour_energy_consume)
        
    #Метод обрахунку заробітку , витрат на зараджання акумулятора , кількості переходів з точки А в точку Б
    def Calculating(self , Weight , Distance_to_client , One_delivery_weight , Weather_impact):
        self.Speed_all = self.Speed + Weather_impact
        self.Working_time = Distance_to_client // self.Speed_all
        

        #Цикл на рахунок кількості повних розрядок акумулятора
        self.Battery_recharging = 0
        for hour in range(self.Working_time):
            self.__Battery - self.hour_energy_consume
            if self.__Battery == 0:
                self.__Battery = 100
                self.Battery_recharging +=1
         #  Підрахунок витрат на зараджання     
        self.Money_recharging = self.Battery_recharging * self.price_of_recharging
        return self.Working_time

    #Мето на поламку робота
    def Get_broken(self):
        self.Robot_broken = 0
        Chance_of_gatting_broken_random = random.randint(1,100)
        if Chance_of_gatting_broken_random % 10 ==0:
            self.Robot_broken +=1
        return  self.Robot_broken   
    #Мето на рух , показує результати обрахунків
    def move(self):
        print("Відбувається рух робота")
        print(f"Робот:{ self.Model} , отримав вагу для перевезень:{Weight} кг.")
        print(f" Буде проведено перевезень:{self.Deliveries_for_Deliverying} , тривалістю: {self.Working_time} год.")
        print(f"Приблизний заробіток становить:{self.Money_of_deliverying}")
        print(f"Буде повних заряджань:{self.Battery_recharging} , що коштує {self.Money_recharging}")
        
pass


#Похідний клас , звичайний дрон
class Fly_Drone(Robot):
    def move(self):
        print("Відбувається політ робота")
        print(f"Робот:{ self.Model} , отримав вагу для транспортування повітряними шляхами:{Weight} кг.")
        print(f" Буде проведено перельотів:{self.Deliveries_for_Deliverying} , тривалістю: {self.Working_time} год.")
        print(f"Приблизний заробіток становить:{self.Money_of_deliverying}")
        print(f"Буде повних заряджань:{self.Battery_recharging} , що коштує {self.Money_recharging}")
pass


#Похідний клас , наземний робот
class Ground_Drone(Robot):
     #Перевизначив метод перевезень , тут обраховується кількість ходок ві співвідношення ваги вантажу до максиальної ваги одної ходки
     # А також обраховується співвідношення об'єму одної ходки до загального. Обирається менше з двох співвідношень
    def Calculating(self , Weight , Distance_to_client , One_delivery_weight , Weather_impact, All_space , Normal_space_of_one_delivery):
        self.Normal_space_of_one_delivery = Normal_space_of_one_delivery
        self.Speed_all = self.Speed + Weather_impact
        self.Deliveries_for_Deliverying_weight = Weight // One_delivery_weight
        self.Deliveries_for_Deliverying_space = All_space // Normal_space_of_one_delivery
        
        if self.Deliveries_for_Deliverying_space < self.Deliveries_for_Deliverying_weight :
            self.Deliveries_for_Deliverying = self.Deliveries_for_Deliverying_space
        else:
            self.Deliveries_for_Deliverying = self.Deliveries_for_Deliverying_weight
            
            
        self.Money_of_deliverying = Weight*20 + Distance_to_client*10
        self.Working_time = Distance_to_client // self.Speed_all

    #Мето руху , покащ результавтів обрахунків    
    def move(self):
        print("Відбувається процес подолання відстаней на дорожному плато роботом")
        print(f"Робот:{ self.Model} , отримав вагу для транспортування наземними шляхами:{Weight} кг.")
        print(f" Буде проведено поїздок:{self.Deliveries_for_Deliverying} , тривалістю: {self.Working_time} год.")
        print(f"Приблизний заробіток становить:{self.Money_of_deliverying}")
        print(f"Буде повних заряджань:{self.Battery_recharging} , що коштує {self.Money_recharging}")
pass


#похідний клас водного робота-перевізника
class Water_Drone(Robot):
    def move(self):
        print("Відбувається подолання водних перешкод роботом")
        print(f"Робот:{ self.Model} , отримав вагу для транспортування морськими шляхами:{Weight} кг.")
        print(f" Буде проведено водних подорожей:{self.Deliveries_for_Deliverying} , тривалістю: {self.Working_time} год.")
        print(f"Приблизний заробіток становить:{self.Money_of_deliverying}")
        print(f"Буде повних заряджань:{self.Battery_recharging} , що коштує {self.Money_recharging}")
pass


















        

        

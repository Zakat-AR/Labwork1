from Logs import logger_robots_ground, logger_robots_water, logger_robots_air
#Створення батьківського класу робота-перевізника
import Logs
import random
class Robot:
    def __init__(self , model_1 , speed_1 , distance_energy_consume , drone_charge_price_1 ):
        self.drone_charge_price_1 = drone_charge_price_1
        self.model_1 = model_1
        self.speed_1 = speed_1
        self._Robot__price_1 = 1000
        self._Robot__battery_1 = 100
        self.distance_energy_consume = distance_energy_consume

    def info(self):
        logger_robots_ground.info(f"Модель: {self.model_1}")
        logger_robots_ground.info(f"Швидкість:  {self.speed_1}")
        logger_robots_ground.info(f"Ціна:  {self._Robot__price_1}")
        logger_robots_ground.info(f"Ціна заряджання:  {self.drone_charge_price_1}")
        logger_robots_ground.info(f"Ємність батареї:  {self._Robot__battery_1}")
        logger_robots_ground.info(f"Споживання заряду на годину {self.distance_energy_consume}")
        
    #Метод обрахунку заробітку , витрат на зараджання акумулятора , кількості переходів з точки А в точку Б
    def Calculating_time(self  , distance_to_client_1 , weather_impact_1):
        self.distance_to_client_1 = distance_to_client_1
        self.speed_all_1 = self.speed_1 + weather_impact_1
        self.working_time_1 = self.distance_to_client_1 // self.speed_all_1
        return self.working_time_1

    def Calculating_number_of_deliveries(self , weight_1 , one_delivery_weight_1):
        self.weight_1 = weight_1
        self.deliveries_for_deliverying_weight_1 = weight_1 // one_delivery_weight_1
        self.charges_percents_1 = self.distance_to_client_1 * self.distance_energy_consume * 5
        self.charges_times_1 = self.charges_percents_1 // self._Robot__battery_1
        self.charges_times_1 = self.charges_times_1 *  self.deliveries_for_deliverying_weight_1 
        self.charges_times_1 = int(self.charges_times_1)
        return self.deliveries_for_deliverying_weight_1 

    def Money_for_charging(self ,  charges_1):
            
        
        self.money_charging_1 = charges_1  * 10 
        return int(self.money_charging_1)

    #Мето на поламку робота
    def Get_broken(self , broken_robots_1): 
        chance_of_getting_broken_random_1 = random.randint(1,10)
        chance_1 = chance_of_getting_broken_random_1 % 4 == 0
        if chance_1 :
            broken_robots_1 = broken_robots_1 + 1

        return broken_robots_1



    
    #Метод на рух , показує результати обрахунків
    def move(self):
        logger_robots_ground.info("Відбувається рух робота")
        logger_robots_ground.info(f"Робот:{ self.model_1} , отримав вагу для перевезень:{weight_1} кг.")
        logger_robots_ground.info(f"Буде проведено перевезень:{self.deliveries_for_deliverying_weight_1 } , тривалістю: {self.working_time_1} год.")
        logger_robots_ground.info(f"Приблизний заробіток становить:{self.money_of_deliverying_1}")
        logger_robots_ground.info(f"Буде повних заряджань:{self.battery_recharging_1} , що коштує {self.money_recharging_1}")
        
pass


#Похідний клас , звичайний дрон
class Fly_Drone(Robot):


    def info(self):
        logger_robots_air.info(f"Модель: {self.model_1}")
        logger_robots_air.info(f"Швидкість:  {self.speed_1}")
        logger_robots_air.info(f"Ціна:  {self._Robot__price_1}")
        logger_robots_air.info(f"Ціна заряджання:  {self.drone_charge_price_1}")
        logger_robots_air.info(f"Ємність батареї:  {self._Robot__battery_1}")
        logger_robots_air.info(f"Споживання заряду на годину {self.distance_energy_consume}")

        
    def move(self ,money_of_deliverying_1 , charges_1, all_weight , all_deliveries , all_time ):
        logger_robots_air.info("Відбувається політ робота")
        logger_robots_air.info(f"Робот:{ self.model_1} , отримав вагу для транспортування повітряними шляхами:{all_weight} кг.")
        logger_robots_air.info(f"Буде проведено перельотів:{all_deliveries } , тривалістю: {all_time} год.")
        logger_robots_air.info(f"Приблизний заробіток становить:{money_of_deliverying_1}")
        logger_robots_air.info(f"Буде повних заряджань:{charges_1} , що коштує {self.money_charging_1}")
pass


#Похідний клас , наземний робот
class Ground_Drone(Robot):

    def info(self):
        logger_robots_ground.info(f"Модель: {self.model_1}")
        logger_robots_ground.info(f"Швидкість:  {self.speed_1}")
        logger_robots_ground.info(f"Ціна:  {self._Robot__price_1}")
        logger_robots_ground.info(f"Ціна заряджання:  {self.drone_charge_price_1}")
        logger_robots_ground.info(f"Ємність батареї:  {self._Robot__battery_1}")
        logger_robots_ground.info(f"Споживання заряду на годину {self.distance_energy_consume}")
    
    
    #Метод руху , показ результавтів обрахунків    
    def move(self ,money_of_deliverying_1 , charges_times_1 , all_weight , all_deliveries , all_time ):
        logger_robots_ground.info("Відбувається поїздка робота")
        logger_robots_ground.info(f"Робот:{ self.model_1} , отримав вагу для транспортування наземними шляхами:{all_weight} кг.")
        logger_robots_ground.info(f"Буде проведено поїздок:{all_deliveries } , тривалістю: {all_time} год.")
        logger_robots_ground.info(f"Приблизний заробіток становить:{money_of_deliverying_1}")
        logger_robots_ground.info(f"Буде повних заряджань:{charges_times_1} , що коштує {self.money_charging_1}")
pass


#похідний клас водного робота-перевізника
class Water_Drone(Robot):


    def info(self):
        logger_robots_water.info(f"Модель: {self.model_1}")
        logger_robots_water.info(f"Швидкість:  {self.speed_1}")
        logger_robots_water.info(f"Ціна:  {self._Robot__price_1}")
        logger_robots_water.info(f"Ціна заряджання:  {self.drone_charge_price_1}")
        logger_robots_water.info(f"Ємність батареї:  {self._Robot__battery_1}")
        logger_robots_water.info(f"Споживання заряду на годину {self.distance_energy_consume}")

        

    def Calculating_deliveries_space(self, materials_space , normal_space):
        self.normal_space = normal_space
        self.materials_space = materials_space
        self.deliveries_space_1 = self.materials_space // self.normal_space
        return self.deliveries_space_1 



    def Calculating_number_of_deliveries(self , weight_1 , one_delivery_weight_1):
        self.weight_1 = weight_1
        self.deliveries_for_deliverying_weight_1 = weight_1 // one_delivery_weight_1
        self.charges_percents_1 = self.distance_to_client_1 * self.distance_energy_consume * 0.1
        self.charges_times_1 = self.charges_percents_1 // 100
        return self.deliveries_for_deliverying_weight_1



    
    def move(self, charges_times_1 , money_of_deliverying_1 ,all_weight , deliveries_1 , all_space  , all_time  ,one_delivery_space_1):
        logger_robots_water.info("Відбувається подолання водних перешкод роботом")
        logger_robots_water.info(f"Робот:{ self.model_1} , отримав вагу для транспортування морськими шляхами:{all_weight} кг.")
        logger_robots_water.info(f"Буде проведено водних подорожей:{deliveries_1} , тривалістю: {all_time} год.")
        logger_robots_water.info(f"Приблизний заробіток становить:{money_of_deliverying_1}")
        logger_robots_water.info(f"Буде повних заряджань:{charges_times_1*deliveries_1} , що коштує {self.money_charging_1*deliveries_1}")
        logger_robots_water.info(f"Об'єм вантажу одного перевезення становить:  {one_delivery_space_1}")
        logger_robots_water.info(f"Весь об'єм перевезень стаовить:{all_space}")
pass


















        

        

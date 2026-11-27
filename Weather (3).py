from Logs import logger_weather
#Клас погода , впливає на швидкість пересування роботів
import random
import Logs
class Weather:
    def __init__(self , days_of_existing):
        self.days_of_existing = days_of_existing
     #Метод на рандомну погоду , яка з часом змінюється.
    def Random_Weather(self ):
        
        weather_list_1 = ["Файний вітер","Безвітряна погода","Зустрічний вітер","Штиль","Ураган","Прилив","Дощ","Сонячна погода","Ожеледиця"]
        Weather = random.choice(weather_list_1)
        if Weather == "Файний вітер" :
            water_transport_speed_change_1 = 5
            ground_transport_speed_change_1 = 0
            air_transport_speed_change_1 = 10
            
            logger_weather.info(Weather)
            logger_weather.info(f"Вплив погоди на швидкість водного танспорту:  {water_transport_speed_change_1}")
            logger_weather.info(f"Вплив погоди на швидкість наземного  танспорту:  {ground_transport_speed_change_1}")
            logger_weather.info(f"Вплив погоди на швидкість повітряного танспорту:  {air_transport_speed_change_1}")
            
        if Weather == "Безвітряна погода" :
            water_transport_speed_change_1 = 0
            ground_transport_speed_change_1 = 0
            air_transport_speed_change_1 = 0
            
            logger_weather.info(Weather)
            logger_weather.info(f"Вплив погоди на швидкість водного танспорту:  {water_transport_speed_change_1}")
            logger_weather.info(f"Вплив погоди на швидкість наземного  танспорту:  {ground_transport_speed_change_1}")
            logger_weather.info(f"Вплив погоди на швидкість повітряного танспорту:  {air_transport_speed_change_1}")
            
        elif Weather == "Зустрічний вітер" :
            water_transport_speed_change_1 = -5
            ground_transport_speed_change_1 = 0
            air_transport_speed_change_1 = -10
            
            logger_weather.info(Weather)
            logger_weather.info(f"Вплив погоди на швидкість водного танспорту:  {water_transport_speed_change_1}")
            logger_weather.info(f"Вплив погоди на швидкість наземного  танспорту:  {ground_transport_speed_change_1}")
            logger_weather.info(f"Вплив погоди на швидкість повітряного танспорту:  {air_transport_speed_change_1}")
            
        elif Weather == "Штиль" :
            water_transport_speed_change_1 = 0
            ground_transport_speed_change_1 = 0
            air_transport_speed_change_1 = 0
            
            logger_weather.info(Weather)
            logger_weather.info(f"Вплив погоди на швидкість водного танспорту:  {water_transport_speed_change_1}")
            logger_weather.info(f"Вплив погоди на швидкість наземного  танспорту:  {ground_transport_speed_change_1}")
            logger_weather.info(f"Вплив погоди на швидкість повітряного танспорту:  {air_transport_speed_change_1}")
            
        elif Weather == "Ураган" :
            water_transport_speed_change_1 = -10
            ground_transport_speed_change_1 = -10
            air_transport_speed_change_1 = -10
            
            logger_weather.info(Weather)
            logger_weather.info(f"Вплив погоди на швидкість водного танспорту:  {water_transport_speed_change_1}")
            logger_weather.info(f"Вплив погоди на швидкість наземного  танспорту:  {ground_transport_speed_change_1}")
            logger_weather.info(f"Вплив погоди на швидкість повітряного танспорту:  {air_transport_speed_change_1}")
            
        elif Weather == "Прилив" :
            water_transport_speed_change_1 = 10
            ground_transport_speed_change_1 = 0
            air_transport_speed_change_1 = 0
            
            logger_weather.info(Weather)
            logger_weather.info(f"Вплив погоди на швидкість водного танспорту:  {water_transport_speed_change_1}")
            logger_weather.info(f"Вплив погоди на швидкість наземного  танспорту:  {ground_transport_speed_change_1}")
            logger_weather.info(f"Вплив погоди на швидкість повітряного танспорту:  {air_transport_speed_change_1}")
            
        elif Weather == "Дощ" :
            water_transport_speed_change_1 = 0
            ground_transport_speed_change_1 = 0
            air_transport_speed_change_1 = -5
            
            logger_weather.info(Weather)
            logger_weather.info(f"Вплив погоди на швидкість водного танспорту:  {water_transport_speed_change_1}")
            logger_weather.info(f"Вплив погоди на швидкість наземного  танспорту:  {ground_transport_speed_change_1}")
            logger_weather.info(f"Вплив погоди на швидкість повітряного танспорту:  {air_transport_speed_change_1}")
            
        elif Weather == "Сонячна погода" :
            water_transport_speed_change_1 = 0
            ground_transport_speed_change_1 = 5
            air_transport_speed_change_1 = 0
            
            logger_weather.info(Weather)
            logger_weather.info(f"Вплив погоди на швидкість водного танспорту:  {water_transport_speed_change_1}")
            logger_weather.info(f"Вплив погоди на швидкість наземного  танспорту:  {ground_transport_speed_change_1}")
            logger_weather.info(f"Вплив погоди на швидкість повітряного танспорту:  {air_transport_speed_change_1}")
            
        elif Weather == "Ожеледиця":
            water_transport_speed_change_1 = 0
            ground_transport_speed_change_1 = 10
            air_transport_speed_change_1 = 0
            
            logger_weather.info(Weather)
            logger_weather.info(f"Вплив погоди на швидкість водного танспорту:  {water_transport_speed_change_1}")
            logger_weather.info(f"Вплив погоди на швидкість наземного  танспорту:  {ground_transport_speed_change_1}")
            logger_weather.info(f"Вплив погоди на швидкість повітряного танспорту:  {air_transport_speed_change_1}")
            
        
        

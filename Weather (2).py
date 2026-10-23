#Клас погода , впливає на швидкість пересування роботів
import random
class Weather:
    def __init__(self , days_of_existing):
        self.days_of_existing = days_of_existing
     #Метод на рандомну погоду , яка з часом змінюється.
    def Random_Weather(self ):
        
        Weather_list = ["Файний вітер","Безвітряна погода","Зустрічний вітер","Штиль","Ураган","Прилив","Дощ","Сонячна погода","Ожеледиця"]
        Weather = random.choice(Weather_list)
        if Weather == "Файний вітер" :
            Water_transport_speed_change = 5
            Ground_transport_speed_change = 0
            Air_transport_speed_change = 10
            
            print(Weather)
            print("Вплив погоди на швидкість водного танспорту: ", Water_transport_speed_change)
            print("Вплив погоди на швидкість наземного  танспорту: ", Ground_transport_speed_change)
            print("Вплив погоди на швидкість повітряного танспорту: ", Air_transport_speed_change)
            
        if Weather == "Безвітряна погода" :
            Water_transport_speed_change = 0
            Ground_transport_speed_change = 0
            Air_transport_speed_change = 0
            
            print(Weather)
            print("Вплив погоди на швидкість водного танспорту: ", Water_transport_speed_change)
            print("Вплив погоди на швидкість наземного  танспорту: ", Ground_transport_speed_change)
            print("Вплив погоди на швидкість повітряного танспорту: ", Air_transport_speed_change)
            
        elif Weather == "Зустрічний вітер" :
            Water_transport_speed_change = -5
            Ground_transport_speed_change = 0
            Air_transport_speed_change = -10
            
            print(Weather)
            print("Вплив погоди на швидкість водного танспорту: ", Water_transport_speed_change)
            print("Вплив погоди на швидкість наземного  танспорту: ", Ground_transport_speed_change)
            print("Вплив погоди на швидкість повітряного танспорту: ", Air_transport_speed_change)
            
        elif Weather == "Штиль" :
            Water_transport_speed_change = 0
            Ground_transport_speed_change = 0
            Air_transport_speed_change = 0
            
            print(Weather)
            print("Вплив погоди на швидкість водного танспорту: ", Water_transport_speed_change)
            print("Вплив погоди на швидкість наземного  танспорту: ", Ground_transport_speed_change)
            print("Вплив погоди на швидкість повітряного танспорту: ", Air_transport_speed_change)
            
        elif Weather == "Ураган" :
            Water_transport_speed_change = -10
            Ground_transport_speed_change = -10
            Air_transport_speed_change = -10
            
            print(Weather)
            print("Вплив погоди на швидкість водного танспорту: ", Water_transport_speed_change)
            print("Вплив погоди на швидкість наземного  танспорту: ", Ground_transport_speed_change)
            print("Вплив погоди на швидкість повітряного танспорту: ", Air_transport_speed_change)
            
        elif Weather == "Прилив" :
            Water_transport_speed_change = 10
            Ground_transport_speed_change = 0
            Air_transport_speed_change = 0
            
            print(Weather)
            print("Вплив погоди на швидкість водного танспорту: ", Water_transport_speed_change)
            print("Вплив погоди на швидкість наземного  танспорту: ", Ground_transport_speed_change)
            print("Вплив погоди на швидкість повітряного танспорту: ", Air_transport_speed_change)
            
        elif Weather == "Дощ" :
            Water_transport_speed_change = 0
            Ground_transport_speed_change = 0
            Air_transport_speed_change = -5
            
            print(Weather)
            print("Вплив погоди на швидкість водного танспорту: ", Water_transport_speed_change)
            print("Вплив погоди на швидкість наземного  танспорту: ", Ground_transport_speed_change)
            print("Вплив погоди на швидкість повітряного танспорту: ", Air_transport_speed_change)
            
        elif Weather == "Сонячна погода" :
            Water_transport_speed_change = 0
            Ground_transport_speed_change = 5
            Air_transport_speed_change = 0
            
            print(Weather)
            print("Вплив погоди на швидкість водного танспорту: ", Water_transport_speed_change)
            print("Вплив погоди на швидкість наземного  танспорту: ", Ground_transport_speed_change)
            print("Вплив погоди на швидкість повітряного танспорту: ", Air_transport_speed_change)
            
        elif Weather == "Ожеледиця":
            Water_transport_speed_change = 0
            Ground_transport_speed_change = 10
            Air_transport_speed_change = 0
            
            print(Weather)
            print("Вплив погоди на швидкість водного танспорту: ", Water_transport_speed_change)
            print("Вплив погоди на швидкість наземного  танспорту: ", Ground_transport_speed_change)
            print("Вплив погоди на швидкість повітряного танспорту: ", Air_transport_speed_change)
            
        
        

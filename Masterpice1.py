#Імпорт рандому та класів
import random
from Boss import Boss
from Boss import Workers_list1
from Worker import Worker
from Client import Client
from Storage import Storage
from Robots import Robot
from Robots import Fly_Drone
from Robots import Ground_Drone
from Robots import Water_Drone
from Weather import Weather
from Client import Client_food
from Client import Client_materials
from Client import Client_furniture
      
#Рандомне налаштування Боса  
Number_of_day_simulation = int(input("Введіть кількість днів симуляції: " ))
Boss_Name_list = ["Макс" ,"Степан","Олександр","Федір" , "Трай" , "Флок" , "Джон" , "Майкан" ,"Дроул"]
Boss_Hobby_list = ["Шахи","Кулінарія","Програмування"]
Boss_Name = random.choice(Boss_Name_list)
Boss_Work_Time = random.randint(1 , 10)
Boss_Hobby = random.choice(Boss_Hobby_list)
Boos1 = Boss(Boss_Name, Boss_Work_Time ,Boss_Hobby)
Boos1.show_info()

#Рандомне налаштування перших робітників
Workers_list = []
Workers_number = random.randint(1,5)
for worker_number in range(Workers_number):
  Worker_name_list = ["Олексій","Антон","Федір","Микита","Максим","Олександр","Дмитро","Григорій" , "Афанасій" , "Вольтман"]
  Salary_list = [1500 , 2000 , 2500 , 3000  ]
  Worker_salary = int(random.choice(Salary_list))
  Worker.Name = random.choice(Worker_name_list)
  worker = Worker(Worker.Name ,Worker_salary )
  print("Робітник: ",worker.Name,"приступає до роботи")
  Workers_list.append(worker)

#Отримуємо рандомну кількість дронів кожного виду
Random_Drone_number = random.randint(1,12)
Random_Ground_Drone_number = random.randint(1,12)
Random_Water_Drone_number = random.randint(1,12)


# Налаштування Drones
Drones = []
for Drone in range(Random_Drone_number):
  Models_list = ["AR-101","AR-102","AR-103","AR-104","AR-105","AR-106",
                 "AR-107","AR-108","AR-109",
                 "AR-110","AR-111","AR-112",
                 "AR-113","AR-114","AR-115",
                 "AR-116","AR-117","AR-118",
                 "AR-119","AR-120","AR-121",
                 "AR-122","AR-123","AR-124",
                 "AR-125","AR-126","AR-127"]
  Drone_charge_price = 75
  Drone_Name = random.choice(Models_list)
  Drone_Speed = 50
  Drone_hour_energy_consume = 5
  Flying_drone = Fly_Drone(Drone_Name , Drone_Speed  , Drone_hour_energy_consume , Drone_charge_price)
  Drones.append(Flying_drone)
  
# Налаштування Ground_Drones
Ground_Drones = []
for Drone in range(Random_Ground_Drone_number):
  Models_list = ["ARB-101","ARB-102","ARB-103","ARB-104","ARB-105","ARB-106",
                 "ARB-107","ARB-108","ARB-109",
                 "ARB-110","ARB-111","ARB-112",
                 "ARB-113","ARB-114","ARB-115",
                 "ARB-116","ARB-117","ARB-118",
                 "ARB-119","ARB-120","ARB-121",
                 "ARB-122","ARB-123","ARB-124",
                 "ARB-125","ARB-126","ARB-127"]
  Ground_drone_charge_price = 50
  Ground_drone_Name = random.choice(Models_list)
  Ground_drone_Speed = 30
  Ground_drone_hour_energy_consume = 7.5
  Ground_drone = Ground_Drone(Ground_drone_Name , Ground_drone_Speed  , Ground_drone_hour_energy_consume ,  Ground_drone_charge_price )
  Ground_Drones.append(Ground_drone)


# Налаштування Sea_Drones
Sea_Drones = []
for Drone in range(Random_Water_Drone_number):
  Models_list = ["ARC-101","ARC-102","ARC-103","ARC-104","ARC-105","ARC-106",
                 "ARC-107","ARC-108","ARC-109",
                 "ARC-110","ARC-111","ARC-112",
                 "ARC-113","ARC-114","ARC-115",
                 "ARC-116","ARC-117","ARC-118",
                 "ARC-119","ARC-120","ARC-121",
                 "ARC-122","ARC-123","ARC-124",
                 "ARC-125","ARC-126","ARC-127"]
  Sea_Drone_Name = random.choice(Models_list)
  Sea_drone_charge_price = 30
  Sea_Drone_Speed = 45
  Sea_Drone_hour_energy_consume = 10
  Sea_drone = Water_Drone(Sea_Drone_Name , Sea_Drone_Speed  , Sea_Drone_hour_energy_consume ,  Sea_drone_charge_price )
  Sea_Drones.append(Sea_drone)

 #Перевірка 
for Number in range(len(Drones)):
  Drone = Drones[Number]
  Drone.show_info()

for Number in range(len(Sea_Drones)):
  Drone = Sea_Drones[Number]
  Drone.show_info()

for Number in range(len(Ground_Drones)):
  Drone = Ground_Drones[Number]
 

#Останні приготування перед циклом 
All_money = 0
Clients = []
Boos1.Experience()
storage_food = Storage()
storage_materials = Storage()
storage_furniture = Storage()
for Day in range(Number_of_day_simulation):

  #Заставка нового дня
  print("="*35)
  print(f"День роботи: {Day +1}")
  print("="*35)

  #Базові налаштування для дронів
  One_delivery_weight_air = 20
  One_delivery_weight_water = 30
  One_delivery_space = 40
  One_delivery_weight_ground = 25
  Day_money = 0
  Water_transport_speed_change = 0
  Ground_transport_speed_change = 0
  Air_transport_speed_change = 0


  #Налаштування погоди
  Days_for_weather = random.randint(3,6)
  weather = Weather(Days_for_weather)
  weather.Random_Weather()

  #Переговори боса з іншими компаніями
  Supply_change = 0
  Boos1.Deal(Day)
  

  #Завезення товару до складу
  storage_food.new_products_Food(Supply_change)
  storage_materials.new_products_Materials(Supply_change)
  storage_furniture.new_products_Furniture(Supply_change)
  
  Boos1.random_mood()
  time = 4


  #Кількість клієнтів
  Number_of_clients_food = random.randint(1,25)
  Number_of_clients_furniture = random.randint(1,25)
  Number_of_clients_materials = random.randint(1,25)

  
  #Цикл на рандомне надання характеристик клієнтам-покупцям їжі
  clients_food = []
  for client in range(Number_of_clients_food ):
    
    weight_food = random.randint(1,150)
    distance_for_food_to_client = random.randint(1,200)
    client = Client_food(weight_food , distance_for_food_to_client )
    clients_food.append(client)


  # Цикл на рандомне надання характеристик клієнтам-покупцям матеріалів
  clients_materials = []
  for client in range(Number_of_clients_materials):
    
    weight_materials = random.randint(1,150)
    distance_for_materials_to_client = random.randint(1,200)
    space_materials = random.randint(1 , 75)
    
    client = Client_materials(weight_materials , distance_for_materials_to_client , space_materials)
    clients_materials.append(client)

  #Цикл на рандомне надання характеристик клієнтам-покупцям меблів
  clients_furniture = []
  for client_furniture in range(Number_of_clients_furniture):

    weight_furniture = random.randint(1,125)
    distance_for_furniture_to_client = random.randint(1,175)

    client_furniture = Client_furniture(weight_furniture , distance_for_furniture_to_client)
    clients_furniture.append(client_furniture)

  #Отримуємо співвідношення дронів до клієнтів-покупців їжі
  Clients_for_drones_food = Number_of_clients_food // Random_Drone_number
  print("Їжа: ",Clients_for_drones_food)

  #Отримуємо співвідношення водних дронів до клієнтів-покупців матеріалів
  Clients_for_drones_materials = Number_of_clients_materials // Random_Water_Drone_number
  print("Матеріали: ",Clients_for_drones_materials)

  #Отримуємо співвідношення наземних дронів до кількості клієнтів-покупців меблів
  Clients_for_drones_furniture = Number_of_clients_furniture // Random_Ground_Drone_number
  print("Меблі: ",Clients_for_drones_furniture)


  #Цикл на обрахування діяльності дронів , що розвозять їжу. Тут рахуємо загальнич час перельотів , загальну вагу перевезень , заробіток , чи була доставка вчасною
  Drone_number_for_cycle = 0
  Money_food = 0
  Food_weight = 0
  Deliveries_food = 0
  Charges_food = 0
  Food_time_delivering = 0
  for x in range(Random_Drone_number):
    
    Drone = Drones[x]
    Food_weight_cycle = 0
    Deliveries = 0
    Charges = 0
    Time_delivering = 0
    Money = 0

    #Умова , щоб в поле обробки дрона додати відповідних йому клієнтів 
    if x!= Clients_for_drones_food - 1:
      Drone_number_for_cycle += Clients_for_drones_food
    elif  x == Clients_for_drones_food - 1 or Clients_for_drones_food == 0 :
      Drone_number_for_cycle = Drone_number_for_cycle + Clients_for_drones_food + Number_of_clients_food % Random_Drone_number
      
    #Цикл на обрахування взаємодії певного дрона з клієнтами       
    for y in range(Drone_number_for_cycle):
      
      #Ще одна умова . щоб відокремити від дрона чужих клієнтів
      if y > (x-1)*Clients_for_drones_food:
        Client = clients_food[y]
        Distance_to_client = Client.distance_to_client
        Product_weight = Client.product_weight
        Food_weight_cycle += Product_weight

        Drone.Calculating_time(Distance_to_client , Air_transport_speed_change )
        Working_time = Drone.Working_time

      
        Drone.Calculating_number_of_deliveries(Product_weight , One_delivery_weight_air)
        Deliveries_for_Deliverying_weight = Drone.Deliveries_for_Deliverying_weight

        Client.client_food_reaction(Working_time)
      
        Time_delivering += Working_time * Deliveries_for_Deliverying_weight
        Deliveries += Deliveries_for_Deliverying_weight
        Charges += Drone.Charges_times
        Money += Client.Earned_Money
        Money -=  Drone.Charges_times * 10
    #Сумування отриманих даних  , щоб потім до них була можливість звернутись , метод move для кожного робота.
    Drone.Money_for_charging(Charges)    
    Money_food += Money
    Food_time_delivering += Time_delivering
    Food_weight += Food_weight_cycle
    Deliveries_food += Deliveries
    Charges_food += Charges   
    Drone.move(Money, Charges ,  Food_weight_cycle , Deliveries , Time_delivering)


    print(f"Гроші , зароблені за доставку їжі: {Money_food}")
    print(f"Загальний час роботи дронів: {Food_time_delivering}")
    print(f"Загальна вага перевезень: {Food_weight}")
    print(f"Кількість перельтів усіх дронів: {Deliveries_food}")
    print(f"Кількість заряджань усіх дронів: {Charges_food}")




  #Цикл на обрахування дій наземних дронів , що виконують перевезення меблів
  Drone_number_for_cycle = 0
  Money_furniture = 0
  furniture_weight = 0
  Deliveries_furniture = 0
  Charges_furniture = 0
  furniture_time_delivering = 0
  for x in range(Random_Ground_Drone_number):
    
    Drone = Ground_Drones[x]
    furniture_weight_cycle = 0
    Deliveries = 0
    Charges = 0
    Time_delivering = 0
    Money = 0

    # Умова на додавання до поля обрахунку дрона відповідних йому клієнтів    
    if x!= Clients_for_drones_furniture - 1:
      Drone_number_for_cycle += Clients_for_drones_furniture
    elif  x == Clients_for_drones_furniture - 1 or Clients_for_drones_furniture == 0 :
      Drone_number_for_cycle = Drone_number_for_cycle + Clients_for_drones_furniture + Number_of_clients_furniture % Random_Ground_Drone_number

     #Цикл на прорахування взаємодії дрона з клієнтами        
    for y in range(Drone_number_for_cycle):
      #Умова на відокремлення чужих клієнтів
      if y > (x-1)*Clients_for_drones_furniture:
        Client = clients_furniture[y]
        Distance_to_client = Client.distance_to_client
        Product_weight = Client.product_weight
      

        Drone.Calculating_time(Distance_to_client , Ground_transport_speed_change )
        Working_time = Drone.Working_time 

      
        Drone.Calculating_number_of_deliveries(Product_weight , One_delivery_weight_ground)
        Deliveries_for_Deliverying_weight = Drone.Deliveries_for_Deliverying_weight

        Client.client_furniture_reaction(Working_time)

        furniture_weight_cycle += Product_weight
        Time_delivering += Working_time * Deliveries_for_Deliverying_weight
        Deliveries += Deliveries_for_Deliverying_weight
        Charges += Drone.Charges_times
        Money += Client.Earned_Money
        Money -=  Drone.Charges_times * 10
    #Збереження даних у списках , метод move для кожного робота.
    Money_charge = Drone.Money_for_charging(Charges)    
    Money_furniture += Money
    furniture_time_delivering += Time_delivering
    furniture_weight += furniture_weight_cycle
    Deliveries_furniture += Deliveries
    Charges_furniture += Charges   
    Drone.move(Money, Charges , furniture_weight_cycle , Deliveries , Time_delivering)


    print(f"Гроші , зароблені за перевезення меблів: {Money_furniture}")
    print(f"Загальний ча перевезення меблів: {furniture_time_delivering}")
    print(f"Загальна вага меблів: {furniture_weight}")
    print(f"Загальна кількість поїздок дронів: {Deliveries_furniture}")
    print(f"Загальна кількість заряджань дронів: {Charges_furniture}")





  #Обрахування роботи водних дронів на доставку матеріалів , введення списків та змінної для маутніх циклів
  Drone_number_for_cycle = 0
  Money_materials = 0
  materials_weight = 0
  Deliveries_materials = 0
  Charges_materials = 0
  materials_time_delivering = 0
  Materials_space_list = 0
  #Початок циклу
  for x in range(Random_Water_Drone_number):
    #Отримання об'єктів-дронів для морських перевезень зі списку , налаштування потрібних для підрахунку змінних у циклу
    Drone = Sea_Drones[x]
    materials_weight_cycle = 0
    Deliveries = 0
    Charges = 0
    Time_delivering = 0
    Money = 0
    Materials_space = 0
    #Умова на збільшення діапазону роботи кожного наступного робота відповідно до номерів його клієнтів
    if x!= Clients_for_drones_materials - 1:
      Drone_number_for_cycle += Clients_for_drones_materials
    elif  x == Clients_for_drones_materials - 1 or Clients_for_drones_materials == 0 :
      Drone_number_for_cycle = Drone_number_for_cycle + Clients_for_drones_materials + Number_of_clients_materials % Random_Water_Drone_number
    #Цикл на обрахування роботи одного робота з його клієнтами    
    for y in range(Drone_number_for_cycle):
      #Умова на відокремлення чужих клієнтів
      if y > (x-1)*Clients_for_drones_materials:
        Client = clients_materials[y]
        Distance_to_client = Client.distance_to_client
        Product_weight = Client.product_weight
        Materials_space = Client.space
      

        Drone.Calculating_time(Distance_to_client , Water_transport_speed_change )
        Working_time = Drone.Working_time

      
        Drone.Calculating_number_of_deliveries(Product_weight , One_delivery_weight_water)
        Drone.Calculating_deliveries_space(Materials_space ,One_delivery_space)
        
        Deliveries_for_Deliverying_weight = Drone.Deliveries_for_Deliverying_weight
        Deliveries_for_Deliverying_space = Drone.Deliveries_space


        materials_weight_cycle += Product_weight
        Materials_space += Drone.Deliveries_space
        
        #Особливістю товару - матеріали є характеристика об'єму , яки потрібно враховувати для перевезень. Кількість перевезень буде вираховуватись як сума більших значень перевезень для кожного клієнта
        if Deliveries_for_Deliverying_weight >= Deliveries_for_Deliverying_space:
          Deliveries += Deliveries_for_Deliverying_weight
          Time_delivering += Working_time * Deliveries_for_Deliverying_weight
          
        elif Deliveries_for_Deliverying_weight < Deliveries_for_Deliverying_space:
          Deliveries += Deliveries_for_Deliverying_space
          Time_delivering += Working_time * Deliveries_for_Deliverying_space
          
        Charges += Drone.Charges_times
        Client.client_reaction_materials()
        Money += Client.price
        Money -=  Drone.Charges_times * 10
        
    #Збереження результатів у списках , відображення деяких з них методом move.
    Money_charge = Drone.Money_for_charging(Charges)    
    Money_materials += Money
    materials_time_delivering += Time_delivering
    materials_weight += furniture_weight_cycle
    Deliveries_materials += Deliveries
    Charges_materials += Charges

    Drone.Money_for_charging(Charges)
    Drone.move(Charges , Money, materials_weight_cycle , Deliveries , Materials_space , Time_delivering , One_delivery_space )


    print(f"Гроші , отримані за перевезення матеріалів: {Money_materials}")
    print(f"Загальний час перевезення матеріалів: {materials_time_delivering}")
    print(f"Загальна вага матеріалів: {materials_weight}")
    print(f"Загальна кількість плавань роботів-перевізників: {Deliveries_materials}")
    print(f"Загальна кількість заряджань рботів: {Charges_materials}")


  storage_food.last_products_Food(Number_of_clients_food , clients_food)
  storage_materials.last_products_Materials(Number_of_clients_materials , clients_materials)
  storage_furniture.last_products_Furniture(Number_of_clients_furniture , clients_furniture)

  Money_food = Money_food - storage_food.Reqired_Money_food
  Money_materials = Money_materials - storage_materials.Reqired_Money_materials
  Money_furniture = Money_furniture - storage_furniture.Reqired_Money_furniture

  print(f"Гроші за перевезення їжі після вирахування витрат на дозакупівлю: {Money_food}")
  print(f"Гроші за перевезення матеріалів після вирахування витрат на дозакупівлю: {Money_materials}")
  print(f"Гроші за перевезення меблів після вирахування витрат на дозакупівлю: {Money_furniture}")


  Broken_robots = 0
  
  for Chance in range(Random_Drone_number ):
    Drone = Drones[Chance]
    Broken_robots = Drone.Get_broken(Broken_robots)


  for Chance in range(Random_Ground_Drone_number):
    Drone = Ground_Drones[Chance]
    Broken_robots = Drone.Get_broken(Broken_robots)



  for Chance in range(Random_Ground_Drone_number ):
    Drone = Ground_Drones[Chance]
    Broken_robots = Drone.Get_broken( Broken_robots)


  print("Кількість зламаних роботів: ",Broken_robots)  

  Broken_robots_workers = Broken_robots // Workers_number

  for number in range(Workers_number):
    Worker = Workers_list[number]
    Worker.All_Drons_Repaired(Broken_robots_workers)


  Lost_workers = 0
  
  for number in range(Workers_number):
    Worker = Workers_list[number]
    Lost_workers = Worker.Refuse_work(Lost_workers)

  for number in range(Lost_workers):
      Workers_list.pop(-1)
    

  Boos1.Find_worker(Lost_workers)

  for number in range(len(Workers_list1)):
    worker = Workers_list1[number]
    Workers_list.append(worker)


  for number in range(len(Workers_list)):
    worker = Workers_list[number]
    worker.show_information()
      
  
  

  All_money = All_money + Money_food + Money_materials + Money_furniture
  print(f"Загальний заробіток: {All_money}")



  
  




    


    
        

    

      

      
      
      
      
      
      

    
    

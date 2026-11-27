from Logs import logger_main
#Імпорт рандому та класів
import random
import Logs
import graph_v6
from graph_v6 import find_distance
from graph_v6 import answer
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
boss_list = []
number_of_day_simulation_1 = int(input("Введіть кількість днів симуляції: " ))
boss_name_list_1 = ["Макс" ,"Степан","Олександр","Федір" , "Трай" , "Флок" , "Джон" , "Майкан" ,"Дроул"]
boss_hobby_list_1 = ["Шахи","Кулінарія","Програмування"]
boss_name_1 = random.choice(boss_name_list_1)
boss_work_time_1 = random.randint(1 , 10)
boss_hobby_1 = random.choice(boss_hobby_list_1)
boos1_1 = Boss(boss_name_1, boss_work_time_1 ,boss_hobby_1)
boss_list.append(boos1_1)


#Рандомне налаштування перших робітників
workers_list_1 = []
workers_number_1 = random.randint(1,5)
for worker_number in range(workers_number_1):
  worker_name_list_1 = ["Олексій","Антон","Федір","Микита","Максим","Олександр","Дмитро","Григорій" , "Афанасій" , "Вольтман"]
  salary_list_1 = [1500 , 2000 , 2500 , 3000  ]
  worker_salary_1 = int(random.choice(salary_list_1))
  Worker.name_1 = random.choice(worker_name_list_1)
  worker = Worker(Worker.name_1 ,worker_salary_1 )
  print("Робітник: ",worker.name_1,"приступає до роботи")
  workers_list_1.append(worker)

# ==================== ТЕСТ 3: ВУЗЛИ ГРАФА ====================
# У graph_v6 вузли (міста) зберігаються у списку list_cities.
graph_nodes_test_passed = (
    hasattr(graph_v6, "list_cities")
    and len(graph_v6.list_cities) > 0
    and all(isinstance(city_1, graph_v6.cities) for city_1 in graph_v6.list_cities)
)

if graph_nodes_test_passed:
  logger_main.info(
      f"ТЕСТ 3 УСПІШНИЙ: граф містить {len(graph_v6.list_cities)} вузлів."
  )
else:
  logger_main.error("ТЕСТ 3 НЕ ПРОЙДЕНО: граф не містить вузлів або список вузлів некоректний.")

# ==================== ТЕСТ 1: БОС І РОБІТНИКИ ====================
# Перевіряємо, що створено екземпляр Boss і хоча б одного Worker.
boss_test_passed = isinstance(boos1_1, Boss) and len(boss_list) > 0
workers_test_passed = len(workers_list_1) > 0 and all(
    isinstance(worker_1, Worker) for worker_1 in workers_list_1)

if boss_test_passed and workers_test_passed:
  logger_main.info("ТЕСТ 1 УСПІШНИЙ: екземпляр боса та екземпляри робітників існують.")
else:
  logger_main.error(
      f"ТЕСТ 1 НЕ ПРОЙДЕНО: boss={boss_test_passed}, workers={workers_test_passed}")

#Отримуємо рандомну кількість дронів кожного виду
random_drone_number_1 = random.randint(1,12)
random_ground_drone_number_1 = random.randint(1,12)
random_water_drone_number_1 = random.randint(1,12)


# Налаштування Drones
drones_1 = []
for drone_1 in range(random_drone_number_1):
  models_list_1 = ["AR-101","AR-102","AR-103","AR-104","AR-105","AR-106",
                 "AR-107","AR-108","AR-109",
                 "AR-110","AR-111","AR-112",
                 "AR-113","AR-114","AR-115",
                 "AR-116","AR-117","AR-118",
                 "AR-119","AR-120","AR-121",
                 "AR-122","AR-123","AR-124",
                 "AR-125","AR-126","AR-127"]
  drone_charge_price_1 = 75
  drone_name_1 = random.choice(models_list_1)
  drone_speed_1 = 50
  drone_hour_energy_consume_1 = 5
  flying_drone_1 = Fly_Drone(drone_name_1 , drone_speed_1  , drone_hour_energy_consume_1 , drone_charge_price_1)
  drones_1.append(flying_drone_1)
  
# Налаштування Ground_Drones
ground_drones_1 = []
for drone_1 in range(random_ground_drone_number_1):
  models_list_1 = ["ARB-101","ARB-102","ARB-103","ARB-104","ARB-105","ARB-106",
                 "ARB-107","ARB-108","ARB-109",
                 "ARB-110","ARB-111","ARB-112",
                 "ARB-113","ARB-114","ARB-115",
                 "ARB-116","ARB-117","ARB-118",
                 "ARB-119","ARB-120","ARB-121",
                 "ARB-122","ARB-123","ARB-124",
                 "ARB-125","ARB-126","ARB-127"]
  ground_drone_charge_price_1 = 50
  ground_drone_name_1 = random.choice(models_list_1)
  ground_drone_speed_1 = 30
  ground_drone_hour_energy_consume_1 = 7.5
  ground_drone_1 = Ground_Drone(ground_drone_name_1 , ground_drone_speed_1  , ground_drone_hour_energy_consume_1 ,  ground_drone_charge_price_1 )
  ground_drones_1.append(ground_drone_1)


# Налаштування Sea_Drones
sea_drones_1 = []
for drone_1 in range(random_water_drone_number_1):
  models_list_1 = ["ARC-101","ARC-102","ARC-103","ARC-104","ARC-105","ARC-106",
                 "ARC-107","ARC-108","ARC-109",
                 "ARC-110","ARC-111","ARC-112",
                 "ARC-113","ARC-114","ARC-115",
                 "ARC-116","ARC-117","ARC-118",
                 "ARC-119","ARC-120","ARC-121",
                 "ARC-122","ARC-123","ARC-124",
                 "ARC-125","ARC-126","ARC-127"]
  sea_drone_name_1 = random.choice(models_list_1)
  sea_drone_charge_price_1 = 30
  sea_drone_speed_1 = 45
  sea_drone_hour_energy_consume_1 = 10
  sea_drone_1 = Water_Drone(sea_drone_name_1 , sea_drone_speed_1  , sea_drone_hour_energy_consume_1 ,  sea_drone_charge_price_1 )
  sea_drones_1.append(sea_drone_1)
  
#Перевірка
all_units = [boss_list , drones_1 , ground_drones_1 , sea_drones_1]

for element in range (len(all_units)):
  
  object_ = all_units[element]

  for current_element in range(len(object_)):
    
    info_obgect = object_[current_element]
    
    info_obgect.info()
    
 

#Останні приготування перед циклом 
all_money_1 = 0
clients_1 = []
boos1_1.Experience()
storage_food = Storage()
storage_materials = Storage()
storage_furniture = Storage()
for day_1 in range(number_of_day_simulation_1):

  #Заставка нового дня
  logger_main.info("="*35)
  logger_main.info(f"День роботи: {day_1 +1}")
  logger_main.info("="*35)

  #Базові налаштування для дронів
  one_delivery_weight_air_1 = 20
  one_delivery_weight_water_1 = 30
  one_delivery_space_1 = 40
  one_delivery_weight_ground_1 = 25
  day_money_1 = 0
  water_transport_speed_change_1 = 0
  ground_transport_speed_change_1 = 0
  air_transport_speed_change_1 = 0


  #Налаштування погоди
  days_for_weather_1 = random.randint(3,6)
  weather = Weather(days_for_weather_1)
  weather.Random_Weather()

  #Переговори боса з іншими компаніями
  supply_change_1 = 0
  boos1_1.Deal(day_1)
  

  #Завезення товару до складу
  storage_food.new_products_Food(supply_change_1)
  storage_materials.new_products_Materials(supply_change_1)
  storage_furniture.new_products_Furniture(supply_change_1)
  
  boos1_1.random_mood()
  time = 4


  #Кількість клієнтів
  number_of_clients_food_1 = random.randint(1,5)
  number_of_clients_furniture_1 = random.randint(1,5)
  number_of_clients_materials_1 = random.randint(1,5)

  
  #Цикл на рандомне надання характеристик клієнтам-покупцям їжі
  clients_food = []
  for client in range(number_of_clients_food_1 ):
    
    weight_food = random.randint(1,150)
    find_distance(client)
    distance_for_food_to_client = answer
    client = Client_food(weight_food , distance_for_food_to_client )
    clients_food.append(client)


  # Цикл на рандомне надання характеристик клієнтам-покупцям матеріалів
  clients_materials = []
  for client in range(number_of_clients_materials_1):
    
    weight_materials = random.randint(1,150)
    find_distance(client)
    distance_for_materials_to_client = answer
    space_materials = random.randint(1 , 75)
    
    client = Client_materials(weight_materials , distance_for_materials_to_client , space_materials)
    clients_materials.append(client)

  #Цикл на рандомне надання характеристик клієнтам-покупцям меблів
  clients_furniture = []
  for client_furniture in range(number_of_clients_furniture_1):

    weight_furniture = random.randint(1,125)
    find_distance(client)
    distance_for_furniture_to_client = answer

    client_furniture = Client_furniture(weight_furniture , distance_for_furniture_to_client)
    clients_furniture.append(client_furniture)

  # Перевіряємо базові атрибути кожного типу клієнта.
  basic_client_attributes_1 = ("product_weight", "distance_to_client")
  food_client_attributes_1 = basic_client_attributes_1 + ("price_1", "earned_money_1", "time")
  materials_client_attributes_1 = basic_client_attributes_1 + ("space",)
  furniture_client_attributes_1 = basic_client_attributes_1 + ("price_1", "earned_money_1", "time")

  clients_test_groups_1 = [
      ("їжі", clients_food, food_client_attributes_1),
      ("матеріалів", clients_materials, materials_client_attributes_1),
      ("меблів", clients_furniture, furniture_client_attributes_1),]
  clients_test_errors_1 = []

  for group_name_1, client_group_1, required_attributes_1 in clients_test_groups_1:
    
    for client_index_1, client_object_1 in enumerate(client_group_1):
      
      for attribute_1 in required_attributes_1:
        
        if not hasattr(client_object_1, attribute_1):
          
          clients_test_errors_1.append(
              f"Клієнт {group_name_1} №{client_index_1 + 1}: немає атрибута {attribute_1}")

  if not clients_test_errors_1:
    logger_main.info(
        f"ТЕСТ 2 УСПІШНИЙ: перевірено атрибути {len(clients_food) + len(clients_materials) + len(clients_furniture)} клієнтів.")
  else:
    logger_main.error("ТЕСТ 2 НЕ ПРОЙДЕНО: " + "; ".join(clients_test_errors_1))

  #Отримуємо співвідношення дронів до клієнтів-покупців їжі
  clients_for_drones_food_1 = number_of_clients_food_1 // random_drone_number_1
  logger_main.info(f"Їжа:  {clients_for_drones_food_1}")

  #Отримуємо співвідношення водних дронів до клієнтів-покупців матеріалів
  clients_for_drones_materials_1 = number_of_clients_materials_1 // random_water_drone_number_1
  logger_main.info(f"Матеріали:  {clients_for_drones_materials_1}")

  #Отримуємо співвідношення наземних дронів до кількості клієнтів-покупців меблів
  clients_for_drones_furniture_1 = number_of_clients_furniture_1 // random_ground_drone_number_1
  logger_main.info(f"Меблі:  {clients_for_drones_furniture_1}")


  #Цикл на обрахування діяльності дронів , що розвозять їжу. Тут рахуємо загальнич час перельотів , загальну вагу перевезень , заробіток , чи була доставка вчасною
  drone_number_for_cycle_1 = 0
  money_food_1 = 0
  food_weight_1 = 0
  deliveries_food_1 = 0
  charges_food_1 = 0
  food_time_delivering_1 = 0
  for x in range(random_drone_number_1):
    
    drone_1 = drones_1[x]
    food_weight_cycle_1 = 0
    deliveries_1 = 0
    charges_1 = 0
    time_delivering_1 = 0
    money_1 = 0

    #Умова , щоб в поле обробки дрона додати відповідних йому клієнтів 
    if x!= clients_for_drones_food_1 - 1:
      drone_number_for_cycle_1 += clients_for_drones_food_1
    elif  x == clients_for_drones_food_1 - 1 or clients_for_drones_food_1 == 0 :
      drone_number_for_cycle_1 = drone_number_for_cycle_1 + clients_for_drones_food_1 + number_of_clients_food_1 % random_drone_number_1
      
    #Цикл на обрахування взаємодії певного дрона з клієнтами       
    for y in range(drone_number_for_cycle_1):
      
      #Ще одна умова . щоб відокремити від дрона чужих клієнтів
      if y > (x-1)*clients_for_drones_food_1:
        Client = clients_food[y]
        distance_to_client_1 = Client.distance_to_client
        product_weight_1 = Client.product_weight
        food_weight_cycle_1 += product_weight_1

        drone_1.Calculating_time(distance_to_client_1 , air_transport_speed_change_1 )
        working_time_1 = drone_1.working_time_1

      
        drone_1.Calculating_number_of_deliveries(product_weight_1 , one_delivery_weight_air_1)
        deliveries_for_deliverying_weight_1 = drone_1.deliveries_for_deliverying_weight_1

        Client.client_food_reaction(working_time_1)
      
        time_delivering_1 += working_time_1 * deliveries_for_deliverying_weight_1
        deliveries_1 += deliveries_for_deliverying_weight_1
        charges_1 += drone_1.charges_times_1
        money_1 += Client.earned_money_1
        money_1 -=  drone_1.charges_times_1 * 10

        
    #Сумування отриманих даних  , щоб потім до них була можливість звернутись , метод move для кожного робота.
    drone_1.Money_for_charging(charges_1)    
    money_food_1 += money_1
    food_time_delivering_1 += time_delivering_1
    food_weight_1 += food_weight_cycle_1
    deliveries_food_1 += deliveries_1
    charges_food_1 += charges_1   
    drone_1.move(money_1, charges_1 ,  food_weight_cycle_1 , deliveries_1 , time_delivering_1)


    logger_main.info(f"Гроші , зароблені за доставку їжі: {money_food_1}")
    logger_main.info(f"Загальний час роботи дронів: {food_time_delivering_1}")
    logger_main.info(f"Загальна вага перевезень: {food_weight_1}")
    logger_main.info(f"Кількість перельтів усіх дронів: {deliveries_food_1}")
    logger_main.info(f"Кількість заряджань усіх дронів: {charges_food_1}")




  #Цикл на обрахування дій наземних дронів , що виконують перевезення меблів
  drone_number_for_cycle_1 = 0
  money_furniture_1 = 0
  furniture_weight = 0
  deliveries_furniture_1 = 0
  charges_furniture_1 = 0
  furniture_time_delivering = 0
  for x in range(random_ground_drone_number_1):
    
    drone_1 = ground_drones_1[x]
    furniture_weight_cycle = 0
    deliveries_1 = 0
    charges_1 = 0
    time_delivering_1 = 0
    money_1 = 0

    # Умова на додавання до поля обрахунку дрона відповідних йому клієнтів    
    if x!= clients_for_drones_furniture_1 - 1:
      drone_number_for_cycle_1 += clients_for_drones_furniture_1
    elif  x == clients_for_drones_furniture_1 - 1 or clients_for_drones_furniture_1 == 0 :
      drone_number_for_cycle_1 = drone_number_for_cycle_1 + clients_for_drones_furniture_1 + number_of_clients_furniture_1 % random_ground_drone_number_1

     #Цикл на прорахування взаємодії дрона з клієнтами        
    for y in range(drone_number_for_cycle_1):
      #Умова на відокремлення чужих клієнтів
      if y > (x-1)*clients_for_drones_furniture_1:
        Client = clients_furniture[y]
        distance_to_client_1 = Client.distance_to_client
        product_weight_1 = Client.product_weight
      

        drone_1.Calculating_time(distance_to_client_1 , ground_transport_speed_change_1 )
        working_time_1 = drone_1.working_time_1 

      
        drone_1.Calculating_number_of_deliveries(product_weight_1 , one_delivery_weight_ground_1)
        deliveries_for_deliverying_weight_1 = drone_1.deliveries_for_deliverying_weight_1

        Client.client_furniture_reaction(working_time_1)

        furniture_weight_cycle += product_weight_1
        time_delivering_1 += working_time_1 * deliveries_for_deliverying_weight_1
        deliveries_1 += deliveries_for_deliverying_weight_1
        charges_1 += drone_1.charges_times_1
        money_1 += Client.earned_money_1
        money_1 -=  drone_1.charges_times_1 * 10
        
    #Збереження даних у списках , метод move для кожного робота.
    money_charge_1 = drone_1.Money_for_charging(charges_1)    
    money_furniture_1 += money_1
    furniture_time_delivering += time_delivering_1
    furniture_weight += furniture_weight_cycle
    deliveries_furniture_1 += deliveries_1
    charges_furniture_1 += charges_1   
    drone_1.move(money_1, charges_1 , furniture_weight_cycle , deliveries_1 , time_delivering_1)


    logger_main.info(f"Гроші , зароблені за перевезення меблів: {money_furniture_1}")
    logger_main.info(f"Загальний ча перевезення меблів: {furniture_time_delivering}")
    logger_main.info(f"Загальна вага меблів: {furniture_weight}")
    logger_main.info(f"Загальна кількість поїздок дронів: {deliveries_furniture_1}")
    logger_main.info(f"Загальна кількість заряджань дронів: {charges_furniture_1}")





  #Обрахування роботи водних дронів на доставку матеріалів , введення списків та змінної для маутніх циклів
  drone_number_for_cycle_1 = 0
  money_materials_1 = 0
  materials_weight = 0
  deliveries_materials_1 = 0
  charges_materials_1 = 0
  materials_time_delivering = 0
  materials_space_list_1 = 0
  #Початок циклу
  for x in range(random_water_drone_number_1):
    #Отримання об'єктів-дронів для морських перевезень зі списку , налаштування потрібних для підрахунку змінних у циклу
    drone_1 = sea_drones_1[x]
    materials_weight_cycle = 0
    deliveries_1 = 0
    charges_1 = 0
    time_delivering_1 = 0
    money_1 = 0
    materials_space_1 = 0
    #Умова на збільшення діапазону роботи кожного наступного робота відповідно до номерів його клієнтів
    if x!= clients_for_drones_materials_1 - 1:
      drone_number_for_cycle_1 += clients_for_drones_materials_1
    elif  x == clients_for_drones_materials_1 - 1 or clients_for_drones_materials_1 == 0 :
      drone_number_for_cycle_1 = drone_number_for_cycle_1 + clients_for_drones_materials_1 + number_of_clients_materials_1 % random_water_drone_number_1
    #Цикл на обрахування роботи одного робота з його клієнтами    
    for y in range(drone_number_for_cycle_1):
      #Умова на відокремлення чужих клієнтів
      if y > (x-1)*clients_for_drones_materials_1:
        Client = clients_materials[y]
        distance_to_client_1 = Client.distance_to_client
        product_weight_1 = Client.product_weight
        materials_space_1 = Client.space
      

        drone_1.Calculating_time(distance_to_client_1 , water_transport_speed_change_1 )
        working_time_1 = drone_1.working_time_1

      
        drone_1.Calculating_number_of_deliveries(product_weight_1 , one_delivery_weight_water_1)
        drone_1.Calculating_deliveries_space(materials_space_1 ,one_delivery_space_1)
        
        deliveries_for_deliverying_weight_1 = drone_1.deliveries_for_deliverying_weight_1
        deliveries_for_deliverying_space_1 = drone_1.deliveries_space_1


        materials_weight_cycle += product_weight_1
        materials_space_1 += drone_1.deliveries_space_1
        
        #Особливістю товару - матеріали є характеристика об'єму , яки потрібно враховувати для перевезень. Кількість перевезень буде вираховуватись як сума більших значень перевезень для кожного клієнта
        if deliveries_for_deliverying_weight_1 >= deliveries_for_deliverying_space_1:
          deliveries_1 += deliveries_for_deliverying_weight_1
          time_delivering_1 += working_time_1 * deliveries_for_deliverying_weight_1
          
        elif deliveries_for_deliverying_weight_1 < deliveries_for_deliverying_space_1:
          deliveries_1 += deliveries_for_deliverying_space_1
          time_delivering_1 += working_time_1 * deliveries_for_deliverying_space_1
          
        charges_1 += drone_1.charges_times_1
        Client.client_reaction_materials()
        money_1 += Client.price
        money_1 -=  drone_1.charges_times_1 * 10
        
    #Збереження результатів у списках , відображення деяких з них методом move.
    money_charge_1 = drone_1.Money_for_charging(charges_1)    
    money_materials_1 += money_1
    materials_time_delivering += time_delivering_1
    materials_weight += furniture_weight_cycle
    deliveries_materials_1 += deliveries_1
    charges_materials_1 += charges_1

    drone_1.Money_for_charging(charges_1)
    drone_1.move(charges_1 , money_1, materials_weight_cycle , deliveries_1 , materials_space_1 , time_delivering_1 , one_delivery_space_1 )


    logger_main.info(f"Гроші , отримані за перевезення матеріалів: {money_materials_1}")
    logger_main.info(f"Загальний час перевезення матеріалів: {materials_time_delivering}")
    logger_main.info(f"Загальна вага матеріалів: {materials_weight}")
    logger_main.info(f"Загальна кількість плавань роботів-перевізників: {deliveries_materials_1}")
    logger_main.info(f"Загальна кількість заряджань рботів: {charges_materials_1}")


  storage_food.last_products_Food(number_of_clients_food_1 , clients_food)
  storage_materials.last_products_Materials(number_of_clients_materials_1 , clients_materials)
  storage_furniture.last_products_Furniture(number_of_clients_furniture_1 , clients_furniture)

  money_food_1 = money_food_1 - storage_food.reqired_money_food_1
  money_materials_1 = money_materials_1 - storage_materials.reqired_money_materials_1
  money_furniture_1 = money_furniture_1 - storage_furniture.reqired_money_furniture_1

  logger_main.info(f"Гроші за перевезення їжі після вирахування витрат на дозакупівлю: {money_food_1}")
  logger_main.info(f"Гроші за перевезення матеріалів після вирахування витрат на дозакупівлю: {money_materials_1}")
  logger_main.info(f"Гроші за перевезення меблів після вирахування витрат на дозакупівлю: {money_furniture_1}")


  broken_robots_1 = 0
  
  for chance_1 in range(random_drone_number_1 ):
    drone_1 = drones_1[chance_1]
    broken_robots_1 = drone_1.Get_broken(broken_robots_1)


  for chance_1 in range(random_ground_drone_number_1):
    drone_1 = ground_drones_1[chance_1]
    broken_robots_1 = drone_1.Get_broken(broken_robots_1)



  for chance_1 in range(random_ground_drone_number_1 ):
    drone_1 = ground_drones_1[chance_1]
    broken_robots_1 = drone_1.Get_broken( broken_robots_1)


  logger_main.info(f"Кількість зламаних роботів:  {broken_robots_1}")  

  number_of_drons_for_worker_1 = broken_robots_1 // workers_number_1

  for number in range(workers_number_1):
    worker = workers_list_1[number]
    worker.All_Drons_Repaired(number_of_drons_for_worker_1)


  lost_workers_1 = 0
  
  for number in range(workers_number_1):
    worker = workers_list_1[number]
    lost_workers_1 += worker.Refuse_work(lost_workers_1)

  try :
    for number in range(lost_workers_1):
      workers_list_1.pop(-1)

  except :
    a = 2 + 5 
    

  boos1_1.Find_worker(lost_workers_1)

  for number in range(len(Workers_list1)):
    worker = Workers_list1[number]
    workers_list_1.append(worker)


  for number in range(len(workers_list_1)):
    worker = workers_list_1[number]
    worker.show_information()
      
  
  

  all_money_1 = all_money_1 + money_food_1 + money_materials_1 + money_furniture_1
  logger_main.info(f"Загальний заробіток: {all_money_1}")



  
  




    


    
        

    

      

      
      
      
      
      
      

    
    

from Logs import logger_food, logger_furniture
import random
class Client :
  def __init__(self , product_weight , distance_to_client ):
    self.product_weight = product_weight
    self.distance_to_client = distance_to_client
    self.price_1 = self.distance_to_client * 15 + self.product_weight * 20
    self.earned_money_1 = 0
    self.time = 0
  

  def cl_reaction(self , time):
    self.time = time
    self.delivery_possibility_1 = self.time <= 4
    if self.delivery_possibility_1 :
      print("Клієнт заплатив.Доставка відбулась вчасно. ")
      self.earned_money_1 += self.price_1
    else:
      print("Клієнт не заплатив.Доставка не відбулась вчасно.")
      self.earned_money_1 += 0

pass

class Client_food(Client):
  def client_food_reaction(self , working_time):
    self.food_live_time = random.randint(2,10)
    logger_food.info(f"Їжа буде придатною год.: {self.food_live_time}")
    result_1 = self.food_live_time > working_time
    if result_1:
      logger_food.info("Клієнт заплатив.Доставка відбулась вчасно. ")
      self.earned_money_1 += self.price_1
    else:
      logger_food.info("Клієнт не заплатив.Доставка не відбулась вчасно.")
      self.earned_money_1 += 0
  
class Client_materials(Client):
  def __init__(self , product_weight , distance_to_client , space ):
    self.product_weight = product_weight
    self.distance_to_client = distance_to_client
    self.space = space


  def client_reaction_materials(self):
    self.price = self.space*10 + self.product_weight*25 + self.distance_to_client*15 

class Client_furniture(Client):
  def client_furniture_reaction(self , working_time):
    self.price_1 = self.distance_to_client * 10 + self.product_weight * 25
    counter_cycle = 0
    broken_furniture_chance_1 = 0
    while counter_cycle <  working_time and broken_furniture_chance_1 != 5:
      broken_furniture_chance_1 = random.randint(1,100)
      counter_cycle +=1
      

    if broken_furniture_chance_1 == 5:
      logger_furniture.info("Сталась халепа: меблі були пошкоджені протягом доставки.Клієнт не заплатив , фінансові втрати становлять 150 ")
      self.earned_money_1 -= 150
    else:
      logger_furniture.info("Меблі були доставлені без пригод.Клієнт заплатив")
      self.earned_money_1 += self.price_1
      
  pass

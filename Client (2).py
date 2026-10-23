import random
class Client :
  def __init__(self , product_weight , distance_to_client ):
    self.product_weight = product_weight
    self.distance_to_client = distance_to_client
    self.Price = self.distance_to_client * 15 + self.product_weight * 20
    self.Earned_Money = 0
    self.time = 0

  def cl_reaction(self , time):
    self.time = time
    self.Delivery_possibility = self.time <= 4
    if self.Delivery_possibility :
      print("Клієнт заплатив.Доставка відбулась вчасно. ")
      self.Earned_Money += self.Price
    else:
      print("Клієнт не заплатив.Доставка не відбулась вчасно.")
      self.Earned_Money += 0

pass

class Client_food(Client):
  def client_food_reaction(self , working_time):
    self.food_live_time = random.randint(2,10)
    print("Їжа буде придатною год.:",self.food_live_time)
    Result = self.food_live_time > working_time
    if Result:
      print("Клієнт заплатив.Доставка відбулась вчасно. ")
      self.Earned_Money += self.Price
    else:
      print("Клієнт не заплатив.Доставка не відбулась вчасно.")
      self.Earned_Money += 0
  
class Client_materials(Client):
  def __init__(self , product_weight , distance_to_client , space ):
    self.product_weight = product_weight
    self.distance_to_client = distance_to_client
    self.space = space


  def client_reaction_materials(self):
    self.price = self.space*10 + self.product_weight*25 + self.distance_to_client*15 

class Client_furniture(Client):
  def client_furniture_reaction(self , working_time):
    self.Price = self.distance_to_client * 10 + self.product_weight * 25
    counter_cycle = 0
    Broken_furniture_chance = 0
    while counter_cycle <  working_time and Broken_furniture_chance != 5:
      Broken_furniture_chance = random.randint(1,100)
      counter_cycle +=1
      

    if Broken_furniture_chance == 5:
      print("Сталась халепа: меблі були пошкоджені протягом доставки.Клієнт не заплатив , фінансові втрати становлять 150 ")
      self.Earned_Money -= 150
    else:
      print("Меблі були доставлені без пригод.Клієнт заплатив")
      self.Earned_Money += self.Price
      
  pass

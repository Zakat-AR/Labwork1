from Logs import logger_storage_food, logger_storage_furniture, logger_storage_materials
import random
import Logs
#
class Storage :
  #Метод на заповнення складу Food 
  def new_products_Food(self , supply_change_1 ):
    self.new_products_food_1 = 0
    self.products_food_1 = 0
    self.reqired_money_1 = 0
    self.new_products_food_1 = random.randint(300 , 600)
    self.products_food_1 += self.new_products_food_1 + supply_change_1
    logger_storage_materials.info(f"Доставлено на склад продуктів:{self.products_food_1} кг.")

   #Метод на заповнення складу Materials
  def new_products_Materials(self , supply_change_1 ):
    self.new_products_materials_1 = 0
    self.products_materials_1 = 0
    self.reqired_money_1 = 0
    self.new_products_materials_1 = random.randint(300 , 600)
    self.products_materials_1 += self.new_products_materials_1 + supply_change_1
    logger_storage_materials.info(f"Доставлено на склад продуктів:{self.products_materials_1} кг.")
    
   #Метод на заповнення складу Furniture
  def new_products_Furniture(self , supply_change_1 ):
    self.new_products_furniture_1 = 0
    self.products_furniture_1 = 0
    self.reqired_money_1 = 0
    self.new_products_furniture_1 = random.randint(300 , 600)
    self.products_furniture_1 += self.new_products_furniture_1 + supply_change_1
    logger_storage_furniture.info(f"Доставлено на склад продуктів:{self.products_furniture_1} кг.")
    
   # Метод на докупівлю Food
  def last_products_Food(self , number_of_clients_for_food_1 , clients_food):
    all_products_food_1 = 0
    
    for y in range(number_of_clients_for_food_1 ):
      Client = clients_food[y]
      product_weight_1 = Client.product_weight
      all_products_food_1 += product_weight_1
      
    
    if all_products_food_1 > self.products_food_1:
      number_of_served_clients_food_1 = 0
      
      for y in range(number_of_clients_for_food_1):
        
        Client = clients_food[y]
        product_weight_1 = Client.product_weight
        
        self.last_products_food_1 = self.products_food_1 - product_weight_1
        if self.last_products_food_1 > 0:
          number_of_served_clients_food_1 +=1
        else:
          number_of_served_clients_food_1 += 0
         
      logger_storage_food.info("Маємо товар для клієнтів: " + str(number_of_served_clients_food_1))
      logger_storage_food.info(f"Потрібно докупити товару: {all_products_food_1 - self.products_food_1}")
      self.reqired_money_food_1 = (all_products_food_1 - self.products_food_1)*15
      logger_storage_food.info(f"Витрачено грошей:  {self.reqired_money_food_1}")
      
      self.products_food_1 = 0
      
    else:
      logger_storage_food.info("Товару достатньо")
      self.reqired_money_food_1 = 0
    return  self.reqired_money_food_1

  # Метод на докупівлю Materials
  def last_products_Materials(self , number_of_clients_for_materials_1 , clients_materials ):
    all_products_materials_weight_1 = 0
    
    for y in range(number_of_clients_for_materials_1):
      Client = clients_materials[y]
      product_weight_1 = Client.product_weight
      all_products_materials_weight_1 += product_weight_1
      
    
    if all_products_materials_weight_1 > self.products_materials_1:
      number_of_served_clients_materials_1 = 0
      
      for y in range(number_of_clients_for_materials_1):
        
        Client = clients_materials[y]
        product_weight_1 = Client.product_weight
        
        self.last_products_materials_1 = self.products_materials_1 - product_weight_1
        if self.last_products_materials_1 > 0:
          number_of_served_clients_materials_1 +=1
        else:
          number_of_served_clients_materials_1 += 0
         
      logger_storage_materials.info("Маємо товар для клієнтів: " + str(number_of_served_clients_materials_1))
      logger_storage_materials.info(f"Потрібно докупити товару: {all_products_materials_weight_1 - self.products_materials_1}")
      self.reqired_money_materials_1 = (all_products_materials_weight_1 - self.products_materials_1)*15
      logger_storage_materials.info(f"Витрачено грошей:  {self.reqired_money_materials_1}")
      
      self.products_materials_1 = 0
      
    else:
      
      logger_storage_materials.info("Товару достатньо")
      self.reqired_money_materials_1 = 0
      
    return  self.reqired_money_materials_1



  # Метод на докупівлю Furniture
  def last_products_Furniture(self , number_of_clients_furniture_1 , clients_furniture ):
    all_products_furniture_weight_1 = 0
    
    for y in range(number_of_clients_furniture_1):
      Client = clients_furniture[y]
      product_weight_1 = Client.product_weight
      all_products_furniture_weight_1 += product_weight_1
      
    
    if all_products_furniture_weight_1 > self.products_furniture_1:
      number_of_served_clients_furniture_1 = 0
      
      for y in range(number_of_clients_furniture_1):
        
        Client = clients_furniture[y]
        product_weight_1 = Client.product_weight
        
        self.last_products_furniture_1 = self.products_furniture_1 - product_weight_1
        if self.last_products_furniture_1 > 0:
          number_of_served_clients_furniture_1 +=1
        else:
          number_of_served_clients_furniture_1 += 0
         
      logger_storage_furniture.info("Маємо товар для клієнтів: " + str(number_of_served_clients_furniture_1))
      logger_storage_furniture.info(f"Потрібно докупити товару: {all_products_furniture_weight_1 - self.products_furniture_1}")
      self.reqired_money_furniture_1 = (all_products_furniture_weight_1 - self.products_furniture_1)*15
      logger_storage_furniture.info(f"Витрачено грошей:  {self.reqired_money_furniture_1}")
      
      self.products_furniture_1 = 0
      
    else:
      
      logger_storage_furniture.info("Товару достатньо")
      self.reqired_money_furniture_1 = 0
      
    return  self.reqired_money_furniture_1

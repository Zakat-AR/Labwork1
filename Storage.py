import random
#
class Storage :
  #Метод на заповнення складу Food 
  def new_products_Food(self ):
    self.New_products_food = 0
    self.Products_food = 0
    self.Reqired_Money = 0
    self.New_products_food = random.randint(300 , 600)
    self.Products_food += self.New_products_food
    print(f"Доставлено на склад продуктів:{self.Products_food} кг.")

   #Метод на заповнення складу Materials
  def new_products_Materials(self ):
    self.New_products_materials = 0
    self.Products_materials = 0
    self.Reqired_Money = 0
    self.New_products_materials = random.randint(300 , 600)
    self.Products_materials += self.New_products_materials
    print(f"Доставлено на склад продуктів:{self.Products_materials} кг.")
    
   #Метод на заповнення складу Furniture
  def new_products_Furniture(self ):
    self.New_products_furniture = 0
    self.Products_furniture = 0
    self.Reqired_Money = 0
    self.New_products_furniture = random.randint(300 , 600)
    self.Products_furniture += self.New_products_furniture
    print(f"Доставлено на склад продуктів:{self.Products_furniture} кг.")
    
   # Метод на докупівлю Food
  def last_products_Food(self , Number_of_clients_for_food , weight_food ):
    All_products_food = sum(weight_food)
    
    if All_products_food > self.Products_food:
      Number_of_served_clients_food = 0
      for y in range(Number_of_clients_for_food):
       self.Last_products = self.Products_food - weight_food[y]
       if self.Last_products_food > 0:
         Number_of_served_clients_food +=1
       else:
         Number_of_served_clients_food += 0
         
      self.Products_not_enough_food = "Маємо товар для клієнтів: " + str(Number_of_served_clients_food)
      print(self.Products_not_enough_food)
      print("Потрібно докупити товару: " , All_products_food - self.Products_food)
      self.Reqired_Money_food = (All_products_food - self.Products_food)*15
      print("Витрачено грошей: ",self.Reqired_Money_food)
      
    else:
      print("Товару достатньо")
    return  self.Reqired_Money_food

  # Метод на докупівлю Materials
  def last_products_Materials(self , Number_of_clients_for_materials , weight_materials ):
    All_products_materials = sum(weight_materials)
    if All_products_materials > self.Products_materials:
      Number_of_served_clients_materials = 0
      for y in range(Number_of_clients_materials):
       self.Last_products_materials = self.Products_materials - weight_materials[y]
       if self.Last_products_materials > 0:
         Number_of_served_clients_materials +=1
       else:
         Number_of_served_clients_materials += 0
      self.Products_not_enough_materials = "Маємо товар для клієнтів: " + str(Number_of_served_clients_materials)
      print(self.Products_not_enough_materials)
      print("Потрібно докупити товару: " , All_products_materials - self.Products_materials)
      self.Reqired_Money_materials = (All_products_materials - self.Products_materials)*15
      print("Витрачено грошей: ",self.Reqired_Money_materials)
      
    else:
      print("Товару достатньо")
    return  self.Reqired_Money_materials



  # Метод на докупівлю Furniture
  def last_products_Furniture(self , Number_of_clients_furniture , weight_furniture ):
    All_products_furniture = sum(weight_furniture)
    if All_products_furniture > self.Products_furniture:
      Number_of_served_clients_furniture = 0
      for y in range(Number_of_clients_furniture):
       self.Last_products_furniture = self.Products_furniture - weight_furniture[y]
       if self.Last_products_furniture > 0:
         Number_of_served_clients_furniture +=1
       else:
         Number_of_served_clients_furniture += 0
      self.Products_not_enough_furniture = "Маємо товар для клієнтів: " + str(Number_of_served_clients_furniture)
      print(self.Products_not_enough_furniture)
      print("Потрібно докупити товару: " , All_products_furniture - self.Products_furniture)
      self.Reqired_Money_furniture = (All_products_furniture - self.Products_furniture)*15
      print("Витрачено грошей: ",self.Reqired_Money_furniture)
      
    else:
      print("Товару достатньо")
    return  self.Reqired_Money_furniture

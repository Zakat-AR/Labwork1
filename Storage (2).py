import random
#
class Storage :
  #Метод на заповнення складу Food 
  def new_products_Food(self , Supply_change ):
    self.New_products_food = 0
    self.Products_food = 0
    self.Reqired_Money = 0
    self.New_products_food = random.randint(300 , 600)
    self.Products_food += self.New_products_food + Supply_change
    print(f"Доставлено на склад продуктів:{self.Products_food} кг.")

   #Метод на заповнення складу Materials
  def new_products_Materials(self , Supply_change ):
    self.New_products_materials = 0
    self.Products_materials = 0
    self.Reqired_Money = 0
    self.New_products_materials = random.randint(300 , 600)
    self.Products_materials += self.New_products_materials + Supply_change
    print(f"Доставлено на склад продуктів:{self.Products_materials} кг.")
    
   #Метод на заповнення складу Furniture
  def new_products_Furniture(self , Supply_change ):
    self.New_products_furniture = 0
    self.Products_furniture = 0
    self.Reqired_Money = 0
    self.New_products_furniture = random.randint(300 , 600)
    self.Products_furniture += self.New_products_furniture + Supply_change
    print(f"Доставлено на склад продуктів:{self.Products_furniture} кг.")
    
   # Метод на докупівлю Food
  def last_products_Food(self , Number_of_clients_for_food , clients_food):
    All_products_food = 0
    
    for y in range(Number_of_clients_for_food ):
      Client = clients_food[y]
      Product_weight = Client.product_weight
      All_products_food += Product_weight
      
    
    if All_products_food > self.Products_food:
      Number_of_served_clients_food = 0
      
      for y in range(Number_of_clients_for_food):
        
        Client = clients_food[y]
        Product_weight = Client.product_weight
        
        self.Last_products_food = self.Products_food - Product_weight
        if self.Last_products_food > 0:
          Number_of_served_clients_food +=1
        else:
          Number_of_served_clients_food += 0
         
      print("Маємо товар для клієнтів: " + str(Number_of_served_clients_food))
      print("Потрібно докупити товару: " , All_products_food - self.Products_food)
      self.Reqired_Money_food = (All_products_food - self.Products_food)*15
      print("Витрачено грошей: ",self.Reqired_Money_food)
      
      self.Products_food = 0
      
    else:
      print("Товару достатньо")
      self.Reqired_Money_food = 0
    return  self.Reqired_Money_food

  # Метод на докупівлю Materials
  def last_products_Materials(self , Number_of_clients_for_materials , clients_materials ):
    All_products_materials_weight = 0
    
    for y in range(Number_of_clients_for_materials):
      Client = clients_materials[y]
      Product_weight = Client.product_weight
      All_products_materials_weight += Product_weight
      
    
    if All_products_materials_weight > self.Products_materials:
      Number_of_served_clients_materials = 0
      
      for y in range(Number_of_clients_for_materials):
        
        Client = clients_materials[y]
        Product_weight = Client.product_weight
        
        self.Last_products_materials = self.Products_materials - Product_weight
        if self.Last_products_materials > 0:
          Number_of_served_clients_materials +=1
        else:
          Number_of_served_clients_materials += 0
         
      print("Маємо товар для клієнтів: " + str(Number_of_served_clients_materials))
      print("Потрібно докупити товару: " , All_products_materials_weight - self.Products_materials)
      self.Reqired_Money_materials = (All_products_materials_weight - self.Products_materials)*15
      print("Витрачено грошей: ",self.Reqired_Money_materials)
      
      self.Products_materials = 0
      
    else:
      
      print("Товару достатньо")
      self.Reqired_Money_materials = 0
      
    return  self.Reqired_Money_materials



  # Метод на докупівлю Furniture
  def last_products_Furniture(self , Number_of_clients_furniture , clients_furniture ):
    All_products_furniture_weight = 0
    
    for y in range(Number_of_clients_furniture):
      Client = clients_furniture[y]
      Product_weight = Client.product_weight
      All_products_furniture_weight += Product_weight
      
    
    if All_products_furniture_weight > self.Products_furniture:
      Number_of_served_clients_furniture = 0
      
      for y in range(Number_of_clients_furniture):
        
        Client = clients_furniture[y]
        Product_weight = Client.product_weight
        
        self.Last_products_furniture = self.Products_furniture - Product_weight
        if self.Last_products_furniture > 0:
          Number_of_served_clients_furniture +=1
        else:
          Number_of_served_clients_furniture += 0
         
      print("Маємо товар для клієнтів: " + str(Number_of_served_clients_furniture))
      print("Потрібно докупити товару: " , All_products_furniture_weight - self.Products_furniture)
      self.Reqired_Money_furniture = (All_products_furniture_weight - self.Products_furniture)*15
      print("Витрачено грошей: ",self.Reqired_Money_furniture)
      
      self.Products_furniture = 0
      
    else:
      
      print("Товару достатньо")
      self.Reqired_Money_furniture = 0
      
    return  self.Reqired_Money_furniture

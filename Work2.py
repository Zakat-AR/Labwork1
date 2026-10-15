import random 
import Boss
import Worker:
  
class Client :
  def __init__(self , products_weight , distance ):
    self.products_weight = products_weight
    self.distance = distance
    self.Money = self.products_weight* 25 + self.distance * 2
    self.M = 0

  def cl_reaction(self , time):
    self.time = time
    self.timet = self.time <= 2.5
    if self.timet :
      self.D = "Клієнт заплатив.Доставка відбулась вчасно. "
      self.M += self.Money
    else:
      self.D = "Клієнт не заплатив.Доставка не відбулась вчасно."
      self.M += 0
    return self.D

class storage :
  def __init__(self  ):
    self.AA = 0
    self.count = 0
    self.count13 = 0
    self.WW = 0
    
  def products(self):
    self.AA = random.randint(400, 1200)
    print("Привезено сьогодні товару",self.AA)
    self.count += self.AA
    
  def costs(self,count11):
    self.WW = -weight1 - weight2 - weight3
    self.count += self.WW
    if self.count > 0:
      print("Наявий товар: ",self.count)
      print("Необхідний товар: ", -1*self.WW)
      print("Товару вистачає")
    elif  self.count < 0 :
      self.count13 = (self.count - weight1 - weight2 - weight3) * 30
      print("Наявий товар: ",self.count)
      print("Необхідний товар: ", -1*self.WW)
      print("Товару не вистачає,витрачено грошей на докупівлю: " , self.count13)
      count11 += self.count13
      self.count = 0
      print("Наявий товар: ",self.count)
      return self.count13
      
class transport:
  def time_transport (self , distance1 ,speed1 ):
    time_transport = distance1 /speed1
    return time_transport

      
A = int(input("Введіть кількість днів симуляції: " ))
A1 = ["Макс" ,"Степан","Олександр","Федір"]
S1 = ["Шахи","Кулінарія","Програмування"]
D = random.choice(A1)
F = random.randint(1 , 10)
C = random.choice(S1)
Boos1 = Boss(D, F ,C)
Boos1.show_info()
Y = ["Олексій","Антон","Федір","Микита","Максим","Олександр","Дмитро","Григорій"]
worker1 = Worker(random.choice(Y))
worker2 = Worker(random.choice(Y))
worker3 = Worker(random.choice(Y))
print("Робітник: ",worker1.Name,"приступає до роботи")
print("Робітник: ",worker2.Name,"приступає до роботи")
print("Робітник: ",worker3.Name,"приступає до роботи")
Clients = []
Max_weight1 = 25
Max_weight2 = 20
Max_weight3 = 30
#car1 = transport()
#car2 = transport()
#car3 = transport()
M = 0
count12 = 0
Boos1.Ex(F , S1)
Sklad = storage()
for E in range(A):
  count11 = 0
  print("="*35)
  print(f"День роботи: {E +1}")
  print("="*35)
  Boos1.rand()
  time = 2.5
  Speed1 = random.randint(1,4)
  car1 = transport()
  clients_number = random.randint(1,10)
  weight = []
  distance = []
  time_list = []
  time_list.clear()
  reactions = []
  for t in range(clients_number):
    cl_weight = random.randint(1,150)
    cl_distance = random.randint(1,10)
    client = Client(cl_weight , cl_distance)
    weight.append(cl_weight)
    distance.append(cl_distance)
    N_work = clients_number // 3 
    if N_work < 1:
      Number_of_deliveries_1 = sum(weight[0: clients_number // 3])
      Number_of_deliveries_2 = 0
      Number_of_deliveries_3 = 0
      for Dl1 in range (clients_num):
        car1 = transport()
        DD = car1.time_transport(cl_distance , Speed1)
        time_list.append(DD)
    elif N_work >= 1 and N_work <2 :
      Number_of_deliveries_1 = sum(weight[0:3])
      Number_of_deliveries_2 = sum(weight[3: clients_number // 3])
      Number_of_deliveries_3 = 0
      for Dl1 in range (clients_number ):
        car1 = transport()
        DD = car1.time_transport(cl_distance , Speed1)
        time_list.append(DD)
    elif N_work >= 2 and N_work < 3:
      Number_of_deliveries_3 = sum(weight[6:clients_number // 3])
      Number_of_deliveries_2 = sum(weight[3:6])
      Number_of_deliveries_1 = sum(weight[:3])
      #num3 = clients_num % 3
      for Dl1 in range (clients_number):
        car1 = transport()
        DD = car1.time_transport(cl_distance , Speed1)
        time_list.append(DD)
    elif N_work >= 3 :
      ost = 9 + clients_number // 3
      Number_of_deliveries_3= sum(weight[6:ew])
      Number_of_deliveries_2 = sum(weight[3:6])
      Number_of_deliveries_1 = sum(weight[:3])
      for Dl1 in range (clients_num):
        car1 = transport()
        DD = car1.time_transport(cl_distance , Speed1)
        time_list.append(DD)
    client.cl_reaction(time_list[t])
    count11 += client.M
    reactions.append(client.cl_reaction(time_list[t]))
    Clients.append(client)
  
  N_work = clients_number // 3 
  num_of_normal_deliveries_1 = random.randint(1,9)
  num_of_normal_deliveries_2 = random.randint(1,9)
  num_of_normal_deliveries_3 = random.randint(1,9)
  

  if N_work < 1:
    Number_of_deliveries_1 = clients_number % 3
    Number_of_deliveries_1 = sum(weight[0: clients_number% 3])
    Number_of_deliveries_2 = 0
    Number_of_deliveries_3 = 0
    Number_of_deliveries_2 = 0
    Number_of_deliveries_3 = 0
  if N_work >= 1 and N_work <2 :
    Number_of_deliveries_1 = 3
    Number_of_deliveries_2 = clients_number % 3
    Number_of_deliveries_3 = 0 
    products_weight_1 = sum(weight[0:3])
    products_weight_2 = sum(weight[3: 3+ clients_number % 3])
    products_weight_3 = 0
  elif N_work >= 2 and N_work < 3:
    Number_of_deliveries_1 = 3
    Number_of_deliveries_2 = 3
    products_weight_3 = sum(weight[6: 6 + clients_number % 3])
    products_weight_2 = sum(weight[3:6])
    products_weight_1 = sum(weight[:3])
    Number_of_deliveries_3 = clients_number % 3
  elif N_work >= 3 :
     Number_of_deliveries_1 = 3
     Number_of_deliveries_2 = 3
     Number_of_deliveries_3 = 3 + clients_number % 3
     ost = 9 + clients_num % 3
     products_weight_3 = sum(weight[6:ost])
     products_weight_2 = sum(weight[3:6])
     products_weight_1 = sum(weight[:3])
  print("Обрахунки проведені")
  print(f"Сьогодні {worker1.Name} має точок доставки: ",Number_of_deliveries_1 , f"Вага вантажу: {products_weight_1} кг., кількість поїздок: {products_weight_1 // Max_weight1}")
  print(f"Сьогодні {worker2.Name} має точок доставки: ",Number_of_deliveries_2, f"Вага вантажу: {products_weight_2} кг., кількість поїздок: {products_weight_2 // Max_weight2}")
  print(f"Сьогодні {worker3.Name} має точок доставки: ",Number_of_deliveries_3, f"Вага вантажу: {products_weight_3} кг., кількість поїздок: {products_weight_3 // Max_weight3}")  
  Number_of_deliveries_1 = worker_1.work(Max_weight1 , products_weight_1)
  Number_of_deliveries_2 = worker2.work(Max_weight2 , products_weight_2)
  Number_of_deliveries_3 = worker3.work(Max_weight3 , products_weight_3)
  Worker_phrase_1 = worker1.work2(Number_of_deliveries_1, num_of_normal_deliveries_1 , Number_of_deliveries_1)
  Worker_phrase_2 = worker2.work2(Number_of_deliveries_2 , num_of_normal_deliveries_2 , Number_of_deliveries_2)
  Worker_phrase_3 = worker3.work2(Number_of_deliveries_3 , num_of_normal_deliveries_3 , Number_of_deliveries_3) 
  print(f"{worker1.Name} {Worker_phrase_1}")
  print(f"{worker2.Name} {Worker_phrase_2}")
  print(f"{worker3.Name} {Worker_phrase_3}")
  for g in range(clients_number):
    print(reactions[g])
  if count11 >0:
    count11 += 100*Boos1.Exx
  print(clients_number)
  Sklad.products()
  #Sklad.costs(count11)
  ASD = Sklad.costs(count11)
  if ASD == None:
    ASD = 0
  count11 += ASD
  print("Заробіток за день: ",count11)
  count12 += count11
  print("Загальний заробіток: ",count12)
  

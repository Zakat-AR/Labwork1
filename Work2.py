import random 
class Boss:
  def __init__(self , Name , Worktime , Hobby):
    self.Name = Name
    self.Worktime = Worktime
    self.Hobby = Hobby
  def show_info(self ):
    print("Ім'я: ", self.Name )
    print("Стаж роботи: " , self.Worktime)
    print("Хобі боса: " , self.Hobby)

def Ex (self , Worktime , Hobby):
  if Hobby == "Шахи" :
    self.A = 5
  elif Hobby == "Кулінарія" :
    self.A = -2
  elif Hobby == "Програмування" :  
    self.A = 0
    if Worktime <= 1 :
      self.B = -4
  elif Worktime <= 5:
    self.B = 5
  elif Worktime >= 5 :
    self.B = 8
  self.Ef = self.A + self.B
def rand(self ):
  self.phrase = random.choice("У шефа гарний настрій!","Сьогодні шеф спокійний. ","У шефа поганий настрій.","Шеф втомився від роботи.","Шеф втік з роботи.")
  if self.phrase == "У шефа гарний настрій":
    self.F = 3
  if self.phrase == "Сьогодні шеф спокійний":
    self.F = 1
  if self.phrase == "У шефа поганий настрій":
    self.F = -1
  if self.phrase == "Шеф втомився від роботи":
    self.F = -3
  if self.phrase == "Шеф втік з роботи":
    self.F = -10  
  self.Exx = (self.Ef + self.F)//5
  if self.Exx <= 0:
    self.Exx *= -1
    self.Exx = 1 / self.Exx
  return self.Exx
pass 

class Worker:
  def __init__(self,  Name ):
    self.Name = Name
    
    
  def work(self, Max_weight, weight):
    self.weight = weight
    self.Max_weight = Max_weight
    self.S = self.Max_weight // self.weight 
    return self.S
    
  def work2(self, num, Power):
    self.num = num
    self.Power = Power
    self.PP = (self.num + self.S) <= self.Power // 2
    self.PPP = (self.num + self.S) >= self.Power // 2 and self.num <= self.Power * 1.5
    self.PPPP = (self.num + self.S) >= self.Power * 1.5
    if self.PP:
      self.phrase = "Готовий працювати"
    if self.PPP:
      self.phrase = "Працює неохоче"
    if self.PPPP:
      self.prase = "Шукає привід звільнитись"
    return self.prase  
  pass


class Client :
  def __init__(self , cus_weight , distance ):
    self.cus_weigth = cus_weigth
    self.distance = distance

  def cl_reaction(self , time):
    self.time = time
    if self.time :
      self.D = "Клієнт заплатив. "
      self.M = 100
    else:
      self.D = "Клієнт не заплатив."
      self.M = 0
    return self.D , self.M

class storage :
  def __init__(self ,product ):
    self.product = product 

  def pos (self , num ):
    count = 0
    for x in range (num):
      count += list[x].cus_weight
    if count > self.product:
      count1 = 0
      for y in range(num):
       self.R = product - list[y].cus_weight
       if self.R:
         count1c +=1
       else:
         count1 += 0
      self.DD = "Можемо надати товар: " + str(count1) + "для клієнтів"  
    return self.DD  

  class transport:
    def __init__(self, speed):
       self.speed = speed
    def time_transport (self , distance):
      self.time_transport = distance / self.speed
      return self.time_transport

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
worker1.Max_weight = 25
worker2.Max_weight = 20
worker3.Max_weight = 30
for E in range(A):
  time = 15
  S1 = random.randint(1,4)
  S2 = random.randint(1,4)
  S3 = random.randint(1,4)
  car1 = transport(S1)
  car2 = transport(S2)
  car3 = transport(S3)
  clients_num = random.randint(1,10)
  weight = []
  distance = []
  for t in range(clients_num):
    cl_weight = random.randint(1,100)
    cl_distance = random.randint(1,10)
    client = Client(cl_weight , cl_distance)
    weight.append(cl_weight)
    distance.append(cl_distance)
    Clients.append(client)
  N_mork = clients_num // 3 
  if N_mork >0:
    worker1.num = N_work
    if N_mork >1 and N_mork <3:
      worker2.num = N_work + clients_num % 3 
    if N_mork >1: 
      worker2.num = N_work
      if N_mork == 3:
        worker3.num = N_work + clients_num % 3 
   print(f"Сьогодні {worker1.Name} має точок доставки: ",worker1.num)
   print(f"Сьогодні {worker1.Name} має точок доставки: ",worker2.num)
   print(f"Сьогодні {worker1.Name} має точок доставки: ",worker3.num)
  
    
  
  

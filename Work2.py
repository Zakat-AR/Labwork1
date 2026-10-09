import random 
class Boss:
  def __init__(self , Name , Worktime , Hobby):
    self.A = 0
    self.F = 0
    self.B = 0
    self.Ef = 0
    self.Exx = 0
    self.Name = Name
    self.Worktime = Worktime
    self.Hobby = Hobby
  def show_info(self ):
    print("Ім'я: ", self.Name )
    print("Стаж роботи: " , self.Worktime)
    print("Хобі боса: " , self.Hobby)

  def Ex(self , Worktime , Hobby):
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
      return self.Ef
  def rand(self ):
    Event = ["У шефа гарний настрій!","Сьогодні шеф спокійний. ","У шефа поганий настрій.","Шеф втомився від роботи.","Шеф втік з роботи."]
    self.phrase = random.choice(Event)
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
    return self.Exx
pass 

class Worker:
  def __init__(self,  Name ):
    self.Name = Name
    self.S = 0
    self.Max_weight = 0
    self.weight = 0
    self.PP = 0
    self.PPP = 0
    self.PPPP = 0
    
  def work(self, Max_weight, weight):
    self.weight = weight
    self.Max_weight = Max_weight
    self.S = self.weight // self.Max_weight  
    return self.S
    
  def work2(self, num, Power , S):
    self.S = S
    self.num = num
    self.Power = Power
    self.PP = (self.num + self.S) <= self.Power // 2
    self.PPP = (self.num + self.S) >= self.Power // 2 and self.num <= self.Power * 1.5
    self.PPPP = (self.num + self.S) >= self.Power * 1.5
    if self.PP:
      self.phrase = "Готовий працювати"
      return  self.phrase
    elif self.PPP:
     self.phrase = "Працює неохоче"
     return self.phrase
    elif self.PPPP:
      self.prase = "Шукає привід звільнитись"
      return  self.prase
  pass


class Client :
  def __init__(self , cus_weight , distance ):
    self.cus_weight = cus_weight
    self.distance = distance
    self.Money = self.cus_weight * 25 + self.distance * 2
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
  clients_num = random.randint(1,10)
  weight = []
  distance = []
  time_list = []
  time_list.clear()
  reactions = []
  for t in range(clients_num):
    cl_weight = random.randint(1,150)
    cl_distance = random.randint(1,10)
    client = Client(cl_weight , cl_distance)
    weight.append(cl_weight)
    distance.append(cl_distance)
    N_work = clients_num // 3 
    if N_work < 1:
      weight1 = sum(weight[0: clients_num // 3])
      weight2 = 0
      weight3 = 0
      for Dl1 in range (clients_num):
        car1 = transport()
        DD = car1.time_transport(cl_distance , Speed1)
        time_list.append(DD)
    elif N_work >= 1 and N_work <2 :
      weight1 = sum(weight[0:3])
      weight2 = sum(weight[3: clients_num // 3])
      weight3 = 0
      for Dl1 in range (clients_num ):
        car1 = transport()
        DD = car1.time_transport(cl_distance , Speed1)
        time_list.append(DD)
    elif N_work >= 2 and N_work < 3:
      weight3 = sum(weight[6:clients_num // 3])
      weight2 = sum(weight[3:6])
      weight1 = sum(weight[:3])
      #num3 = clients_num % 3
      for Dl1 in range (clients_num):
        car1 = transport()
        DD = car1.time_transport(cl_distance , Speed1)
        time_list.append(DD)
    elif N_work >= 3 :
      ew = 9 + clients_num // 3
      weight3 = sum(weight[6:ew])
      weight2 = sum(weight[3:6])
      weight1 = sum(weight[:3])
      for Dl1 in range (clients_num):
        car1 = transport()
        DD = car1.time_transport(cl_distance , Speed1)
        time_list.append(DD)
    client.cl_reaction(time_list[t])
    count11 += client.M
    reactions.append(client.cl_reaction(time_list[t]))
    Clients.append(client)
  
  N_work = clients_num // 3 
  P1 = random.randint(1,9)
  P2 = random.randint(1,9)
  P3 = random.randint(1,9)
  

  if N_work < 1:
    num1 = clients_num % 3
    weight1 = sum(weight[0: clients_num % 3])
    weight2 = 0
    weight3 = 0
    num2 = 0
    num3 = 0
  if N_work >= 1 and N_work <2 :
    num1 = 3
    num2 = clients_num % 3
    num3 = 0 
    weight1 = sum(weight[0:3])
    weight2 = sum(weight[3: 3+ clients_num % 3])
    weight3 = 0
  if N_work >= 2 and N_work < 3:
    num1 = 3
    num2 = 3
    weight3 = sum(weight[6: 6 + clients_num % 3])
    weight2 = sum(weight[3:6])
    weight1 = sum(weight[:3])
    num3 = clients_num % 3
  if N_work >= 3 :
     num1 = 3
     num2 = 3
     num3 = 3 + clients_num % 3
     ew = 9 + clients_num % 3
     weight3 = sum(weight[6:ew])
     weight2 = sum(weight[3:6])
     weight1 = sum(weight[:3])
  print("Обрахунки проведені")
  print(f"Сьогодні {worker1.Name} має точок доставки: ",num1 , f"Вага вантажу: {weight1} кг., кількість поїздок: {weight1 // Max_weight1}")
  print(f"Сьогодні {worker2.Name} має точок доставки: ",num2, f"Вага вантажу: {weight2} кг., кількість поїздок: {weight2 // Max_weight2}")
  print(f"Сьогодні {worker3.Name} має точок доставки: ",num3, f"Вага вантажу: {weight3} кг., кількість поїздок: {weight3 // Max_weight3}")  
  SS1 = worker1.work(Max_weight1 , weight1)
  SS2 = worker2.work(Max_weight2 , weight2)
  SS3 = worker3.work(Max_weight3 , weight3)
  Ph1 = worker1.work2(num1, P1 , SS1)
  Ph2 = worker2.work2(num2 , P2 , SS2)
  Ph3 = worker3.work2(num3 , P3 , SS2) 
  print(f"{worker1.Name} {Ph1}")
  print(f"{worker2.Name} {Ph2}")
  print(f"{worker3.Name} {Ph3}")
  for g in range(clients_num):
    print(reactions[g])
  if count11 >0:
    count11 += 100*Boos1.Exx
  print(clients_num)
  Sklad.products()
  #Sklad.costs(count11)
  ASD = Sklad.costs(count11)
  if ASD == None:
    ASD = 0
  count11 += ASD
  print("Заробіток за день: ",count11)
  count12 += count11
  print("Загальний заробіток: ",count12)
  

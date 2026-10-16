#Клас робітник. Тут вони вже ремонтники дронів 
class Worker:
  def __init__(self,  Name , salary):
    self.salary = salary
    self.Name = Name
    self.Deliveries = 0
    self.All_Deliveries = 0
    self.One_delivery_weight = 0
    self.All_weight = 0
    self.Points_for_worker_phrase1 = 0
    self.Points_for_worker_phrase2 = 0
    self.Points_for_worker_phrase3 = 0

   #Метод , щоб бачити наявних робітників.
  def show_information(self,):
    print("Робітник: ",self.Name)
    print("Заробітня плата: ",self.salary)
    
    #Метод на ремонт дронів , та ставленння робітників до різної кількості роботи
  def All_Drons_Repaired(self, Number_of_drons_for_worker, Normal_number_of_drons ):
    self.Number_of_drons_for_worker = Number_of_drons_for_worker
    self.Normal_number_of_drons = Normal_number_of_drons
    self.Points_for_worker_phrase1 = self.Number_of_drons_for_worker <= self.Normal_number_of_drons // 2
    self.Points_for_worker_phrase2 = self.Number_of_drons_for_worker >= self.Normal_number_of_drons // 2 and self.Number_of_drons_for_worker <= self.Normal_number_of_drons * 1.5
    self.Points_for_worker_phrase3 = self.Number_of_drons_for_worker >= self.Normal_number_of_drons * 1.5
    
    if self.Points_for_worker_phrase1:
      self.phrase = "Готовий працювати"
      return  self.phrase
    elif self.Points_for_worker_phrase2:
     self.phrase = "Працює неохоче"
     return self.phrase
    elif self.Points_for_worker_phrase3:
      self.prase = "Шукає привід звільнитись"
      return  self.prase
    
   #Метод на звільнення робітника
  def Refuse_work(self , Lost_workers ):
    Chance = random.randint(1,100)
    if Chance % 33 == 0:
      Lost_workers +=1
      
  pass


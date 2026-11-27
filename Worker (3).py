from Logs import logger_workers
#Клас робітник. Тут вони вже ремонтники дронів 
import random
import Logs
class Worker:
  def __init__(self,  name_1 , salary):
    self.salary = salary
    self.name_1 = name_1
    self.deliveries_1 = 0
    self.all_deliveries_1 = 0
    self.one_delivery_weight_1 = 0
    self.all_weight_1 = 0
    self.points_for_worker_phrase1_1 = 0
    self.points_for_worker_phrase2_1 = 0
    self.points_for_worker_phrase3_1 = 0


  def characteristics(self):
    workers_number_1 = random.randint(1,5)
    for worker_number in range(workers_number_1):
      worker_name_list_1 = ["Олексій","Антон","Федір","Микита","Максим","Олександр","Дмитро","Григорій" , "Афанасій" , "Вольтман"]
      salary_list = [1500 , 2000 , 2500 , 3000  ]
      worker_salary_1 = int(random.choice(salary_list))
      Worker.name = random.choice(worker_name_list_1)
      worker__1 = Worker(Worker.name ,worker_salary_1 )
      print("Робітник: ",Worker.name,"приступає до роботи")
      workers_list_1.append(Worker)


    
   #Метод , щоб бачити наявних робітників.
  def show_information(self,):
    logger_workers.info(f"Робітник:  {self.name_1}")
    logger_workers.info(f"Заробітня плата:  {self.salary}")

    
    
    #Метод на ремонт дронів , та ставленння робітників до різної кількості роботи
  def All_Drons_Repaired(self, number_of_drons_for_worker_1 ):
    self.number_of_drons_for_worker_1 = number_of_drons_for_worker_1
    normal_number_of_drons_1 = random.randint(1,10)
    self.points_for_worker_phrase1_1 = self.number_of_drons_for_worker_1 <= normal_number_of_drons_1 // 2
    self.points_for_worker_phrase2_1 = self.number_of_drons_for_worker_1 >= normal_number_of_drons_1 // 2 and self.number_of_drons_for_worker_1 <= normal_number_of_drons_1 * 1.5
    self.points_for_worker_phrase3_1 = self.number_of_drons_for_worker_1 >= normal_number_of_drons_1 * 1.5
    
    if self.points_for_worker_phrase1_1:
      logger_workers.info(f"{self.name_1} Готовий працювати")
      
    
    elif self.points_for_worker_phrase2_1:
     logger_workers.info(f"{self.name_1} Працює неохоче")
     
    
    elif self.points_for_worker_phrase3_1:
      logger_workers.info(f"{self.name_1} Шукає привід звільнитись")
    
    
   #Метод на звільнення робітника
  def Refuse_work(self , lost_workers_1):
    
    chance_1 = random.randint(1,10)
    
    if chance_1 % 3 == 0:
      lost_workers_1 += 1
    else:
      lost_workers_1 += 0
      

    return lost_workers_1
      
  pass


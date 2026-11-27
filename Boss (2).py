import random
from Worker import Worker
Workers_list1 = []
class Boss:
  def __init__(self , name_1 , worktime_1 , hobby_1):
    self.name_1 = name_1
    self.worktime_1 = worktime_1
    self.hobby_1 = hobby_1 
    self.hobby_experience_1 = 0
    self.work_time_experience_1 = 0
    self.work_hobby_experience_1 = 0
    self.resulting_bonus_1 = 0

  def info(self ):
    print("Ім'я: ", self.name_1 )
    print("Стаж роботи: " , self.worktime_1)
    print("Хобі боса: " , self.hobby_1)

  def Experience(self):
    if self.hobby_1 == "Шахи" :
      self.hobby_experience_1 = 8
    elif self.hobby_1 == "Кулінарія" :
      self.hobby_experience_1 = -5
    elif self.hobby_1 == "Програмування" :
      self.hobby_experience_1 = 0
      
    if self.worktime_1 <= 1 :
      self.work_time_experience_1 = -7
    elif self.worktime_1 < 5:
      self.work_time_experience_1 = 8
    elif self.worktime_1 >= 5 :
      self.work_time_experience_1 = 11
    self.work_hobby_experience_1 = self.hobby_experience_1 + self.work_time_experience_1
    return self.work_hobby_experience_1
  
  def random_mood(self):
    self.mood_bonus_1 = 1
    event_1 = ["У шефа гарний настрій!","Сьогодні шеф спокійний. ","У шефа поганий настрій.","Шеф втомився від роботи.","Шеф втік з роботи."]
    self.phrase = random.choice(event_1)
    
    if self.phrase == "У шефа гарний настрій!" :
      self.mood_bonus_1 = 6
      print(self.phrase)
    elif self.phrase == "Сьогодні шеф спокійний. " :
      self.mood_bonus_1 = 4
      print(self.phrase)
    elif self.phrase == "У шефа поганий настрій." :
      self.mood_bonus_1 = -4
      print(self.phrase)
    elif self.phrase == "Шеф втомився від роботи." :
      self.mood_bonus_1 = -6
      print(self.phrase)
    elif self.phrase == "Шеф втік з роботи." :
      self.mood_bonus_1 = -9
      print(self.phrase)
      
    self.resulting_bonus_1_1 = (self.work_hobby_experience_1 + self.mood_bonus_1)
    self.resulting_bonus_2_1 = self.resulting_bonus_1_1 / 2
    return self.resulting_bonus_2_1

  def Deal(self, working_day_1):
    print("Ведуться переговори компаній")
    companies_1 = ["ARTEC ROBOTICS","ZERO CAT","ALFA BETA","SAMSUNG","","TESLA","XORION"]
    possible_results_1 = ["Укладена домовленість","Не вдалось знайти консенсус","Отриманий вигідний контракт","Непередбачувані обставини зашкодили переговорам","Ваша компанія отримала нового ворога"]
    if working_day_1 % 10 == 0:
      another_company_1 = random.choice(companies_1)
      dialoge_result_1 = random.choice(possible_results_1)
      if dialoge_result_1 == "Укладена домовленість":
        supply_change_1 = 100
      elif dialoge_result_1 == "Не вдалось знайти консенсус":
        supply_change_1 = 0
      elif dialoge_result_1 == "Отриманий вигідний контракт":
        supply_change_1 = 150
      elif dialoge_result_1 == "Непередбачувані обставини зашкодили переговорам":
        supply_change_1 = 0
      elif dialoge_result_1 == "Ваша компанія отримала нового ворога":
        supply_change_1 = -100
      print(f"Переговори з: {another_company_1} були завершені. Результат: {dialoge_result_1}  на поставки змінить так: {supply_change_1}")
      return supply_change_1

  def Find_worker(self , lost_workers_1):
    
    for worker_number in range(lost_workers_1):
      
      worker_name_list_1 = ["Олексій","Антон","Федір","Микита","Максим","Олександр","Дмитро","Григорій" , "Афанасій" , "Вольтман"]
      salary_list_1 = [1500 , 2000 , 2500 , 3000  ]
      worker_salary_1 = int(random.choice(salary_list_1))
      worker_name_1 = random.choice(worker_name_list_1)
      worker = Worker(worker_name_1 ,worker_salary_1 )
      print("Робітник: ",worker.name_1,"приступає до роботи")
      Workers_list1.append(worker)

import random
class Boss:
  def __init__(self , Name , Worktime , Hobby):
    self.Hobby_experience = 0
    self.Work_time_experience = 0
    self.Work_hobby_experience = 0
    self.Resulting_bonus = 0
    self.Name = Name
    self.Worktime = Worktime
    self.Hobby = Hobby

  def show_info(self ):
    print("Ім'я: ", self.Name )
    print("Стаж роботи: " , self.Worktime)
    print("Хобі боса: " , self.Hobby)

  def Experience(self):
    if self.Hobby == "Шахи" :
      self.Hobby_experience = 8
    elif self.Hobby == "Кулінарія" :
      self.Hobby_experience = -5
    elif self.Hobby == "Програмування" :
      self.Hobby_experience = 0
      
    if self.Worktime <= 1 :
      self.Work_time_experience = -7
    elif self.Worktime < 5:
      self.Work_time_experience = 8
    elif self.Worktime >= 5 :
      self.Work_time_experience = 11
    self.Work_hobby_experience = self.Hobby_experience + self.Work_time_experience
    return self.Work_hobby_experience
  
  def random_mood(self):
    self.Mood_bonus = 1
    Event = ["У шефа гарний настрій!","Сьогодні шеф спокійний. ","У шефа поганий настрій.","Шеф втомився від роботи.","Шеф втік з роботи."]
    self.phrase = random.choice(Event)
    
    if self.phrase == "У шефа гарний настрій!" :
      self.Mood_bonus = 6
      print(self.phrase)
    elif self.phrase == "Сьогодні шеф спокійний. " :
      self.Mood_bonus = 4
      print(self.phrase)
    elif self.phrase == "У шефа поганий настрій." :
      self.Mood_bonus = -4
      print(self.phrase)
    elif self.phrase == "Шеф втомився від роботи." :
      self.Mood_bonus = -6
      print(self.phrase)
    elif self.phrase == "Шеф втік з роботи." :
      self.Mood_bonus = -9
      print(self.phrase)
      
    self.Resulting_bonus_1 = (self.Work_hobby_experience + self.Mood_bonus)
    self.Resulting_bonus_2 = self.Resulting_bonus_1 / 2
    return self.Resulting_bonus_2

  def Deal(self, Working_Day):
    print("Ведуться переговори компаній")
    Companies = ["ARTEC ROBOTICS","ZERO CAT","ALFA BETA","SAMSUNG","","TESLA","XORION"]
    Possible_results = ["Укладена домовленість","Не вдалось знайти консенсус","Отриманий вигідний контракт","Непередбачувані обставини зашкодили переговорам","Ваша компанія отримала нового ворога"]
    if Working_day % 10 == 0:
      Another_company = random.choice(Companies)
      Dialoge_result = random.choice(Possible_results)
      if Dialoge_result == "Укладена домовленість":
        Supply_change = 100
      elif Dialoge_result == "Не вдалось знайти консенсус":
        Supply_change = 0
      elif Dialoge_result == "Отриманий вигідний контракт":
        Supply_change = 150
      elif Dialoge_result == "Непередбачувані обставини зашкодили переговорам":
        Supply_change = 0
      elif Dialoge_result == "Ваша компанія отримала нового ворога":
        Suply_change = -100
      print(f"Переговори з: {Another_company} були завершені. Результат: {Dialoge_result}  на поставки змінить так: {Supply_change}")
      return Supply_change

  def Find_worker(self , Lost_workers , All_money):
    
    for worker_number in range(Lost_workers):
      Worker_name_list = ["Олексій","Антон","Федір","Микита","Максим","Олександр","Дмитро","Григорій" , "Афанасій" , "Вольтман"]
      Salary_list = [1500 , 2000 , 2500 , 3000  ]
      Worker_salary = int(random.choice(Salary_list))
      Worker.Name = random.choice(Worker_name_list)
      worker = Worker(Worker.Name ,Worker_salary )
      print("Робітник: ",worker.Name,"приступає до роботи")
      Workers_list.append(worker)

      log10_All_money = 0
      log_main = 10
      while log_main < All_money:
        All_money / log_main
        log10_All_money +=1

      Start_worker_number =  len(Workers_list) 

      if  log10_All_money > Start_worker_number:
        for worker_number in range(log10_All_money - Start_worker_number ):
          Worker_name_list = ["Олексій","Антон","Федір","Микита","Максим","Олександр","Дмитро","Григорій" , "Афанасій" , "Вольтман"]
          Salary_list = [1500 , 2000 , 2500 , 3000  ]
          Worker_salary = int(random.choice(Salary_list))
          Worker.Name = random.choice(Worker_name_list)
          worker = Worker(Worker.Name ,Worker_salary )
          print("Робітник: ",worker.Name,"приступає до роботи")
          Workers_list.append(worker)

  def remove_worker(self):
    Start_worker_number_another_side = log10_All_money + 3
    if Start_worker_number_another_side < Start_worker_number:
      for last_worker in range(Start_worker_number_another_side - Start_worker_number):
        Workers_list.pop(-1)
    
     
pass 

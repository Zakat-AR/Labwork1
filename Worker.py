class Worker:
  def __init__(self,  Name ):
    self.Name = Name
    self.Number_of_deliveries = 0
    self.Max_weight = 0
    self.weight = 0
    self.Number_for_phrase_first = 0
    self.Number_for_phrase_second = 0
    self.Number_for_phrase_third = 0
    
  def work(self, Max_weight, weight):
    self.weight = weight
    self.Max_weight = Max_weight
    self.Number_of_deliveries = self.weight // self.Max_weight  
    return self.Number_of_deliveries
    
  def work2(self, num_of_required_deliveries, num_of_normal_deliveries , Number_of_deliveries):
    self.Number_of_deliveries = Number_of_deliveries
    self.num_of_required_deliveries = num_of_required_deliveries
    self.num_of_normal_deliveries = num_of_normal_deliveries
    self.Number_for_phrase_first = (self.num_of_required_deliveries + self.Number_of_deliveries) <= self.num_of_normal_deliveries // 2
    self.Number_for_phrase_second = (self.num_of_required_deliveries + self.Number_of_deliveries) >= self.num_of_normal_deliveries // 2 and self.num_of_required_deliveries <= self.num_of_normal_deliveries * 1.5
    self.Number_for_phrase_third = (self.num_of_required_deliveries + self.Number_of_deliveries) >= self.num_of_normal_deliveries * 1.5
    if self.Number_for_phrase_first:
      self.phrase = "Готовий працювати"
      return  self.phrase
    elif self.Number_for_phrase_second:
     self.phrase = "Працює неохоче"
     return self.phrase
    elif self.Number_for_phrase_third:
      self.prase = "Шукає привід звільнитись"
      return  self.prase
  pass

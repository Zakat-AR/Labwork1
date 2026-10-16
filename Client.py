class Client :
  def __init__(self , product_weight , distance_to_client ):
    self.product_weight = product_weight
    self.distance_to_client = distance_to_client
    self.Price = self.distance_to_client * 5 + self.product_weight * 25
    self.Earned_Money = 0
    self.time = 0

  def cl_reaction(self , time):
    self.time = time
    self.Delivery_possibility = self.time <= 2.5
    if self.Delivery_possibility :
      self.Result_of_Delivery = "Клієнт заплатив.Доставка відбулась вчасно. "
      self.Earned_Money += self.Price
    else:
      self.Result_of_Delivery = "Клієнт не заплатив.Доставка не відбулась вчасно."
      self.Earned_Money += 0
    return self.Result_of_Delivery
pass 

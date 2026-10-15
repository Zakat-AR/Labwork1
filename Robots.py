class Robots:
  def __init__(self, model, battery, speed):
    self.model = model
    self.battery = battery
    self.speed = speed
  def move(self, battery, distance, speed):
    work_time = distance // speed
    energy = work_time * 5
    if battery >= energy:
      battery -= energy
      print(f"Робот{self.model} проїхав{distance},за час{work_time},витратив заряду{energy}"):
  pass
class Drone(Robots):
  pass
class water_drone(Robots):
  pass
class ground(Robots):
  pass
  

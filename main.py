import random 


class character(): 
  def __init__(self):
    self.name = "Randal"
    self.health_points = 100
    self.attack_points = 110
    self.magic_points = 100
    self.stamina = 10
    
  def take_dmg(self, dmg):
    self.hp -= dmg
    if self.hp < 0:
      self.hp = 0
    return self.hp


  def get_atk(self, defence):
    atk = random.rndint(0, self.attack_points)
    print(atk)
    if atk < 1:
      atk = 0
    atk -= defence
    return atk
    
  def is_dead(self):
    if self.hp < 1 :
      return True,
    else:
      return False


pc = character("Master Cheeks")
pc_name = input()
dmg_amt = random.randint(0, pc.ap)
print("The pc took " + str(dmg_amt) + " Damage")
print("The pc has " + str(pc.take_dmg(dmg_amt)) + " health")
#print(f"the pc has {pc.take_dmg(dmg_amt)} health ")
print(pc.get_atk(20))
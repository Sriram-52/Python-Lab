class Robot:
  count = 0

  def __init__(self) -> None:
    self.name = ""
    self.id = ""
    Robot.count += 1

  def set_robot(self, name, id):
    self.name = name
    self.id = id

  def get_robot(self):
    return 'Robot name is ' + self.name + '\n' + 'Robot id is ' + str(self.id)


if __name__ == "__main__":
  robo1 = Robot()
  robo1.set_robot('Chitti', '345')
  robo2 = Robot()
  robo2.set_robot('Nila', '378')
  print(robo1.get_robot())
  print(robo2.get_robot())
  print("Robos count is", Robot.count)

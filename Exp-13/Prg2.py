class ATM:
  count = 0

  def __init__(self):
    self.location = ""
    self.id = ""
    ATM.count += 1

  def set_atm_details(self, location, id):
    self.location = location
    self.id = id

  def get_atm_details(self):
    return 'Location is ' + self.location + '\n' + "It's id is" + self.id


if __name__ == "__main__":
  atm1 = ATM()
  atm1.set_atm_details('TPG', '234')
  atm2 = ATM()
  atm2.set_atm_details('HYD', '567')
  print(atm1.get_atm_details())
  print(atm2.get_atm_details())
  print('Total atms are', ATM.count)

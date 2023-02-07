
class getstring:
  def init(self):
    self.str1 = ""
  def get_string(self):
    self.str1 = input()
  def print_string(self):
    print(self.str1.upper())
str1 = getstring()
str1.get_string()
str1.print_string()

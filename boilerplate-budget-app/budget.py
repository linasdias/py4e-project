class Category:
  def __init__(self, name):
    self.ledger = []
    self.category = name
    self.balance = 0

  def deposit(self, amount, description=None):
# without description
    if description == None:
      description = ""

    self.balance += amount
    self.ledger.append({"amount":amount,"description":description})
  
  def get_balance(self):
    return self.balance

  def transfer(self, amount, Cat):
    if self.withdraw(amount,"Transfer to "+Cat.category):
      Cat.deposit(amount,"Transfer from "+self.category)
      return True
    else:
      return False

  def check_funds(self, amount):
    if self.balance < amount:
      return False
    return True

  def withdraw(self, amount, description=None):
    if description == None:
      description = ""
    if self.check_funds(amount):
      self.balance -= amount
      self.ledger.append({"amount":-amount,"description":description})
      return True
    else:
      return False
  
  def __str__(self):
    s = "*"*((30-len(self.category))//2) + self.category
    s = s + "*"*(30-len(s)) + "\n"
    for i in self.ledger:
      s += i["description"][:23].ljust(23)+str("{:.2f}".format(i["amount"]).rjust(7))+"\n"
    s += "Total: "+str(self.balance)
    return s
  
def round_to_nearest_ten(n):
  if n < 10:
    return 0
  return round(n/10.0)*10
  
  
def create_spend_chart(categories):
  w = []
  max_len_category = 0
  s = 0

  for i in categories:
    wamt = 0
    for j in i.ledger:
      if j["amount"] < 0:
        wamt += -j["amount"]
        s+=(-j["amount"])
        
    if len(i.category)>max_len_category:
      max_len_category=len(i.category)
    w.append([i.category,wamt])
  
  for i in w:
    i.append(round_to_nearest_ten((i[1]/s)*100))
  s=""
  s+="Percentage spent by category\n"
  t=100
  while t>=0:
    
    s+=str(t).rjust(3)+"|"+" "

    for i in range(len(w)):
      if w[i][2]>=t:
        s+="o"+"  "
      else:
        s+="   "
    t-=10
    s+="\n"

  s+="    "+("-"*10)+"\n"

  loop_var=0

  for i in range(max_len_category):
    s+="     "
    for j in range(len(w)):
      if len(w[j][0])-1<loop_var:
        s+="   "
      else:
        s+=w[j][0][loop_var]+"  "
    loop_var+=1
    if i!=max_len_category-1:
      s+="\n"

  return s
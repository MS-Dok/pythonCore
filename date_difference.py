from datetime import date

def daysBetween(year,month,day):
  return date(year,month,day)-date.today()

print(abs(daysBetween(2001,1,1).days))

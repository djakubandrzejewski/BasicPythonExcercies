import datetime
y = datetime.date.today()
x = y.strftime("%A")
if(x == "Monday"):
   print("PONIEDZIAŁEK") 
elif(x == "Tuesday"):
   print("WTOREK")
elif(x == "Wednesday"):
   print("ŚRODA")
elif(x == "Thursday"):
   print("CZWARTEK")
elif(x == "Friday"):
   print("PIĄTEK")
elif(x == "Saturday"):
   print("SOBOTA")
else:
   print("NIEDZIELA")
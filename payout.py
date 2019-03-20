import time

x = input("How much is worth 1 chip($1-$1000): ")
y = input("How many chips on whole number: ")
z = input("How many chips on split: ")
c = input("How many chips on corrner: ")

#ako je x > 0
puni_zetoni = 0
cash_puni = 0

split_zetoni = 0
cash_split = 0

corrner_zetoni = 0
cash_corrner = 0

ukupno_cash = 0
ukupno_zetoni = 0

#Puni broj/Zetoni/Cash
puni_zetoni = y * 35
cash_puni = y * x * 35

#Split broj/Zetoni/Cash
split_zetoni = z * 17
cash_split = z * x * 17

#Corrner broj/ zetoni/cash
corrner_zetoni = c * 8
cash_corrner = c * x * 8

#Ukupno Puni,Split,corrner broj zetona/cash
ukupno_zetoni = puni_zetoni + split_zetoni + corrner_zetoni
ukupno_cash = cash_split + cash_puni + cash_corrner

if y == 0:
	pass
else:
	time.sleep(1)
	print("You will receive "), puni_zetoni, ("chips for whole number.")
	time.sleep(1)
	print("Payout is"), cash_puni , ("in $ for whole number.")
if z == 0:
	pass
else:
	time.sleep(1)
	print("You will receive"), split_zetoni, ("chips for split number.")
	time.sleep(1)
	print("Payout is "), cash_split, ("in $ for split number")
if c == 0:
	pass
else:
	time.sleep(1)
	print("You will receive "), corrner_zetoni, ("chips for corner number.")
	time.sleep(1)
	print("Payout is "), cash_corrner, ("in $ for corner number.")

time.sleep(2)
print("Sum in chips: "), ukupno_zetoni
print("Sum in dollars: "), ukupno_cash

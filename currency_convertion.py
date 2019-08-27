
usd = 1
mx = 0.05
yen = 0.01
yuan = 0.14
eu = 1.1



def calc(quatity, tocurrency, currency):
	print(quatity * tocurrency / currency)

calc(1000, eu, yen)


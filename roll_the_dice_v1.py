import random

roll = "да"
print("Игральные кости v.1")
while roll == "да":
	roll = str.lower(input("\nВведите: да - бросать кости, нет - выйти: "))
	if roll == "да":
		print("На костях выпало:{0} и {1}".format(random.randint(1, 6), random.randint(1, 6)))
	else:
		print("Выход")
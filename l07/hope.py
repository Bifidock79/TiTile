name = "Сааду"
number = 8 
power = 10.5

print(name,"пошел в гости за:" + str(number) + "миль с cилой: " + str(power))
print("%s пошел в гости за:%d миль с силой:%f" %(name, number, power))
print("%4.3s рошел в гости за:%4.3d миль с силой:%4.1f" %(name, number, power))

print("{0} пошел в гости за:{1} миль с милой{0}".format(name, number, power))
print("{0:*^10s} пошел в гости за:{1} миль с милой{0}".format(name, number, power))

animal = {
	"корова": "муу",
	"собака": "гав"
}

print("Собака говорит {0[собака]}, корова говорит {0[корова]}".format(animal))

import random
adv = ["я","свинья","Саид"]
word = random.choice(adv)
print(word)
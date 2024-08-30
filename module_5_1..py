

class House:
    def __init__(self,name,number_of_flors):
        self.name = name
        self.number_of_floors = number_of_flors

    def go_to(self,new_floor):
         if 0 < new_floor <= self.number_of_floors:
            for floor in range(1,new_floor + 1):
                print(floor)
         else:
            print("\nТакого этажа не существует")


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)


h1.go_to(5)
h2.go_to(10)
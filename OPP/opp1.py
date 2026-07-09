class Home:
    hmultiplier=200
    def __init__(self,room,cost,lounge=1): #lounge default değeri
        self.room = room
        self.__cost = cost
        self.lounge = lounge
    def rental_cost(self):
        return self.__cost//self.hmultiplier
    def info(self):
        print(f"{self.room}+{self.lounge} Apartment Cost={self.__cost} Rental_Cost={self.rental_cost()}") #fonksiyon parantezi unutma

class Workplace:
    wmultiplier=300
    def __init__(self,room,cost,lounge=1):
        Home.__init__(self,room,cost,lounge) #self unutma #sabit =1 gerek yok
    def rental_cost(self):                   #override
        return self._Home__cost//self.wmultiplier #encapsilation
    def __str__(self):
        return f"{self.room}+{self.lounge} WorkPlace Cost={self._Home__cost} Rental_Cost={self.rental_cost()}"


home1 = Home('2',10000)
home1.info()
workplace1 = Workplace('0',4000)
print(workplace1) #str değişimi

# from abc import ABC, abstractmethod
#
# class Cars(ABC):
#     @abstractmethod
#     def __init__(self,name,cost):
#         self.name = name
#         self.__cost = cost
#     def info(self):
#         print(f"Name: {self.name}  Cost={self.__cost}")
#
# class BMV(Cars):
#     def __init__(self,name,cost):
#         super().__init__(name,cost)
#
# bmv1 = BMV("BMV1",200000)
# bmv1.info()
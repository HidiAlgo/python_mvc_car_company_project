from src.Controller.StaffController import StaffController
import src.Controller.Data as Data
from src.Model.Car import Car
from src.Model.Model import Model
from src.Model.Manufacturer import Manufacturer
import src.Controller.DatabaseController as DB




class OfficeMemberController(StaffController):

    def addAModel(self, model):
        if type(model) is Model:
            DB.insertModel(model)
        else:
            print("TYPE ERROR")


    def removeAModel(self, modelID):
       DB.removeModel(modelID)


    def addAManufacturer(self, manufacturer):
        if type(manufacturer) is Manufacturer:
            DB.insertManufacturer(manufacturer)
        else:
            print("TYPE ERROR")


    def removeAManufacturer(self, manufacturerID):
        DB.removeManufacturer(manufacturerID)



    def addACar(self, car):
        if type(car) is Car:
            DB.insertCar(car)
        else:
            print("TYPE ERROR")



    def removeACar(self, registrationNumber):
        try:
            index = None
            for i in range(len(Data.cars)):
                if Data.cars[i]['registrationID'] == registrationNumber:
                    index = i
                    break
            if index != None:
                del Data.cars[index]
            else:
                print("NOT FOUND")
        except Exception as e:
            print(e)


    def viewSoldCars(self):
        result = list(filter(lambda x: (x['status'] == False), Data.cars))
        return result



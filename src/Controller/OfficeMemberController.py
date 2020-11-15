from src.Controller.StaffController import StaffController
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



    def addACar(self, car, email):
        if type(car) is Car:
            DB.insertCar(car, email)
        else:
            print("TYPE ERROR")



    def removeACar(self, registrationNumber):
        DB.removeCar(registrationNumber)


    def viewSoldCars(self):
        rows = DB.selectAllCars()
        result = list(filter(lambda x: x[5] == 1, rows))
        return result


    def moreDetailsForSoldCar(self, regNumber):
        return DB.selectSoldCar(regNumber)

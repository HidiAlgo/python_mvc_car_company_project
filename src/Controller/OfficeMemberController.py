from src.Controller.StaffController import StaffController
import src.Controller.Data as Data
from src.Model.Car import Car
from src.Model.Model import Model
from src.Model.Manufacturer import Manufacturer


class OfficeMember(StaffController):
    def addAModel(self, model):
        if type(model) is Model:
            m = {}
            m['id'] = model.getModelID()
            m['name'] = model.getModelName()
            Data.models.append(m)
        else:
            print("TYPE ERROR")

    def removeAModel(self, modelID):
        try:
            index = None
            for i in range(len(Data.models)):
                if Data.models[i]['id'] == modelID:
                    index = i
                    break
            if index != None:
                del Data.models[index]
            else:
                print("NOT FOUND")
        except Exception as e:
            print(e)

    def addAManufacturer(self, manufacturer):
        if type(manufacturer) is Manufacturer:
            m = {}
            m['id'] = manufacturer.getManufacturerID()
            m['name'] = manufacturer.getManufacturerName()
            Data.manufacturers.append(m)
        else:
            print("TYPE ERROR")

    def removeAManufacturer(self, manufacturerID):
        try:
            index = None
            for i in range(len(Data.manufacturers)):
                if Data.manufacturers[i]['id'] == manufacturerID:
                    index = i
                    break
            if index != None:
                del Data.manufacturers[index]
            else:
                print("NOT FOUND")
        except Exception as e:
            print(e)

    def addACar(self, car):
        if type(car) is Car:
            c = {}
            c['registrationID'] = car.getRegistrationNumber()
            c['name'] = car.getCarName()
            c['color'] = car.getColor()
            c['price'] = car.getPrice()
            c['doors'] = car.getNumberOfDoors()
            c['model'] = car.getCarModel()
            c['manufacturer'] = car.getCarManufacturer()
            c['upgrades'] = car.getUpgrades()
            c['status'] = car.getStatus()

            Data.cars.append(c)
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

    def viewAvailableCars(self):
        result = list(filter(lambda x: (x['status'] == False)), Data.cars)
        print(result)


    def viewSoldCars(self):
        result = list(filter(lambda x: (x['status'] == True)), Data.cars)
        print(result)

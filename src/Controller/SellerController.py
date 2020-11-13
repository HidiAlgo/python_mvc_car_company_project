import src.Controller.StaffController as admin
from src.Model.Car import Car
from src.Model.Upgrade import Upgrade
import src.Controller.Data as Data

class SellerController(admin.StaffController):
    def addUpgrades(self, car, upgrade):
        if type(car) is Car and type(upgrade) is Upgrade:
            u = {}
            u['id'] = upgrade.getUpgradeID()
            u['name'] = upgrade.getUpgradeName()
            u['price'] = upgrade.getUpgradePrice()

            for c in Data.cars:
                if c['registrationID'] == car.getRegistrationNumber():
                    c['upgrades'].append(u)
                    break


    def removeUpgrades(self, car, upgradeID):
        index = None
        upgradeIndex = None
        for i in range(len(Data.cars)):
            if Data.cars[i]['registrationID'] == car.getRegistrationNumber():
                index = i
                for j in range(len(Data.cars[i]['upgrades'])):
                    upgradeIndex = j
                    break
                break

        if index != None:
            del Data.cars[index]['upgrades'][upgradeIndex]

    def sell(self, car):
        index = None
        for i in range(len(Data.cars)):
            if Data.cars[i]['registrationID'] == car.getRegistrationNumber():
                index = i
                break

        if index != None:
            Data.cars[index]['status'] = False



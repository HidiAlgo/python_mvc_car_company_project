import src.Controller.Data as Data
from src.Model.OfficeMember import OfficeMember
from src.Model.Seller import Seller
import src.Controller.DatabaseController as DB

class StaffController:
    def searchCarsByModelOrManufacturer(self):
        pass

    def addAnOfficeMember(self, officeMember):
        if type(officeMember) is OfficeMember:
            member = {}
            member['email'] = officeMember.getOfficeMemberEmail()
            member['password'] = officeMember.getOfficeMemberPassword()
            member['name'] = officeMember.getOfficeMemberName()

            Data.officeStaff.append(member)

        else:
            print("TYPE ERROR")

    def addAnSeller(self, seller):
        if type(seller) is Seller:
            s = {}
            s['email'] = seller.getSellerEmail()
            s['password'] = seller.getSellerPassword()
            s['name'] = seller.getSellerName()

            Data.seller.append(s)

        else:
            print("TYPE ERROR")


    def viewAvailableManufacturers(self):
        return DB.selectAllManufacturers()

    def viewAvailableModels(self):
        return DB.selectAllModels()

    def viewAvailableCars(self):
        rows = DB.selectAllCars()
        result = list(filter(lambda x: x[5] == 0, rows))
        return result

    def viewUpgrades(self):
        return DB.selectAllUpgrades()
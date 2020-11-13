import src.Controller.Data as Data
from src.Model.OfficeMember import  OfficeMember
import src.Model.Seller as Seller

def authenticateOfficeStaff(officeStaffMember):
    if type(officeStaffMember) is OfficeMember:
        email = officeStaffMember.getOfficeMemberEmail()
        password = officeStaffMember.getOfficeMemberPassword()

        for member in Data.officeStaff:
            if member['email'] == email and member['password'] == password:
                return True
        else:
            return False

    else:
        print("TYPE ERROR")

def authenticateSeller(seller):
    pass





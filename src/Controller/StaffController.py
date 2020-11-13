import src.Controller.Data as Data

class StaffController:
    def searchCarsByModelOrManufacturer(self):
        pass

    def addAnOfficeMember(self, officeMember):
        member = {}
        member['email'] = officeMember.getOfficeMemberEmail()
        member['password'] = officeMember.getOfficeMemberPassword()
        member['name'] = officeMember.getOfficeMemberName()

        Data.officeStaff.append(member)

    def addAnSeller(self, seller):
        pass
import src.Controller.Data as Data

def authenticateOfficeStaff(email, password):
        for member in Data.officeStaff:
            if member['email'] == email and member['password'] == password:
                return True
        else:
            return False

def authenticateSeller(email, password):
        for member in Data.sellers:
            if member['email'] == email and member['password'] == password:
                return True
        else:
            return False






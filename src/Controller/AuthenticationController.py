<<<<<<< HEAD
from src.Controller import DatabaseController as DB
=======
import src.Controller.Data as Data
import src.Controller.DatabaseController as DB
>>>>>>> 90d5572012b5a6f3a7ea57cd10217bdc5ff740e1
from src.Model.OfficeMember import OfficeMember
from src.Model.Seller import Seller


def authenticateOfficeStaff(email, password):
       auth = DB.selectMember(email, password)
       if auth!=None:
           member = OfficeMember(auth[0], auth[1], auth[2])
           return member
       else:
           return None

def authenticateSeller(email, password):
    auth = DB.selectSeller(email, password)
    if auth!=None:
        seller = Seller(auth[0], auth[1], auth[2])
        return seller
    else:
        return None





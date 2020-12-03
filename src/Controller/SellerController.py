<<<<<<< HEAD
from src.Controller import StaffController as admin, DatabaseController as DB

=======
import src.Controller.StaffController as admin
import src.Controller.DatabaseController as DB
>>>>>>> 90d5572012b5a6f3a7ea57cd10217bdc5ff740e1

class SellerController(admin.StaffController):

    def sell(self, regNumber, upgrades, price, email, date, time):
        DB.sellCar(regNumber, upgrades, price, email, date, time)



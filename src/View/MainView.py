from src.Controller.OfficeMemberController import OfficeMemberController
from src.Controller.AuthenticationController import *
from src.Controller.SellerController import SellerController
from src.Model.Car import Car
from src.Model.Manufacturer import Manufacturer
from src.Model.Model import Model
from datetime import date
from datetime import datetime


def showMemberOptions():
    print("Enter one of the options you need as a member")
    print("01.) View available models")
    print("02.) View available manufacturers")
    print("03.) add a model")
    print("04.) add a manufacturer")
    print("05.) View available cars")
    print("06.) View sold cars")
    print("07.) add a car")
    print("08.) remove a model")
    print("09.) remove a manufacturer")
    print("10.) remove a car")
    print("11.) View available upgrades")
    print("12.) add an upgrade")
    print("13.) remove an upgrade")

def showSellerOptions():
    print("Enter one of the options you need as a seller")
    print("01.) View available models")
    print("02.) View available manufacturers")
    print("03.) View available cars")
    print("04.) View available upgrades")



def showAvailableModelsOrManufacturers(rows, title):
    print("--Available ",title ,"--")
    print("ID\t|\tNAME")
    print("--------------------------")
    for i in rows:
        print(i[0],"\t|\t",i[1])

def showCars(rows):
    print("\n--Available Cars--")
    print("ID\t|\t\t\tNAME\t|\t\t\tCOLOR\t|\t\t\tPRICE\t|\t\t\tMODEL\t|\t\t\tMANUFACTURER\t|\t\t\tADDED BY")
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    for car in rows:
        print(car[0],"\t|\t\t",car[1],"\t|\t\t\t",car[2],"\t|\t\t\t",car[3],"£\t|\t",car[-3],"\t|\t\t\t",car[-2],"\t|\t\t",car[-1])


def showUpgrades(rows, title):
    print("--"+title+" Upgrades--")
    print("ID\t|\t\t\tNAME\t|\t\t\tCOST\t|\t\t\t")
    print("---------------------------------------------------------------------")
    for row in rows:
        print(row[0],"\t|\t\t\t"+row[1],"\t|\t\t\t",row[2],"£")

def showCurrency(title, defualt, currency):
    print("\nPOUND £\t|\t"+title)
    print(defualt,"\t|\t", currency)

def showSoldCars(upgrades, sells, soldCar):
    carList = ['CAR ID','CAR NAME', 'COLOR', 'INITIAL PRICE']

    sellsList = ['SOLD BY','DATE', 'TIME']

    finalPrice = soldCar[3]
    initialPrice = finalPrice
    for u in upgrades:
        initialPrice-=u[2]

    soldCar[3] = initialPrice

    for i in range(4):
        print(carList[i]," |\t\t\t",soldCar[i])

    for i in range(len(upgrades)):
        print("UPGRADE |\t\t\t",upgrades[i][1]," PRICE ",upgrades[i][2])

    for i in range(3):
        print(sellsList[i]," |\t\t\t",sells[i+2])

    print("FINAL PRICE\t|\t",finalPrice)

def buy(upgrades, carID, defualtCurrency, changedCurrency, currencySymbol, user):
    purchase = input("type 'yes' to sell, otherwise 'no'")
    if purchase.lower() == 'yes':
        print("CAR ID\t|\tPOUND £\t+|\t",currencySymbol,"\t|\tDATE\t|\tTIME")
        d = date.today().strftime("%B %d, %Y")
        time = datetime.now().strftime("%H:%M:%S")
        print(carID,"\t|\t", defualtCurrency,"\t|\t", changedCurrency,"\t|\t",d,"\t|\t",time)

        seller = SellerController()
        seller.sell(carID, upgrades, defualtCurrency,user.getSellerEmail(), d, time)

        #carID,upgradeIDs,last price,date,time, seller email
    else:
        print("Thank you")

def checkAvailablility(rows, ID):
    for item in rows:
        if item[0] == ID:
            return False
    else:
        return True





def seller(user):
    print("\n---------------HI "+user.getSellerName().upper()+"------------------")
    showSellerOptions()
    seller = SellerController()

    selection = int(input("Enter your selection number here : "))
    if selection == 1:
        rows = seller.viewAvailableModels()
        showAvailableModelsOrManufacturers(rows, "Models for Sellers")

    elif selection == 2:
        rows = seller.viewAvailableManufacturers()
        showAvailableModelsOrManufacturers(rows, "Manufacturers for Sellers")

    elif selection == 3:
        carRows = seller.viewAvailableCars()
        showCars(carRows)

        reg_number = input("Enter the id for the car which you are going to sell: ")
        while checkAvailablility(carRows, reg_number):
            reg_number = input("Sorry that id does not exist please select one from the above list")

        price = 0
        selectedUpgrades = []

        option = int(input("If you want to add upgrades press 1 otherwise press 0 continue : "))
        for i in carRows:
            if i[0] == reg_number:
                price = i[3]
                break
        if option == 1:
            print("\nThese are the upgrades available for you to customize the selected car")
            upgradeRows = seller.viewUpgrades()
            showUpgrades(upgradeRows, "Available")

            for i in range(len(upgradeRows)):
                close = input("\nIf you want to close adding upgrades to the car press y otherwise press n")
                if close == 'y':
                    break
                else:
                    count = 0
                    upgrade = int(input("Press the upgrade ID to add it to the car here: "))

                    while count<3 and checkAvailablility(upgradeRows, upgrade):
                        upgrade = int(input("Please select an ID from above table : "))
                        count += 1

                    #Here I am getting a list of tuple, so i only get one tuple inside the list
                    #That is why I used [0][index] like this, because
                    #first i have to select the tuple, and then the element in that tuple
                    #It is always gonna be zero because, the list contains only one tuple

                    selected = list(filter(lambda x: x[0] == upgrade, upgradeRows))
                    selectedUpgrades.append(selected[0])
                    print("NEW PRICE = ", price, " + ", selected[0][2]," = ", price+selected[0][2])
                    price += selected[0][2]
            showUpgrades(selectedUpgrades, "Selected ")

            decision = input("If you want to delete one of these upgrades press y otherwise press n to purchase : ")
            if decision.lower() == 'y':
                deletIDinput = input("Enter the space seperated IDs for the upgrades which you want to delete : ")
                deletIDLIst = deletIDinput.split(' ')
                for i in deletIDLIst:
                    for j in range(len(selectedUpgrades)):
                        if selectedUpgrades[j][0] == int(i):
                            price -= selectedUpgrades[j][2]
                            del selectedUpgrades[j]
                            break
                showUpgrades(selectedUpgrades,"Updated List Of Selected")



        print("NEW PRICE = ",price)
        purchase = input("If you want to buy the car to this price with the given upgrades press y, to cancel press n")

        if purchase.lower() == 'y':
            print("SELECT YOUR CURRENCY TO PAY")
            print("1.) Sri Lankan Rupees")
            print("2.) USA dollar")
            print("3.) Euro")
            currency = int(input("Enter the number for the currency which you want to use"))
            if currency == 1:
                showCurrency("RUPEES Rs",price, price*244)
                buy(selectedUpgrades,reg_number,price,price*244,"Rs",user)
            elif currency == 2:
                showCurrency("USA $",price, price*1.32)
            elif currency == 3:
                showCurrency("EURO €",price, price*1.11)
            else:
                print("Sorry invalid selection")
        else:
            print("Thank you for using our service")






    elif selection == 4:
        rows = seller.viewUpgrades()
        print(rows)

    else:
        print("Invalid selection")


def member(user):
    print("\n-----------HI "+user.getOfficeMemberName().upper()+"---------------")
    showMemberOptions()
    member = OfficeMemberController()

    selection = int(input("Enter your selection number here : "))
    if selection == 1:
        rows = member.viewAvailableManufacturers()
        showAvailableModelsOrManufacturers(rows, "Models")

    elif selection == 2:
        rows = member.viewAvailableManufacturers()
        showAvailableModelsOrManufacturers(rows, "Manufacturers")

    elif selection == 3:
        name = input("Enter your model name here: ")
        model = Model(name)
        member.addAModel(model)
        print("SUCCESSFULLY ADDED")


    elif selection == 4:
        name = input("Enter your manufacturer name here: ")
        manufacturer = Manufacturer(name)
        member.addAManufacturer(manufacturer)
        print("SUCCESSFULLY ADDED")

    elif selection == 5:
        showCars(member.viewAvailableCars())

    elif selection == 6:
        cars = member.viewSoldCars()
        showCars(cars)

        car = input("Enter an reg number for an car which you want see more details : ")
        while checkAvailablility(cars, car):
            car = input("Sorry the given registration number is not available enter again : ")

        result = member.moreDetailsForSoldCar(car)
        selectedCar = list(filter(lambda x: x[0] == car, cars))


        showSoldCars(result[0], result[1], selectedCar[0])
    elif selection == 7:
        manufacturerRows = member.viewAvailableManufacturers()
        showAvailableModelsOrManufacturers(manufacturerRows, "Manufacturers")
        manuufactureID = int(input("Enter the id of a manufacturer wich you want"))

        while checkAvailablility(manufacturerRows, manuufactureID):
            manuufactureID = int(input("Sorry that ID is not available in the list please select one from the table above: "))

        modelRows = member.viewAvailableModels()
        showAvailableModelsOrManufacturers(modelRows,"Models")
        modelID = int(input("Enter the id of a model which you want"))

        while checkAvailablility(modelRows, modelID):
            manuufactureID = int(input("Sorry that ID is not available in the list please select one from the table above: "))

        registrationID = input("Enter the registration number: ")
        name = input("Enter the name here: ")
        color = input("Enter the color which you want here: ")
        price = int(input("Enter the initial price without any upgrades here: "))
        doors = int(input("Enter number of doors you need 3 or 5: "))

        car = Car(registrationID, name, color, price, doors, modelID, manuufactureID)
        member.addACar(car, user.getOfficeMemberEmail())

    elif selection == 8:
        rows = member.viewAvailableModels()
        showAvailableModelsOrManufacturers(rows, "Models")
        id = int(input("Enter the id of a model which you want to delete: "))
        member.removeAModel(id)
        print("SUCCESSFULLY DELTED")

    elif selection == 9:
        rows = member.viewAvailableManufacturers()
        showAvailableModelsOrManufacturers(rows, "Manufacturers")
        id = int(input("Enter the id of a manufacturer which you want to delete: "))
        member.removeAManufacturer(id)
        print("SUCCESSFULLY DELTED")

    elif selection == 10:
        cars = member.viewAvailableCars()
        showCars(cars)
        registration_number = input("Enter the registration number for a car to remove")

        while checkAvailablility(cars, registration_number):
            registration_number = input("Sorry that ID is not available in the list please select one from the table above: ")

        member.removeACar(registration_number)

    else:
        print("Invalid selection")




print("------------------HI THIS IS RUSH CAR SERVICE---------------------")
sellerOrMember = int(input("Press 1 if you are a seller or press 2 if you are a member "))

email = input("enter your email here: ")
password = input("enter your password here: ")

if sellerOrMember == 1:
    user = authenticateSeller(email, password)
    if user!=None:
        seller(user)
    else:
        print("Invalid credentials")

else:
    user = authenticateOfficeStaff(email, password)
    if user!=None:
        member(user)
    else:
        print("Invalid credentials")




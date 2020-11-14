from src.Controller.OfficeMemberController import OfficeMemberController
from src.Controller.AuthenticationController import *
from src.Model.Car import Car
from src.Model.Manufacturer import Manufacturer
from src.Model.Model import Model


def showMemberOptions():
    print("\n-----------HI MEMBER---------------")

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

def showAvailableModelsOrManufacturers(rows, title):
    print("--Available ",title ,"--")
    print("ID\t|\tNAME")
    print("--------------------------")
    for i in rows:
        print(i[0],"\t|\t",i[1])


def seller():
    print("\n---------------HI SELLER------------------")


def checkAvailablility(rows, ID):
    for item in rows:
        if item[0] == ID:
            return False
    else:
        return True



def member():
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
        print(member.viewAvailableCars())

    elif selection == 6:
        print(member.viewSoldCars())

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
        member.addACar(car)

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

    else:
        print("Sorry invalid input")
print("------------------HI THIS IS RUSH CAR SERVICE---------------------")
sellerOrMember = int(input("Press 1 if you are a seller or press 2 if you are a member "))

email = input("enter your email here: ")
password = input("enter your password here: ")

if sellerOrMember == 1:
    if authenticateSeller(email, password):
        seller()
    else:
        print("Invalid credentials")

else:
    if authenticateOfficeStaff(email, password):
        member()
    else:
        print("Invalid credentials")




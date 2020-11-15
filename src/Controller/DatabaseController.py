import sqlite3

conn = sqlite3.connect('./../../database/database.db')
cur = conn.cursor()
#-----------------------------------------------------------------------------------
def insertModel(model):
    cur.execute("insert into model(name) values(?)",(model.getModelName(),))
    conn.commit()

def selectAllModels():
    cur.execute('select * from model')
    rows = cur.fetchall()
    return rows

def removeModel(modelID):
    try:
        cur.execute("delete from model where id=?",(modelID,))
        conn.commit()
    except Exception as e:
        print(e)

#------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------
def insertManufacturer(manufacturer):
    cur.execute("insert into manufacturer(name) values(?)", (manufacturer.getManufacturerName(),))
    conn.commit()

def selectAllManufacturers():
    cur.execute('select * from manufacturer')
    rows = cur.fetchall()
    return rows

def removeManufacturer(manufacturerID):
    try:
        cur.execute("delete from manufacturer where id=?",(manufacturerID,))
        conn.commit()
    except Exception as e:
        print(e)
#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------
def insertCar(car,email):
    query = "insert into car values(?,?,?,?,?,?,?,?,?)"
    values=(car.getRegistrationNumber(), car.getCarName(),car.getColor(), car.getPrice(), car.getNumberOfDoors(), car.getStatus(),
            car.getCarModel(), car.getCarManufacturer(),email)

    cur.execute(query,values)
    conn.commit()

def selectAllCars():
    cur.execute('select * from car')
    rows = cur.fetchall()
    result = []

    #This for loop might make you confuse
    """
        All i am doing inside the for loop is,
            in the car table we only have the foriegn keys for the model and the manufacturer
            but for the end users, it is better if we can show them the names instead of just numbers
            what i am doing inside the for loop is that taking the ids and executing some other queries to take the names for those ids
            and finally I am assigning those names to the list and return it to the end user
        
    """
    for row in rows:
        out = list(row)

        cur.execute('select name from model where id=?', (row[-3],))
        modelName = cur.fetchone()
        cur.execute('select name from manufacturer where id=?', (row[-2],))
        manufacturerName=cur.fetchone()

        out[-3] = modelName[0]
        out[-2] = manufacturerName[0]
        result.append(out)

    return result

def removeCar(registration_number):
    try:
        cur.execute("delete from manufacturer where id=?",(registration_number,))
        conn.commit()
    except Exception as e:
        print(e)

def sellCar(regNumber, upgrades, price,email, date, time):
    cur.execute("update car set status=1, price=? where registration_number=?",(price,regNumber))
    conn.commit()
    for u in upgrades:
        cur.execute("insert into orders(carID, upgradeID) values(?,?)",(regNumber, u[0]))
        conn.commit()
    cur.execute("insert into sells(carID, seller, date, time) values(?,?,?,?)",(regNumber,email,date,time))
    conn.commit()

def selectSoldCar(regNumber):
    cur.execute('select * from orders where carID=?',(regNumber,))
    inter = cur.fetchall()
    order = []

    for o in inter:
        cur.execute('select * from upgrade where id=?',(o[2],))
        order.append(cur.fetchone())

    cur.execute('select * from sells where carID=?',(regNumber,))
    sells = cur.fetchone()

    out = [order, sells]
    return out
#--------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------
def selectAllUpgrades():
    cur.execute("select * from upgrade")
    rows = cur.fetchall()
    return rows
#--------------------------------------------------------------------------------------



#--------------------------------------------------------------------------------------
def selectMember(email, password):
    cur.execute("select * from staff_member where email=? and password=?",(email, password))
    return cur.fetchone()

def selectSeller(email, password):
    cur.execute("select * from seller where email=? and password=?",(email, password))
    return cur.fetchone()
#---------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------


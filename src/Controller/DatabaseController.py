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
def insertCar(car):
    query = "insert into car values(?,?,?,?,?,?,?,?)"
    values=(car.getRegistrationNumber(), car.getCarName(),car.getColor(), car.getPrice(), car.getNumberOfDoors(), car.getStatus(),
            car.getCarModel(), car.getCarManufacturer(),)

    cur.execute(query,values)
    conn.commit()

def selectAllCars():
    cur.execute('select * from car')
    rows = cur.fetchall()
    return rows
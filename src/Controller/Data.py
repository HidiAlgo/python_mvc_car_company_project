sellers=[
    {'email': 'perera@sellerMail.com', 'password': '000', 'name': 'Perera'},
    {'email': 'piyal@sellerMail.com', 'password': '111', 'name': 'Piyal'},
    {'email': 'sahan@sellerMail.com', 'password': '222', 'name': 'Sahan'}
]

officeStaff=[
    {'email': 'nishan@officeMail.com', 'password': '123', 'name':'Nishan'},
    {'email': 'saman@officeMail.com', 'password': '456', 'name':'Saman'},
    {'email': 'kumara@officeMail.com', 'password': '789', 'name':'Kumara'}
]

models = [
    {'id': 1, 'name': 'model1'},
    {'id': 2, 'name': 'model2'},
    {'id': 3, 'name': 'model3'}
]

manufacturers = [
    {'id': 1, 'name': 'manufacturer1'},
    {'id': 2, 'name': 'manufacturer2'},
    {'id': 3, 'name': 'manufacturer3'}
]

upgrades = [
    {'id':1, 'name': 'upgrade1', 'price': 10},
    {'id':2, 'name': 'upgrade2', 'price': 20},
    {'id':3, 'name': 'upgrade3', 'price': 30},
]

cars = [
    {'registrationID': 1, 'name': 'Car1', 'color': 'red', 'price': 10, 'doors': 5,
     'model': models[0], 'manufacturer':manufacturers[0], 'upgrades': [upgrades[0]],
     'status': True},
    {'registrationID': 2, 'name': 'Car2', 'color': 'Green', 'price': 20, 'doors': 3,
     'model': models[0], 'manufacturer': manufacturers[1], 'upgrades': [upgrades[1], upgrades[0]],
     'status': True},
    {'registrationID': 1, 'name': 'Car1', 'color': 'red', 'price': 10, 'doors': 5,
     'model': models[2], 'manufacturer': manufacturers[2], 'upgrades': [upgrades[0]],
     'status': False}
]


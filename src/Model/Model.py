class Model:
    '''
    This is the Model class, this class maintains the details for a model.
    ----------------------------------------------------------------------------------

    PRIVATE ATTRIBUTES:-
    --------------------
        __modelID: int
            an auto generated/ manually added ID
        __modelName: str
            a specific name for a model

    METHODS:-
    ---------
        getManufacturerID()
        getManufacturerName()
        setManufacturerID()
        setManufacturerName()
    '''

    def __init__(self, modelName, modelID=None):
        self.__modelName = modelName
        self.__modelID = modelID

    def getModelID(self):
        return self.__modelID

    def setModelID(self, modelID):
        self.__modelID = modelID

    def getModelName(self):
        return self.__modelName

    def setModelName(self, modelName):
        self.__modelName = modelName


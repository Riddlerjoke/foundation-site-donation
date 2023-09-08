class Site :
    def __init__(self, id, lieu) :
        self.__id = id
        self.__lieu = lieu

    def __get__id(self):
        return self.__id
    
    def __get__lieu(self):
        return self.__lieu
    
    id = property(__get__id)
    lieu = property(__get__lieu)
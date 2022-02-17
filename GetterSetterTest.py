class Shape:
    def __init__(self,hekef,age):
        self.__hekef = hekef
        self.__area = area

    def __str__(self):
        return f'Hekef = {self.__hekef}, Area = {self.__area}'

    def __repr__(self):
        return f'Shape({self.__hekef},{self.__area})'

    @property
    def hekef(self):
        return self.__hekef

    @hekef.setter
    def hekef(self,hekefValue):
        self.__hekef = hekefValue

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self,areaValue):
        self.__area = areaValue








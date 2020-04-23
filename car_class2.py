# Car Class example
#   Info on classes:
#   https://docs.python.org/3/tutorial/classes.html

class Car:
    """Common base class for all cars"""
    car_count = 0    # class variable for keeping a cars created counter

    # The __init__method accepts arguments for the
    # make, model, and mileage. It initializes the data
    # attributes with these values and increments the car counter.
    def __init__(self, year, make, model, mileage):
        self.__year = year
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        Car.car_count += 1

    # The __str__method returns a string representation of the object.
    def __str__(self):
        return '{0:s} {1:s} {2:s} with {3:,d} miles'.format(self.__year, self.__make, self.__model, self.__mileage)

    # The __add__method "overloards" the addition + operator for the Car class to increment the mileage.
    def __add__(self, miles):
        return self.__mileage + miles


    # The following methods are mutators (setters)
    # for the class's data attributes.
    def set_year(self, year):
        self.__year = year

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_mileage(self, mileage):
        self.__mileage = mileage

    # The following methods are the accessors (getters)
    # for the class's data attributes.
    def get_year(self):
       return self.__year

    def get_make(self):
       return self.__make

    def get_model(self):
        return self.__model

    def get_mileage(self):
        return self.__mileage

    # A method to increase the car mileage by miles driven
    def add_mileage(self, miles):
        self.__mileage += miles


###########################################################
## Test the Car class
###########################################################
## The main function.
def main():
    print('Create car1 ...')
    car1 = Car('2019', 'Ford', 'Mustang', 1000)
    print('Year:{:s}'.format(car1.get_year()) )
    print('Make:{:s}'.format(car1.get_make()) )
    print('Model: {:s}'.format(car1.get_model()) )
    print('Mileage: {:,d}'.format(car1.get_mileage()) )
    print(car1)

    print('\nAdd 500 to car1 mileage ...')
    car1.add_mileage(500)
    print(car1)

    print('\nCreate car2 ...')
    car2 = Car('2018', 'Chevrolet', 'Cruze', 5000)
    print(car2)

    print('\nCreate car3 ...')
    car3 = Car('2015', 'BMW', '3 Series', 8000)
    print(car3)

    print()
    print('Total Car Count: {:,d}'.format(Car.car_count))
    print()


# Call the main function.
if __name__ == '__main__':
    main()




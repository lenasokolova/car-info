class Car():
    """Prosta próba zaprezentowania samochodu."""

    def __init__(self, make, model, year):
        """Inicjalizacja atrybutów opisujących samochód."""
        self.make = make
        self. model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_neme(self):
        """Zwrot elegancko sformatowanego opisu samochodu."""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """Wyświetla informację o przebiegu samochodu."""
        print("Ten samochód ma przejechane " + str(self.odometer_reading) +  " km.")

    def update_odometr(self, mileage):
        """Przypisanie podanej wartości licznikowi przebiegu samochodu.
        Zmiana zostanie odrzucona w przypadku próby cofnięcia licznika."""

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Nie można cofnąć licznika przebiegu samochodu!")


my_new_car = Car('audi','a4', '2016')
print(my_new_car.get_descriptive_neme())
my_new_car.update_odometr(23)
my_new_car.read_odometer()
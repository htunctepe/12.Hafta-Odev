class Vehicle(object):
    list_of_vehicles = []
    no_of_vehicles = 0
    no_of_wheels = 4        # tekerlek_sayisi degiskeni
    current_speed = 0       # Istenilmemis ama, extra bir ozellik olarak, durdurma, hizlandirma ve yavaslatma
                            # fonksiyonlarinda kullanilmak uzere olusturdum.

    # def CarList(self):
    #     Vehicle.list_of_vehicles = [k for k, v in globals().items() if v is self]
    #     return Vehicle.list_of_vehicles

    def __init__(self, make, model, color, engine_power, no_of_seats, km_stand, year_of_sales):
        self.make = make                        # markasi
        self.model = model                      # modeli
        self.color = color                      # rengi
        self.engine_power = engine_power        # motor_gucu
        self.no_of_seats = no_of_seats          # koltuk_sayisi
        self.km_stand = km_stand                # km_durumu
        self.year_of_sales = year_of_sales      # satis yili
        Vehicle.list_of_vehicles.append(self)   # Olusturulan objeler bu listeye ekleniyor
        Vehicle.no_of_vehicles += 1             # Her arac olusturuldugunda, arac sayisi 1 artiyor
                                                # 4. tasit miktarini_guncelle. Sinif her orneklendiginde
                                                # tasit miktarini 1 artirmali.
        # Vehicle.CarList(self)


# 1.koltuk sayisini goster(tasitin koltuk sayisini ekrana yazdirmali
    def ShowNoOfSeats(self):
        print('\nThis vehicle ({} {}) has '.format(f'{self.make}', f'{self.model}') +
              f'{self.no_of_seats}' + ' seats.')

# 2.modelini goster (tasitin modelini ekrana yazdirmali)
    def ShowCarModel(self):
        print('\nCar Model: ' + f'{self.model}')

# 3. km_durumunu al (tasitin kilometre durumunu return etmeli)
    def ShowCar_KM_Stand(self):
        return self.km_stand

    def show_cars_detailed_info(self):
        print('\n' + '-'*30 + '\nMake:\t\t\t' + f'{self.make}' + '\nModel:\t\t\t' + f'{self.model}' +
              '\nColor:\t\t\t' + f'{self.color}' + '\nEngine Power:\t' + f'{self.engine_power}' +
              '\nNo Of Seats:\t' + f'{self.no_of_seats}' + '\nKM Stand:\t\t' + f'{self.km_stand}' +
              '\nSales Year:\t\t' + f'{self.year_of_sales}')

# - bu sinifa ait ozellik olan tasit_miktari’ni sinif disarisindan ulasilamayacak sekilde gizleyiniz.
# - class method olarak tasit_miktarini gosterecek bir method tanimlayiniz.
    @classmethod
    def ShowNoOfVehicles(cls):
        print('\nNo of Vehicles: ' + len(cls.list_of_vehicles) + '\n' + 'Vehicles: ' + ', '.join(cls.list_of_vehicles))


# ########Sorunun devaminda, bir Araba sinifi tanimlayiniz ve bu sinifi,
# ########Tasit sinifindan miras aliniz.
# ########Tasit sinifindan miras aldiginiz init fonksiyonunu muhafaza ediniz ve
# ########max_hiz isimli bir ornek niteligi tanimlayiniz ve
# ########bu nitelik her orneklenme durumunda parametre olarak verilsin.
# ########Bu sinifta su methodlari tanimlayiniz;

class Car(Vehicle):
    def __init__(self, make, model, color, engine_power, no_of_seats, km_stand, year_of_sales, max_speed):
        super().__init__(make, model, color, engine_power, no_of_seats, km_stand, year_of_sales)

        self.max_speed = max_speed

    def show_cars_detailed_info(self):
        super().show_cars_detailed_info()
        print('Max Speed:\t\t' + f'{self.max_speed}')


    def StopTheCar(self):           # 1.arabayi_durdur (“araba durdu” seklinde ekrana yazsin)
        Vehicle.current_speed = 0
        print('\nThe car ' + f'{self.make}' + ' ' + f'{self.model}' + ' has stopped!' +
              '\nCurrent Speed: ' + str(Vehicle.current_speed))


    def SpeedUp(self):              # 2. gaza_bas(“araba hizlaniyor” seklinde ekrana yazsin)
        Vehicle.current_speed += 50
        print('\nThe car ' + f'{self.make}' + ' ' + f'{self.model}' + ' speeding up!' +
              '\nCurrent Speed: ' + str(Vehicle.current_speed))


    def SlowDown(self):             # 3.  arabayi_yavaslat(“araba yavasliyor” seklinde ekrana yazsin)
        Vehicle.current_speed -= 50
        print('\nThe car ' + f'{self.make}' + ' ' + f'{self.model}' + ' is slowing down!' +
              '\nCurrent Speed: ' + str(Vehicle.current_speed))
        if Vehicle.current_speed < 0:
            print('\nBe careful!!! Car is going backwards!'
                  '\nDriving backwards is difficult.')

    # 4. arabanin_durumunu goster(bir kosul durumu yaziniz;eger Araba sinifi Tasit sinifinin alt sinifi ise
    # “Bu sinif Tasit sinifindan miras alinmistir” seklinde cikti versin. Degilse ‘ Araba sinifi Tasit sinifindan
    # miras alinmamistir.’ seklinde yazsin)
    # ######## Bu kismi pek acik degil. Onceki belirttiginiz gereksinimlere gore zaten ####################
    # ######## Araba sinifi, Tasit sinifinin alt sinifi. Bu bahsettiginiz nasil olacak anlamadim. ########

    def ShowCarStatus(self):
        if issubclass(Car, Vehicle):
            print('\nThis class is inherited from the Vehicle class.\n')


vehicle1 = Vehicle('Honda', 'Civic', 'Blue', 90, 5, 15000, 2015)
vehicle2 = Vehicle('Toyota', 'Corolla', 'Pearl White', 100, 5, 12000, 2016)
car1 = Car('Mercedes', 'E200', 'Black', 100, 5, 32000, 2017, 220)
car2 = Car('Audi', 'Q7', 'Red', 130, 7, 500, 2019, 220)

# print(Vehicle.list_of_vehicles)
# for i in Vehicle.list_of_vehicles:
#     print(Vehicle.show_car_info(Vehicle.list_of_vehicles[i]))

# vehicle1.show_cars_detailed_info()
# vehicle2.show_cars_detailed_info()
# car1.show_cars_detailed_info()
# Car.show_cars_detailed_info(car2)
#
# print("\nCar's KM Stand: " + str(car1.ShowCar_KM_Stand()))
# car1.ShowCarModel()
# car1.ShowCarStatus()
# car1.ShowNoOfSeats()
# car1.show_cars_detailed_info()
# car1.SpeedUp()
#  Try car1.SpeedUp() is commented and uncommented before the line below.
# car1.SlowDown()
# car1.StopTheCar()
# Car.ShowCarStatus(car2)

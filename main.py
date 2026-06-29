from ride import Ride, RideRequest, RideMatching, RideSharing
from user import Rider, User, Driver
from vichel import Bike, Car



niye_jao = RideSharing("Niye jao")
rahim = Rider("Rahim", "rahim@gamil.com", 12345, "Mohakhali", 1200)
niye_jao.add_rider(rahim)

kofiluddin = Driver("Kofiluddin", "kofiluddin@gmail.com", 1232323, "Gulsan")
niye_jao.add_driver(kofiluddin)





print(niye_jao)
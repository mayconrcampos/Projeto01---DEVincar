from faker import Faker
from faker_vehicle import VehicleProvider
import datetime

fake = Faker(["pt-BR", "pt-BR", "pt-BR", "pt-BR"])
fake.add_provider(VehicleProvider)


#print(fake.vehicle_make_model())

def gerador_de_modelo():
    return fake.vehicle_make_model()


#print(fake.safe_color_name())
#print(gerador_de_modelo())


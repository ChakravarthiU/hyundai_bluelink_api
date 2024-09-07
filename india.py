from hyundai_kia_connect_api import *
import os

# login = os.getenv("BL_LOGIN")
# pswd = os.getenv("BL_PSWD")
# pin = os.getenv("BL_PIN")
# creta_id = os.getenv("I20_ID")

login=""
pswd=""
pin=""
creta_id=""

vm = VehicleManager(region=6, brand=2, username=login, password=pswd, pin=pin)
vm.check_and_refresh_token()
vm.update_all_vehicles_with_cached_state()
# print(vm.vehicles)
creta = vm.get_vehicle(creta_id)
# vm.update_day_trip_info(creta_id, '20231101')
# print(creta)
# vm.force_refresh_vehicle_state(creta_id)
# i20 = vm.get_vehicle(creta_id)
# print(i20.location)
vm.update_day_trip_info(creta_id, '20240904')
# print(creta.day_trip_info)
# vm.update_month_trip_info(creta_id, '202310')

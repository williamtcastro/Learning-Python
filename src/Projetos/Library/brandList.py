import urllib.parse
import requests

main_api = 'https://fipe.parallelum.com.br/api/v1/'

#-----------------------------

def vehicleBrands(vehicle_type):

    url = main_api + vehicle_type + '/marcas'

    json_data = requests.get(url).json()

    vehicle_brands = []
    car_names = []
    car_codes = []

    for brand_code in json_data:
        car_name = brand_code['nome']
        car_code = brand_code['codigo']

        car_names.append(car_name)
        car_codes.append(car_code)

    vehicle_brands = dict(zip(car_names, car_codes))

    return vehicle_brands

#--------------------------------------------------------------------------------

def vehicleModel(vehicle_type, brand_code):

    url = main_api + vehicle_type + '/marcas/' + brand_code + '/modelos'

    json_data = requests.get(url).json()
    formated_data = json_data['modelos'][0:]

    car_models = []
    models_code = []
    models_codes = []

    for model_code in formated_data:
        car_model = model_code['nome']
        model_code = model_code['codigo']

        car_models.append(car_model)
        models_code.append(model_code)

    models_codes = dict(zip(car_models, models_code))

    return models_codes

#--------------------------------------------------------------------------------

def vehicleVersion(vehicle_type, brand_code, vehicle_version_code):

    url = main_api + vehicle_type + '/marcas/' + brand_code + '/modelos/' + vehicle_version_code + '/anos' 
    json_data = requests.get(url).json()

    # vehicles_codes = []
    # vehicleCodes = []
    vehicle_year_gas = []

    for vehicle_code in json_data:
        vehicle_year = vehicle_code['nome']
        # vehicleCode = vehicle_code['codigo'] #não necessário no momento

        # vehicleCodes.append(vehicleCode)
        vehicle_year_gas.append(vehicle_year)

    # vehicles_codes = dict(zip(vehicle_year_gas, vehicleCodes))

    return vehicle_year_gas

#--------------------------------------------------------------------------------
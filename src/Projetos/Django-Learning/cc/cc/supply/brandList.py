import urllib.parse
import requests

main_api = 'https://fipe.parallelum.com.br/api/v1/'

#-----LISTS-----------------

brands = []
names = []
codes = []

#----

models = []
modelsCode = []
models_codes = []

#----

vehicleYearGas = []

#-----------------------------

def brandList(vehicleType):

    url = main_api + vehicleType + '/marcas'

    json_data = requests.get(url).json()

    # brands = []
    # names = []
    # codes = []

    for brand_code in json_data:
        name = brand_code['nome']
        code = brand_code['codigo']

        names.append(name)
        codes.append(code)

    brands = dict(zip(names, codes))

    return names , brands

#--------------------------------------------------------------------------------

def vehicleModel(vehicleType, brandCode):

    url = main_api + vehicleType + '/marcas/' + brandCode + '/modelos'

    json_data = requests.get(url).json()
    formated_data = json_data['modelos'][0:]

    # models = []
    # modelsCode = []
    # models_codes = []

    for model_code in formated_data:
        model = model_code['nome']
        code = model_code['codigo']

        models.append(model)
        modelsCode.append(code)

    models_codes = dict(zip(models, modelsCode))

#--------------------------------------------------------------------------------

def vehicleVersion(vehicleType, brandCode, vehicleVersionCode):

    url = main_api + vehicleType + '/marcas/' + brandCode + '/modelos/' + vehicleVersionCode + '/anos' 
    json_data = requests.get(url).json()

    # vehicles_codes = []
    # vehicleCodes = []
    # vehicleYearGas = []

    for vehicle_code in json_data:
        vehicleYear = vehicle_code['nome']
        # vehicleCode = vehicle_code['codigo'] #não necessário no momento

        # vehicleCodes.append(vehicleCode)
        vehicleYearGas.append(vehicleYear)

    # vehicles_codes = dict(zip(vehicleYearGas, vehicleCodes))

#--------------------------------------------------------------------------------
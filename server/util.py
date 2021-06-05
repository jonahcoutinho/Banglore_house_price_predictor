import json,pickle,numpy as np
import sklearn
__locations=None
__data_columns=None
__model=None


def get_estimated_price(area,location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
        ar = {'Super built-up  Area': 1, 'Plot  Area': 2, 'Built-up  Area': 3, 'Carpet  Area': 4}
    except:
        loc_index=-1
    x = np.zeros(len(__data_columns))
    x[0] = ar[area]
    x[1] = sqft
    x[2] = bath
    x[3] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0],2)

def get_location_names():
    return __locations
def load_saved_artifacts():
    print('Loading saved artifacts..')
    global __data_columns
    global __locations
    with open("./artifacts/columns.json",'r') as f:
        __data_columns=json.load(f)['data_columns']
        __locations=__data_columns[4:]
    global __model
    with open("./artifacts/BangloreHousePrice.pickle", 'rb') as f:
        __model=pickle.load(f)

if __name__ == "__main__":
    load_saved_artifacts()
    print(get_estimated_price('Super built-up  Area', '1st Phase JP Nagar', 1000, 2, 2))
    print(get_location_names())

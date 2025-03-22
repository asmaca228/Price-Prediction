import json
import pickle
import sklearn
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,bhk,bath,total_sqft):
    try:
        loc_index=__data_columns.index(location.lower())
    except:
        loc_index=-1
        
    z=np.zeros(len(__data_columns))
    z[0]=bhk
    z[1]=bath
    z[2]=total_sqft
    if loc_index >= 0:
        z[loc_index]=1
    return round(__model.predict([z])[0],2)



def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    with open("./BHP/server/artifacts/columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    global __model
    if __model is None:
        with open('./BHP/server/artifacts/banglore_home_price_model.pkl', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns
    


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    
    print(get_estimated_price("1st phase jp nagar",2,2,1000))
    print(get_estimated_price("Kalhalli",2,2,1000))
    print(get_estimated_price("1st phase jp nagar",4,2,1000))
    
 
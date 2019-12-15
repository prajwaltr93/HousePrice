import pandas as pd
import requests as req
import finddist as fd
import numpy as np
csv_data = pd.read_csv("houseprices99acres.csv",names=[0,1,2,3,4])
reference_lat = 12.972442
reference_long = 77.580643
invalid_lat = 39.78373
invalid_lng = -100.445882
#locations = csv_data['location']

count = 0
invalid_count = 0
for i in range(0,csv_data.shape[0]):
    #print(location)
    #if count == 20:
    #    break
    #print(csv_data[2][i])
    #'''
    resp = req.get("http://open.mapquestapi.com/geocoding/v1/address?key=GAJXRMasoSuJjzJZxQiTiH4aYHIYvL9h&location="+str(csv_data[2][i]))
    data = resp.json()
    #data['results'][0]['locations'][0]['latLng']
    lat = data['results'][0]['locations'][0]['latLng']['lat']
    long = data['results'][0]['locations'][0]['latLng']['lng']
    #print(lat,long)
    #print(location)
    count += 1
    if ((not lat == invalid_lat) and (not long == invalid_lng)) and (10 <= int(str(lat).split('.')[0]) <= 15):
        actual_dist = fd.find_dist(lat,long)
        #modify dataframe by adding distance instead of actual location
        if actual_dist > 150:
            print("invalid distance found !!")
            invalid_count += 1
            csv_data[2][i] = np.nan
            continue
        print("approx distance for {} at {} , {} = ".format(csv_data[2][i],lat,long),actual_dist)
        csv_data[2][i] = actual_dist
        #csv_data['location'][location] = actual_dist
        #print(lat,long)

    else:
        #location = None
        print("invalid lat,long found !!")
        invalid_count += 1
        csv_data[2][i] = np.nan
    #'''
print("\nData instances lost = ",((invalid_count/count)*100))
#print(csv_data)
#write the modified csv to file
csv_data.to_csv("m99acreshouseprices.csv")

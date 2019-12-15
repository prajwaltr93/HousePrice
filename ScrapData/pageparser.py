import os
from bs4 import BeautifulSoup as bs
import html.parser
import re
import csv
#compile patterns
bedroom_no_re = re.compile(r"(\d)(\sBHK\s|\sBedroom\s)")
location_re = re.compile(r".*\sin\s(.*)")
feature_re = re.compile(r"Semifurnished|Furnished")
#globals
price_list = []
house_location_list = []
area_list = []
furnished_list = []
bedroom_list = []
#utility functions
def extract_bed_location(info_string):
    #extract number of bedrooms and house location and append to list
    try:
        bed_no = int(bedroom_no_re.search(info_string).group(1))
    except:
        bed_no = 0
    try:
        location = location_re.search(info_string).group(1)
    except:
        location = None
    return (bed_no,location)

    #print(bed_no)
#scan for files in this directory
basepath = './htmlfiles/'
#read all files iterate
count = 0
for entry in os.listdir(basepath):
    #extract data from htmlfiles
    #print(entry)
    file =  open(basepath+entry,"r")
    house_soup = bs(file,"html.parser")
    #get individual houses
    house_list = house_soup.select('div[style^="color: rgb"]')
    #print(len(house_list))

    for house in house_list:
        #get house price for that house
        price = house.select('b[id="undefined"]')[0].getText().strip()
        '''
        print(len(price))
        print(price[0].getText().strip())
        break
        '''
        #info string in <a class="undefined"> text has bedroom number and house_location
        info_string = house.select('a[class="undefined"]')[0].getText().strip().split("\n")[-1].strip()
        #print(info_string)
        #print(" ".join(loc_string))
        extracted_info = extract_bed_location(info_string)
        bed_no = extracted_info[0]
        location = extracted_info[1]
        #print(bed_no,location)
        #area string in <span> > <b> text , get area and append to area_list
        area = house.select("div > span > b")[0].getText().strip()[:-1]
        #print(area)
        features_soup = house.select("span span")
        furnished = " "
        for feature in features_soup:
            feature = feature.getText().strip()
            furnished = feature_re.search(feature)
            #print(furnished)
            if furnished:
                furnished = furnished.group(0)
                break
            else:
                furnished = None
        #print all variables to chech data scrap
        #print(price,bed_no,location,area,furnished)
        #write to csv file
        with open("houseprices99acres.csv","a") as csv_file:
            csv_writer = csv.writer(csv_file,delimiter=",",quotechar='"',quoting=csv.QUOTE_ALL)
            csv_writer.writerow([area,bed_no,location,furnished,price])
        count += 1
print("samples written to file : "+str(count))

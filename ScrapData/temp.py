import pandas as pd

data = pd.read_csv("backfinaltest.csv")
'''
for i in range(0,data.shape[0]):
    temp_data = data['4'][i].split(",")
    if len(temp_data) == 1:
        try:
            temp_data = data['4'][i].split(" ")
            #data defined in lakhs ex 4.5 lak convert to thousands

            # print(lak_term)
            if(len(temp_data) == 2):
                lak_term = temp_data[0].split(".")
                if len(lak_term) == 1:
                    #print(lak_term)
                    lak_th = int(lak_term[0])*100000
                else:
                    #print(lak_term)
                    lak_th = (int(lak_term[0])*100000)+(int(lak_term[1])*10000)
                temp_data = [lak_th]
        except:
            temp_data = [int(temp_data[0])]
    else:
        #data terms in multiples of 10 thousands to thousands
        th_s = int(temp_data[0]+temp_data[1])
        temp_data = [th_s]
    data['4'][i] = temp_data[0]
    #print(temp_data)
    # data['0'][i] = (data['0'][i].split(" ")[0])
'''
#
# print(data)
for i in range(0,data.shape[0]):
    temp_data = str(data['2'][i]).split(".")
    temp_data[1] = temp_data[1][:2]
    data['2'][i] = float(".".join(temp_data))
data.to_csv("finaltest.csv")

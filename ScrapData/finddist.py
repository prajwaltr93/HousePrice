from math import sin,cos,atan2,sqrt,radians
R = 6373
lat2 = radians(12.972442) #reference lat long to bangalore
lon2 = radians(77.580643)
def find_dist(lat1,lon1):
    dlon = lon2 - radians(lon1)
    dlat = lat2 - radians(lat1)
    #print(dlon,dlat)
    a = ((sin(dlat/2)**2 )+(cos(lat1) * cos(lat2) * (sin(dlon/2)**2)))
    c = 2 * atan2( sqrt(a), sqrt(abs(1-a)) )
    d = R * c
    return d

if __name__ == "__main__":
    d_lat = 12.846855
    d_lng = 77.676927
    find_dist(d_lat,d_lng)

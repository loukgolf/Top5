class Coldiness:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

place = []

def test(placeList):
    origin = []
    dest = []
    for i in placeList:
        for _ in range(1,len(placeList)):
            origin.append(i)
            #print(i)
        for j in placeList:
            if(j is not i):
                dest.append(j)
                #print(i)
    return origin, dest


place.append("A")
place.append("B")
place.append("C")
place.append("D")
place.append("E")

print(test(place))
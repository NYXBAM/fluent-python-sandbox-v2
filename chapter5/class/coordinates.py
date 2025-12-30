class Coordinate:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        
        
moscow = Coordinate(55.76, 37.62)
print(moscow)   #<__main__.Coordinate object at 0x10e3d4ec0>
location = Coordinate(55.76, 37.62)

print(location == moscow) # False 

# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    def __init__(self, latValue, lonValue):
        self.lat = latValue
        self.lon = lonValue

class1 = LatLon(143, 144)
print(class1.lat)

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
    def __init__(self, lat, lon, name):
        super().__init__(lat, lon)
        self.name = name
    def __str__(self):
        return 'name: {}, lat: {}, lon: {}'.format(self.name, self.lat, self.lon)

class2 = Waypoint(142, 144, 'class 2')
print(class2.lat, class2.lon, class2.name)
# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, lat, lon, name, size, difficulty):
        super().__init__(lat, lon, name)
        self.difficulty = difficulty
        self.size = size
    def __str__(self):
        return 'name: {}, lat: {}, lon: {}\nsize: {}, difficulty: {}'.format(self.name, self.lat, self.lon, self.size, self.difficulty)
# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
waypoint = Waypoint(41.70505, -121.51521, "Catacombs")
# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache(44.052137, -121.41556, "Newberry Views", 2, 1.5)
# Print it--also make this print more nicely
print(geocache)

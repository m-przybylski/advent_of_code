input = "day9"

cities = [line.replace("to", "=").split(" = ") for line in open(input).read().splitlines()]

city_map = {}

for city_from, city_to, distance in cities:
    if city_from not in city_map:
        city_map[city_from] = {}

    if city_to not in city_map:
        city_map[city_to] = {}

    city_map[city_from][city_to] = int(distance)
    city_map[city_to][city_from] = int(distance)


class Route():
    def __init__(self, cities) -> None:
        self.distance = 0
        self.cities = []
        for city in cities:
            self.add_city(city)
        pass

    def add_city(self, city) -> bool:
        if city not in self.cities:
            if len(self.cities):
                self.distance += city_map[self.cities[-1]][city]
            self.cities.append(city)
            return True
        
        return False
    
    def len(self):
        return len(self.cities)
    
    def __repr__(self) -> str:
        return str(self.cities)
    

def copy_route(route: Route) -> Route:
    return Route(route.cities) 

cities = list(city_map.keys())

routes = [Route([city]) for city in cities]

while all([route.len() < len(cities) for route in routes]):
    rs = []
    while len(routes):
        route = routes.pop()

        for city in cities:
            r = copy_route(route)
            if r.add_city(city):
                rs.append(r)

    routes = rs;

min_distance = routes[0].distance
for route in routes:
    if min_distance > route.distance:
        min_distance = route.distance

print(min_distance)


max_distance = routes[0].distance
for route in routes:
    if max_distance < route.distance:
        max_distance = route.distance

print(max_distance)

class City:
    
    def __init__(self, name, attractions, country, visited = False, wishlist = False, id = None):
        self.name = name 
        self.attractions = attractions
        self.country = country
        self.visited = visited
        self.wishlist = wishlist
        self.id = id 
class Restaurant:
    '''Describing a restaurant'''
    
    def __init__(self, restaurant_name, cuisine_type):
        '''Initialize name and type'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        '''Describing the restaurant'''
        print(f"The restaurant's name is {self.restaurant_name}.")
        print(f"The restaurant's cuisine type is {self.cuisine_type}.")
    
    def open_restaurant(self):
        '''Simulate opening the restaurant'''
        print(f"{self.restaurant_name} is now open!")

restaurant = Restaurant('McDonalds', 'Fast Food')
restaurant.describe_restaurant()
restaurant.open_restaurant()
print("\n")
restaurant2 = Restaurant('Burger King', 'Fast Food')
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

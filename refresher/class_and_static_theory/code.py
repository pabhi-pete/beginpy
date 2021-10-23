"""
@classmethod and @staticmenthod
Oct 22, 2020 11:57AM
"""

"""
Conditions: 1. The franchise method, which takes in a store as argument.
it should return a new Store object, with a name equal to the argument + " - franchise"
2. The store details method, which also takes in a store as argument. It should return a string --
representing the argument
Example:
store = Store("Test")
store2 = Store("Amazon")
store2.add_item("Keyboard", 160)

Store.franchise(store) # returns a Store with name "Test - franchise"
Store.franchise(store2) # returns a Store with name "Amazon - franchise"

Store.store_details(store) # return "Test, total stock price: 0"
Store.store_details(store2) # return "Test, total stock price: 160"

"""

class Store:
    def __init__(self, name):
        self.name = name
        self.items = list()

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            "price": price
        })
    
    def stock_price(self):
        total = 0
        for item in self.items:
            total = total + item['price']
        return total
    
    @classmethod
    def franchise(cls, store):
        new_store = cls(store.name + '- franchise')
        return new_store

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME', total stock price: TOTAL'
        return '{}, total stock price: {}'.format(store.name, int(store.stock_price()))

####### Execution Program ########
# store = Store("Test")
# store2 = Store("Amazon")
# store2.add_item("Keyboard", 160)

# Store.franchise(store) # returns a Store with name "Test - franchise"
# Store.franchise(store2) # returns a Store with name "Amazon - franchise"

# Store.store_details(store) # return "Test, total stock price: 0"
# Store.store_details(store2) # return "Test, total stock price: 160"

########## End Program ########
#Hint to call the object have 2 solution
class ClassTest:
    def instance_method(self):
        print(f'test{self}')
    @classmethod
    def class_method(cls):
        #cls === ClasTest()
        print(f'called class_method of {cls}')
    @staticmethod
    def static_method():
        print('called static_method.')

"""
1. create the new object 
test = ClassTest(), 
then called 
test.instance_method()
2. or ClassTest.instance_method(test)
"""
"""
@classmethod
we can called ClassTest.class_method() right aways dont need to pass anything to it
because cls is ClassTest.class_method(ClassTest ==> cls)

@staticmethod, it is the function it own seperate function,
and can call ClassTest.static_method()
it is convinince to use to call any values from other class or object
"""

class Myclass:
    # class variable 
    category = 'Utility'

    def __init__(self, name):
        self.name = name 
    
    # Instance method 
    def show_instance(self):
        print(f"Instance name: {self.name}")
    
    # Class method 
    @classmethod
    def show_category(cls):
        print(f'Class category: {cls.category}')

    # Static method
    @staticmethod
    def help():
        print('This is the help method')

obj = Myclass('Widget')
obj.show_instance()
obj.show_category()

obj.help()
Myclass.help()


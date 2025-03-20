"""Learn instance, class and static methods"""

class DemoClass:
    def instance_method(self):
        return ("Instance method called", self)
    
    @classmethod
    def class_method(cls):
        return ("class method called", cls)
    
    @staticmethod
    def static_method():
        return ("static method called",)
    

obj = DemoClass()

# instance access
print(obj.instance_method())
print(obj.class_method())
print(obj.static_method())

# class access
print(DemoClass.class_method())
print(DemoClass.static_method())
print(DemoClass.instance_method(obj)) # passing an instance object manually
class Car:
    
    def __init__(self, color, manufacturer, model):
        self.color = color
        self.manufacturer = manufacturer
        self.model = model
        self.speed = 0 # 
    
    def accelerate(self):
        if self.speed >= 160:
            return False
        self.speed += 16
        return True
    
    def brake(self):
        if self.speed <= 0:
            return False
        self.speed -= 16
        return True
    
    def get_speed(self):
        return self.speed
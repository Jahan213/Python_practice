class Car:
    def __init__(self):
        self.accelerator = False
        self.brk = False
        self.clutch =  False 
    def start(self):
        self.clutch = True
        self.accelerator = True
        print("Car started..")
    
car1 = Car()
car1.start()
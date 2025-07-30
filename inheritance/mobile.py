# Base class
class MobilePhone:
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def make_call(self, number):
        print(f"Calling {number}...")

    def receive_call(self):
        print("Receiving a call...")

    def take_a_picture(self):
        print(f"Taking a picture with {self.rear_camera} rear camera.")

# Derived class: Apple
class Apple(MobilePhone):
    def __init__(self, model, front_camera, rear_camera, ram, storage):
        
        super().__init__("OLED Touch Screen", "5G", False, front_camera, rear_camera, ram, storage)
        self.model = model

    def use_face_id(self):
        print(f"{self.model} is using Face ID.")

# Derived class: Samsung
class Samsung(MobilePhone):
    def __init__(self, model, dual_sim, front_camera, rear_camera, ram, storage):
       
        super().__init__("AMOLED Touch Screen", "4G/5G", dual_sim, front_camera, rear_camera, ram, storage)
        self.model = model

    def use_fingerprint(self):
        print(f"{self.model} is using fingerprint sensor.")

# Creating Apple objects
iphone13 = Apple("iPhone 13", "12MP", "48MP", "4GB", "64GB")
iphone13.make_call("9876543210")
iphone13.take_a_picture()
iphone13.use_face_id()
print()

iphone_se = Apple("iPhone SE", "8MP", "12MP", "3GB", "32GB")
iphone_se.receive_call()
iphone_se.use_face_id()
print()

# Creating Samsung objects
galaxy_s21 = Samsung("Galaxy S21", True, "16MP", "48MP", "4GB", "64GB")
galaxy_s21.make_call("1234567890")
galaxy_s21.use_fingerprint()
print()

galaxy_a12 = Samsung("Galaxy A12", True, "8MP", "32MP", "3GB", "32GB")
galaxy_a12.take_a_picture()
galaxy_a12.receive_call()
galaxy_a12.use_fingerprint()

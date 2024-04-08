class Computer:
    def __init__(self, manufacturer, model, processor, ram, display_size):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = processor
        self.ram = ram
        self.display_size = display_size

    def print_info(self):
        info = f"Manufacturer: {self.manufacturer}, Model: {self.model}, Processor: {self.processor}, RAM: {self.ram}, Display Size: {self.display_size}"
        print(info)

class Laptop(Computer):
    def __init__(self, manufacturer, model, processor, ram, display_size, weight, is_touchscreen):
        super().__init__(manufacturer, model, processor, ram, display_size)
        self.weight = weight
        self.is_touchscreen = is_touchscreen

    def print_info(self):
        super_info = super().print_info()
        additional_info = f"Weight: {self.weight}, Touchscreen: {self.is_touchscreen}"
        print(additional_info)

class Desktop(Computer):
    def __init__(self, manufacturer, model, processor, ram, display_size, type):
        super().__init__(manufacturer, model, processor, ram, display_size)
        self.type = type
        # TODO_5: Define the constructor of the derived class 2 (Desktop)
        # Hint: Again, you will need to call the constructor of the base class

    def print_info(self):
        super_info = super().print_info()
        additional_info = f"Type: {self.type}"
        print(additional_info)


# driver code. No modification is necessary after this line.
computer1 = Laptop('Apple', 'MacBook Air', 'Apple M1', '16GB', '13.3"', '2.7 lbs', False)
computer2 = Laptop('HP', 'Envy', 'core i5', '8GB', '15.6"', '4lbs', True)
computer3 = Desktop('Dell', 'Inspiron', 'core i7', '32GB', '27"', 'All-in-One')
computer1.print_info()
computer2.print_info()
computer3.print_info()


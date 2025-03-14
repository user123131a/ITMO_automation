class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)



rect1 = Rectangle(35, 5)
rect2 = Rectangle(8, 2)
rect3 = Rectangle(12, 52)


rectangles = [rect1, rect2, rect3]


for i, rect in enumerate(rectangles, start=1):
    area = rect.area()
    perimeter = rect.perimeter()
    print(f"Прямоугольник {i}:")
    print(f"  Площадь: {area}")
    print(f"  Периметр: {perimeter}\n")



class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        result = self.a + self.b
        print(f"Сложение: {self.a} + {self.b} = {result}")

    def multiplication(self):
        result = self.a * self.b
        print(f"Умножение: {self.a} * {self.b} = {result}")

    def division(self):
        if self.b != 0:
            result = self.a / self.b
            print(f"Деление: {self.a} / {self.b} = {result}")

    def subtraction(self):
        result = self.a - self.b
        print(f"Вычитание: {self.a} - {self.b} = {result}")


math_operations = Math(115, 52)


math_operations.addition()
math_operations.multiplication()
math_operations.division()
math_operations.subtraction()




class Button:
    def __init__(self, text, button_type="Кнопка", locator=""):
        self.text = text
        self.button_type = button_type
        self.locator = locator

    def click(self):
        return f"Клик по кнопке {self.text}"


button_text_box = Button("Text Box")
button_check_box = Button("Check Box")
button_radio_button = Button("Radio Button")
button_web_tables = Button("Web Tables")
button_buttons = Button("Buttons")
button_links = Button("Links")
button_broken_links = Button("Broken Links - Images")
button_upload_and_download = Button("Upload and Download")
button_dynamic_properties = Button("Dynamic Properties")

buttons = [button_text_box,
           button_check_box,
           button_radio_button,
           button_web_tables,
           button_buttons,
           button_links,
           button_broken_links,
           button_upload_and_download,
           button_dynamic_properties,]

for button in buttons:
    print(button.text)

for button in buttons:
    print(button.click())
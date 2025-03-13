class Label:
    def __init__(self, text, font):
        self._text = text
        self._font = font

    def get_text(self):
        return self._text
    
    def set_text(self, value):
        self._text = value
    
    def get_font(self):
        return self._font
    
    def set_font(self, value):
        self._font = value

label = Label("Hello world", "Arial")

print(label.get_text())

print(label.get_font())

label.set_text("Hello dozie!")
label.set_font("Times new roman")
print(label.get_text())

print(label.get_font())
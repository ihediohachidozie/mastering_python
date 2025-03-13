class Label:
    def __init__(self, text, font):
        self.set_text(text)
        self._font = font

    def get_text(self):
        return self._text
    
    def set_text(self, value):
        self._text = value.upper()

label1 = Label("Hello world", "Arial")
label1.text = 'Hello word2'

print(label1.get_text())

label1.set_text("Hello dozie")
print(label1.get_text())
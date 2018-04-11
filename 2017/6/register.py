class Register:
    def __init__(self, content):
        self.content = content
        self.hash = hash(str(self.content))

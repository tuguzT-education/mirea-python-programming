class HTML:
    def body(self):
        return self.Block('body')

    def div(self):
        return self.Block('div')

    def p(self, text: str):
        return self.P(text)

    class Block:
        def __init__(self, name: str):
            self.name = name

        def __enter__(self):
            print(f'<{self.name}>')
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            print(f'</{self.name}>')

    class P(Block):
        def __init__(self, text: str):
            super().__init__('p')
            self.text = text

        def __enter__(self):
            print(f'<{self.name}>{self.text}')
            return self

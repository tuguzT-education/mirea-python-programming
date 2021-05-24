import math
from random import randint
from tkinter import Tk, Canvas, Button

# PART 1

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600

NODE_R = 15

C1 = 2
C2 = 50
C3 = 20000
C4 = 0.1

DELAY = 16


class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normal(self):
        magnitude = self.magnitude()
        return self / magnitude if magnitude else Vec(0, 0)

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)

    def __neg__(self):
        return Vec(-self.x, -self.y)

    def __mul__(self, other: float):
        return Vec(self.x * other, self.y * other)

    def __truediv__(self, other: float):
        return Vec(self.x / other, self.y / other)


class Node:
    def __init__(self, text):
        self.text = text
        self.targets = []
        self.vec = Vec(0, 0)

    def to(self, *nodes):
        for n in nodes:
            self.targets.append(n)
            n.targets.append(self)
        return self


class Graph:
    def __init__(self):
        self.nodes = []

    def add(self, text):
        self.nodes.append(Node(text))
        return self.nodes[-1]


class GUI:
    def __init__(self, root):
        self.root = root
        self.canvas = Canvas(root, width=CANVAS_WIDTH,
                             height=CANVAS_HEIGHT, bg="white")
        self.draw_button = Button(root, text="Draw", command=self.start_draw)
        self.canvas.pack()
        self.draw_button.pack()
        self.nodes = None
        self.busy = None

    def draw_node(self, x, y, text, r=NODE_R):
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="MistyRose2")
        self.canvas.create_text(x, y, text=text)

    def draw_graph(self):
        for n in self.nodes:
            for t in n.targets:
                self.canvas.create_line(n.vec.x, n.vec.y, t.vec.x, t.vec.y)
        for n in self.nodes:
            self.draw_node(n.vec.x, n.vec.y, n.text)

    def start_draw(self):
        self.canvas.delete("all")
        if self.busy:
            self.root.after_cancel(self.busy)
        random_layout(self.nodes)
        self.animate()

    def animate(self):
        self.canvas.delete("all")
        for _ in range(DELAY):
            force_layout(self.nodes)
        self.draw_graph()
        self.busy = self.root.after(5, self.animate)


def random_layout(nodes):
    for n in nodes:
        n.vec.x = randint(NODE_R * 4, CANVAS_WIDTH - NODE_R * 4 - 1)
        n.vec.y = randint(NODE_R * 4, CANVAS_HEIGHT - NODE_R * 4 - 1)


def f_spring(u: Vec, v: Vec):
    in_log = (u - v).magnitude() / C2
    return (v - u).normal() * C1 * (math.log(in_log) if in_log else 0)


def f_ball(u: Vec, v: Vec):
    return (u - v).normal() * C3 / ((u - v).magnitude() ** 2)


def force_layout(nodes):
    forces = {}
    for node in nodes:
        for target in node.targets:
            forces[node] = forces.get(node, Vec(0, 0)) + f_spring(node.vec, target.vec)
        for w_node in nodes:
            if w_node not in node.targets and w_node is not node:
                forces[node] += f_ball(node.vec, w_node.vec)
        node.vec += (forces[node] * C4)


def main1():
    g = Graph()
    n1 = g.add("1")
    n2 = g.add("2")
    n3 = g.add("3")
    n4 = g.add("4")
    n5 = g.add("5")
    n6 = g.add("6")
    n7 = g.add("7")
    n1.to(n2, n3, n4, n5)
    n2.to(n5)
    n3.to(n2, n4)
    n6.to(n4, n1, n7)
    n7.to(n5, n1)

    root = Tk()
    w = GUI(root)
    w.nodes = g.nodes
    root.mainloop()


# PART 2


class PS:
    def __init__(self):
        self.stack = []
        self.words = {
            'dup': self.op_dup,
            'pop': self.op_pop,
            'add': self.bin_op(lambda a, b: a + b),
            'sub': self.bin_op(lambda a, b: a - b),
            'mul': self.bin_op(lambda a, b: a * b),
            'div': self.bin_op(lambda a, b: a // b),
            'eq': self.bin_op(lambda a, b: a == b),
            'ifelse': self.op_ifelse,
            'def': self.op_def,
        }

    def parse(self, tokens, start=0):
        code = []
        pos = start
        while pos < len(tokens):
            token = tokens[pos]
            if token.isdigit():
                code.append(('num', int(token)))
            elif token == '{':
                block, pos = self.parse(tokens, pos + 1)
                code.append(('code', block))
            elif token == '}':
                return code, pos
            elif token[0] == '/':
                code.append(('name', token[1:]))
            else:
                code.append(('word', token))
            pos += 1
        return code

    def execute(self, code):
        for tag, value in code:
            if tag == 'word':
                self.words[value]()
            elif tag in ('code', 'name', 'num'):
                self.stack.append(value)

    def bin_op(self, func):
        def op():
            a = self.stack.pop()
            b = self.stack.pop()
            self.stack.append(func(b, a))

        return op

    def op_dup(self):
        self.stack.append(self.stack[-1])

    def op_pop(self):
        self.stack.pop()

    def op_def(self):
        code = self.stack.pop()
        n = self.stack.pop()
        self.words[n] = lambda: self.execute(code)

    def op_ifelse(self):
        code2 = self.stack.pop()
        code1 = self.stack.pop()
        if self.stack.pop():
            self.execute(code1)
        else:
            self.execute(code2)


def main2():
    source = '''
    /fact {
        dup 0 eq { pop 1 } { dup 1 sub fact mul } ifelse
        } def
    5 fact
    '''

    ps = PS()
    ast = ps.parse(source.split())
    ps.execute(ast)
    print(ps.stack)

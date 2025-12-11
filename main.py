from Foo.kernel import Process, Event, Timeline

class message:
    def __init__(self, name, msg) -> None:
        self._name = name
        self._msg = msg

    def say(self):
        print(self._name, "says:", self._msg)

    def tell(self, n: int):
        print(self._msg * n)

A = message("A", "hello")
B = message("B", "Hi")

##################################################

TL = Timeline()

p1 = Process(A, "say")
p2 = Process(B, "say")

p3 = Process(B, "tell", [5])

e1 = Event(1, p1)
e2 = Event(2, p2)

# Min heap
e3 = Event(3, p1, 2.0)
e4 = Event(3, p2, 1.0)

e5 = Event(0, p3)

TL.schedule([e1,e2,e3,e4])
TL.schedule(e5)

TL.run()

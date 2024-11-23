class GeneratorTurboDisel:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        for value in range(self.start, self.end + 1):
            yield value

object = GeneratorTurboDisel(1, 1000000000^100)

for item in object:
    print(item)

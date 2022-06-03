class Agents():

    def __init__(self, name, height, weight, national):

        self.name = name
        self.height = height
        self.weight = weight
        self.national = national


ag1 = Agents(name='Binita', height=165, weight=48, national='NPR')
ag2 = Agents(name='Mou', height=172, weight=68, national='NMB')

print(ag1.national)

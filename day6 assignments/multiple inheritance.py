class HarryPotterBook:
    def __init__(self):
        self.author = "J.K.Rowling"
        print(self.author)


class LiteraryAgents:
    def __init__(self):
        self.agent = "christoper"
        print(self.agent)


class Publishers(HarryPotterBook, LiteraryAgents):
    def __init__(self):
        self.publish = "Elephant house"
        print(self.publish)
        HarryPotterBook.__init__(self)
        LiteraryAgents.__init__(self)

    def some_functions(self):
        print(self.agent, self.author)


p_ = Publishers()
p_.some_functions()




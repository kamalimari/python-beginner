class Book:
    def __init__(self, author):
        self.author = author
        # print(self.author)


class LiteraryAgents(Book):
    def __init__(self, author, agent):
        Book.__init__(self, author)
        self.agent = agent
        # print(self.agent)


class Publishers(LiteraryAgents):
    def __init__(self, author, agent, publish):
        LiteraryAgents.__init__(self, author, agent)
        self.publish = publish
        # print(self.publish)

    def some_functions(self):
        print(self.author, self.agent)


p = Publishers("harrypotter", "christoper", "elephanthouse")
p.some_functions()
print(p.agent)





class Agent:
    def __init__(self, name):
        self.name = name
        print(self.name)


class LiteraryAgent(Agent):
    def __init__(self, name, literary):
        Agent.__init__(self, name)
        self.literary = literary
        print(self.literary)


class SelfPublishingLiteraryAgent(Agent):
    def __init__(self, name, self_publishing_):
        Agent.__init__(self, name)
        self.self_publishing_ = self_publishing_
        print(self.self_publishing_)


class Publishers(LiteraryAgent, SelfPublishingLiteraryAgent):
    def __init__(self, name, literary, self_publishing_, publishers_name):
        LiteraryAgent.__init__(self, name, literary)
        SelfPublishingLiteraryAgent.__init__(self, name, self_publishing_)
        self.publishers_name = publishers_name
        print(self.publishers_name)

    def some_functions(self):
        print(self.name, self.literary)


p = Publishers("lord of the ring", "christoper", "alex", "elephant house")
p.some_functions()


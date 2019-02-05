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
    def __init__(self, name, selfpublishing_):
        Agent.__init__(self, name)
        self.selfpublishing_ = selfpublishing_
        print(self.selfpublishing_)


class Publishers(LiteraryAgent, SelfPublishingLiteraryAgent):
    def __init__(self, name, literary, selfpublishing_, publishers_name):
        self.__init__(self, name, literary)
        self.__init__(self, name, selfpublishing_)
        self.publishers_name = publishers_name
        print()

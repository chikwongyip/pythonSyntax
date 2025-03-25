class Tool(object):
    count = 0

    @classmethod
    def show_toolcount(cls):
        print("工具对象总数%d" % cls.count)

    def __init__(self, name):
        self.name = name
        Tool.count += 1


tool1 = Tool("1")
tool2 = Tool("1")
tool3 = Tool("1")
print(Tool.count)

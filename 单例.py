class Dog(object):
    # 类中只允许只有一个实例
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance


dog1 = Dog()
dog2 = Dog()
print(id(dog1))
print(id(dog2))

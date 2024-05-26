class OemCustomClazz(object):

    def customMethod(self):
        return 'this is from custom method/custom clazz'


def testmethod(oemServiceInstance):
    return "this is from direct clazz call "


def testMethodWithParams(self, *args):
    for arg in args:
        print("this is method with params ", arg)


def testMethodWithKwArgs(**kwargs):
    print('data', type(kwargs))
    for key, value in kwargs.items():
        print("this is kw args", key + '=' + value)

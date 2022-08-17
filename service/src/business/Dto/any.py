class AnyDto(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
     
class AnyListDto(object):
    def __init__(self, data, pure=True):
        self.children = list()
        for item in data:
            if pure:
                self.children.append(AnyDto(**item).__dict__)
            else:
                self.children.append(AnyDto(**item))
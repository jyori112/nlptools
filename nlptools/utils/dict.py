import json

class Dict(dict):
    def __setattr__(self, name, value):
        if isinstance(value, dict):
            self[name] = Dict(value)
        else:
            self[name] = value

    def __getattr__(self, name):
        if name in self:
            return self[name]
        else:
            self[name] = Dict()
            return self[name]

    def todict(self):
        return dict(self)

    def save(self, fp, **kwargs):
        json.dump(self.todict(), fp, **kwargs)

    @staticmethod
    def load(fp, **kwargs):
        return Dict(json.load(fp, **kwargs))

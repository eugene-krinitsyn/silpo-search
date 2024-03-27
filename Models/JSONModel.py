class JSONModel:
    @classmethod
    def from_json(cls, json_data):
        filtered_data = {key: value for key, value in json_data.items() if key in cls.__annotations__}
        return cls(**filtered_data)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
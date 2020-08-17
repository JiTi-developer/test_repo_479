from api.Exam.exam import Example

class OnlineBusiness():
    def __init__(self, api_root_url, **kwargs):
        self.api_root_url = api_root_url
        self.example = Example(self.api_root_url, **kwargs)


from core.rest_client import RestClient

class Example(RestClient):
    def register(self, **kwargs):
        return self.post("/xxx/user/v1/register", **kwargs)

    def login(self, **kwargs):
        return self.post("/xxx/user/v1/login", **kwargs)

    def modify_user_nick(self, **kwargs):
        return self.put("/xxx/user/verify/v1/modifyUserNick", **kwargs)

    def modify_user_pwd(self, **kwargs):
        return self.put("/xxx/user/verify/v1/modifyUserPwd", **kwargs)
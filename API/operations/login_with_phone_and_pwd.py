from core.base import CommonItem

def login_with_phone_and_pwd(ob,phone,pwd):
    """
    用户登录
    :param obonlinebusiness对象:
    :param phone: string，电话号码
    :param pwd: string，密码
    :return: common item
    """
    result = CommonItem()
    payload = {
        "phone":phone,
        "pwd":pwd,
    }
    response=ob.example.login(json=payload)
    if response.content['status'] != '0000':
        result.success = False
        result.error = "登陆失败"
        return result
    userid = response.content['result']['userid']
    seiionid = response.content['result']['sessionid']
    ob = OnlineBusiness(api_root_url=ob.api_root_url,userid=userid,sessionid=sessionid)

    result.success = True
    result.ob = ob
    return result
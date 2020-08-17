from onlinebusiness import OnlineBusiness

if __name__ == '__main__':
    ob = OnlineBusiness(api_root_url='http://127.0.0.1')
    payload = {
        "phone":phone
        "pwd":pwd
    }
    response=ob.example.login(json=payload)
    assert response.content['status'] == '0000'
    userid = response.content['result']['userid']
    ob = OnlineBusiness(api_root_url='http://127.0.0.1', userid=userid,sessionid=sessionid)
    payload = {
        "nickName":"新昵称"，
    }
    response=ob.example.modify_user_nick(json=payload)
    assert response.content['status'] == '0000'
    assert response.content['nickName'] == '新昵称'
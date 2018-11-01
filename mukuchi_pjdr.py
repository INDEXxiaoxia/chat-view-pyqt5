def pjdr_0(user_name,user_id,user_psd):
    L=list(['0001','aaaa','bbbb'])


    print('昵称：%s账号：%s密码：%s'%(user_name,user_id,user_psd))


    if user_id not in L:
        return 'IDOK'
    else:
        return 'IDERROR'
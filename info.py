#-*- coding: utf-8 -*-

class PersonalInfo:
    login_info = {
    'u':'19114059',
    'p':'011018'
    }
    def set_info(self,user,password):
        self.login_info['u'] = user
        self.login_info['p'] = password

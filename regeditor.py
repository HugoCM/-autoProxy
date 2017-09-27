'''
Created on 2017年9月27日

@author: Mi
'''
'''
  # Title   : setRegProxy
  # Author  : Solomon Xie
  # Utility : Via Registry key of windows, change proxy settings of IE on Windows.
  # Require : Python 2.x, Windows 7
  # Reg Path: HKUC\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Connections
  # Anlysis : 注册表的二进制值(及关键信息)如下："46 00 00 00 00 00 00 00 开关 00 00 00 IP长度 00 00 00 IP地址 00 00 00 是否跳过本地代理 21 00 00 00 PAC地址"
  # Method  : 通过在cmd中导入reg文件的方式执行并立即生效。
  # Notes   : - 二进制值的设置选项在代码中已经体现了。本代码可以根据需要自动设置代理。
  # switcher: 开关：0F全部开启(ALL)；01全部禁用(Off)
              03使用代理服务器(ProxyOnly)；05使用自动脚本(PacOnly)；
              07使用脚本和代理(ProxyAndPac)；09自动检测设置(D)；
              0B自动检测并使用代理(DIP)；0D自动检测并使用脚本(DS)；
'''

import os
options = {'On':'0b','Off':'09'}

def set(opt):
    print('--Creating reg file--')
    option = options.get(opt)
    reg_value = 'Windows Registry Editor Version 5.00\n\n[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\Connections]\n"DefaultConnectionSettings"=hex:46,00,00,00,38,03,00,00,'+option+',00,00,00,16,00,00,\
00,70,72,6f,78,79,2e,65,63,2d,6c,69,6c,6c,65,2e,66,72,3a,33,31,32,38,11,00,\
00,00,31,32,37,2e,30,2e,30,2e,31,3b,3c,6c,6f,63,61,6c,3e,2d,00,00,00,68,74,\
74,70,3a,2f,2f,31,32,37,2e,30,2e,30,2e,31,3a,31,30,38,30,2f,70,61,63,3f,74,\
3d,32,30,31,37,30,39,30,36,31,39,35,34,31,38,33,35,33,00,00,00,00,00,00,00,\
00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00'
    filePath = '%s\DefaultConnectionSettings.reg'%os.getcwd() 
    with open(filePath, 'w') as f:
        f.write(reg_value)
    print('--Importing reg file--')
    cmd = 'reg import "%s"' %filePath
    result  = os.popen(cmd)
    if len(result.readlines()) < 2 :
        print ('---Successfully import proxy into Registry on this machine.---')
    return 
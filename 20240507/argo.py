import tagui as r
# import requests
# import certifi
import os
import argparse
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
# 设置命令行代码页为UTF-8
#subprocess.run('chcp 65001', shell=True)
# 设置命令行代码页为UTF-8
#subprocess.run(['chcp', '65001'])
os.system('chcp 65001')
batch_file = 'argo.bat'
# response = requests.get('https://github.com', verify=certifi.where())
r.init(visual_automation=True, chrome_browser=False)
# r.init(visual_automation=True, chrome_browser=False)

# r.clipboard('1499')    
# r.echo('Hello, world!')
# #貼上剪貼簿
# #r.keyboard('[ctrl]v')149
# r.echo(r.keyboard('[ctrl]v'))
# #清除剪貼簿
# r.keyboard('[clear]')
# r.close()


def parse_args_argparse():
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument("--userid", type=str, default="123", help="使用者帳號")
    parser.add_argument("--userpwd", type=str, default="123", help="使用者密碼")
    parser.add_argument("--autologin", type=bool,default=True, help="使用者密碼")

    args = parser.parse_args()
    return args

try:
    if __name__ == '__main__':
        args = parse_args_argparse()
        
    os.system(batch_file)
    #subprocess.run([batch_file], capture_output=True, text=True)
    #r.click('1.png')
    r.clipboard(args.userid)
    r.keyboard('[ctrl]v')
    r.keyboard('[tab]')
    r.clipboard(args.userpwd)
    r.keyboard('[ctrl]v')
    #r.click('2.png')
    # r.echo(args.userpwd)
    # r.echo(args.autologin)
    r.close()        
       
except Exception as e:
    print(f"文件写入失败: {e}")        
    
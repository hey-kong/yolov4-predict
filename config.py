import configparser


# 创建配置文件对象
def get_config(file):
    con = configparser.ConfigParser()
    con.read(file, encoding='utf-8')
    items = con.items('application')
    items = dict(items)
    return items
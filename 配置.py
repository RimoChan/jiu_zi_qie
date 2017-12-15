import yaml

f=open('data/配置.yaml',encoding='utf8')
配置=yaml.load(f)

if __name__=='__main__':
    print(配置)
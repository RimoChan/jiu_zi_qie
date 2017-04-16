from jinja2 import *
env = Environment(loader = FileSystemLoader('html'))

def tp(file_in,file_out,**dict):
    file_out='html/'+file_out
    template=  env.get_template(file_in)
    f_out=open(file_out,'w',encoding='utf-8')
    f_out.write(template.render(**dict))
    f_out.close()
import json
import os

root='../CategorizedJSON/'
j=json.JSONDecoder()
def create_individual_docs(srcfilename):
    filename=os.path.join(root,srcfilename)
    print filename
    dirname=os.path.join(root,"dir_"+srcfilename[:-5])
    print dirname
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    f=open(filename)
    fnamebase='review_'
    i=0
    for l in f:
        if l=='\n':
            continue
        t=j.decode(l)['text']
        i=i+1
        
        newfname=os.path.join(dirname,fnamebase+'_%04d.txt'%i);
        fw=open(newfname,'w')
        fw.write(t.encode('utf8'))
        fw.close()
    f.close()


def main():
    create_individual_docs('category_Indian.json')


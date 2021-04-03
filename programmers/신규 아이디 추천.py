# https://programmers.co.kr/learn/courses/30/lessons/72410

from string import ascii_lowercase
import re
 

def solution(new_id):
    a = list(ascii_lowercase)+['-','_'+'.']
    answer = ''
    id1=make_lower(new_id)
    id2=delete_s(id1)
    id3=delete_double_dot(id2)
    id4=delete_dot(id3)
    id5=fill_blank(id4)
    id6=delete_dot(id5[:15])
    
    return fill(id6)

def make_lower(id):
    return id.lower()

def delete_s(id):
    return re.sub(r"[^a-z0-9-_.]","", id)

def delete_dot(id):
    while len(id)>0 and id[0]=='.':
        id=id[1:]
    while len(id)>0 and id[-1]=='.':
        id=id[:-1]
    
    return id

def delete_double_dot(id):
    a=re.search('\.\.',id)
    while a:
        id=id[:a.span()[0]]+id[a.span()[1]-1:]
        a=re.search('\.\.',id)
    return id

def fill_blank(id):
    return id if len(id)>0 else 'a'

def fill(id):
    while len(id)<3:
        id+=id[-1]
    return id

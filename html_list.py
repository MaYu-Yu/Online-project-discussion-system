class Html_list():
    def __init__(self):
        self.word = [] 
    def __str__(self):
        html = ''
        for i in self.word:
            html +=i
        return html

#part 
class Part_list(Html_list):
    def add(self, proj_id, proj_name):
        word = '''<div onClick="location.href='/discuss?id={}'">{}</div>'''.format(proj_id, proj_name)
        self.word.append(word)
#user
class User_list(Html_list):
    def add(self, name, account, id):
        word = '''<tr>
            <td>{}</td>
            <td>{}</td>
            <td>
                <a href="/update?id={}">修改
                <a href="/db_delete?id={}">刪除
            </td>
        </tr>'''.format(name, account, id, id)
        self.word.append(word)
#proj
class Proj_list(Html_list):
    def add(self, name, id):
        word ='''<tr>
            <td>{}</td>
            <td>
                <a href="/proj_add_user?id={}">指定成員
                <a href="/proj_update?id={}">修改
                <a href="/db_proj_del?id={}">刪除
            </td>
        </tr>'''.format(name, id, id, id)
        self.word.append(word)

class Proj_add_user(Html_list):
    def add(self, id, name):
        word = '<option value = "{}">{}</option>'.format(id, name)
        self.word.append(word)
class Proj_add_user1(Html_list):
    def add(self, id, name):
        word = '<input type ="checkbox" name="member" value="{}">{}<br>'.format(id, name)   
        self.word.append(word)
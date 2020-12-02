class Html_list():
    word = []  
    def get_word(self): 
        return self.word
#part 
class Part_Click(Html_list):
    def add_onClick(self, proj_id, proj_name):
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
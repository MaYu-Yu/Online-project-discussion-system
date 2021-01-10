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
        word = '''<div style="color: deepskyblue; font-size:25px;" onClick="location.href='/discuss?id={}'">{}</div></br>'''.format(proj_id, proj_name)
        self.word.append(word)
#user
class User_list(Html_list):
    def add(self, user_id, name, account, id):
        word = '''<tr>
            <td>{}</td>
            <td>{}</td>
            <td><a href="/update?id={}">修改'''.format(name, account, id)
        if user_id == 1:
            word += '<a href="/db_del?id={}">刪除'.format(id)
        word += "</td></tr>"
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
#Proj_add_user
class Proj_add_user(Html_list):
    def add(self, id, name):
        #word = '<option value = "{}">{}</option>'.format(id, name)
        word = '<input type ="radio" name="leader" value="{}">{}<br>'.format(id, name)   
        self.word.append(word)
class Proj_add_member(Html_list):
    def add(self, id, name):
        word = '<input type ="checkbox" name="member[]" value="{}">{}<br>'.format(id, name)   
        self.word.append(word)
#Proj_update
class Proj_update(Html_list):
    def add(self, direction):
        word = '''
            <p>面向名稱：<input type="text" value="{}" name="direction_name[]" required>
            面向說明：<input type="text" value="{}" name="direction_description[]" required>
            <input type="hidden" value="{}" name="direction_id[]">
            <input type="button" class="btn btn-danger" value="X" data-dismiss="alert"></p>
            '''.format(direction[0], direction[1], direction[2])
        self.word.append(word)

#discuss
class Discuss_list(Html_list):
    def add(self, name):
        word = "專案名稱: {}".format(name) 
        self.word.append(word)
class Discuss_list1(Html_list):
    def add(self, name, description, id):
        word ='''<tr>
                    <td>{}</td>
                    <td>{}</td>
                    <td><button onclick="location.href='/opinion?id={}'">討論</td>
                </tr>'''.format(name, description, id)
        self.word.append(word)
#opinion 
class Opinion_list(Html_list):
    def add(self, opinion_id, title, description, time, name, avg, people):
        word = '''<tr>
        <td align ="center">{}</td>
        <td align ="center">{}</td>
        <td align ="center">{}</td>
        <td align ="center">{}</td>
        <td align ="center">{}</td>
        <td align ="center">{}</td>
        <td align ="center">{}</td>
        '''.format(opinion_id, title, description, time, name, avg, people)
        self.word.append(word)
    def set_score(self, opinion_id):
        word = "<td><select name='score[]'>"
        for i in range(0,6):
            word += "<option value='{}'>{}</option>".format(i,i)
        word+= "<input type ='hidden' name='opinion_id[]' value={}>".format(opinion_id)
        self.word.append(word)
#stat
class stat_list(Html_list):
    def add(self, name, title, score):
        word = '''<tr>
        <td align ="center">{}</td>
        <td align ="center">{}</td>
        <td align ="center">{}</td>'''.format(name, title, score)
        self.word.append(word)
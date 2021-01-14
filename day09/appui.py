import wx;

import app1
from sqlitedb import *
from userdb import *
data = []
users = app1.init()
for user in users:
    data.append("%s %s %d" % (user.id, user.name, user.age))

app = wx.App()
frame = wx.Frame(None, title='Shop Management')
panel1 = wx.Panel(frame)
panel2 = wx.Panel(frame)


panel1.SetBackgroundColour(colour='yellow')
panel2.SetBackgroundColour(colour='purple')

textId = wx.TextCtrl(panel1)
textId.SetHint("ID: ")
textPwd = wx.TextCtrl(panel1)
textPwd.SetHint("PWD: ")
textName = wx.TextCtrl(panel1)
textName.SetHint("NAME: ")
textage = wx.TextCtrl(panel1)
textage.SetHint("AGE: ")
bt = wx.Button(panel1, label='ADD')

userList = wx.ListBox(panel2, choices=data)
userList.SetBackgroundColour(colour='red')
userList.SetSize(wx.Size(120,150))

def itemselect(event):
    dataCnt = userList.GetSelection()
    wx.MessageBox(data[dataCnt],"User Information", wx.OK)

userList.Bind(wx.EVT_LISTBOX, itemselect)


def onClick(event):
    id = textId.GetValue()
    pwd = textPwd.GetValue()
    name = textName.GetValue()
    age = textage.GetValue()
    wx.MessageBox(id+"생성 완료", 'Alert', wx.OK)
    data.append((id+" , "+pwd+" , "+name+" , "+age))
    userList.Append(id+" "+name+age)
    app1.userInsert(User(id=id, pwd=pwd, name=name,age=int(age)))
    textId.SetValue('')
    textPwd.SetValue('')
    textName.SetValue('')
    textage.SetValue('')
    print(id)

bt.Bind(wx.EVT_BUTTON, onClick)

box1 = wx.BoxSizer(wx.VERTICAL)
box1.Add(textId)
box1.Add(textPwd)
box1.Add(textName)
box1.Add(textage)
box1.Add(bt)
panel1.SetSizer(box1)

grid = wx.GridSizer(1,2,10,10)
grid.Add(panel1,0,wx.EXPAND)
grid.Add(panel2,1,wx.EXPAND)

frame.SetSizer(grid)
frame.Show(True)
app.MainLoop()

# 1. 화면에서 데이터를 입력하면 DB에 INSERT 되고 List화면에 출력된다.
# 2. List화면에는 ID 와 NAME 만 출력되고 항목을 클릭했을 때 ID, PWD, NAME 모두 출력하게된다.
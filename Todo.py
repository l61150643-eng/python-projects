# coding:UTF-8
# @Author:exile_min
def load_todos():
    '''
    从todo.txt加载代办数据，返回列表
    '''
    todos=[]
    try:
        with open("todo.txt",mode="rt",encoding="utf-8")as f:
            for line in f:
                line=line.strip()
                if not line:
                    continue
                content,status=line.split("|",1)
                todos.append({'content':content,'status':status})
    except FileNotFoundError:
        pass
    return todos

def save_todos(todos):
    '''
    把内存中的待办列表保存到todo.txt
    '''
    with open("todo.txt",mode="at",encoding="utf-8")as f:
        for todo in todos:
            f.write(f"{todo['content']}|{todo['status']}\n")

def add_todo(todos):
    '''添加待办：用户输入内容，追加到列表'''
    content=input("请输入待办内容：>>>").strip()
    if not content :
        print("待办内容不能为空😜")
        return
    todos.append({'content':content,'status':"未完成"})
    print(f"已添加待办：{content}")

def show_todos(todos):
    '''查看所有待办 带序号 区分状态'''
    if not todos:
        print("暂无待办事项！😎")
        return
    print("\n 待办清单：")
    for i,todo in enumerate(todos,start=1):
        status_icon="✅" if todo['status']=="已完成" else "🔲"
        print(f"{i}.{status_icon}{todo['content']} {todo['status']}")
    print()

def mark_todo(todos):
    '''标记待办已完成：用户输入序号，修改状态'''
    show_todos(todos)
    if not todos:
        return
    try:
        index=int(input("请输入要标记完成的待办序号："))-1
        if 0<=index<len(todos):
            todos[index]["status"]="已完成"
            print(f"已标记{todos[index]['content']}为已完成✌️")
        else:
            print("序号无效！😵")
    except ValueError:
        print("请输入有效的数字！😵")

def delete_todo(todos):
    '''删除待办：用户输入序号，从列表删除'''
    show_todos(todos)
    if not todos:
        return
    try:
        index=int(input("请输入要删除的代办序号："))-1
        if 0<=index<len(todos):
            deleted=todos.pop(index)
            print(f"已删除待办:{deleted['content']}")
        else:
            print("序号无效！")
    except ValueError:
        print("请输入有效的数字！😵")

def main():
    '''程序主入口：加载数据-菜单循环-保存数据'''
    todos=load_todos()
    print("welcome to this todos-tool")
    while True:
        print("{0:*^20}".format("Todo工具菜单"))
        print("1.添加待办")
        print("2.查看待办")
        print("3.标记待办为已完成")
        print("4.删除待办")
        print("5.推出程序")
        print("--"*30)

        choice=input("请输入你的选择（1-5）：>>>").strip()
        if choice=='1':
            add_todo(todos)
            save_todos(todos)
        elif choice=='2':
            show_todos(todos)
        elif choice=='3':
            mark_todo(todos)
            save_todos(todos)
        elif choice=='4':
            delete_todo(todos)
            save_todos(todos)
        elif choice=='5':
            print("再见~")
            break
        else:
            print("无效输入，请输入1-5之间的数字")

if __name__=='__main__':
    main()


#记录所有的名片字典
card_list = []
def show_menu():
    print("*" * 50)
    print("欢迎使用【名片管理系统】V.1.0")
    print("")
    print("1.新增名片")
    print("2.显示全部")
    print("3.搜索名片")
    print("")
    print("0.退出系统")
    print("*" * 50)
def new_card():
    '''新增名片'''
    print("↓" * 20,end="进入新界面")
    print("↓" * 20)
    print("新增名片界面")
    #1.提示用户输入名片信息
    name_str = input("请输入姓名：")
    phone_num = input("请输入电话：")
    qq_str = input("请输入QQ：")
    email = input("请输入邮箱：")

    #2.使用用户输入的信息建立一个名片字典
    card_dict = {"name":name_str,
                "phone":phone_num,
                "qq":qq_str,
                "email":email}
    #3.将名片字典添加到列表中
    card_list.append(card_dict)
    print(card_list)
    #4.提示用户添加成功
    print("添加%s的名片成功。"% name_str)

def show_all():
    print("↓" * 20,end="进入新界面")
    print("↓" * 20)
    print("显示所有名片界面")
    #判断是否存在名片记录，如果没有，提示用户并且返回
    if len(card_list) == 0:
        print("当前没有任何名片存储，请先添加。")
        #return可以返回一个函数的执行结果、
        #下方的代码不会被执行
        #如果return后面没有任何内容，表示会返回到调用函数的位置
        #并且不返回任何结果
        return
    #打印表头
    for name in ["姓名","电话","QQ","邮箱"]:
        print(name,end="\t\t")
    print("")
        #打印分割线
    print("="*50)
        #遍历名片列表依次输出字典的信息
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t"% (card_dict["name"],card_dict["phone"],card_dict["qq"],card_dict["email"]))


def search_card():
    print("↓" * 20,end="进入新界面")
    print("↓" * 20)
    print("搜索名片界面")
    #1.提示用户要搜索的姓名
    #2.遍历名片列表，查询要搜索的姓名，如果没有找到要提示用户
    find_name = input("输入要查找的姓名：")
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("="*50)
            print("%s\t\t%s\t\t%s\t\t%s\t\t"% (card_dict["name"],card_dict["phone"],card_dict["qq"],card_dict["email"]))
            deal_card(card_dict)
            break
    else :
        print("抱歉，没有找到 %s.请重新核对信息。" % find_name)

def deal_card(find_dict):
    print(find_dict)
    action_str = input("请选择要执行的操作 1 修改/ 2 删除/ 3 返回上一级，请输入：")
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"],"姓名：")
        find_dict["phone"] = input_card_info(find_dict["phone"],"电话：")
        find_dict["qq"] = input_card_info(find_dict["qq"],"qq：")
        find_dict["email"] = input_card_info(find_dict["email"],"email：")
        print("修改名片成功！")
    elif action_str =="2":
        card_list.remove(find_dict)
        print("删除名片成功")

    else:
        print("成功返回上一级")

def input_card_info(dict_value,tip_message):

    #1.提示用户输入内容
    result_str = input(tip_message)
    #2.针对用户的输入进行判断，如果用户输入了内容，直接返回结果
    if len(result_str) > 0:
        return result_str
    #3.如果用户没有输入内容，返回字典中原有的值
    else:
        return dict_value
card_list = []


def show_menu():
    print("*" * 50)
    print("欢迎使用【名片管理系统】v1.0")
    print("")
    print("1.新建名片")
    print("2.显示全部")
    print("3.查询名片")
    print("")
    print("0.退出系统")
    print("*" * 50)


def new_card():
    print("*" * 50)
    print("功能：新建名片")

    name = input("请输入姓名：")
    phone = input("请输入电话：")
    qq = input("请输入qq号：")
    email = input("请输入邮箱")

    card_dict = {"name": name,
                 "phone": phone,
                 "qq": qq,
                 "email": email}
    card_list.append(card_dict)

    print(card_list)
    print("成功添加 %s" % card_dict)

    print(card_list)


def show_all():
    if len(card_list) == 0:
        print("提示：没有任何名片记录")
        return

    for name in ["姓名", "电话", "qq号", "邮箱"]:
        print(name, end="\t\t\t")
    print("")

    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t\t%s" % (card_dict["name"],
                                          card_dict["phone"],
                                          card_dict["qq"],
                                          card_dict["email"]))
    print("*" * 50)


def search_all():
    find_name = input("请输入检索对象")
    print("*" * 50)
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            for name in ["姓名", "电话", "qq号", "邮箱"]:
                print(name, end="\t\t")
            print("")
            print("%s\t\t\t%s\t\t\t%s\t\t\t%s" % (card_dict["name"],
                                                  card_dict["phone"],
                                                  card_dict["qq"],
                                                  card_dict["email"]))
            print("*" * 50)
            deal_card(card_dict)

            break
    else:
        print("没有找到")
    print("*" * 50)


def deal_card(find_dict):
    print(find_dict)

    action_str = input("请选择要执行的操作  【1】修改 【2】删除 【0】结束")
    print("")
    if action_str == "1":

        find_dict["name"] = input_card_info(find_dict["name"], "请输入姓名：")
        find_dict["phone"] = input_card_info(find_dict["phone"], "请输入电话：")
        find_dict["qq"] = input_card_info(find_dict["qq"], "请输入qq号：")
        find_dict["email"] = input_card_info(find_dict["email"], "请输入邮箱")
        print("%s 的名片修改成功" % find_dict)

    elif action_str == "2":
        card_list.remove(find_dict)
        print("删除成功")

    elif action_str == "0":
        print("结束")


def input_card_info(dict_value, tip_message):

    result_str = input(tip_message)

    if len(result_str) > 0:
        return result_str
    else:
        return dict_value

import card_tools


while True:

    card_tools.show_menu()
    action = input("请输入您的操作：")
    print("您的操作是 %s " % action)

    if action == "1":
        card_tools.new_card()
    elif action == "2":
        card_tools.show_all()
    elif action == "3":
        card_tools.search_all()
    elif action == "0":
        print("退出系统")
        break
    else:
        print("输入错误，请重新输入")



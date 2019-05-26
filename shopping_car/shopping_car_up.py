# -*- encoding: utf-8 -*-
# __author: iamironman
# @file: shopping_car_2.py
# @time: 2019年01月01日
# @email: 875674794@qq.com


import os


def deduction_of_money():  # 结算后扣钱
    with open('user_account_balance_file.txt', encoding='utf-8', mode='r') as f_user_account_revise, \
            open('user_account_balance_file.bak', encoding='utf-8', mode='w') as f_user_account_bak:
        for user_account_line_revise in f_user_account_revise:
            user_account_line_revise_list = user_account_line_revise.strip().split()
            if user_account_line_revise_list:
                if user_account_name == user_account_line_revise_list[0]:
                    user_account_line_revise_list[1] = str(
                        int(user_account_line_revise_list[1]) - total_price)
                f_user_account_bak.write(' '.join(user_account_line_revise_list))
                f_user_account_bak.write('\n')
    os.remove('user_account_balance_file.txt')
    os.rename('user_account_balance_file.bak', 'user_account_balance_file.txt')


def recharge_money_read():  # 读取用户账户余额文件的充值钱数
    user_account_balance_read = 0
    with open('user_account_balance_file.txt', encoding='utf-8', mode='r') as f_user_account_read:
        for user_account_line in f_user_account_read:
            user_account_line_list = user_account_line.strip().split()
            if user_account_line_list:
                if user_account_name == user_account_line_list[0]:
                    user_account_balance_read = int(user_account_line_list[1])
    return user_account_balance_read


def recharge_money():  # 升级：充钱功能
    with open('user_account_balance_file.txt', encoding='utf-8', mode='r') as f1, \
            open('user_account_balance_file.bak', encoding='utf-8', mode='w') as f2:
        user_recharge_money = input('请输入充值金额：').strip()
        if user_recharge_money.isdigit():
            user_recharge_money = int(user_recharge_money)
            for line in f1:
                line_list = line.strip().split()
                if line_list:
                    if user_account_name == line_list[0]:
                        line_list[1] = str(
                            int(line_list[1]) + user_recharge_money)
                    f2.write(' '.join(line_list))
                    f2.write('\n')
        else:
            print('请输入数字！')
    os.remove('user_account_balance_file.txt')
    os.rename('user_account_balance_file.bak', 'user_account_balance_file.txt')


def not_purchased_revise():  # 升级：没有买商品在购物车中存到一个文件中
    with open('shopping_car_not_purchased.txt', encoding='utf-8') as f1, \
            open('shopping_car_not_purchased.bak', encoding='utf-8', mode='w') as f2:
        list1 = f1.readlines()
        f1.seek(0)
        if user_account_name in f1.read():
            for i in range(len(list1)):
                if list1[i][:len(user_account_name)].strip() == user_account_name:
                    del list1[i]
                    str_all = str()
                    for k, v in shopping_car.items():
                        str_car = '%s %s %s %s ' % (str(k), v['name'], v['price'], str(v['mount']))
                        str_all += str_car
                    list1.append(user_account_name + ' ' + str_all + '\n')
                    f2.seek(0, 2)
                    f2.write(''.join(list1))
                    break
        else:
            str_all = str()
            for k, v in shopping_car.items():
                str_car = '%s %s %s %s ' % (str(k), v['name'], v['price'], str(v['mount']))
                str_all += str_car
            list1.append(user_account_name + ' ' + str_all + '\n')
            f2.seek(0, 2)
            f2.write(''.join(list1))
    os.remove('shopping_car_not_purchased.txt')
    os.rename('shopping_car_not_purchased.bak', 'shopping_car_not_purchased.txt')


def purchase_information():  # 用户购买的商品，数量，单价，此次共消费多少钱，账户余额作为购买信息写入文件
    with open('purchase_information.txt', encoding='utf-8') as f1, \
            open('purchase_information.bak', encoding='utf-8', mode='w') as f2:
        list1 = f1.readlines()
        f1.seek(0)
        if user_account_name in f1.read():
            for i in range(len(list1)):
                if list1[i][:len(user_account_name)].strip() == user_account_name:
                    del list1[i]
                    str_all = str()
                    for k, v in shopping_car.items():
                        str_car = '%s %s %s %s ' % (str(k), v['name'], v['price'], str(v['mount']))
                        str_all += str_car
                    list1.append(user_account_name + ' ' + str_all + str(total_price) + str(balance) + '\n')
                    f2.seek(0, 2)
                    f2.write(''.join(list1))
                    break
        else:
            str_all = str()
            for k, v in shopping_car.items():
                str_car = '%s %s %s %s ' % (str(k), v['name'], v['price'], str(v['mount']))
                str_all += str_car
            list1.append(user_account_name + ' ' + str_all + str(total_price) + str(balance) + '\n')
            f2.seek(0, 2)
            f2.write(''.join(list1))
    os.remove('purchase_information.txt')
    os.rename('purchase_information.bak', 'purchase_information.txt')


def print_product():  # 封装显示购物车商品功能
    for shopping_car_title, shopping_car_dict in shopping_car.items():
        if shopping_car_dict['mount'] == 0:
            continue
        else:
            print('{}\t{}\t{}\t{}'.format(shopping_car_title, shopping_car_dict[title_name],
                                          shopping_car_dict[title_price],
                                          shopping_car_dict['mount']))


# 主程序：
# 充钱功能 用户先给自己的账户充钱：比如先充3000元。
# 账户余额文件 user account balance file.txt


with open('user_account_balance_file.txt', encoding='utf-8', mode='r+') as f_user_account:
    user_account_name = input('请输入账户名称：').strip()
    if user_account_name not in f_user_account.read():
        user_account_balance = input('请给您的账户充值：').strip()
        if user_account_balance.isdigit():
            user_account_balance = int(user_account_balance)
            f_user_account.seek(0, 2)
            f_user_account.write('{} {}\n'.format(user_account_name, user_account_balance))
        else:
            print('请输入数字！')
# 读取商品信息文件product_info.txt将文件中的数据转化成goods变量

with open('product_info.txt', encoding='utf-8', mode='r') as f_product:
    title_list = f_product.readline().strip().split()  # ['name', 'price']
    title_name = title_list[0]
    title_price = title_list[1]
    goods = []
    for line1 in f_product:
        dict_append = dict()
        dict_append[title_name] = line1.strip().split()[0]
        dict_append[title_price] = line1.strip().split()[1]
        goods.append(dict_append)

# 页面显示 序号 + 商品名称 + 商品价格 + n 购物车结算 + q或者Q退出程序
for serial_number, goods_dict in enumerate(goods, start=1):
    print('{}\t{}\t{}'.format(serial_number, goods_dict[title_name], goods_dict[title_price]))
print('n\t购物车结算')
print('q或者Q退出程序')

# goods=[{'name': '电脑', 'price': '1999'}, {'name': '鼠标', 'price': '10'},
# 构建购物车字典,如：shopping_car_1.1 = {1:{"name": "电脑", "price": 1999,mount:3}}
shopping_car = {}
title_list.append('mount')
# shopping_car_dict = dict.fromkeys(title_list, '')  # {'name': '', 'price': '', 'mount': ''}
for i in range(1, len(goods) + 1):
    shopping_car[i] = goods[i - 1]
    goods[i - 1]['mount'] = 0
# shopping_car_1.1={
# 1: {'name': '电脑', 'price': '1999', 'mount': 0},
# 2: {'name': '鼠标', 'price': '10', 'mount': 0},
# 3: {'name': '游艇', 'price': '20', 'mount': 0},
# }
# 用户输入选择的商品序号，然后print商品名称及商品价格
# 如果用户输入的商品序号有误，则提示输入有误，并重新输入
# 如果用户输入商品序号正确:
# 将此商品，添加到购物车，用户还可继续添加商品(重复让用户输入商品序号，直到输入n结算或q或Q退出）
# 用户输入n为计算购物车总价，依次显示用户购物车里面的商品，数量及单价
while 1:
    choice_product = input('请输入商品序号/n结算/q、Q退出').strip()
    if choice_product.isdigit():
        choice_product = int(choice_product)
        if choice_product in range(1, len(goods) + 1):
            shopping_car[choice_product]['mount'] += 1
            print('您选择了以下商品，并成功添加到购物车')
            print('{}\t{}'.format(shopping_car[choice_product][title_name], shopping_car[choice_product][title_price]))
        else:
            print('没有该商品，请重新输入：')
    elif choice_product == 'n':
        print('您购物车里的商品如下：')
        print_product()
        break
    elif choice_product.upper() == 'Q':
        print('未购买商品如下：')
        print_product()
        not_purchased_revise()
        break
    else:
        print('请输入数字！')
# 计算用户购物车的总价
single_price = 0
total_price = 0
for shopping_car_dict_mount in shopping_car.values():
    single_price = int(shopping_car_dict_mount[title_price]) * int(shopping_car_dict_mount['mount'])
    total_price += single_price

# 并与购物车总价比较
# 若充值的钱数<总价，则让用户删除某商品，直至用户余额大于购物车总价
# 若充值的钱数>=总价，则显示购买成功 ，并修改用户账户余额文件为用户余额减去购物车总价
# 读取用户账户钱数
user_account_balance_read = recharge_money_read()
if choice_product.upper() == 'N':
    while 1:
        if user_account_balance_read < total_price:
            choice_balance = input('您的余额不足，目前余额为%s,请输入商品序号删除某个商品,输入r/R充值，输入q/Q退出：' \
                                   % user_account_balance_read).strip()
            if choice_balance.isdigit():
                choice_balance = int(choice_balance)
                if choice_balance in range(1, len(shopping_car) + 1):
                    shopping_car[choice_balance]['mount'] -= 1
                    if shopping_car[choice_balance]['mount'] == -1:
                        shopping_car[choice_balance]['mount'] += 1
                        print('您输入的商品序号没有添加到购物车，删除失败，请输入正确序号：')
                    else:
                        print('删除成功！')
                        total_price -= int(shopping_car[choice_balance][title_price])
                        print('您购物车里的商品如下：')
                        print_product()
                else:
                    print('没有该商品！请输入正确的商品序号！')
            elif choice_balance.upper() == 'R':
                recharge_money()
                user_account_balance_read = recharge_money_read()
            elif choice_balance.upper() == 'Q':
                print('您有以下商品未购买:')
                print_product()
                not_purchased_revise()
                break
            else:
                print('请输入数字！')
        elif user_account_balance_read >= total_price:
            count1_sum = 0
            for count1 in shopping_car.values():
                count1_sum += int(count1['mount'])
            if count1_sum:
                balance = int(user_account_balance_read) - total_price
                print('购买成功!您此次购买了如下商品：')
                print_product()
                print('您此次一共消费了%s元' % total_price)
                print('您目前的余额是%d' % balance)
                deduction_of_money()
                purchase_information()
                break
            else:
                print('您的购物车中没有任何商品，购买失败！')
                break

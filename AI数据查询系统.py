import pymysql

ip_address = "rm-2zewoy4d914af4lepqo.mysql.rds.aliyuncs.com"
admin_id = "test_account"
admin_password = "QWer1234"
using_database = "ai_database"

db = pymysql.connect(host=ip_address, port=3306, user=admin_id, password=admin_password, database=using_database)
cursor = db.cursor()
cursor.execute("select * from user_information")
data = cursor.fetchall()
print(data[-1])


#用户注册#
def user_register():
    while True:
        a=str(input("请注册，输入用户名："))
        b=eval(input("请输入密码："))
        #判断密码长度是否在6-16位之间
        if 5<len(b)<17:
            #连接数据库
            db = pymysql.connect(host=ip_address, port=3306, user=admin_id, password=admin_password, database=using_database)
            u1 = db.cursor()
            u1.execute("select user_name from user_information")
            data1 = u1.fetchall()
            name_lst = []
            #判断用户名是否在表中
            for name in data1:
                name_lst.append()
            if a in name_lst:
                print("用户名已存在！")
            else:
                u1.execute("insert into user_information (user_name,user_password) values (a,b)" )
                print("注册成功！")
            db.commit()
            u1.close()
            db.close()
            break
        else:
            print("密码设置不合法！")
            continue
        
        
#用户登录#
def user_signin(my_user,my_password):
    while True:
        my_user = input("请输入用户名：")
        my_password = eval(input("请输入密码："))
    #创建列表用于判段用户名密码是否在表中以及是否对应
    my_list = []
    my_user_list = []
    my_password_list = []
    #连接数据库
    db = pymysql.connect(host=ip_address, port=3306, user=admin_id, password=admin_password, database=using_database)
    u2 = db.cursor()
    u2.execute("select user_name,user_password from user_information")
    data2 = u2.fetchall()
    u2.close()
    db.close()
    
    for item in data2:
        my_list.append(item)
        #用户数据列表
        my_user_list.append(item[1])
        #密码数据列表
        my_password_list.append(item[2])
        
    for i,list in enumerate(my_list):
        #判断用户名是否在表中
        if my_user in my_user_list:
            #判断密码是都在表中
            if my_password in my_password_list:
                #判断用户名与密码是否对应
                for list in my_list:
                    if my_user_list.index(my_user) == my_password_list.index(my_password):
                        print("登陆成功！")
                    else:
                        print("密码错误！")
            else:
                print("密码错误！")
        
        else:
            print("用户名错误！")
                
#群组注册
def creat_group():
    while True:
        a = str(input('请输入想要创建的群组名：'))
        b = str(input('请输入创建者用户名：'))
        #连接数据库
        db = pymysql.connect(host=ip_address, port=3306, user=admin_id, password=admin_password, database=using_database)
        u1 = db.cursor()
        u1.execute("select group_name from group_information")
        data1 = u1.fetchall()
        u2 = db.cuisor()
        u2.execute('select user_name from user_information')
        data2 = u2.fetchall()
        group_lst = []
        name_lst = []
        #判断用户名是否在表中
        for group in data1:
            group_lst.append()
        for name in data2:
            name_lst.append()
        if a in group_lst:
            print("群组已存在！")
        elif b in name_lst:
            print('用户名不在范围内！')
        else:
            u1.execute("insert into group_information (group_name,group_creator_id) values (a,b)" )
            print("创建成功！")
        db.commit()
        u1.close()
        u2.close()
        db.close()
      
        
    
    
                
                
                
                
                
                
                
                
                
                
            
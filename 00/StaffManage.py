# coding=utf-8

from pymongo import MongoClient


class StaffManage(object):

    def __init__(self):
        """
        管理员工信息的实例初始化：
            1. 连接数据库服务器
            2. 选择数据库中的数据集合
            3. 生成操作数据集合的函数字典
            4. 运行与用户交互的函数
        """
        client = MongoClient()
        self.coll = client.staff.emp
        self.operation_dict = {
            'add': self.add_emp,
            'delete': self.delete_emp,
            'update': self.update_emp,
            'show': self.show_emp,
            'help': self.help,
            'exit': exit,
        }
        self.run()

    def run(self):
        """
        启动循环，直到用户输入 'exit' 时退出
            1. 获取用户输入信息
            2. 分析输入信息来选择相应操作
        :return:
        """
        command = 'help'
        while command != 'exit':
            command = self.get_input()
            self.analysis_handler(command)
        return

    @staticmethod
    def get_input():
        """
        获取用户输入信息
        :return: command str 除首尾空格的字符串命令
        """
        command = raw_input('please input command, type "help" to show the usage:\n').strip()
        return command

    def analysis_handler(self, command):
        """
        分析用户的输入命令，执行相应的操作:
            命令是一个以 空格 区分的字符串，因此需要使用 split 将命令切分成一个 列表
                第0个元素代表命令，后面的元素是参数
        :param command: 去除前后空格的字符串命令
        :return:
        """
        if not command:
            return None
        command_list = command.split()
        operation = command_list[0]
        if operation in self.operation_dict:
            # 生成操作函数的参数
            para_dict = self.generate_para_dict(command_list[1:])
            # 当 操作是 'help', 'exit'时，不需要参数
            self.operation_dict[operation](para_dict) \
                if operation not in ['help', 'exit'] else self.operation_dict[operation]()
        else:
            # 当 不是支持的操作时，显示帮助信息
            self.operation_dict['help']()
        return

    @staticmethod
    def generate_para_dict(para_list):
        """
        生成命令操作函数所需的参数字典
        :param para_list: 参数字符串
        :return: 参数字典
        """
        para_dict = {}
        try:
            for para in para_list:
                name, value = para.split('=')
                para_dict[name] = value
            return para_dict
        except Exception as e:
            print 'the para error: {}'.format(e)

    def add_emp(self, para_dict):
        """
        新增员工信息
        :param para_dict: 包含员工信息的字典参数
        :return:
        """
        col_name_set = ['id', 'name', 'age', 'sex', 'salary']

        def check_if_id_exists(emp_id):
            """
            遍历数据查询 id 是否存在
            :param emp_id: 员工id
            :return: 如果存在返回 False，存在返回 True
            """
            return True if [x for x in self.coll.find({'id': emp_id})] else False

        try:
            if set(para_dict.keys()) != set(col_name_set):
                print 'info is incomplete! can not add to database'
                return
        except Exception as e:
            print 'the para_dict is invalid!', e
            return

        if not para_dict or 'id' not in para_dict:
            print 'everyone must have id!'
            return

        exi = check_if_id_exists(para_dict['id'])
        if exi:
            print 'id has already exists, please change to another one'
            return
        try:
            self.coll.insert(para_dict)
        except Exception as e:
            print 'sorry, insert info error because: {}'.format(e)
        return

    def delete_emp(self, para_dict):
        """
        删除员工信息，必须指定 id 值
        """
        if not para_dict:
            print 'you have to identify who you want to delete'
            return
        try:
            result = self.coll.delete_many(para_dict)
            result = "you have delete {} persons(s)".format(result.deleted_count)
        except Exception as e:
            result = "delete employee's info error: {}".format(e)
        self.show_result(result)
        return

    def update_emp(self, para_dict):
        """
        更新员工信息，id 是必须的
        :return:
        """
        if not para_dict or 'id' not in para_dict:
            print 'please use id to identify person'
            return None
        set_dic = {}
        emp_id = para_dict['id']
        try:
            for key, value in para_dict.items():
                if key != 'id':
                    set_dic[key] = value
            self.coll.update_one({'id': emp_id}, {'$set': set_dic})
        except Exception as e:
            print 'update info error, because: {}'.format(e)
        return

    def show_emp(self, paras_dict):
        """
        显示员工信息，当没有指定参数时显示所有员工的信息
        :param paras_dict: 参数字典
        :return:
        """
        if paras_dict:
            try:
                result = self.coll.find(paras_dict)
                self.show_result(result)
            except Exception as e:
                print 'find info error: {}'.format(e)
        else:
            try:
                result = self.coll.find()
                self.show_result(result)
            except Exception as e:
                print 'find info error: {}'.format(e)
        return

    def help(self):
        """
        帮组操作
        :return: 帮助信息
        """
        result = '''
        the basic usage is like this:

        command [col_title=info [,col_title2=info2 [, ...] ] ]

        for example:

        show
        show id=1
        show age=20 name=carson

        add id=8 name=carson sex=male salary=22222

        del id=3

        update id=2 name=carson
        '''
        self.show_result(result)

    @staticmethod
    def show_result(result):
        if type(result) == str:
            print result
        else:
            table = 'id'.ljust(20) + \
                'name'.ljust(20) + \
                'age'.center(20) + \
                'sex'.center(20) + \
                'salary'.rjust(20) + '\n'
            for emp in result:
                try:
                    table += str(emp['id']).ljust(20) + \
                        emp['name'].ljust(20) + \
                        str(emp['age']).center(20) + \
                        emp['sex'].center(20) + \
                        str(emp['salary']).rjust(20) + '\n'
                except Exception as e:
                    print 'error, because: {}'.format(e)
            print table
        return

if __name__ == '__main__':
    staff_manage = StaffManage()

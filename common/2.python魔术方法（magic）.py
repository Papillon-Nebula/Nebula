from typing import Mapping


class User:
    table_name = 'users'

    def  __init__(self) -> None:
        self.username = 'mike'
        self.password = '1111'
        self.email = 'email@qq.com'

    def method(self, value):
        print("Hello %s" % value)

    # 链式操作，底部47行查看效果
    def chain(self):
        print("通过返回当前类的实例进行连续的方法调用")
        return self
    
    def hello(self):
        print("Hello!")
        return self


if __name__ == '__main__':
    user = User()
    print(User.__dict__)
    print(User.__class__)
    print(User.__class__.__dict__)
    print(User.__name__)
    print(user.__dict__)   # 获取实例属性或变量
    
    # 通过 __ 来区分那些是自定义的属性和方法：
    for k, v in User.__dict__.items():
        if not k.startswith('__'):
            print(k, v)

    user.nickname = 'xixi'                        # 动态为实例设置属性，不建议使用
    # user.__setattr__('nickname', 'xixihaha')      # 动态为实例设置属性（通过面向对象的方式配置）
    # setattr(user, 'nickname', 'xixihaha')      # 动态为实例设置属性（通过全局函数调用配置，面向过程）
    # print(user.__dict__)                          # 获取实例属性或变量
    print(user.__getattribute__('nickname'))
    user.__getattribute__('method')('chengdu')
    getattr(user, 'method')('beijing')


    user.chain().chain().hello()
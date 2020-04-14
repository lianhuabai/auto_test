## 接口自动化测试文档  

### 环境准备  
* 语言 python3  
* 库 pytest、requests、allure-pytest (pytest-allure-adaptor已停止更新，python3开始改用allure-pytest)  
* 开源测试报告框架 allure2(需要Java环境，jdk1.8+)

### 项目目录结构  

* Utils 自定义封装类
   * Requests.py 封装Requests请求方式
   * Email.py 邮件发送封装
   * Constans.py 变量
   * Assert.py 断言
   * Log.py 封装Log
   * Token.py 登录token获取
* Config 配置文件信息
* Datas测试数据
* TestCases 测试用例
* Reports 测试报告文档
* Logs 日志文件
* run.py 主程序入口，执行测试  
---
### 代码解析  
*配置文件封装 ./Config/config.py*  
* 封装定义ConfigParser  
```
#实例化类ConfigParser
    config = ConfigParser()
#配置文件读写方法
    def get_config(self,title,value):
        return self.config.get(title,value)

    def set_config(self,title,value,text):
        self.config.set(title,value,text)
        with open(self.congfig_path,'wb') as f:
            return self.config.write(f)

    def add_config(self,title):
        self.config.add_section(title)
        with open(self.config_path,'wb') as f:
            return self.config.write(f)
```
*日志封装./Utils/Log.py*  
* 创建日志文件函数  
```
#判断传入的路劲/文件是否存在
def create_file(file):
    path = file[0:file.rfind('/')]
    if not os.path.isdir(path):
        os.makedirs(path)
    if not os.path.isfile(file):
        fd = open(file,mode='w',encoding='utf-8')
        fd.close()
    else:
        pass
```
* 实例化日志写入流FileHandler,指定文件路劲和编码方式
```
handler = logging.FileHandler(log_file,encoding='utf-8')
```
* 日志写入函数  
```
#add Handler后再次调用此时logger存在多个Handler导致日志重复，需要后置处理remove掉Handler
    def warning(log_msg):
        add_handler('warning')
        logger.warning("[WARNING" + get_current_time() + "]" + log_msg)
        remove_handler('WARNING')
        
```


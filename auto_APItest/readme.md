## 接口自动化测试文档  

### 环境准备  
* 语言 python3  
* 库 pytest、requests、allure-pytest (pytest-allure-adaptor已停止更新，python3开始改用allure-pytest)  
* 开源测试报告框架 allure2(需要Java环境，jdk1.8+)

### 项目目录结构  

* Utils 自定义封装类
   * Requests.py 封装Requests请求方式
   * Email.py 邮件发送封装
   * Assert.py 常用断言
   * Log.py 封装Log日志打印
   * Token.py 登录token获取
   * Mock.py 自定义mock
* Config 配置文件信息  
    * Config.py 封装ConfigParser文件读取
    * config.ini 配置文件
* Datas测试数据
    * data 存放yaml测试数据文件夹
    * datas.py 测试数据以类的形式封装
    * Read_yaml.py 封装读取yaml文件
    * Constans.py 全局变量
* Tools 测试工具类文件夹
* TestCases 测试用例
* Reports 测试报告文档
* Logs 日志文件
* run.py 主程序入口，执行测试  
---
### 代码解析  
*配置文件封装 ./Config/config.py*  
* 封装定义ConfigParser  
```
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)))
    '''
    os.pardir 获取当前目录的父目录字符串名称 '..'
    os.path.dirname(path)返回path的父路劲,__file__当前脚本运行的路劲
    os.path.join(path,name)连接目录与文件名
    os.path.abspath(name)返回脚本的绝对路劲
    '''
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
#判断传入的路劲是否存在
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
*Utils/Requests.py封装requests的get、post请求* 
```
    def post(self,url,headers,data):
        try:
            response = requests.post(url=url,headers=headers,data=data)

        except requests.RequestException as e:
            self.log.info("请求失败:"+ str(e)+"请求失败url"+ url)

        response_time = response.elapsed.total_seconds()
        Constans.STRESS_LIST.append(response_time)
        return response.json()
```
*Utils/Email.py 邮件发送*
```
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username,password)
        smtp.sendmail(sender,receiver,message.as_string())
    except smtplib.SMTPException as e:
        self.log.error("邮件发送失败" + str(e))

    else:
        self.log.info("邮件发送成功")
```
*Utils/Assert.py 断言封装*
```
    def assert_status(self,code,assert_code):
        '''
        请求响应状态码断言
        :data code:
        :data assert_code:
        :return:
        '''
        try:
            assert code == assert_code
            return True
        except:
            self.log.error("请求状态码对比失败,请求状态码为:{0},断言状态码为:{1}".format(code,assert_code))
            Constans.RESULT_LIST.append('fail')
            raise
```
*Datas/Read_yaml.py 读取yaml文件方法封装*
```
    def get_data_list():
        data_list = {}
        #读取原始测试数据
        data_yaml = parse()
        for page, value in data_yaml.items():
            #获取字典中参数
            parameters = value['parameter']
            list = []
            for parameter in parameters:
                print(parameter)
                list.append(parameter)
            data_list[page] = list
        print(data_list)
        return data_list
```
*run.py 测试执行入口*
``` 
    #执行用例，设置报告路劲
    pytest.main(['-s','-v','--alluredir',xml_report_path])
    #生成html测试报告并指定路劲
    allure generate xml_path -o html_path
    
```


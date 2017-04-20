# Common
该项目包含一些公共的有用的工具,方法,算法等

1.useful.py

    is_normal_url:
        将url字符串进行检查,返回是否是合法的url字符串,True代表是,False代表否

    paser_urls:
        使用正则表达式获取字符串content中包含的所有的url

    analysis_url:
        将url进行分解,返回该url使用的协议,主机名,端口号,路径

    get_file_name:
        根据file_type生成一个唯一的文件名

    get_md5:
        将data字符串进行md5并返回

    get_randints:
        随机获取从[start -> end)之间的n个不相同的整数,若n比该区间大,就返回该区间打乱顺序的随机数

2.useful2.py

    def checkip:
        判断ip是否是正确的ip地址True--是ip地址,False--不是ip地址

    def is_legal_phone:
        判断字符串是否是合理的电话号码

    def revert_to_str:
        将时间戳转换为日期字符串,时间戳为精确到秒的整数

    def revert_to_timestamp:
        将日期字符串转换为时间戳

3.idcard.py

    def get_age_from_idcard:
        通过身份证号计算年龄 [23,9,2]--23岁,9个月2天

    def get_gender_from_idcard:
        通过身份证号获取性别 -1---身份证号不正确;1---表示男;2---表示女

4.word_cut.py

    def word_cut:
        将字符串content按照model模式分词 model 分别有全模式(all) ,精确模式(accurate),搜索引擎模式(search_engine)三种

5.mycrypt.py

    class myCrypt:
        使用pycrypto模块进行加密和解密 对称加密:AES

        def encrypt:
            加密函数，如果text不是16的倍数【加密文本text必须为16的倍数！】，那就补足为16的倍数

        def decrypt:
            解密后，去掉补足的空格用strip() 去掉

6.mybase64.py

    class myBase64:
        字符串和base64编码的互相转换

        def b64encode:
            将字符串s 经过base64编码

        def b64decode:
            将b64 通过base64解码

7.mypickle.py

    class myPickle:
        将一个Python对象序列化和反序列化

        def dumps:
            将一个Python对象序列化为字符串

        def loads:
            将字符串反序列化为Python对象

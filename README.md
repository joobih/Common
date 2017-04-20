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

    checkip:
        判断ip是否是正确的ip地址True--是ip地址,False--不是ip地址

    is_legal_phone:
        判断字符串是否是合理的电话号码

    revert_to_str:
        将时间戳转换为日期字符串,时间戳为精确到秒的整数

    revert_to_timestamp:
        将日期字符串转换为时间戳

3.idcard.py

    get_age_from_idcard:
        通过身份证号计算年龄 [23,9,2]--23岁,9个月2天

    get_gender_from_idcard:
        通过身份证号获取性别 -1---身份证号不正确;1---表示男;2---表示女

4.word_cut.py

    word_cut:
        将字符串content按照model模式分词 model 分别有全模式(all) ,精确模式(accurate),搜索引擎模式(search_engine)三种

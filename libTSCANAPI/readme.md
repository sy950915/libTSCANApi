<!--
 * @Author: seven 865762826@qq.com
 * @Date: 2023-06-11 14:07:18
 * @LastEditors: seven 865762826@qq.com
 * @LastEditTime: 2023-06-11 15:48:44
-->

如果需要本库能直接集成进入Python-can

只需要将config.py文件中的IS_ADD_PYTHON_CAN设置为True即可

注意：IS_ADD_PYTHON_CAN = True后需要调用本库运行一次，将配置文件写入到python-can中，之后就可以直接使用，不需要再做此配置

使用TSDB.py库时需注意：本库在开始运行时，会将dbc.py文件直接剪切至cantools库中进行替换（原因是cantools解析dbc时没有判断报文类型，因此在原基础上，本库下的dbc.py增加了一个函数进行识别报文为can 还是canfd报文）


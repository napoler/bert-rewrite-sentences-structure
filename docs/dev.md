python生成依赖环境常用操作
========================
## 创建虚拟环境
在当前目录创建虚拟环境：
　
 
> python3 -m venv . 
　

 


## 激活虚拟环境
在Posix标准平台下：

```

source <venv>/bin/activate

```

##　安装依赖
生成requirements.txt文件
pip freeze > requirements.txt

安装requirements.txt依赖
pip install -r requirements.txt


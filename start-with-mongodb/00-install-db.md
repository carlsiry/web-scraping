# MongoDB 安装和使用

linux 系统环境下：

```
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927

# ubuntu 14
echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list

# ubuntu 16
echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list

apt-get update

apt-get install -y mongodb-org

# 固定版本
echo "mongodb-org hold" | sudo dpkg --set-selections
echo "mongodb-org-server hold" | sudo dpkg --set-selections
echo "mongodb-org-shell hold" | sudo dpkg --set-selections
echo "mongodb-org-mongos hold" | sudo dpkg --set-selections
echo "mongodb-org-tools hold" | sudo dpkg --set-selections

```

Mac 系统环境下：

```

使用homebrew安装：

brew update
brew install mongodb
```

Windows 系统环境下：

```
1)下载并安装：https://www.mongodb.com/download-center?jmp=nav#community

2)创建文件夹用来存放数据文件：D:\MongoDB\DB

3)在MongoDB的安装文件夹中，按住Shift键并点击鼠标右键，选择“在此处打开命令窗口”，然后输入以下代码启动MongoDB：

mongod.exe --dbpath D:\MongoDB\DB
```

MongoDB官方文档：https://docs.mongodb.com/manual/administration/install-community/

## MongoDB 基本使用

```
# 启动MongoDB
sudo service mongod start

# 查看服务状态
sudo service mongod status

# 远程连接配置
vim /etc/mongod.conf
vim: #bind_ip 127.0.0.1 监听所有外网ip

# 下载管理脚本
wget https://github.com/mongodb/mongo/raw/master/debian/init.d
sudo mv init.d /etc/init.d/mongodb
sudo chmod +x /etc/init.d/mongodb

# 修改内核
sudo sh -c 'echo never > /sys/kernel/mm/transparent_hugepage/enabled'
sudo sh -c 'echo never > /sys/kernel/mm/transparent_hugepage/defrag'

# 卸载
sudo service mongod stop
sudo apt-get purge mongodb-org*
sudo rm -r /var/log/mongodb
sudo rm -r /var/lib/mongodb

# 查看配置文件
vim /etc/mongod.conf

#设置开机启动
sudo systemctl enable mongod

#取消开机启动
sudo systemctl disable mongod
```


## 图形化图形化管理工具

- RoboMongo：https://robomongo.org/download
- MongoDB Compass: mongodb 官网

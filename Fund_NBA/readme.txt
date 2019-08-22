创建数据库nba

python版本python3.5
安装python模块
pymysql
django


环境安装好之后，按下面步骤运行
1.进入网页NBA_web目录
  执行python3 manage.py migrate

  运行python3 manage.py runserver 127.0.0.1:8999
  浏览器输入http://127.0.0.1:8999

2.进入爬虫目录spider
   运行爬虫python3 get_NBAdata.py
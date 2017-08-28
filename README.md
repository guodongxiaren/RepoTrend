# RepoTrend
本项目用于GitHub中某一仓库的fork和star的趋势监控及绘制图表 
 
可定制性极强，你也可以监控其他你感兴趣的事件。
## 配置文件
1. 将 trend.json 重命名为 trend.local.json (或者修改配置文件中的路径为trend.json)

2. 将 config.json 重命名为 config.local.json(或者修改脚本文件中的路径为config.json)，并修改文件中的配置信息 
## 计划任务
1. 确保你的机器已安装crontab

2. 修改repotrend文件中的用户名（foo）为你的用户名，python命令后面的脚本路径改为你的该repo.py脚本所在的绝对路径

3. 将repotrend文件放到crontab的目录下，通常为：/etc/cron.d/


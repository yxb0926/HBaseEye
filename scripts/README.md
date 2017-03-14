# Hbase Region Server 及 HDFS 监控及报警
通过jmx采集数据，然后经过健康检查，进行短信及邮件报警。

#### 部署方式：
配置简单的cron任务即可，如下：
<pre>
<code>
*/5 * * * * hdfsMonitor.py >> /tmp/hdfsMonitor.log
*/5 * * * * regionMonitor.py >> /tmp/regionMonitor.log
</code>
</pre>

#### 注意事项：
要使用该脚步，你需要修改几个地方。

- 修改hdfsMonitor.py 和 regionMonitor.py 中main()函数的host|port 值为你服务器的值；
- 修改HbaseMonitor.py中sedMail()和sedMsg()函数中邮箱地址、密码为你的邮箱地址及密码。sedMsg()可能需要改为你的短信接口。


3Ks.

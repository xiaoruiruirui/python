# http协议是浏览器在请求服务器的时候的一种规范，目前一般是http/1.1版本的。
# 浏览器在对服务器发出请求时（比如在浏览器输入服务器的ip和端口:127.0.0.1:8080,
# 没有添加/和html文件，会在下面的显示信息中GET / 后面显示空格。
# 如果添加了html文件，会在GET/后面显示该html的地址信息，
# 服务器收到信息会将数据打包发给浏览器，用户就可以看到需要的信息，比如网页，浏览器会自动解压解析数据包），
# 会给服务器发出请求信息，下面是用浏览器给udptcp测试助手tcp服务器发送请求时，发送的信息。

#GET是客户端像服务器发送请求

# 【Receive from 127.0.0.1 :62700】：GET / HTTP/1.1
# Host: 127.0.0.1:8080
# Connection: keep-alive
# Cache-Control: max-age=0
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36
# Sec-Fetch-User: ?1
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
# Sec-Fetch-Site: cross-site
# Sec-Fetch-Mode: navigate
# Accept-Encoding: gzip, deflate, br
# Accept-Language: zh-CN,zh;q=0.9

# 服务器的应答（检查网页代码，network,name,右侧会显示）：会将http协议header和body(代码，在浏览器自动解析成网页)，发给用户，用户可以查到。

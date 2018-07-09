# pybp - a simple HTTP interception with Scapy*

In recent, Our branch need a HTTP interceptor (with Intruder and Repeater for modify HTTP requests).
There is no python package can be found and use, without MITM mode(Only sniff).
The 'pyby' using 'Scapy' module to implemention basic features.
Apparently, we wanted to make a burpsuite with Python.
For convenience when you are audit a web application in automation (or half-automation).


Make modify as you want!

## 0. Requirements
In Python 2.7 env.
- Scapy==2.4.0
- Scapy-http==1.8.0

## 1. Support Protocols

- HTTP GET / POST

## 2. Data fetch

1.  GET
    - URL
    - Request Header


2.  POST
    - URL
    - Request Header
    - Data

## 3. Examples

- GET request:
Format :
TIME - METHOD - URL - DATA

```shell
2018-07-09 10:26:48.818615 - GET - http://test.com/?id=123123&pppp=123123123
{
  "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
  "Accept-Encoding": "gzip, deflate",
  "Path": "/?id=123123&pppp=123123123",
  "Cache-Control": "max-age=0",
  "Connection": "keep-alive",
  "Accept":
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
  "User-Agent":
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36",
  "Headers":
    "Accept-Language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7\r\nAccept-Encoding: gzip, deflate\r\nIf-Modified-Since: Mon, 02 Jul 2018 02:57:14 GMT\r\nConnection: keep-alive\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36\r\nDNT: 1\r\nHost: test.com\r\nCache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1",
  "Host": "test.com",
  "If-Modified-Since": "Mon, 02 Jul 2018 02:57:14 GMT",
  "Additional-Headers": "DNT: 1\r\nUpgrade-Insecure-Requests: 1\r\n",
  "Http-Version": "HTTP/1.1",
  "Method": "GET"
}

```

- POST request:

```
2018-07-09 10:31:20.216071 - POST - http://coolaf.com/tool/ajaxhzp - article=%E4%BD%A0%E5%A5%BD%0A&aid=2
{
  "Content-Length": "35",
  "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
  "Accept-Encoding": "gzip, deflate",
  "Method": "POST",
  "Connection": "keep-alive",
  "Accept": "application/json, text/javascript, */*; q=0.01",
  "User-Agent":
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36",
  "Headers":
    "Origin: http://coolaf.com\r\nCookie: urladd=\r\nContent-Length: 35\r\nAccept-Language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nAccept: application/json, text/javascript, */*; q=0.01\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36\r\nDNT: 1\r\nHost: coolaf.com\r\nX-Requested-With: XMLHttpRequest\r\nReferer: http://coolaf.com/tool/hzp\r\nContent-Type: application/x-www-form-urlencoded; charset=UTF-8",
  "Host": "coolaf.com",
  "Referer": "http://coolaf.com/tool/hzp",
  "Path": "/tool/ajaxhzp",
  "Cookie": "urladd=",
  "Http-Version": "HTTP/1.1",
  "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
  "Additional-Headers":
    "Origin: http://coolaf.com\r\nDNT: 1\r\nX-Requested-With: XMLHttpRequest\r\n"
}


```

## 4. TODO

- Make Beautiful Parameters for start sniffer.
- More useful(Simple) BPF compile.
- Support HTTPS (NO MITM, A new challenge!).
- Audit sensitive data in every response.
- Complete a spider.

## 5. TL;DR

Integrated with 'Sulley' and 'requests', make it like a 'burpsuite-pro'!
We are apologize that we were not running a unit test. If you found any bugs or have any advance, make an issue in this repository.

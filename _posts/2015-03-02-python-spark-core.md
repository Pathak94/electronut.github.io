---
layout: post
title: A Python script to talk to the Spark Core
excerpt: "A Python script to communicate with the Spark Core using their cloud API, which lists registered Cores as well as implements a Server Sent Events (SSE) notification scheme that uses Spark.publish()."  
tags: [Spark Core, WiFi, IoT, Python]
categories: [Python, Electronics]
comments: true
modified:
image:
  feature: header.jpg
---

I have been playing around with the [Spark Core][1] and am very
impressed with the built-in software support from Spark. This is a
quick project that uses Python to talk to the Spark Core using the
Spark cloud API. I also wanted the Spark Core to sent notifications to
my program, and for this I am using `Spark.publish()` and *Server Sent
Events (SSE)*.

Here is a sample run of the program. (You can get the *access token* from Spark Build IDE.)

```
$ python talk_spark.py --at XXXX_ACCESS_TOKEN --list
[{u'connected': True, u'last_heard': u'2015-02-26T02:17:22.450Z', u'last_app': None, u'id': u'xxxxxxx', u'name': u'yyyy'}]

$ python talk_spark.py --at XXXX_ACCESS_TOKEN --listen
Notification: Yo 4 at 2015-02-26T01:59:02.272Z
Notification: Yo 5 at 2015-02-26T01:59:07.278Z
Notification: Yo 6 at 2015-02-26T01:59:12.281Z
^Cexiting.
```

You can find the source files for the project here, which has the Python code, 
as well as a simple Spark Core program for testing notifications.

[https://github.com/electronut/talk_spark][2]


I look forward to playing with the Spark Photon soon!

[1]: https://www.spark.io/
[2]: https://github.com/electronut/talk_spark 
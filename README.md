CTDB ec2 VIP support
====

This project is about collecting scripts to support CTDB based HA
on AWS infrastructure

Currently supported configuration is AWS instances running under a
VPC (Virtual Private Cloud)

Usage
====

Please follow Amazon docs for setting up ec2 tools on a Linux instance [1]

On your Linux box, please do
~~~
$ git clone git://github.com/harshavardhana/ctdb-ec2.git
$ cd ctdb-ec2/
$ make dist
$ make rpm
~~~

You have your RPM ready to be installed on AWS nodes.

[1] - http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/SettingUp_CommandLine.html

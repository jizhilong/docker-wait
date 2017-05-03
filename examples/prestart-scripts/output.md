```
Building dresponse
Step 1/3 : FROM jizhilong/docker-wait
 ---> 010f75a0cb79
Step 2/3 : ADD dresponse.cfg /etc/docker-wait/dresponse.cfg
 ---> Using cache
 ---> bd20184081f4
Step 3/3 : ADD scripts /var/lib/docker-wait/prestart
 ---> Using cache
 ---> 356ec4543744
Successfully built 356ec4543744
Recreating prestartscripts_dresponse_1
Recreating prestartscripts_normal-container_1
Attaching to prestartscripts_dresponse_1, prestartscripts_normal-container_1
[36mdresponse_1         |[0m *** Starting uWSGI 2.0.15 (64bit) on [Sun Apr 30 23:59:33 2017] ***
[36mdresponse_1         |[0m compiled with version: 4.9.2 on 30 April 2017 11:01:08
[36mdresponse_1         |[0m os: Linux-4.9.13-moby #1 SMP Sat Mar 25 02:48:44 UTC 2017
[36mdresponse_1         |[0m nodename: moby
[36mdresponse_1         |[0m machine: x86_64
[36mdresponse_1         |[0m clock source: unix
[36mdresponse_1         |[0m pcre jit disabled
[36mdresponse_1         |[0m detected number of CPU cores: 4
[36mdresponse_1         |[0m current working directory: /
[36mdresponse_1         |[0m detected binary path: /usr/local/bin/uwsgi
[36mdresponse_1         |[0m uWSGI running as root, you can use --uid/--gid/--chroot options
[36mdresponse_1         |[0m *** WARNING: you are running uWSGI as root !!! (use the --uid flag) *** 
[36mdresponse_1         |[0m *** WARNING: you are running uWSGI without its master process manager ***
[36mdresponse_1         |[0m your memory page size is 4096 bytes
[36mdresponse_1         |[0m detected max file descriptor number: 1048576
[36mdresponse_1         |[0m lock engine: pthread robust mutexes
[36mdresponse_1         |[0m thunder lock: disabled (you can enable it with --thunder-lock)
[36mdresponse_1         |[0m uwsgi socket 0 bound to UNIX address /var/run/dwait/dwait.sock fd 3
[36mdresponse_1         |[0m Python version: 2.7.13 (default, Apr 26 2017, 19:32:55)  [GCC 4.9.2]
[36mdresponse_1         |[0m *** Python threads support is disabled. You can enable it with --enable-threads ***
[36mdresponse_1         |[0m Python main interpreter initialized at 0x144a320
[36mdresponse_1         |[0m your server socket listen backlog is limited to 100 connections
[36mdresponse_1         |[0m your mercy for graceful operations on workers is 60 seconds
[36mdresponse_1         |[0m mapped 72768 bytes (71 KB) for 1 cores
[36mdresponse_1         |[0m *** Operational MODE: single process ***
[36mdresponse_1         |[0m WSGI app 0 (mountpoint='') ready in 0 seconds on interpreter 0x144a320 pid: 9 (default app)
[36mdresponse_1         |[0m *** uWSGI is running in multiple interpreter mode ***
[36mdresponse_1         |[0m spawned uWSGI worker 1 (and the only) (pid: 9, cores: 1)
[36mdresponse_1         |[0m hostname: e13619df38af
[36mdresponse_1         |[0m image: busybox
[36mdresponse_1         |[0m image author: 
[36mdresponse_1         |[0m container labels:
[36mdresponse_1         |[0m CONTAINER_LABEL_COM_DOCKER_COMPOSE_CONFIG-HASH=94a7074cf7c0adfd47f75e502b0666f3adddc77cfe692aff8bd2a8d642dac29e
[36mdresponse_1         |[0m CONTAINER_LABEL_COM_DOCKER_COMPOSE_CONTAINER-NUMBER=1
[36mdresponse_1         |[0m CONTAINER_LABEL_COM_DOCKER_COMPOSE_VERSION=1.11.2
[36mdresponse_1         |[0m CONTAINER_LABEL_COM_DOCKER_COMPOSE_ONEOFF=False
[36mdresponse_1         |[0m CONTAINER_LABEL_COM_DOCKER_COMPOSE_SERVICE=normal-container
[36mdresponse_1         |[0m CONTAINER_LABEL_COM_DOCKER_COMPOSE_PROJECT=prestartscripts
[36mdresponse_1         |[0m lrwxrwxrwx 1 root root 0 Apr 30 23:59 /hostroot/proc/23974/root -> /
[36mdresponse_1         |[0m 1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1
[36mdresponse_1         |[0m     link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
[36mdresponse_1         |[0m     inet 127.0.0.1/8 scope host lo
[36mdresponse_1         |[0m        valid_lft forever preferred_lft forever
[36mdresponse_1         |[0m     inet6 ::1/128 scope host 
[36mdresponse_1         |[0m        valid_lft forever preferred_lft forever
[36mdresponse_1         |[0m 2: tunl0@NONE: <NOARP> mtu 1480 qdisc noop state DOWN group default qlen 1
[36mdresponse_1         |[0m     link/ipip 0.0.0.0 brd 0.0.0.0
[36mdresponse_1         |[0m 3: gre0@NONE: <NOARP> mtu 1476 qdisc noop state DOWN group default qlen 1
[36mdresponse_1         |[0m     link/gre 0.0.0.0 brd 0.0.0.0
[36mdresponse_1         |[0m 4: gretap0@NONE: <BROADCAST,MULTICAST> mtu 1462 qdisc noop state DOWN group default qlen 1000
[36mdresponse_1         |[0m     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff
[36mdresponse_1         |[0m 5: ip_vti0@NONE: <NOARP> mtu 1332 qdisc noop state DOWN group default qlen 1
[36mdresponse_1         |[0m     link/ipip 0.0.0.0 brd 0.0.0.0
[36mdresponse_1         |[0m 6: ip6_vti0@NONE: <NOARP> mtu 1500 qdisc noop state DOWN group default qlen 1
[36mdresponse_1         |[0m     link/tunnel6 :: brd ::
[36mdresponse_1         |[0m 7: sit0@NONE: <NOARP> mtu 1480 qdisc noop state DOWN group default qlen 1
[36mdresponse_1         |[0m     link/sit 0.0.0.0 brd 0.0.0.0
[36mdresponse_1         |[0m 8: ip6tnl0@NONE: <NOARP> mtu 1452 qdisc noop state DOWN group default qlen 1
[36mdresponse_1         |[0m     link/tunnel6 :: brd ::
[36mdresponse_1         |[0m 9: ip6gre0@NONE: <NOARP> mtu 1448 qdisc noop state DOWN group default qlen 1
[36mdresponse_1         |[0m     link/gre6 00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00 brd 00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00
[36mdresponse_1         |[0m 253: eth0@if254: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
[36mdresponse_1         |[0m     link/ether 02:42:ac:13:00:02 brd ff:ff:ff:ff:ff:ff
[36mdresponse_1         |[0m     inet 172.19.0.2/16 scope global eth0
[36mdresponse_1         |[0m        valid_lft forever preferred_lft forever
[36mdresponse_1         |[0m     inet6 fe80::42:acff:fe13:2/64 scope link tentative 
[36mdresponse_1         |[0m        valid_lft forever preferred_lft forever
[33mnormal-container_1  |[0m entrypoint: []
[33mnormal-container_1  |[0m command: [cat /tmp/hello]
[33mnormal-container_1  |[0m argv: [cat /tmp/hello]
[33mnormal-container_1  |[0m path: /bin/cat
[36mdresponse_1         |[0m [pid: 9|app: 0|req: 1/1] 0.0.0.0 () {28 vars in 307 bytes} [Sun Apr 30 23:59:35 2017] POST /init => generated 153 bytes in 190 msecs (HTTP/1.1 200) 2 headers in 72 bytes (3 switches on core 0)
[33mnormal-container_1  |[0m hello, world!
[33mprestartscripts_normal-container_1 exited with code 0
[0mStopping prestartscripts_dresponse_1 ... 
[1A[2KStopping prestartscripts_dresponse_1 ... done[1BAborting on container exit...
```

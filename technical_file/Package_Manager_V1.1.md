## 包管理器

我们在复刻github上的项目的时候会看到非常多的命令操作，刚开始的时候我们都一脸懵逼，它们都在做什么呢。

我们先来找一个项目作为实例先来做一个粗浅的了解。

![](assets/Package_Manager_V1.1/file-20260323105642282.png)

我们可以看到，这个里有5行命令，每一个命令的开头都是pip install这个形式，install我们都知道什么意思，安装嘛，那前面的pip呢，其实它是一个包管理器的名字，那这里我们基本也就大概能猜出个大概了，就是包管理器安装了一个东西，东西就是install后面的内容了。

比如下面的三个命令

- pip install wifi-densepose
- pip install wifi-densepose[gpu]
- pip install wifi-densepose[all]

这三个命令都是安装了wifi-densepose这个python包，这个包是做什么的感兴趣的可以深入去查询下，对于刚接触命令行的我们来说，只要能看懂就可以了，后面中括号内的是对这个包的扩展描述。

比如gpu后缀的就是在基础版上额外安装支持GPU加速的依赖。

## 包管理工具大全


debian系统包管理：dpkg  **apt**

arch系统包管理：pacman

gentoo系统包管理：emerge

slackware包管理：pkg

solus包管理：eopkg

redhat系统包管理：**dnf yum**

SUSE包管理：zypper

|  包管器名称   |               可以支持的系统               |       跨平台使用       |
| :------: | :---------------------------------: | :---------------: |
| APT dpkg |      Debian、Ubuntu等Debian衍生版系统      | 仅支持Linux Dibian系统 |
|  pacman  |      Linux Arch、Manjaro等衍生版系统       |  仅支持Linux Arch系统  |
| Portage  |  Linux Gentoo、Funtoo、ChromeOS底层系统   | 仅支持Linux Gentoo系统 |
|   pkg    | FreeBSD、NetBSD、OpenBSD、DragonFlyBSD |    仅支持BSD系列系统     |
|   DNF    |   RHEL/CentOS/Fedora 体系下**旧版**系统    | 仅支持Linux RHEL旧版系统 |
|   YUM    |   RHEL/CentOS/Fedora 体系下**新版**系统    | 仅支持Linux RHEL新版系统 |
|  Zypper  |  openSUSE、SUSE Linux Enterprise等系统  |  仅支持Linux SUSE系统  |
|          |                                     |                   |





































































































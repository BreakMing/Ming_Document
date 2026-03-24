## 包管理器

我们在复刻github上的项目的时候会看到非常多的命令行操作，刚开始的时候我们都一脸懵逼，它们都在做什么呢。

我们先来找一个项目作为实例先来做一个粗浅的了解。

![](assets/Package_Manager_V1.1/file-20260323105642282.png)

我们可以看到，这里有 5 行命令，均以 `pip install` 开头。`install` 意为安装，`pip` 则是一个包管理器的名字，不难理解，这是用包管理器安装 `install` 后面的内容。

比如下面的三个命令

- pip install wifi-densepose
- pip install wifi-densepose[gpu]
- pip install wifi-densepose[all]

这三个命令都是安装 `wifi-densepose` 这个 `Python` 包（其用途感兴趣的可深入查询，刚接触命令行只需看懂即可），中括号内是包的扩展描述。

比如 `gpu` 后缀，就是在基础版上额外安装支持 GPU 加速的依赖。

## 系统级包管理工具

系统级包管理工具，是操作系统官方或主流维护的底层工具，负责系统全局软件包的依赖解析、版本管理、安装 / 卸载 / 更新，以及软件源管理、系统软件一致性保障等管理流程，仅作用于操作系统层面，不触碰单一编程语言的开发 / 应用运行环境组件。

|  包管器名称   |                        可以支持的系统                         |                       跨平台使用                        |
| :------: | :----------------------------------------------------: | :------------------------------------------------: |
| APT dpkg |               Debian、Ubuntu等Debian衍生版系统                |                 仅支持Linux Dibian系统                  |
|  pacman  |                Linux Arch、Manjaro等衍生版系统                |                  仅支持Linux Arch系统                   |
| Portage  |            Linux Gentoo、Funtoo、ChromeOS底层系统            |              仅支持Linux Gentooe和BSD系列系统              |
|   pkg    |          FreeBSD、NetBSD、OpenBSD、DragonFlyBSD           |                     仅支持BSD系列系统                     |
|   DNF    |             RHEL/CentOS/Fedora 体系下**旧版**系统             |                 仅支持Linux RHEL旧版系统                  |
|   YUM    |             RHEL/CentOS/Fedora 体系下**新版**系统             |                 仅支持Linux RHEL新版系统                  |
|  Zypper  |           openSUSE、SUSE Linux Enterprise等系统            |                  仅支持Linux SUSE系统                   |
|   RPM    | RHEL系列、Fedora、CentOS、openSUSE、SUSE Linux Enterprise等系统 |               仅支持Linux REL和SUSE系统底层                |
|   Nix    |                         NixOS                          |          支持全Linux发行版、macOS、Windows WSL2系统          |
| Homebrew |               macOS、Linux、Windows（WSL2）                |          支持全Linux发行版、macOS、Windows WSL2系统          |
|   Snap   |                  Ubuntu、绝大多数Linux发行版                   | Ubuntu 默认安装，支持绝大多数 Linux 发行版，Windows、macOS 提供实验性支持 |
| Flatpak  |           Fedora、Ubuntu、Debian、Arch等Linux系统            |        支持主流的 Linux 系统，Windows、macOS 提供实验性支持        |
|  winget  |                Windows10、Windows11以上版本                 |                    仅支持Windows系统                    |
| MacPorts |                        macOS全系                         |                     仅支持macOS系统                     |
|   Fink   |                        macOS全系                         |                     仅支持macOS系统                     |

### APT

Dibian、Ubuntu等Debian官方默认的系统级包管理器，基于dpkg包工具构建，是Linux生态中使用最广泛的系统级包管理器。

#### 基础操作讲解

```
apt update
```

更新本地软件包列表，不升级任何已安装的工具。

```
apt install 包名
```

自动解析并安装该软件包的所有依赖，自动完成安装。

```
apt upgrade
```

升级已安装的软件包到软件包列表的最新版本。

```
apt search 关键词
```

在软件列表中查找包含关键词的软件包，查看包名和简介。

```
apt list
```

列出软件列表中所有的软件包。

### winget

Windows原生的系统级包管理器，默认预装在Win10、Win11系统上，支持管理 exe、msi、msix、微软商店应用等全类型 Windows 软件。

#### 基础操作讲解

```
winget install 包名
```

下载一个软件包，一键安装、自动处理依赖、适配系统架构、申请管理员权限、无需手动电击。

```
winget uninstall 包名
```

调用软件自带的卸载脚本，但会保留用户配置和缓存数据等信息。

```
winget uninstall 包名 --purge
```

完全卸载软件，同时清除用户配置、缓存等信息。

```
winget upgrade --all
```

升级所有被winget管理的软件到最新版本。

```
winget show 包名
```

查看软件的完整信息，包括最新版本、发布者、支持架构、安装参数、许可协议、官网地址等。

## 编程语言级包管理工具

专门用于特定编程语言生态的工具，负责该语言的第三方库、框架、工具链的依赖解析、版本管理、安装 / 卸载 / 更新，以及项目构建、发布等开发流程，通常不直接管理操作系统核心组件，可配合系统级包管理器使用。

|  包管器名称   |         编程语言          |         可支持的系统平台         |
| :------: | :-------------------: | :----------------------: |
|   pip    |         Pyhon         | 全平台（Linux、Windows、macOS） |
|  Conda   |    Pyton、R 、Julia     | 全平台（Linux、Windows、macO）  |
|   npm    | JavaScript、TypeScript | 全平台（Linux、Windows、macO）  |
|   yarn   | JavaScript、TypeScript | 全平台（Linux、Windows、macO）  |
|   pnpm   | JavaScript、TypeScript | 全平台（Linux、Windows、macO）  |
|  maven   |  Java、Kotlin、C#、Ruby  | 全平台（Linux、Windows、macO）  |
|  Gradle  |   Java、Kotlin、C/C++   | 全平台（Linux、Windows、macO）  |
|  go mod  |          Go           | 全平台（Linux、Windows、macO）  |
|  Cargo   |         Rust          | 全平台（Linux、Windows、macO）  |
|   gem    |         Ruby          | 全平台（Linux、Windows、macO）  |
| Bundler  |         Ruby          | 全平台（Linux、Windows、macO）  |
| Composer |          PHP          | 全平台（Linux、Windows、macO）  |
|  NuGet   |         .NET          |         Windows          |

### pip

Python 官方默认的编程语言级包管理器，是 Python 生态中使用最广泛的包管理工具，全平台（Windows、macOS、Linux）通用，负责 Python 第三方库、框架的安装与基础管理。

#### 础操作讲解
```
pip install 包名
```

自动解析并安装该 Python 包的所有依赖，自动完成安装。

```
pip uninstall 包名
```

卸载已安装的 Python 包，自动清理相关数据文件。

```
pip install --upgrade 包名
```

将已安装的 Python 包升级到当前可用的最新版本。

```
pip search 关键词
```

在 PyPI 官方包仓库中，查找包含关键词的 Python 包，查看包名与简介。

```
pip list
```

列出当前 Python 环境中，所有已安装的 Python 包及其版本号。





### conda

面向 Python、R、Julia 等数据科学语言的跨平台编程语言级包与环境管理器，全平台（Windows、macOS、Linux）通用，可实现不同项目的环境隔离与依赖统一管理。

#### 基础操作讲解

```
conda create -n 环境名 python = 版本号
```

创建一个指定 Python 版本的独立虚拟环境。

```
conda activate 环境名
```

激活指定的虚拟环境，后续所有包操作均仅作用于该环境。

```
conda install 包名
```

在当前激活的环境中，自动解析并安装对应包的所有依赖，自动完成安装。

```
conda uninstall 包名
```

在当前激活的环境中，卸载已安装的包，清理相关安装文件。

```
conda deactivate
```

退出当前激活的虚拟环境，回到系统默认的基础环境。


### npm

Node.js 官方默认的 JavaScript、TypeScript 编程语言级包管理器，是前端与 Node.js 生态中使用最广泛的包管理工具，全平台（Windows、macOS、Linux）通用，负责前端框架、Node.js 工具库的安装与项目依赖管理。

基础操作讲解

npm install 包名

自动解析并安装该包的所有依赖，自动完成安装，支持指定包版本，默认安装到当前项目目录下。

npm install -g 包名

全局安装对应包，安装后可在系统任意位置直接调用该包的命令行工具。

npm uninstall 包名

卸载当前项目中已安装的包，清理相关安装文件与依赖记录。

npm update 包名

更新指定依赖包到当前可用的最新兼容版本。

npm list

列出当前项目中所有已安装的包及其版本号。


## 网络请求下载工具

网络数据传输工具，仅负责**网络文件 / 数据的传输和下载**。

| 工具名称  |                       核心功能                       |
| :---: | :----------------------------------------------: |
| curl  |                支持三十多种网络协议的网络传输工具                 |
| wget  |            用于HTTP/HTTPS/FTP协议的文件下载工具             |
| aria2 | 支持多协议、多线程并行下载加速，支持HTTP/FTP/BT/SFTP/Metalink的下载工具 |
| axel  |           用于HTTP/HTTPS/FTP协议的多线程加速下载工具           |
| rsync |                SSH加密本地与远程的文件传输工具                 |
|  scp  |             SSH加密本地和服务器间文件/目录双向传输工具              |



























































































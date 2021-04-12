
### 1. Achitecture: VM vs Dcoker

#### Docker utilises the kernel of the host instead of having an entirely separate kernel. This allows docker to use less resources, but still maintain a completely contained environment.

![image](https://user-images.githubusercontent.com/39177230/114329814-e8d85200-9b72-11eb-9cbb-ff640a99c339.png)

#### Docker相比于传统虚拟化方式具有更多的优势：

* docker 启动快速属于秒级别。虚拟机通常需要几分钟去启动
* docker 需要的资源更少， docker 在操作系统级别进行虚拟化， docker 容器和内核交互，几乎没有性能损耗，性能优于通过 Hypervisor 层与内核层的虚拟化
* docker 更轻量， docker 的架构可以共用一个内核与共享应用程序库，所占内存极小。同样的硬件环境， Docker 运行的镜像数远多于虚拟机数量，对系统的利用率非常高,与虚拟机相比， docker 隔离性更弱， docker 属于进程之间的隔离，虚拟机可实现系统级别隔离
* 安全性： docker 的安全性也更弱。 Docker 的租户 root 和宿主机 root 等同，一旦容器内的用户从普通用户权限提升为root权限，它就直接具备了宿主机的root权限，进而可进行无限制的操作。虚拟机租户 root 权限和宿主机的 root 虚拟机权限是分离的，并且虚拟机利用如 Intel 的 VT-d 和 VT-x 的 ring-1 硬件隔离技术，这种隔离技术可以防止虚拟机突破和彼此交互，而容器至今还没有任何形式的硬件隔离，这使得容器容易受到攻击
* 可管理性： docker 的集中化管理工具还不算成熟。各种虚拟化技术都有成熟的管理工具，例如 VMware vCenter 提供完备的虚拟机管理能力
* 高可用和可恢复性： docker 对业务的高可用支持是通过快速重新部署实现的。虚拟化具备负载均衡，高可用，容错，迁移和数据保护等经过生产实践检验的成熟保障机制， VMware 可承诺虚拟机 99.999% 高可用，保证业务连续性
* 快速创建、删除：虚拟化创建是分钟级别的， Docker 容器创建是秒级别的， Docker 的快速迭代性，决定了无论是开发、测试、部署都可以节约大量时间
交付、部署：虚拟机可以通过镜像实现环境交付的一致性，但镜像分发无法体系化。 Docker 在 Dockerfile 中记录了容器构建过程，可在集群中实现快速分发和快速部署

![image](https://user-images.githubusercontent.com/39177230/114330350-1a055200-9b74-11eb-8456-4115df163bf9.png)

### 2. Docker 中包括三个基本的概念：

* Image(镜像)
* Container(容器)
* Repository(仓库)

#### 镜像是 Docker 运行容器的前提，仓库是存放镜像的场所，可见镜像更是 Docker 的核心。

* 镜像(Image)
#### 镜像，从认识上简单的来说，就是面向对象中的类，相当于一个模板。从本质上来说，镜像相当于一个文件系统。Docker 镜像是一个特殊的文件系统，除了提供容器运行时所需的程序、库、资源、配置等文件外，还包含了一些为运行时准备的一些配置参数（如匿名卷、环境变量、用户等）。镜像不包含任何动态数据，其内容在构建之后也不会被改变。

* 容器(Container)
#### 容器，从认识上来说，就是类创建的实例，就是依据镜像这个模板创建出来的实体。容器的实质是进程，但与直接在宿主执行的进程不同，容器进程运行于属于自己的独立的命名空间。因此容器可以拥有自己的root 文件系统、自己的网络配置、自己的进程空间，甚至自己的用户ID 空间。容器内的进程是运行在一个隔离的环境里，使用起来，就好像是在一个独立于宿主的系统下操作一样。这种特性使得容器封装的应用比直接在宿主运行更加安全。

* 仓库(Repository)
#### 仓库，从认识上来说，就好像软件包上传下载站，有各种软件的不同版本被上传供用户下载。镜像构建完成后，可以很容易的在当前宿主机上运行，但是，如果需要在其它服务器上使用这个镜像，我们就需要一个集中的存储、分发镜像的服务，Docker Registry 就是这样的服务。





























[Reference: Learning Docker](https://github.com/willitscale/learning-docker)

[Reference: Docker入门吐血总结](https://blog.csdn.net/deng624796905/article/details/86493330?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522161818379316780255273360%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=161818379316780255273360&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-2-86493330.first_rank_v2_pc_rank_v29&utm_term=docker+&spm=1018.2226.3001.4187)

[Reference: Docker——入门实战](https://blog.csdn.net/bskfnvjtlyzmv867/article/details/81044217)





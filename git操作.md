# git 操作

1. 本地git配置

```
//更改账户的名字和邮箱
git config --global user.name ruixinMRK
git config --global user.email 270197698@qq.com   
git config --list //显示出配置文件(查看修改后的内容)
```
   
2. 拷贝代码

```
git clone http://github.com/xxxx/xxx.git  //clone git
```

3. 配置ssh key

    生成公钥文件  `ssh-keygen -t rsa -C "your_email@youremail.com"`

    注意每台电脑需要生成一个公钥

    C:\Users\用户名\.ssh 文件夹下找到 id_rsa.pub文件,把文件内容添加到官网上去

4. 常用命令

```
git status  查看当前文件的状态
git status -s //查看当前文件的具体状态

git branch   //查看分支
git branch tryagin  //创建分支
git branch -a 可以查看远程分支
git push origin --delete <branchName> 或者 git push origin :<branchName>   是删除远程分支
git branch -m devel develop     重命名本地分支

git checkout tryagin//切换分支  (先要add和commit)
git branch -d tryagin //删除分支
```

在主分支上合并其他分支   (git merge 其他)

```
$ makdir ~/hello-world    //创建一个项目hello-world
$ cd ~/hello-world       //打开这个项目
$ git init             //初始化 
$ touch README
$ git add README        //更新README文件
$ git commit -m 'first commit'     //提交更新，并注释信息“first commit”
git remote rm origin               //删除已经定义的路径
git remote -v		显示远程仓的信息
$ git remote add origin git@github.com:defnngj/hello-world.git     //连接远程github项目  
$ git push -u origin master     //将本地项目更新到github项目上去
```

```
git reset --hard HEAD^    回退版本(commit)
git reflog                查询版本号
git pull origin master  将远程库拉到本地
git tag ..(打上标签方便以后查询)
git tag    （显示标签）
git show .. （查看标签详细信息）
git checkout -b devTemp   新建并且换分支
$ git checkout -b devTemp origin/devTemp  新建分支并切换并从远程仓拉回
git remote -v 显示远程仓地址

git fetch origin master
git reset --hard origin/master 撤销本地修改  也可以更新到最新版本
git reset --hard 3628164
git reset --hard HEAD~3

git log 显示提交的日志(commit)
git reflog  记录每一次操作命令


git checkout -- readme.txt  回到最近一次git commit或git add时的状态  丢弃工作区的修改 可用于文件的无意被删除
git reset HEAD readme.txt   将已经加到暂存区的文件删除
git rm   删除文件
```

5. 参考链接

>http://blog.csdn.net/qq_26787115/article/details/52133008
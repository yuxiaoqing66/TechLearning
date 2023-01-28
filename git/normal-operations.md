# github常见操作

## 创建一个git 仓库

### 从零开始

- 创建一个空的git仓库
  `git init`
- 在github创建一个空的库
- 添加文件后上传到github库

```git
  git add .
  git commit -m "{{message}}"
  git remote add origin <ssh>
  git push origin master
```

### 已有文件

- 在一个空文件夹里创建空的git仓库
  `git init`
- 将文件拷贝至这个文件夹中
- 在github上创建一个新的仓库
- 上传至github

```git
  git add .
  git commit -m "{{message}}"
  git remote add origin <ssh>
  git push origin master
```

## 分支操作

### 创建一个新的分支

- 在本地创建一个新的分支
  `git checkout -b newbranch`
- 添加文件及更改
  ```
  git add .
  git commit -m "{{message}}"
  ```
- 将分支推送到github
  `git push origin newbranch`

### 删除指定分支

> 删除分支的前置条件是，该分支不能是github的默认分支（需要先将默认分支调整为其他分支）

- 在本地删除指定分支
  ```
  git checkout otherbranch    # 切换到其他分支
  git branch -D branchtodel    # 删除指定分支，注意是-D，D大写
  ```
- 在远程github仓库删除该分支
  `git push origin :branchtodel  # 待删除分支前加上:`

### 在指定分支上工作

- 本地如果已经有该分支：
  如果已经在该分支上，正常修改提交即可；
  若不在该分支上，可以 `git checkout thisbranch`,再修改提交；
- 另一种情况是本地没有这个分支，需要远程拉取：
  法一：

  - 从指定分支克隆git仓库

  ```
  git clone <ssh>
  git checkout thisbranch
  git pull
  ```

  - 上传更改到指定分支
    `git push origin thisbranch`
    法二：
- 从指定分支克隆git库

```
   git clone -b thisbranch <ssh>
```

- 上传修改
  `git push`

### 从指定分支创建新分支

- 克隆git库
  `git clone <ssh>`
- 切换到指定分支

```
  git checkout thisbranch
  git pull
```

- 创建新分支
  `git checkout -b newbranch`
- 将新分支推送到远程仓库
  `git push origin newbranch`

### 合并分支

  将一个branch1合并入branch2的标准方法是：

```
  (branch1)git checkout branch2
  (branch2)git merge branch1
```

  有几种情形：

- 在从branch2创建branch1至merge时，branch2并未有任何修改提交：
  > *这种情形下不会产生合并冲突*
  >
- 在从branch2创建branch1至merge时，branch2有修改，但是与branch1的修改并无冲突(修改在不同地方)：
  > *这种情形下不会产生合并冲突*
  >
- 在从branch2创建branch1至merge时，branch2有修改，且与branch1的修改修改了同一地方：
  
  <font color=red>产生合并冲突 </font>
  
  **产生冲突后的处理方法：**
  ```git
  git status  # 查看冲突位置
  # 打开冲突文件，修改并解决冲突
  git add . 
  git commit -m "merge..."
  git push origin  # 使用这种方法会自动将branch1删除
  git push origin branch2  # 使用这种方法不会将branch1删除
  ```


## 版本回退

一般使用`git reset`命令进行版本回退

<font color=red>注意：这种回退方式会消除掉回退版本之后的提交记录！</font>

使用方法：

- 法一：
  ```
  git reset HEAD^  # 回退到上一个版本
  git reset HEAD^^  # 回退到上上个版本
  git reset HEAD~5  # 向上回退5个版本
  ```
- 法二：
  ```
  git log
  git reset <版本号>  # 回退到指定版本
  ```

- 关于参数：
  ```
  --hard  # 同时回退HEAD、暂存区和工作区
  --mixed  # 同时回退HEAD和暂存区，不回退工作区
  --soft  # 只回退HEAD，不回退暂存区和工作区
  # 不加参数默认是mixed
  ```
- 取消版本回退

  - 使用版本号取消版本回退
    ```
    git reset --hard <版本号>
    ```

  - 获取版本号
    ```
    # 回退之前的git log获取的版本号依然可以用
    # 还可用git reflog查看指令记录
    git reflog
    # 举例
    $ git reflog
    f19aa42 (HEAD -> main2, origin/main2) HEAD@{0}: commit: main2一test
    9ee29b1 HEAD@{1}: reset: moving to 9ee29b11
    047274d HEAD@{2}: merge refs/remotes/origin/main2: Fast-forward
    9ee29b1 HEAD@{3}: reset: moving to 9ee29b112abf1
    4e1d3fd HEAD@{4}: merge refs/remotes/origin/main2: Merge made by the 'ort' strategy.
    1da4036 HEAD@{5}: commit: main2三^
    9ee29b1 HEAD@{6}: reset: moving to 9ee29b112abf1f6e7d
    047274d HEAD@{7}: merge refs/remotes/origin/main2: Fast-forward
    9ee29b1 HEAD@{8}: reset: moving to 9ee29b112abf1f6e7d
    047274d HEAD@{9}: merge refs/remotes/origin/main2: Fast-forward
    9ee29b1 HEAD@{10}: reset: moving to 9ee29b112abf1f6e7d
    047274d HEAD@{11}: pull: Fast-forward
    9ee29b1 HEAD@{12}: reset: moving to 9ee29b112abf1f6e7
    047274d HEAD@{13}: commit: main2三！
    0eb33c2 HEAD@{14}: commit: main2二！
    9ee29b1 HEAD@{15}: commit: main2一！
    085ade6 HEAD@{16}: clone: from github.com:yuxiaoqing66/git-test.git
    ```

# github常见操作

### 创建一个git 仓库

#### 从零开始

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

#### 已有文件

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

### 分支操作

#### 创建一个新的分支

- 在本地创建一个新的分支
  `git checkout -b newbranch`
- 添加文件及更改
  ```
  git add .
  git commit -m "{{message}}"
  ```
- 将分支推送到github
  `git push origin newbranch`

#### 删除指定分支

> 删除分支的前置条件是，该分支不能是github的默认分支（需要先将默认分支调整为其他分支）

- 在本地删除指定分支
  ```
  git checkout otherbranch    # 切换到其他分支
  git branch -D branchtodel    # 删除指定分支，注意是-D，D大写
  ```
- 在远程github仓库删除该分支
  `git push origin :branchtodel  # 待删除分支前加上:`

#### 在指定分支上工作

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

#### 从指定分支创建新分支

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

#### 合并分支

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

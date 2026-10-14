# 部分克隆指南

[English](en-US/PARTIAL_CLONE.md)

Dress 仓库包含大量图片。只使用 `--depth 1` 会省略旧提交，但仍会下载当前版本中的全部图片。若你只准备修改自己的目录，推荐同时使用部分克隆和稀疏检出：Git 先下载提交与目录结构，仅在检出所选目录时按需下载其中的文件。

> 需要 Git 2.25 或更高版本。可运行 `git --version` 查看版本。

## 首次克隆

先在 GitHub 上 Fork 本仓库，再克隆你自己的 Fork。将命令中的用户名和目录替换为实际值：

```bash
git clone --filter=blob:none --sparse --depth 1 https://github.com/<你的用户名>/Dress.git
cd Dress

# 只检出自己的目录；即使远端尚无该目录，也可以先设置
git sparse-checkout set '<首字母>/<你的文件夹名>'
```

例如，要使用 `Y/Yueosa`：

```bash
git sparse-checkout set 'Y/Yueosa'
```

此时工作区会包含根目录文档和 `Y/Yueosa`，不会出现其他贡献者的图片。若文件夹名以数字或符号开头，请使用 `#` 目录，并务必给路径加引号：

```bash
git sparse-checkout set '#/233'
```

接下来可以创建目录、添加照片并正常使用 `git add`、`git commit` 和 `git push`。完整贡献流程请继续阅读[新手指南](GUIDE.md)。

## 管理检出目录

查看当前选择的目录：

```bash
git sparse-checkout list
```

追加另一个目录，同时保留已有目录：

```bash
git sparse-checkout add 'A/AnotherName'
```

重新选择目录时，`set` 会替换之前的目录列表：

```bash
git sparse-checkout set 'F/FirstName' 'S/SecondName'
```

Git 会在需要时自动下载新选目录中的文件，因此目录越小，下载量和磁盘占用通常越少。

## 获取更多历史

`--depth 1` 创建的是浅克隆，只包含最新一次提交。普通的添加照片和发起 PR 不受影响；若需要查看完整历史，可运行：

```bash
git fetch --unshallow
```

这会获取完整提交历史，但图片内容仍由部分克隆按需下载。

## 恢复完整仓库

如果只想让当前版本的所有文件出现在工作区，可关闭稀疏检出：

```bash
git sparse-checkout disable
```

该命令会下载当前版本中尚未获取的文件，数据量可能很大。仓库仍然保留部分克隆设置，旧版本文件会继续按需下载。

如果确实需要把仓库转换为包含全部历史和文件内容的完整克隆，可继续运行：

```bash
git fetch --unshallow --no-filter
git config --unset remote.origin.partialclonefilter
git config --unset remote.origin.promisor
```

若之前已经执行过 `git fetch --unshallow`，再次执行时会提示仓库并非浅克隆；此时改用 `git fetch --no-filter` 即可。

## 常见问题

### 为什么根目录文档仍会出现？

`git clone --sparse` 默认使用锥形模式。该模式会保留仓库根目录的文件，便于直接阅读 `README.md`、`GUIDE.md` 等说明文档。

### 为什么看不到刚选择的目录？

先运行 `git sparse-checkout list` 核对路径、大小写和首字母目录。远端不存在的新目录不会自动显示，创建并加入文件后才会出现在工作区中。

### 部分克隆会影响提交或 PR 吗？

不会。未检出的文件仍由 Git 管理，不会因为 `git add` 或提交自己的目录而被删除。请只修改自己的目录，并在提交前使用 `git status` 核对变更。

## 参考

- [关于仓库体积的讨论](https://github.com/orgs/Cute-Dress/discussions/11)
- [Git 官方文档：部分克隆](https://git-scm.com/docs/partial-clone)
- [Git 官方文档：稀疏检出](https://git-scm.com/docs/git-sparse-checkout)

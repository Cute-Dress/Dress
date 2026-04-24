# 🌟 新手指南 / Beginner Guide

欢迎来到 Dress 项目！这份指南将帮助你完成第一次 Pull Request（PR）。

Welcome to the Dress project! This guide will help you complete your first Pull Request (PR).

---

## 📋 提交流程概览 / Submission Workflow Overview

```
Fork 仓库 → 添加你的照片 → 提交 Commit → 发起 Pull Request → 等待审核合并
Fork repo → Add your photos → Commit → Open Pull Request → Wait for review & merge
```

---

## 第一步：Fork 仓库 / Step 1: Fork the Repository

> **Fork** = 把别人的仓库「复制」一份到你自己的 GitHub 账号下，让你可以自由修改喵，不会影响原项目喵!  
> **Fork** = Creating your own copy of someone else's repository under your GitHub account, so you can freely make changes without affecting the original.

1. 打开 [Dress 仓库页面](https://github.com/Cute-Dress/Dress)
2. 点击页面右上角的 **Fork** 按钮
3. 这会在你的 GitHub 账号下创建一份仓库副本

---

1. Go to the [Dress repository page](https://github.com/Cute-Dress/Dress)
2. Click the **Fork** button at the top right
3. This creates a copy of the repository under your GitHub account

---

## 第二步：添加你的照片 / Step 2: Add Your Photos

> **Commit** = 给你的修改拍一张「快照」，记录你改了什么内容，每次 Commit 都会生成一条历史记录喵!  
> **Commit** = Taking a "snapshot" of your changes, recording what you modified. Each commit creates a point in the project history.

### 方法 A：直接在 GitHub 网页上传（最简单）/ Method A: Upload via GitHub Web (Easiest)

1. 进入你 Fork 后的仓库页面（`https://github.com/<你的用户名>/Dress`）
2. 找到你 GitHub ID 首字母对应的文件夹（如 ID 为 `Yueosa`，则进入 `Y` 文件夹）
3. 点击 **Add file** → **Create new file**
4. 在文件名栏输入 `你的GitHubID/README.md`（如 `Yueosa/README.md`），这会自动创建文件夹
5. 在文件中随意写一些内容（如自我介绍）
6. 点击 **Commit changes**
7. 再次点击 **Add file** → **Upload files**，将你的照片上传到刚创建的文件夹中
8. 点击 **Commit changes**

---

1. Go to your forked repository (`https://github.com/<your-username>/Dress`)
2. Navigate to the folder matching the first letter of your GitHub ID (e.g., `Y` for `Yueosa`)
3. Click **Add file** → **Create new file**
4. Type `YourGitHubID/README.md` (e.g., `Yueosa/README.md`) in the filename field — this auto-creates the folder
5. Write some content (e.g., a brief introduction)
6. Click **Commit changes**
7. Click **Add file** → **Upload files** again, and upload your photos into the folder you just created
8. Click **Commit changes**

---

### 方法 B：使用 Git 命令行 / Method B: Using Git CLI

> **Clone** = 把远程仓库下载到本地电脑。
> **Push** = 把本地的 Commit 上传同步到远程仓库（你的 Fork）。  
> **Clone** = Downloading the remote repository to your local machine. 
> **Push** = Uploading your local commits back to the remote repository (your Fork).

```bash
# 1. 克隆你 Fork 的仓库 / Clone your forked repository
# 💡 由于仓库 commit 历史较多，直接 clone 可能较慢。
#    推荐使用 --depth 1 仅拉取最近一次提交，速度更快喵！
# 💡 The repo has a large commit history, so a full clone may be slow.
#    Consider using --depth 1 to only fetch the latest commit for a faster download!
git clone --depth 1 https://github.com/<你的用户名>/Dress.git
cd Dress

# 2. 创建你的文件夹并添加照片 / Create your folder and add photos
#    将 <首字母> 替换为你 GitHub ID 的首字母，<你的GitHubID> 替换为你的 GitHub ID
#    Replace <FirstLetter> with the first letter of your GitHub ID
mkdir -p <首字母>/<你的GitHubID>
cp /path/to/your/photos/* <首字母>/<你的GitHubID>/

# 3. 提交更改 / Commit your changes
git add .
git commit -m "Add photos for <你的GitHubID>"

# 4. 推送到你的 Fork / Push to your fork
git push origin main
```

---

## 第三步：发起 Pull Request / Step 3: Open a Pull Request

> **Pull Request（PR）** = 向原仓库的维护者提出申请：「我在我的 Fork 里做了一些修改，请把它们合并到原项目里吧喵！」  
> **Pull Request (PR)** = A request to the original repository's maintainers saying: "I've made some changes in my Fork — please merge them into the original project!"

1. 回到你 Fork 的仓库页面
2. 你会看到一个提示 **"This branch is X commits ahead"**，点击 **Contribute** → **Open pull request**
3. 填写 PR 模板中的描述和检查清单
4. 点击 **Create pull request**

---

1. Go back to your forked repository page
2. You should see a prompt saying **"This branch is X commits ahead"** — click **Contribute** → **Open pull request**
3. Fill in the description and checklist in the PR template
4. Click **Create pull request**

---

## 第四步：等待审核 / Step 4: Wait for Review

提交 PR 后，自动化机器人会帮你检查：

- 📏 **文件大小检查**：图片是否在 1MB 以内
- 🔒 **EXIF 信息检查**：图片是否包含高敏感元数据（主要是 **GPS 坐标**及地址类字段）

> 机器人只会拦截高敏感字段（例如 GPS 坐标、IPTC/XMP 地址信息），普通摄影参数（光圈、快门等）不会导致 PR 被拒。
> 了解详情请阅读 [EXIF.md](EXIF.md)。

如果检查未通过，机器人会留下评论告诉你如何修正。你可以按照提示修改后再次推送（push），PR 会自动更新。

维护者审核通过后，你的 PR 就会被合并。恭喜你完成了第一次开源贡献！🎉

---

After submitting the PR, automated bots will check:

- 📏 **File size check**: Are images under 1MB?
- 🔒 **EXIF data check**: Do images contain high-sensitivity metadata (primarily **GPS coordinates** and address fields)

> The bot only blocks high-sensitivity fields such as GPS coordinates and IPTC/XMP location data.
> Regular photography parameters (aperture, shutter speed, etc.) will not cause your PR to fail.
> See [EXIF.md](EXIF.md) for details.

If any check fails, the bot will leave a comment explaining how to fix it. You can make changes and push again — the PR will update automatically.

Once a maintainer approves, your PR will be merged. Congratulations on your first open-source contribution! 🎉

---

## ⚠️ 提交前请注意 / Before You Submit

1. **压缩图片** — 确保每张图片小于 1MB。可以使用 [TinyPNG](https://tinypng.com/) 等在线工具压缩。
2. **移除高敏感 EXIF 信息** — 最重要的是删除 **GPS 坐标**，它能精确暴露你的拍摄地点。照片还可能携带地址、联系方式等信息。详见 [EXIF.md](EXIF.md) 和 [CONTRIBUTING.md](CONTRIBUTING.md)。
3. **正确命名文件夹** — 使用你的 GitHub ID 命名，并放在对应首字母目录下。
4. **原创图片** — 只提交你自己的照片，不接受盗图。
5. **只修改自己的文件夹** — 请不要改动他人的文件夹或其他项目文件，避免给维护者带来不必要的麻烦。
6. **文件名避免中文和空格** — 文件名中的中文字符或空格可能导致部分系统无法正常显示或下载，请尽量使用英文字母、数字和连字符。

---

1. **Compress images** — Make sure each image is under 1MB. Use tools like [TinyPNG](https://tinypng.com/).
2. **Remove sensitive EXIF data** — The most important thing is to strip **GPS coordinates**, which can reveal your exact shooting location. Photos may also carry address and contact-info fields. See [EXIF.md](EXIF.md) and [CONTRIBUTING.md](CONTRIBUTING.md).
3. **Name your folder correctly** — Use your GitHub ID and place it under the matching alphabetical directory.
4. **Original images only** — Only submit your own photos. Stolen images are not accepted.
5. **Only modify your own folder** — Do not touch other contributors' folders or any other project files.
6. **Avoid Chinese characters and spaces in filenames** — Use letters, numbers, and hyphens only to ensure compatibility across all systems.

---

## 🔗 参考链接 / Useful Links

- [项目说明 / Project README](README.md)
- [贡献指南 / Contributing Guide](CONTRIBUTING.md)
- [EXIF 说明 / EXIF Guide](EXIF.md)
- [项目详细说明 / Detailed README](README_DETAIL.md)
- [已合并的 PR 参考 / Merged PRs for reference](https://github.com/Cute-Dress/Dress/pulls?q=is%3Apr+is%3Amerged)

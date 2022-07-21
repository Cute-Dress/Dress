# LittleYe233/Dress

## 简介

本仓库为上游仓库 [komeiji-satori/Dress](https://github.com/komeiji-satori/Dress) 的分支，用以向上游仓库发起合并女装照片的请求。

## 规范

上游仓库 [komeiji-satori/Dress](https://github.com/komeiji-satori/Dress) 的 [README.md](https://github.com/komeiji-satori/Dress/blob/master/README.md) 中有：

> 你可以从这里学习从克隆项目，创建分支，提交和同步修改，到合并分支请求的整套流程，一次即可熟悉 Git/GitHub 的使用。

基于此，本仓库的文件内容、命名、提交、合并等将尽可能遵循软件开发的常用惯例，作练习和提示他人用。

<details>
<summary>规范详情</summary>

### 国际化

考虑到上游仓库的国际化情况及他人阅读代码的便利性，本仓库的主要文件名和说明文档使用简体中文，提交消息中与仓库内容相关的可使用简体中文，与提交情况和行为 (如 `Create` 、 `Remove`) 相关的一般使用英文。

### 分支

本仓库的默认分支为 [dev](https://github.com/LittleYe233/Dress/tree/dev) 。考虑到上游仓库默认分支 [master](https://github.com/komeiji-satori/Dress/tree/master) 体积已很大，当前分支并不始于其任何一次提交。

### 提交

一般所有在 `git` 上进行的提交均位于本仓库默认分支。

一般提交消息的格式形如： `<行为>: <对象>` 或 `<描述性语句>` ，如 `Create: 图片001.png` 或 `Append more information to README`。

### 更新与推送

考虑到上游仓库维护者更新情况，本仓库的默认分支更新频率较上游仓库高，且仅更新文档时将不会推送至上游仓库。

推送至上游仓库时，将先依次让上游仓库的 `master` 分支与本地仓库的 `dev` 分支与本地仓库的 `master` 分支合并，再由本地仓库的 `master` 分支向上游仓库发起 Pull Requests 。

</details>

## 公共特征

若无其他说明，本仓库中主要文件均具有如下公共特征：

<details>
<summary>公共特征</summary>

| 参数名 | 参数值 |
| :-: | :-: |
| 拍摄对象 | 仓库拥有者 |
| 拍摄者 | 仓库拥有者 |
| 拍摄设备 | 手机 |
| 是否对图片二次加工 | 是 |
| 图片二次加工的目的 | 调整文件体积，去除隐私等敏感信息 |
| 是否保留二次加工前图片 | 否 |

</details>

## 文件列表

<details>
<summary>文件列表</summary>

| 文件名 | 标签 | 二次加工方式 (除去除 EXIF 信息) |
| :-: | :-: | :-: |
| <IMG_20211014_214637.jpg> | `女仆` | `缩放 0.5x` |
| <IMG_20211017_193725.jpg> | `女仆` | `缩放 0.5x` |
| <IMG_20211213_020404.jpg> | `JK` | `画笔遮盖` `缩放 0.5x` |
| <IMG_20211214_212728.jpg> | `JK` | `缩放 0.5x` |
| <IMG_20211220_131537.jpg> | `JK` | `缩放 0.5x` |
| <IMG_20211220_133031.jpg> | `JK` `白丝` | `缩放 0.5x` |
| <IMG_20220102_131004.jpg> | `女仆` `白丝` `缩放 0.5x` |  |
| <IMG_20220301_093020.jpg> | `m:scale:0.7` |
| <IMG_20220305_111148.jpg> | `m:scale:0.9` |
| <IMG_20220309_110201.jpg> | `m:scale:no` |
| <IMG_20220314_143749.jpg> | `m:scale:0.7` |
| <IMG_20220405_102517.jpg> | `m:scale:0.9` |
| <IMG_20220423_013027.jpg> | `m:scale:no` |
| <IMG_20220425_014658.jpg> | `m:scale:no` |
| <IMG_20220506_012442.jpg> | `m:scale:no` |
| <IMG_20220514_021011.edited.jpg> | `m:scale:no` |
| <IMG_20220627_074454.jpg> | `m:scale:0.8` |
| <IMG_20220628_163516.jpg> | `m:scale:no` |
| <IMG_20220630_050442.jpg> | `m:scale:0.7` |
| <IMG_20220704_041929.jpg> | `m:scale:0.8` |
| <IMG_20220705_031826.jpg> | `m:scale:no` |
| <IMG_20220708_042554.jpg> | `m:scale:0.9` |
| <IMG_20220710_134651.jpg> | `m:scale:no` |
| <IMG_20220711_142147.jpg> | `m:scale:0.9` |
| <IMG_20220714_041044.jpg> | `m:scale:0.9` |
| <IMG_20220716_032223.jpg> | `m:scale:no` |
| <MVIMG_20220621_132055_1655788858283.jpg> | `m:scale:0.8` |
| <MVIMG_20220709_135754.jpg> | `m:scale:0.8` |

</details>

## 常见问题

<details>
<summary>常见问题详情</summary>

### 部分照片模糊？

- 常亮闪光灯拍摄效果不好；
- 拍摄姿势导致手抖 (已尽可能排除此种干扰) ；
- 已经过图像压缩处理。

### 女装的目的？

- ~~变得可爱~~；
- 体型控制；
- 了解相关知识 (包括生活常识) ；
- 为他人提供相关帮助。

### 更新频率？

暂不定期。与时间表相关。

### 目前的障碍？

- 没有合适的地点，无全身镜；
- 体型控制仍在进行中；
- 资金略匮乏；
- 时间略匮乏。

### 女装的主要发展方向？

暂未定。

</details>

## 附录

参见本仓库的 [APPENDIX](APPENDIX) 。附录各条目列表如下：

<details>
<summary>条目列表</summary>

| 条目名 | 条目链接 |
| :-: | :-: |
| 使用 Python 去除图片的 EXIF 信息 | <APPENDIX/python_exif_removal.md> |

</details>
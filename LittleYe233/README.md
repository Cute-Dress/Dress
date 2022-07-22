# LittleYe233/Dress

## Introduction

本仓库为上游仓库 [komeiji-satori/Dress](https://github.com/komeiji-satori/Dress) 的分支，用以向上游仓库发起合并女装照片的请求。

## Code of conduct

<details>
<summary>规范详情</summary>

### Internationalization

考虑到上游仓库的国际化情况及他人阅读代码的便利性，本仓库的主要文件名和说明文档使用简体中文，提交消息中与仓库内容相关的可使用简体中文，与提交情况和行为 (如 `Create` 、 `Remove`) 相关的一般使用英文。

### Branches

可以在本仓库中执行 `git log --oneline --graph` 或在网页端中查看本仓库分支的结构。

相关提案：<https://github.com/komeiji-satori/Dress/issues/1169>

- [dev](https://github.com/LittleYe233/Dress/tree/dev)：默认分支。考虑到上游仓库默认分支 [master](https://github.com/komeiji-satori/Dress/tree/master) 体积已很大，当前分支并不始于其任何一次提交。
- [clone_init](https://github.com/LittleYe233/Dress/tree/clone_init)：上游仓库 `master` 分支的第一个提交，作为本地合并的基础。
- [contribute](https://github.com/LittleYe233/Dress/tree/contribute)：由于 `dev` 分支与上游仓库 `master` 分支没有历史公共提交，需要本分支用于与 `dev` 分支合并并提交 PR 到上游。本分支首条提交与 `clone_init` 相同。
- [master](https://github.com/LittleYe233/Dress/tree/master)：fork 时的上游仓库 `master` 分支。

### Conventional commit

自提交 [aaad089](https://github.com/LittleYe233/Dress/commit/aaad089eece9ff8693a4455076cf84e5cc059745) 起，本仓库的提交遵循“[语义化提交](https://www.conventionalcommits.org/)”规则。

</details>

## Common features

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

## File list

<details>
<summary>文件列表</summary>

| 文件名 | 标签 |
| :-: | :-: |
| [IMG_20211014_214637.jpg](IMG_20211014_214637.jpg) | `d:maid` `m:scale:0.5` |
| [IMG_20211017_193725.jpg](IMG_20211017_193725.jpg) | `d:maid` `m:scale:0.5` |
| [IMG_20211213_020404.jpg](IMG_20211213_020404.jpg) | `d:jk` `m:censored:texture` `m:scale:0.5` |
| [IMG_20211214_212728.jpg](IMG_20211214_212728.jpg) | `d:jk` `m:scale:0.5` |
| [IMG_20211220_131537.jpg](IMG_20211220_131537.jpg) | `d:jk` `m:scale:0.5` |
| [IMG_20211220_133031.jpg](IMG_20211220_133031.jpg) | `d:jk` `d:pantyhose:white` `m:scale:0.5` |
| [IMG_20220102_131004.jpg](IMG_20220102_131004.jpg) | `d:maid` `d:pantyhose:white` `m:scale:0.5` |
| [IMG_20220301_093020.jpg](IMG_20220301_093020.jpg) | `c:rem` `d:collar` `m:scale:0.7` |
| [IMG_20220305_111148.jpg](IMG_20220305_111148.jpg) | `c:rem` `d:collar` `d:pantyhose:black` `m:scale:0.9` |
| [IMG_20220309_110201.jpg](IMG_20220309_110201.jpg) | `c:rem` `d:collar` `m:censored:mosaic` `m:scale:no` |
| [IMG_20220314_143749.jpg](IMG_20220314_143749.jpg) | `c:emilia` `m:scale:0.7` |
| [IMG_20220405_102517.jpg](IMG_20220405_102517.jpg) | `c:rem` `d:collar` `d:pantyhose:black` `d:wig:blue` `m:scale:0.9` |
| [IMG_20220423_013027.jpg](IMG_20220423_013027.jpg) | `c:rem` `d:collar` `d:wig:blue` `m:censored:texture` `m:flashlight` `m:scale:no` |
| [IMG_20220425_014658.jpg](IMG_20220425_014658.jpg) | `c:emilia` `d:wig:silver` `m:censored:texture` `m:flashlight` `m:scale:no` |
| [IMG_20220506_012442.jpg](IMG_20220506_012442.jpg) | `d:collar` `d:lolita` `d:school_gym_uniform` `m:flashlight` `m:scale:no` |
| [IMG_20220514_021011.edited.jpg](IMG_20220514_021011.edited.jpg) | `c:emilia` `m:scale:no` |
| [IMG_20220627_074454.jpg](IMG_20220627_074454.jpg) | `d:breasts:d` `d:lolita` `d:stockings:blue_and_white` `m:censored:texture` `m:scale:0.8` |
| [IMG_20220628_163516.jpg](IMG_20220628_163516.jpg) | `d:lolita` `d:stockings:blue_and_white` `m:scale:no` |
| [IMG_20220630_050442.jpg](IMG_20220630_050442.jpg) | `d:lolita` `m:censored:texture` `m:scale:0.7` |
| [IMG_20220704_041929.jpg](IMG_20220704_041929.jpg) | `c:emilia` `m:censored:texture` `m:scale:0.8` |
| [IMG_20220705_031826.jpg](IMG_20220705_031826.jpg) | `d:lolita` `d:pantyhose:black` `m:scale:no` |
| [IMG_20220708_042554.jpg](IMG_20220708_042554.jpg) | `c:minato_aqua` `m:censored:texture` `m:scale:0.9` |
| [IMG_20220710_134651.jpg](IMG_20220710_134651.jpg) | `c:snow_miku` `m:scale:no` |
| [IMG_20220711_142147.jpg](IMG_20220711_142147.jpg) | `c:snow_miku` `d:stockings` `m:scale:0.9` |
| [IMG_20220714_041044.jpg](IMG_20220714_041044.jpg) | `c:snow_miku` `m:censored_texture` `m:scale:0.9` |
| [IMG_20220716_032223.jpg](IMG_20220716_032223.jpg) | `d:lolita` `m:censored:texture` `m:scale:no` |
| [MVIMG_20220621_132055_1655788858283.jpg](MVIMG_20220621_132055_1655788858283.jpg) | `d:lolita` `d:pantyhose:white` `m:scale:0.8` |
| [MVIMG_20220709_135754.jpg](MVIMG_20220709_135754.jpg) | `d:lolita` `m:scale:0.8` |

</details>

## FAQ

<details>
<summary>常见问题详情</summary>

### 部分照片模糊？

- 常亮闪光灯拍摄效果不好；
- 拍摄姿势导致手抖 (已尽可能排除此种干扰) ；
- 已经过图像压缩处理。

### 更新频率？

暂不定期。与时间表相关。

</details>

## Appendix

参见本仓库的 [APPENDIX](APPENDIX) 。附录各条目列表如下：

<details>
<summary>条目列表</summary>

| 条目名 | 条目链接 |
| :-: | :-: |
| 使用 Python 去除图片的 EXIF 信息 | [APPENDIX/python_exif_removal.md](APPENDIX/python_exif_removal.md) |
| 标签定义表 | [APPENDIX/tag_spec.md](APPENDIX/tag_spec.md) |

</details>
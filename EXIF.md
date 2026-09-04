# 📋 EXIF 是什么？

## 简介

**EXIF**（Exchangeable Image File Format）是嵌入在图片文件中的一份"数字档案"。  
每次你用手机或相机拍照，设备会自动把拍摄时的各种信息记录进去——包括你**在哪里拍**、**用什么设备拍**、**什么时候拍**。

除了 EXIF 本身，图片还可能携带 **IPTC**、**XMP** 等元数据格式，同样能存储位置和个人信息。  

照片提交准则和常用元数据清理方法请查看 [贡献准备](CONTRIBUTING.md)。

---

## 🔴 高度敏感

**这些字段会被本项目的工作流自动检测，发现即要求修正。**  

| 字段 | 说明 |
|---|---|
| `GPS:GPSLatitude` / `GPS:GPSLongitude` | 精确地理坐标，可定位到米级 |
| `GPS:GPSAltitude` | 海拔高度 |
| `GPS:GPSDateStamp` + `GPS:GPSTimeStamp` | 精确拍摄时刻（结合坐标可还原行踪）|
| `GPS:GPSSpeed` / `GPS:GPSTrack` / `GPS:GPSImgDirection` | 移动速度、方向 |
| `IPTC:City` / `IPTC:Country` / `IPTC:Sub-location` / `IPTC:Province-State` | 文字形式的拍摄地址 |
| `XMP-photoshop:City` / `XMP-photoshop:Country` / `XMP-photoshop:State` | Photoshop/Lightroom 写入的地址 |
| `XMP-iptcCore:CreatorWorkEmail` | Creator's work email |
| `XMP-iptcCore:CreatorWorkTelephone` | 创作者电话 |
| `XMP-iptcCore:CreatorCity` / `CreatorCountry` / `CreatorPostalCode` | 创作者通讯地址 |

---

## 🟠 较敏感

**这些字段不会导致 PR 被拒，但建议留意——尤其是序列号类信息可以跨图片追踪到同一台设备。**  

| 字段 | 说明 |
|---|---|
| `EXIF:BodySerialNumber` / `EXIF:CameraSerialNumber` | 设备序列号，可跨图追踪 |
| `EXIF:LensSerialNumber` | 镜头序列号 |
| `EXIF:Artist` / `XMP-dc:Creator` | 拍摄者/创作者姓名 |
| `MakerNotes:FaceName` / `XMP-mwg-rs:PersonInImageName` | 相机人脸识别绑定的人名 |

---

## 🟡 低度敏感

**通常对隐私影响较小，本项目不拦截，保留这些信息是可以接受的。**  

| 字段 | 说明 |
|---|---|
| `EXIF:DateTimeOriginal` | 拍摄时间（无位置时风险较低） |
| `EXIF:Make` / `EXIF:Model` | 相机/手机品牌型号 |
| `EXIF:Software` | 后期处理软件 |
| `EXIF:FNumber` / `EXIF:ExposureTime` / `EXIF:ISO` | 光圈、快门、感光度等摄影参数 |
| `EXIF:Copyright` | 版权声明 |

---

## 🔍 如何自查

提交前可用以下命令查看图片中是否残留高敏感信息：  

```bash
# 安装 exiftool
# macOS:   brew install exiftool
# Ubuntu:  sudo apt install libimage-exiftool-perl
# Windows: https://exiftool.org/

# 检查单张图片
exiftool -GPS:all -IPTC:City -IPTC:Country-PrimaryLocationName \
  -XMP-photoshop:City -XMP-iptcCore:CreatorWorkEmail your_photo.jpg

# 若以上命令无任何输出，说明高敏感字段均已清除。
```

### 完整清除所有元数据
```bash
# 删除全部 EXIF/XMP/IPTC（最彻底）
exiftool -all= -o cleaned_photo.jpg your_photo.jpg
```

---

## 📖 延伸阅读

如果你对 EXIF 感兴趣，可以通过以下资源深入了解：  

- [ExifTool 官方文档](https://exiftool.org/)
- [EXIF（维基百科）](https://en.wikipedia.org/wiki/Exif)

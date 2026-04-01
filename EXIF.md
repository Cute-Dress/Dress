# 📋 EXIF 是什么？/ What is EXIF?

## 简介 / Introduction

**EXIF**（Exchangeable Image File Format）是嵌入在图片文件中的一份"数字档案"。  
每次你用手机或相机拍照，设备会自动把拍摄时的各种信息记录进去——包括你**在哪里拍**、**用什么设备拍**、**什么时候拍**。

**EXIF** (Exchangeable Image File Format) is a set of metadata embedded directly in your image file.  
Every time you take a photo, your device silently records details about when, where, and how the shot was taken.

除了 EXIF 本身，图片还可能携带 **IPTC**、**XMP** 等元数据格式，同样能存储位置和个人信息。  
Besides EXIF itself, images may also carry **IPTC** and **XMP** metadata, which can also store location and personal details.

---

## 🔴 高度敏感 / Highly Sensitive

**这些字段会被本项目的工作流自动检测，发现即要求修正。**  
**These fields are automatically detected by our CI workflow. A PR containing them will be asked to remove them.**

| 字段 / Field | 说明 / Description |
|---|---|
| `GPS:GPSLatitude` / `GPS:GPSLongitude` | 精确地理坐标，可定位到米级 / Precise coordinates, accurate to meters |
| `GPS:GPSAltitude` | 海拔高度 / Altitude |
| `GPS:GPSDateStamp` + `GPS:GPSTimeStamp` | 精确拍摄时刻（结合坐标可还原行踪）/ Exact timestamp combined with location can reveal your routine |
| `GPS:GPSSpeed` / `GPS:GPSTrack` / `GPS:GPSImgDirection` | 移动速度、方向 / Movement speed and direction |
| `IPTC:City` / `IPTC:Country` / `IPTC:Sub-location` / `IPTC:Province-State` | 文字形式的拍摄地址 / Textual shooting address |
| `XMP-photoshop:City` / `XMP-photoshop:Country` / `XMP-photoshop:State` | Photoshop/Lightroom 写入的地址 / Address written by Photoshop or Lightroom |
| `XMP-iptcCore:CreatorWorkEmail` | 创作者工作邮箱 / Creator's work email |
| `XMP-iptcCore:CreatorWorkTelephone` | 创作者电话 / Creator's phone number |
| `XMP-iptcCore:CreatorCity` / `CreatorCountry` / `CreatorPostalCode` | 创作者通讯地址 / Creator's mailing address |

---

## 🟠 较敏感 / Moderately Sensitive

**这些字段不会导致 PR 被拒，但建议留意——尤其是序列号类信息可以跨图片追踪到同一台设备。**  
**These won't block your PR, but be aware — serial numbers in particular can link multiple photos back to the same device.**

| 字段 / Field | 说明 / Description |
|---|---|
| `EXIF:BodySerialNumber` / `EXIF:CameraSerialNumber` | 设备序列号，可跨图追踪 / Device serial number, linkable across photos |
| `EXIF:LensSerialNumber` | 镜头序列号 / Lens serial number |
| `EXIF:Artist` / `XMP-dc:Creator` | 拍摄者/创作者姓名 / Photographer's name |
| `MakerNotes:FaceName` / `XMP-mwg-rs:PersonInImageName` | 相机人脸识别绑定的人名 / Face recognition tags with names |

---

## 🟡 低度敏感 / Low Sensitivity

**通常对隐私影响较小，本项目不拦截，保留这些信息是可以接受的。**  
**These generally carry low privacy risk and won't be flagged by our workflow.**

| 字段 / Field | 说明 / Description |
|---|---|
| `EXIF:DateTimeOriginal` | 拍摄时间（无位置时风险较低）/ Capture time (low risk without location) |
| `EXIF:Make` / `EXIF:Model` | 相机/手机品牌型号 / Camera or phone brand and model |
| `EXIF:Software` | 后期处理软件 / Post-processing software |
| `EXIF:FNumber` / `EXIF:ExposureTime` / `EXIF:ISO` | 光圈、快门、感光度等摄影参数 / Photography parameters |
| `EXIF:Copyright` | 版权声明 / Copyright notice |

---

## 🔍 如何自查 / How to Verify

提交前可用以下命令查看图片中是否残留高敏感信息：  
Before submitting, run the following to check if any high-sensitivity data remains:

```bash
# 安装 exiftool / Install exiftool
# macOS:   brew install exiftool
# Ubuntu:  sudo apt install libimage-exiftool-perl
# Windows: https://exiftool.org/

# 检查单张图片 / Check a single image
exiftool -GPS:all -IPTC:City -IPTC:Country-PrimaryLocationName \
  -XMP-photoshop:City -XMP-iptcCore:CreatorWorkEmail your_photo.jpg

# 若以上命令无任何输出，说明高敏感字段均已清除。
# If the command produces no output, all high-sensitivity fields have been removed.
```

### 完整清除所有元数据 / Strip all metadata

```bash
# 删除全部 EXIF/XMP/IPTC（最彻底）/ Remove all metadata (most thorough)
exiftool -all= -o cleaned_photo.jpg your_photo.jpg
```

---

## 📖 延伸阅读 / Further Reading

如果你对 EXIF 感兴趣，可以通过以下资源深入了解：  
If you'd like to learn more about image metadata:

- [ExifTool 官方文档 / Official ExifTool Documentation](https://exiftool.org/)
- [EXIF（维基百科）/ EXIF (Wikipedia)](https://en.wikipedia.org/wiki/Exif)

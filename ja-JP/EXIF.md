# 📋 EXIF ってなに？

## 概要

**EXIF**（Exchangeable Image File Format）は、画像ファイルに埋め込まれた「デジタルな履歴書」のようなものです。  
スマホやカメラで写真を撮るたびに、撮影時のさまざまな情報が自動で記録されます。たとえば、**どこで撮ったか**、**どの機材で撮ったか**、**いつ撮ったか**などです。

EXIF だけでなく、画像には **IPTC** や **XMP** などのメタデータ形式が含まれていることもあり、これらも位置情報や個人情報を保存できます。

写真提出のガイドラインと一般的なメタデータ削除方法は [コントリビューションの準備](CONTRIBUTING.md) をご覧ください。

---

## 🔴 高感度

**これらのフィールドは本プロジェクトのワークフローで自動検出され、見つかった場合は修正が必要です。**

| フィールド | 説明 |
|---|---|
| `GPS:GPSLatitude` / `GPS:GPSLongitude` | 正確な地理座標。メートル単位で特定可能 |
| `GPS:GPSAltitude` | 標高 |
| `GPS:GPSDateStamp` + `GPS:GPSTimeStamp` | 正確な撮影時刻（座標と組み合わせると行動履歴を復元可能） |
| `GPS:GPSSpeed` / `GPS:GPSTrack` / `GPS:GPSImgDirection` | 移動速度、方向 |
| `IPTC:City` / `IPTC:Country` / `IPTC:Sub-location` / `IPTC:Province-State` | テキスト形式の撮影住所 |
| `XMP-photoshop:City` / `XMP-photoshop:Country` / `XMP-photoshop:State` | Photoshop/Lightroom が書き込む住所 |
| `XMP-iptcCore:CreatorWorkEmail` | Creator's work email |
| `XMP-iptcCore:CreatorWorkTelephone` | 制作者の電話番号 |
| `XMP-iptcCore:CreatorCity` / `CreatorCountry` / `CreatorPostalCode` | 制作者の連絡先住所 |

---

## 🟠 やや敏感

**これらのフィールドは PR の拒否にはなりませんが、注意しておきましょう。特にシリアル番号系の情報は、複数の画像から同一機材を追跡できることがあります。**

| フィールド | 説明 |
|---|---|
| `EXIF:BodySerialNumber` / `EXIF:CameraSerialNumber` | 機材のシリアル番号。複数画像から追跡可能 |
| `EXIF:LensSerialNumber` | レンズのシリアル番号 |
| `EXIF:Artist` / `XMP-dc:Creator` | 撮影者・制作者の名前 |
| `MakerNotes:FaceName` / `XMP-mwg-rs:PersonInImageName` | カメラの顔認識で紐付けられた人名 |

---

## 🟡 低感度

**通常はプライバシーへの影響が小さく、本プロジェクトではブロックしません。これらの情報が残っていても問題ありません。**

| フィールド | 説明 |
|---|---|
| `EXIF:DateTimeOriginal` | 撮影時間（位置情報がなければリスクは低い） |
| `EXIF:Make` / `EXIF:Model` | カメラ・スマホのブランドと型番 |
| `EXIF:Software` | 現像・編集ソフト |
| `EXIF:FNumber` / `EXIF:ExposureTime` / `EXIF:ISO` | 絞り、シャッタースピード、ISO 感度などの撮影パラメータ |
| `EXIF:Copyright` | 著作権表示 |

---

## 🔍 セルフチェックの方法

提出前に、以下のコマンドで画像に高感度情報が残っていないか確認できます：

```bash
# exiftool をインストール
# macOS:   brew install exiftool
# Ubuntu:  sudo apt install libimage-exiftool-perl
# Windows: https://exiftool.org/

# 1枚の画像をチェック
exiftool -GPS:all -IPTC:City -IPTC:Country-PrimaryLocationName \
  -XMP-photoshop:City -XMP-iptcCore:CreatorWorkEmail your_photo.jpg

# 上記コマンドで何も出力されなければ、高感度フィールドはすべて削除済みです。
```

### すべてのメタデータを完全に削除
```bash
# EXIF/XMP/IPTC をすべて削除（最も徹底的）
exiftool -all= -o cleaned_photo.jpg your_photo.jpg
```

---

## 📖 さらに詳しく

EXIF に興味があれば、以下のリソースで詳しく学べます：

- [ExifTool 公式ドキュメント](https://exiftool.org/)
- [EXIF（Wikipedia）](https://en.wikipedia.org/wiki/Exif)

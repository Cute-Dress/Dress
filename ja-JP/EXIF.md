# 📋 EXIF ってなに？

## 概要

**EXIF**（Exchangeable Image File Format）は、写真ファイルの中に自動で埋め込まれる「撮影情報のメモ」のことです。  
スマホやデジカメで撮った写真には、見た目には分からない形で、**どこで撮ったか**、**どの機材で撮ったか**、**いつ撮ったか**などの情報が一緒に保存されています。

EXIF だけでなく、写真には **IPTC** や **XMP** などのメタデータ形式が含まれていることもあり、これらにも位置情報や個人情報が保存されます。

写真提出のガイドラインと一般的なメタデータ削除方法については [コントリビューションの準備](CONTRIBUTING.md) をご覧ください。

---

## 🔴 センシティブ

**これらのフィールドは本プロジェクトのワークフローで自動検出され、見つかった場合は修正が必要です。**

| フィールド | 説明 |
|---|---|
| `GPS:GPSLatitude` / `GPS:GPSLongitude` | 正確な地理座標。メートル単位で特定可能 |
| `GPS:GPSAltitude` | 標高 |
| `GPS:GPSDateStamp` + `GPS:GPSTimeStamp` | 正確な撮影時刻（座標と組み合わせると行動履歴を復元可能） |
| `GPS:GPSSpeed` / `GPS:GPSTrack` / `GPS:GPSImgDirection` | 移動速度、方向 |
| `IPTC:City` / `IPTC:Country` / `IPTC:Sub-location` / `IPTC:Province-State` | テキスト形式の撮影住所 |
| `XMP-photoshop:City` / `XMP-photoshop:Country` / `XMP-photoshop:State` | Photoshop/Lightroom が書き込んだアドレス |
| `XMP-iptcCore:CreatorWorkEmail` | 作成者の仕事用メール |
| `XMP-iptcCore:CreatorWorkTelephone` | 作成者の電話番号 |
| `XMP-iptcCore:CreatorCity` / `CreatorCountry` / `CreatorPostalCode` | 作成者の連絡先住所 |

---

## 🟠 ややセンシティブ

**これらのフィールドは PR の拒否にはなりませんが、注意しておきましょう。特にシリアル番号系の情報は、複数の画像から同一機材を追跡できることがあります。**

| フィールド | 説明 |
|---|---|
| `EXIF:BodySerialNumber` / `EXIF:CameraSerialNumber` | 機材のシリアル番号。複数画像から追跡可能 |
| `EXIF:LensSerialNumber` | レンズのシリアル番号 |
| `EXIF:Artist` / `XMP-dc:Creator` | 撮影者・作成者の名前 |
| `MakerNotes:FaceName` / `XMP-mwg-rs:PersonInImageName` | カメラの顔認識で紐付けられた人名 |

---

## 🟡 一般的

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

提出前に、以下のコマンドで画像にセンシティブな情報が残っていないか確認できます：

```bash
# exiftool をインストール
# macOS:   brew install exiftool
# Ubuntu:  sudo apt install libimage-exiftool-perl
# Windows: https://exiftool.org/

# 1枚の画像をチェック
exiftool -GPS:all -IPTC:City -IPTC:Country-PrimaryLocationName \
  -XMP-photoshop:City -XMP-iptcCore:CreatorWorkEmail your_photo.jpg

# 上記コマンドで何も出力されなければ、センシティブなフィールドはすべて削除済みということです。
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

# 📋 What is EXIF?

## Introduction

**EXIF** (Exchangeable Image File Format) is a set of metadata embedded directly in your image file.  
Every time you take a photo, your device silently records details about when, where, and how the shot was taken.
  
Besides EXIF itself, images may also carry **IPTC** and **XMP** metadata, which can also store location and personal details.

See the [Contribution Preparation](CONTRIBUTING.md) for photo submission criteria and common metadata removal methods.

---

## 🔴 Highly Sensitive

**These fields are automatically detected by our CI workflow. A PR containing them will be asked to remove them.**

| Field | Description |
|---|---|
| `GPS:GPSLatitude` / `GPS:GPSLongitude` | Precise coordinates, accurate to meters |
| `GPS:GPSAltitude` | Altitude |
| `GPS:GPSDateStamp` + `GPS:GPSTimeStamp` | Exact timestamp combined with location can reveal your routine |
| `GPS:GPSSpeed` / `GPS:GPSTrack` / `GPS:GPSImgDirection` | Movement speed and direction |
| `IPTC:City` / `IPTC:Country` / `IPTC:Sub-location` / `IPTC:Province-State` | Textual shooting address |
| `XMP-photoshop:City` / `XMP-photoshop:Country` / `XMP-photoshop:State` | Address written by Photoshop or Lightroom |
| `XMP-iptcCore:CreatorWorkEmail` | Creator's work email |
| `XMP-iptcCore:CreatorWorkTelephone` | Creator's phone number |
| `XMP-iptcCore:CreatorCity` / `CreatorCountry` / `CreatorPostalCode` | Creator's mailing address |

---

## 🟠 Moderately Sensitive

**These won't block your PR, but be aware — serial numbers in particular can link multiple photos back to the same device.**

| Field | Description |
|---|---|
| `EXIF:BodySerialNumber` / `EXIF:CameraSerialNumber` | Device serial number, linkable across photos |
| `EXIF:LensSerialNumber` | Lens serial number |
| `EXIF:Artist` / `XMP-dc:Creator` | Photographer's name |
| `MakerNotes:FaceName` / `XMP-mwg-rs:PersonInImageName` | Face recognition tags with names |

---

## 🟡 Low Sensitivity

**These generally carry low privacy risk and won't be flagged by our workflow.**

| Field | 说Description |
|---|---|
| `EXIF:DateTimeOriginal` | Capture time (low risk without location) |
| `EXIF:Make` / `EXIF:Model` | Camera or phone brand and model |
| `EXIF:Software` | Post-processing software |
| `EXIF:FNumber` / `EXIF:ExposureTime` / `EXIF:ISO` | Photography parameters |
| `EXIF:Copyright` | Copyright notice |

---

## 🔍 How to Verify
  
Before submitting, run the following to check if any high-sensitivity data remains:

```bash
# Install exiftool
# macOS:   brew install exiftool
# Ubuntu:  sudo apt install libimage-exiftool-perl
# Windows: https://exiftool.org/

# Check a single image
exiftool -GPS:all -IPTC:City -IPTC:Country-PrimaryLocationName \
  -XMP-photoshop:City -XMP-iptcCore:CreatorWorkEmail your_photo.jpg

# If the command produces no output, all high-sensitivity fields have been removed.
```

### Strip all metadata

```bash
# Remove all metadata (most thorough)
exiftool -all= -o cleaned_photo.jpg your_photo.jpg
```

---

## 📖 Further Reading
  
If you'd like to learn more about image metadata:

- [Official ExifTool Documentation](https://exiftool.org/)
- [EXIF (Wikipedia)](https://en.wikipedia.org/wiki/Exif)

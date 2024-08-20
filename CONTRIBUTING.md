## 照片准则 Photo Submission Criteria

- 不接受盗图和未授权转载他人图片
- Stolen pictures and unauthorized photos of other people are not accepted.
- 萌即正义
- Loveliness is righteous.
- 性别不限
- Gender is unlimited.

### 隐私提醒 Privacy Notice

照片中有 EXIF 数据，会存储地理位置、拍照设备等信息。请留意意外的个人信息泄漏，push照片前，请仔细检查照片的EXIF信息是否得到妥善处理。如果你不想公开这些信息，可以删除 EXIF。

删除方法参考：

> 使用 [GIMP](https://www.gimp.org/downloads/)：打开 GIMP，导入需要处理的图片。点击「文件」 > 「导出为」，选择图片格式如 JPEG。在弹出的「导出图像」窗口中，点击「高级选项」。取消勾选「保存 EXIF 数据」。点击「导出」，保存图片时EXIF信息将被删除。
> 
> 使用命令行工具 [ExifTool](https://exiftool.org/)：打开命令行（Windows命令提示符、Mac/Linux终端）。使用以下命令删除图片中的所有EXIF信息并保存为新文件：
> ```bash
> exiftool -all= -o new_image.jpg image.jpg
> ```
> 使用在线工具：打开任意一个EXIF删除的在线工具网站，上传需要处理的图片文件，网站会自动处理图片并去除EXIF信息，下载处理后的图片即可。（如考虑到安全问题请采取其他方法）

Please pay attention to preventing the accidental leakage of personal information. Please check carefully whether the EXIF information is properly handled (such as GPS tags) before you push the photo(s). If you want to delete EXIF, you can refer to the means below:

> Via [GIMP](https://www.gimp.org/downloads/)：Open GIMP and import the image you want to edit. Go to "File" > "Export As" and choose a format like JPEG. In the "Export Image" window, click on "Advanced Options". Uncheck the "Save EXIF data" option. Click "Export" to save the image without EXIF data.
> 
> Via Command-Line Tool [ExifTool](https://exiftool.org/)：Open the command prompt (Windows) or terminal (Mac/Linux).Use the following command to delete all EXIF information from the picture and save it as a new file:
> ```bash
> exiftool -all= -o new_image.jpg image.jpg
> ```
> Via Online Tools：Go to an online EXIF removal tool，Upload the image you want to edit. The website will automatically remove the EXIF data, and you can then download the processed image.(If you consider safety issues, please take other methods)

# LittleYe233/Dress 附录 - 使用 Python 去除图片的 EXIF 信息

可以使用 `pillow` 模块。

在终端中执行：

```bash
pip install pillow
```

在 Python 解释器中执行：

```python
from PIL import Image
img = Image.open('/path/to/image.jpg')
# print(img.size)  # 输出图片大小
# img.resize(NEW_SIZE)  # 调整图片大小
img.save('/path/to/new_image.jpg')  # 重新保存，此时 EXIF 信息已被去除
```

检查图片的 EXIF 信息：

```text
$ file image.jpg
image.jpg: JPEG image data, Exif standard: [TIFF image data, big-endian, direntries=14, height=4000, bps=0, manufacturer=HUAWEI, model=ART-AL00x, orientation=[*0*], xresolution=200, yresolution=208, resolutionunit=2, software=ARTH-AL00 9.1.1.204(C00E95R3P6), datetime=2021:06:17 21:36:14, width=3000], baseline, precision 8, 3000x4000, components 3

$ file new_image.jpg
new_image.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 3000x4000, components 3
```
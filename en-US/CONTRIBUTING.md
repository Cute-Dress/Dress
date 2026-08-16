## Photo Submission Criteria

- Stolen pictures and unauthorized photos of other people are not accepted.
- Loveliness is righteous.
- Gender is unlimited.

### Privacy Notice

Please pay attention to preventing the accidental leakage of personal information. Please check carefully whether the EXIF information is properly handled (such as GPS tags) before you push the photo(s). If you want to delete EXIF, you can refer to the means below:

The project automatically blocks high-sensitivity metadata such as GPS, address, and contact fields. See the [EXIF field guide](EXIF.md) for the exact scope and sensitivity levels.

> 1.Via [GIMP](https://www.gimp.org/downloads/)：Open GIMP and import the image you want to edit. Go to "File" > "Export As" and choose a format like JPEG. In the "Export Image" window, click on "Advanced Options". Uncheck the "Save EXIF data" option. Click "Export" to save the image without EXIF data.
> 
> 2.Via Command-Line Tool [ExifTool](https://exiftool.org/)：Open the command prompt (Windows) or terminal (Mac/Linux).Use the following command to delete all EXIF information from the picture and save it as a new file:
> ```bash
> exiftool -all= -o new_image.jpg image.jpg
> ```
> 3.Via Online Tools：Go to an online EXIF removal tool，Upload the image you want to edit. The website will automatically remove the EXIF data, and you can then download the processed image.(If you consider safety issues, please take other methods)
>
>*(If EXIF data still cannot be removed, you can use the /auto-fix command from the repository when merging your PR to remove it.)*

### Pay attention to case sensitivity

To prevent excessive resource usage on GitHub, please check the photo size before uploading. If it exceeds `1MB`, you need to compress the image.

Compression methods are as follows:

> **Use an online tool:** Open any online image compression website, upload the image file you want to process, and the site will automatically compress it. Then, simply download the processed image. (If you have security concerns, please use alternative methods.)
>
> *(If the image size is still greater than 1MB after compression, you can use the repository's `/auto-fix` command when merging your PR to compress the image.)*
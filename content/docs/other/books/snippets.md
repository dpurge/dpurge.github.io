# Snippets

## Export PDF to PNG

```pwsh
Import-Module -Name D:\src\github.com\dpurge\jdp-psmodule\src\JdpBookbind
Invoke-Book2Image -OutputDirectory img -InputFile book.pdf
```

## Merge two directories with images

```pwsh
$a = Get-ChildItem -Filter *.png ./img1
$b = Get-ChildItem -Filter *.png ./img2

$imgs = $a + $b
$i = 0

foreach ($img in $imgs) {
  $f = "./img/page-{0:d3}.png" -f $i
  Write-Host "$img -> $f"
  Move-Item -Path $img -Destination $f
  $i++
}
```

## Render PDF pages

```pwsh
0..350 | %{D:\pgm\ImageMagick\convert.exe -density 300 book.pdf[$_] -quality 100 ("./img/page-{0:d3}.tif" -f $_)}
0..350 | %{D:\pgm\ImageMagick\convert.exe -density 300 book.pdf[$_] -quality 100 -type Grayscale -filter Lanczos ("./img/page-{0:d3}.png" -f $_)}
```

## Convert to grayscale

```pwsh
$files = Get-ChildItem -Filter *.png
foreach($file in $files) {
  $outfile = "${pwd}\out\$($file.Name)"
  Write-Host "$file -> $outfile"
  # D:\pgm\ImageMagick\convert.exe -grayscale Rec709Luminance $file $outfile
  D:\pgm\ImageMagick\convert.exe -negate $file $outfile
  # D:\pgm\ImageMagick\convert.exe $file -depth 4 -colorspace gray -define png:color-type=0 -define png:bit-depth=4 $outfile
}
```

## Convert FLAC to MP3

```pwsh
$files = Get-ChildItem -Filter *.flac
foreach($file in $files) {
  $outfile = ($file.Fullname -replace '.flac$','.mp3')
  Write-Host "$file -> $outfile"
  D:\pgm\ffmpeg\bin\ffmpeg.exe -i $file -ab 320k -map_metadata 0 -id3v2_version 3 $outfile
}
```

## Convert WMA to MP3

```pwsh
$files = Get-ChildItem -Filter *.wma
foreach($file in $files) {
  $outfile = ($file.Fullname -replace '.wma$','.mp3')
  Write-Host "$file -> $outfile"
  D:\pgm\ffmpeg\bin\ffmpeg.exe -i $file -ab 192k $outfile
}
```

## Convert WEBM to MP3

```pwsh
D:\pgm\ffmpeg\bin\ffmpeg.exe -i nagranie.webm -vn -ab 128k -ar 44100 -y nagranie.mp3
```

## Download from YouTube

```pwsh
youtube-dl -x --audio-format mp3 <Video-URL>
youtube-dl -f bestaudio[ext=m4a] --embed-thumbnail --add-metadata <Video-URL>
```

## Convert PNG to SVG

```pwsh
$files = Get-ChildItem -Filter *.png
foreach($pngfile in $files) {
  $bmpfile = ($pngfile.Fullname -replace '([^.]).png','.bmp')
  $svgfile = ($pngfile.Fullname -replace '([^.]).png','.svg')
  Write-Host "$pngfile -> $bmpfile -> $svgfile"
  D:\pgm\ImageMagick\convert.exe $pngfile $bmpfile
  potrace.exe -s -a0 $bmpfile
}
```

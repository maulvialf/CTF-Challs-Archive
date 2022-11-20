## Judul Soal
QR Blocks

## Deskripsi Soal
>It was originally QR code. But for some reason, it was turned into several identical blocks

## Hint Soal
- Each of QR blocks are identical & have the same property

---

## Penjelasan Penyelesaian Soal

Given a PNG file `qr.png`. As stated in the description, we know that each block are identical that make a QR Code. Based on these fact, we can assumed that each blocks also have the same IHDR chunk.

<br>

**Identification**

After several inspection on `chunks level`, we found some repetitive oFFs-IDAT patterns. It also has some kind of identifier on its CRC. For example, `496d3531` equals to `Im51`

```
$ head <<< $(pchunk_info qr.png)                                                                                                      
Filename: qr.png
Size: 6241

Chunk Info
Id   Type Offset    Size         Data Length CRC                           
0    IHDR 0xc       13           13          3644b51c                      
1    oFFs 0x25      9            9           496d3531 (Must be e2607100)   
2    IDAT 0x3a      55           55          496d3531 (Must be caafa716)   
3    oFFs 0x7d      9            9           496d3339 (Must be 12361ed6)   
4    IDAT 0x92      55           55          496d3339 (Must be c7f544fa)  
```

Thus, we can assumed that it represents an individual QR code

<br>

**QR code Arrangement**

Based on this [literature](http://www.libpng.com/pub/png/book/chapter11.html#png.ch11.div.10), the oFFS chunk is used to represents the absolute position of image on a canvas.

```
For images that are available separately but envisioned as part of a greater whole, the image-offset chunk, oFFs, can be used to specify the absolute positioning of each. The most common example is positioning on a printed page, especially in conjunction with the pHYs chunk.
``` 

Thus, we can arrange each of QR blocks based on given oFFs in order to restore the original QR code. Here is the implementation using `solver.py`

```
$ python2 solve.py 
redmask{qr_c0de_in_mon0chrom3_haystack}
```

[](solver/flag.png)
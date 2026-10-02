import os,shutil
from PIL import Image
res="android/app/src/main/res"
shutil.rmtree(res+"/mipmap-anydpi-v26",ignore_errors=True)
im=Image.open("icon.png").convert("RGBA")
for d,s in {"mdpi":48,"hdpi":72,"xhdpi":96,"xxhdpi":144,"xxxhdpi":192}.items():
    r=im.resize((s,s),Image.LANCZOS)
    for n in ("ic_launcher","ic_launcher_round","ic_launcher_foreground"):
        r.save(f"{res}/mipmap-{d}/{n}.png")

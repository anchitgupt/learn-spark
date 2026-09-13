"""Recreate the original silent explainer. Optional tools: Pillow and ffmpeg."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
font_paths = ['/System/Library/Fonts/Supplemental/Arial.ttf', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf']
font_path = next((p for p in font_paths if Path(p).exists()), None)
def font(size):
    return ImageFont.truetype(font_path, size) if font_path else ImageFont.load_default()
rows = [('Pune',0,0,0,0,'#ae4427'),('Delhi',0,1,1,0,'#527966'),('Mumbai',1,0,2,0,'#627994'),('Pune',1,1,0,1,'#ae4427'),('Delhi',2,0,1,1,'#527966'),('Pune',2,1,0,2,'#ae4427')]
with tempfile.TemporaryDirectory(prefix='spark-video-') as temp:
    for frame in range(288):
        t = frame / 24
        im = Image.new('RGB',(1000,600),'#f8f7f3')
        d = ImageDraw.Draw(im)
        d.text((40,27),'SPARK FIELDNOTES  /  THE SHUFFLE',font=font(17),fill='#ae4427')
        title = 'Same data. Scattered keys.' if t < 3 else 'Bring matching city keys together.' if t < 8 else 'Now each city can be counted.'
        d.text((40,68),title,font=font(32),fill='#29332e')
        d.text((45,130),'INPUT PARTITIONS',font=font(15),fill='#626e5d')
        d.text((684,130),'OUTPUT PARTITIONS',font=font(15),fill='#626e5d')
        for i in range(3):
            for x in [40,680]:
                d.rounded_rectangle((x,165+i*105,x+280,250+i*105),radius=6,fill='#eeefe7',outline='#d5dacb')
                d.text((x+12,172+i*105),'P'+str(i),font=font(13),fill='#626e5d')
        progress = max(0,min(1,(t-3)/5)); progress = progress*progress*(3-2*progress)
        for city,inp,slot,target,out,color in rows:
            x1,y1 = 80+slot*105,200+inp*105
            x2,y2 = 721+out*74,200+target*105
            if t>=3: d.line((x1+35,y1+15,x2+35,y2+15),fill='#d7d7cb',width=2)
            x,y=x1+(x2-x1)*progress,y1+(y2-y1)*progress
            d.rounded_rectangle((x,y,x+70,y+33),radius=5,fill=color)
            d.text((x+5,y+7),city,font=font(15),fill='white')
        caption = 'Six rows. Three partitions. Pune appears in each input.' if t < 3 else 'Illustrated key assignment: records cross partition boundaries.' if t < 8 else 'Pune: 3      Delhi: 2      Mumbai: 1'
        d.text((40,494),caption,font=font(21),fill='#29332e')
        d.text((40,548),'Conceptual model: Spark may aggregate locally before shuffling.',font=font(15),fill='#697161')
        im.save(Path(temp)/f'{frame:04}.png')
        if frame == 0: im.save(ROOT/'assets/video-poster.png')
    subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate','24','-i',str(Path(temp)/'%04d.png'),'-c:v','libx264','-pix_fmt','yuv420p','-movflags','+faststart',str(ROOT/'assets/shuffle.mp4')],check=True)
print('Created 12-second H.264 explainer and poster.')

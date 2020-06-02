import hue
import pychromecast

# input
h = hue.Bridge()
tmedia = input('Play url: ')

# magic
#tmedia = 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4'
ctype = 'video/mp4'

print (tmedia, ctype)

h.setGroup(1,on=False)
h.setGroup(2,on=False)
chromecasts = pychromecast.get_chromecasts()
cast = next(cc for cc in chromecasts if cc.device.friendly_name == "TV")
cast.wait()
mc = cast.media_controller
mc.play_media ( tmedia, ctype)
mc.block_until_active()
#h.setGroup(1,on=True)
#h.setGroup(2,on=True)

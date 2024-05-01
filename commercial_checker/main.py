from ipytv import playlist


url = "https://iptv-org.github.io/iptv/index.m3u"
pl = playlist.loadu(url)
print(pl.length())


for channel in pl:
  if "tnt" == channel.name.lower():
    tnt = channel

print(tnt.attributes)
print(tnt.name)

print(tnt.url)


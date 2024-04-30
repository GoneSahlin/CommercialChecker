from m3u_parser import M3uParser

url = "https://iptv-org.github.io/iptv/index.m3u"
useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"

# Instantiate the parser
parser = M3uParser(timeout=5, useragent=useragent)

# Parse the m3u file
parser.parse_m3u(url)

# Get the list of streams
print(len(parser.get_list()))


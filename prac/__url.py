import urllib.request

urllib.request.get("http://www.hertaville.com/interfacing-an-spi-adc-mcp3008-chip-to-the-raspberry-pi-using-c.html", timeout=60)

with urllib.request.urlopen('http://www.hertaville.com/interfacing-an-spi-adc-mcp3008-chip-to-the-raspberry-pi-using-c.html') as f:
	print(f.read(1000))
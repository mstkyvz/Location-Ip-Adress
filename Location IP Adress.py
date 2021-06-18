import pygeoip # pip install pygeoip
gip = pygeoip.GeoIP("GeoLiteCity.dat")
res = gip.record_by_addr('ip adress')
for key, val in res.items():
    print('%s : %s' % (key,val))
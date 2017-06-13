from opensky_api import OpenSkyApi
import time

api = OpenSkyApi()
while (1):
    s = api.get_states()
   # i = 0
    for obj in s.states:
        if obj.origin_country == "France":
            #print(obj)
            koala = ""
            koala += ("altitude=" + str(obj.altitude) + ";")
            koala += ("callsign=" + str(obj.callsign) + ";")
            koala += ("heading=" + str(obj.heading) + ";")
            koala += ("icao24=" + str(obj.icao24) + ";")
            koala += ("latitude=" + str(obj.latitude) + ";")
            koala += ("longitude=" + str(obj.longitude) + ";")
            koala += ("on_ground=" + str(obj.on_ground) + ";")
            koala += ("origin_country=" + str(obj.origin_country) + ";")
            koala += ("sensors=" + str(obj.sensors) + ";")
            koala += ("time_position=" + str(obj.time_position) + ";")
            koala += ("time_velocity=" + str(obj.time_velocity) + ";")
            koala += ("velocity=" + str(obj.velocity) + ";")
            koala += ("vertical_rate=" + str(obj.vertical_rate))
            print(koala)
            #i = i + 1
    print("")
    #print(i)
    time.sleep(10)

import json
import requests
import exifread
import geoip2.database
import pyowm


def get_information():
    with open('20211227_190825.jpg', 'rb') as f:
        exif_dict = exifread.process_file(f)

        # 经度
        lon_ref = exif_dict["GPS GPSLongitudeRef"].printable
        lon = exif_dict["GPS GPSLongitude"].printable[1:-1].replace(" ", "").replace("/", ",").split(",")
        lon = float(lon[0]) + float(lon[1]) / 60 + float(lon[2]) / float(lon[3]) / 3600
        if lon_ref != "E":
            lon = lon * (-1)

        # 纬度
        lat_ref = exif_dict["GPS GPSLatitudeRef"].printable
        lat = exif_dict["GPS GPSLatitude"].printable[1:-1].replace(" ", "").replace("/", ",").split(",")
        lat = float(lat[0]) + float(lat[1]) / 60 + float(lat[2]) / float(lat[3]) / 3600
        if lat_ref != "N":
            lat = lat * (-1)
        print('Latitude and longitude of the photo：', (lat, lon))

        # 调用百度地图api转换经纬度为详细地址
        secret_key = 'MAsVGINLNyTGiM4UulcaeluCekGnAFxj'  # 百度地图api 需要注册创建应用
        baidu_map_api = 'http://api.map.baidu.com/reverse_geocoding/v3/?ak={}&output=json&coordtype=wgs84ll&location={},{}'.format(
            secret_key, lat, lon)
        content = requests.get(baidu_map_api).text
        gps_address = json.loads(content)
        # 结构化的地址
        formatted_address = gps_address["result"]["formatted_address"]
        # 国家（若需访问境外POI，需申请逆地理编码境外POI服务权限）
        country = gps_address["result"]["addressComponent"]["country"]
        # 省
        province = gps_address["result"]["addressComponent"]["province"]
        # 市
        city = gps_address["result"]["addressComponent"]["city"]
        # 区
        district = gps_address["result"]["addressComponent"]["district"]
        # 语义化地址描述
        sematic_description = gps_address["result"]["sematic_description"]

        print(formatted_address)
        print(gps_address["result"]["business"])


def get_location(ip):
    reader = geoip2.database.Reader('./GeoLite2-City.mmdb')
    response = reader.city(ip)
    return response.city.names["en"]


def get_IP():
    request = requests.get('http://ifconfig.me/ip', timeout=1).text.strip()
    return request

def get_weather():
    """w has "detailed_status" "wind()" "humidity" "temperature('celsius')" "rain" "heat_index" """
    location = str(get_location(get_IP()))[:-3]
    owm = pyowm.OWM('ce26aec49e7330404ec4f1cb536210be')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(location)
    w = observation.weather
    return w



if __name__ == '__main__':
    w = get_weather()
    print(w.detailed_status)
    print(w.humidity)
    print(w.temperature("celsius"))


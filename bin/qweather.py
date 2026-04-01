#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QWeather API Tool - Python Version
和风天气 API 查询工具

Usage:
    python qweather.py <command> [args]

Commands:
    lookup CITY             Search city by pinyin (with auto-cache)
    now CITYID              Current weather
    forecast CITYID [DAYS]  Weather forecast (3d/7d/10d/15d/30d)
    indices CITYID [DAYS]   Life indices
    storm-list [YEAR]       Typhoon list ⚠️ PAID (¥0.003/call)
    storm-track ID          Typhoon track ⚠️ PAID (¥0.003/call)
    storm-forecast ID       Typhoon forecast ⚠️ PAID (¥0.003/call)
    minutely LOC            Minute precipitation
    alert LOC               Weather alert
    air-now LOC             Air quality
    air-hourly LOC          Hourly air quality
    air-daily LOC           Daily air quality
    sun LOC [DATE]          Sunrise/sunset
    moon LOC [DATE]         Moonrise/moonset
    cache-list              List cached cities
    help                    Show this help

⚠️  Notice: Typhoon commands (storm-list, storm-track) are PAID interfaces.
    Free tier does NOT include typhoon data. Use with caution!

Cache:
    - lookup 命令会自动缓存查询过的城市
    - 优先从缓存查找，减少 API 调用
    - 缓存文件：city-cache.json
"""

import os
import sys
import json
import requests
import io
from datetime import datetime
from pathlib import Path

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# Get script directory
SCRIPT_DIR = Path(__file__).parent
ROOT_DIR = SCRIPT_DIR.parent
ENV_FILE = ROOT_DIR / ".env"
CACHE_FILE = ROOT_DIR / "city-cache.json"

# Load .env file
def load_env():
    if ENV_FILE.exists():
        with open(ENV_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip().strip('"').strip("'")
                    os.environ[key] = value

# Cache functions
def load_cache():
    if CACHE_FILE.exists():
        try:
            with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_cache(cache):
    with open(CACHE_FILE, 'w', encoding='utf-8') as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

def find_in_cache(pinyin):
    cache = load_cache()
    pinyin = pinyin.lower()
    for city_id, data in cache.items():
        if data.get('pinyin', '').lower() == pinyin:
            return data
    return None

def add_to_cache(location, pinyin):
    cache = load_cache()
    city_id = location.get('id')
    now = datetime.now().astimezone().isoformat()
    
    if city_id not in cache:
        cache[city_id] = {
            'id': location.get('id'),
            'name': location.get('name'),
            'adm1': location.get('adm1'),
            'adm2': location.get('adm2'),
            'country': location.get('country'),
            'lat': location.get('lat'),
            'lon': location.get('lon'),
            'pinyin': pinyin,
            'firstQueried': now,
            'lastQueried': now,
            'queryCount': 1
        }
    else:
        cache[city_id]['lastQueried'] = now
        cache[city_id]['queryCount'] += 1
    
    save_cache(cache)
    return cache[city_id]

# API functions
def api_request(endpoint, params=None):
    api_key = os.environ.get('QWEATHER_API_KEY')
    api_host = os.environ.get('QWEATHER_API_HOST', 'devapi.qweather.com')
    
    if not api_key:
        print("Error: QWEATHER_API_KEY not configured", file=sys.stderr)
        print("\nPlease create .env file with:", file=sys.stderr)
        print("  QWEATHER_API_KEY=your_api_key_here", file=sys.stderr)
        print("  QWEATHER_API_HOST=your_api_host_here\n", file=sys.stderr)
        sys.exit(1)
    
    url = f"https://{api_host}{endpoint}"
    headers = {'X-QW-Api-Key': api_key}
    
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()

def cmd_lookup(pinyin):
    """Search city by pinyin with auto-cache"""
    # Try cache first
    cached = find_in_cache(pinyin)
    if cached:
        print(f"✅ 从缓存找到：{cached['name']} (ID: {cached['id']})")
        print(f"   已查询：{cached['queryCount']} 次，最后查询：{cached['lastQueried']}")
        result = {
            'code': '200',
            'location': [cached],
            'refer': {'sources': ['QWeather Cache'], 'license': ['QWeather Developers License']}
        }
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return
    
    # Call API
    print(f"🔍 缓存未找到，调用 API 查询：{pinyin}")
    result = api_request('/geo/v2/city/lookup', {'location': pinyin})
    
    if result.get('code') == '200' and result.get('location'):
        first = result['location'][0]
        first['pinyin'] = pinyin
        cached = add_to_cache(first, pinyin)
        print(f"✅ 已缓存：{cached['name']} (ID: {cached['id']})")
    
    print(json.dumps(result, ensure_ascii=False))

def cmd_now(city_id):
    """Current weather"""
    result = api_request('/v7/weather/now', {'location': city_id})
    print(json.dumps(result, ensure_ascii=False))

def cmd_forecast(city_id, days='3d'):
    """Weather forecast"""
    result = api_request(f'/v7/weather/{days}', {'location': city_id})
    print(json.dumps(result, ensure_ascii=False))

def cmd_indices(city_id, days='1d', types=None):
    """Life indices"""
    if types is None:
        types = '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16'
    result = api_request(f'/v7/indices/{days}', {'location': city_id, 'type': types})
    print(json.dumps(result, ensure_ascii=False))

def cmd_storm_list(year=None):
    """Typhoon list - PAID interface"""
    print("⚠️  WARNING: Typhoon interface is PAID (¥0.003/call), NOT included in free tier!", file=sys.stderr)
    print("⚠️  警告：台风接口为付费接口（¥0.003/次），不在免费额度内！\n", file=sys.stderr)
    
    if year is None:
        year = datetime.now().year
    result = api_request('/v7/tropical/storm-list', {'year': year, 'basin': 'NP'})
    print(json.dumps(result, ensure_ascii=False))

def cmd_storm_track(storm_id):
    """Typhoon track - PAID interface"""
    print("⚠️  WARNING: Typhoon interface is PAID (¥0.003/call), NOT included in free tier!", file=sys.stderr)
    print("⚠️  警告：台风接口为付费接口（¥0.003/次），不在免费额度内！\n", file=sys.stderr)
    
    result = api_request('/v7/tropical/storm-track', {'stormId': storm_id})
    print(json.dumps(result, ensure_ascii=False))

def cmd_storm_forecast(storm_id):
    """Typhoon forecast - PAID interface"""
    print("⚠️  WARNING: Typhoon interface is PAID (¥0.003/call), NOT included in free tier!", file=sys.stderr)
    print("⚠️  警告：台风接口为付费接口（¥0.003/次），不在免费额度内！\n", file=sys.stderr)
    
    result = api_request('/v7/tropical/storm-forecast', {'stormId': storm_id})
    print(json.dumps(result, ensure_ascii=False))

def parse_location(loc):
    """Parse location to lon,lat"""
    if ',' in loc:
        return loc
    # Try to get coords from city ID
    result = api_request('/geo/v2/city/lookup', {'location': loc})
    if result.get('code') == '200' and result.get('location'):
        first = result['location'][0]
        return f"{first['lon']},{first['lat']}"
    raise ValueError(f"Cannot get coords for {loc}")

def cmd_minutely(loc):
    """Minute precipitation"""
    coords = parse_location(loc)
    lon, lat = coords.split(',')
    result = api_request('/v7/minutely/5m', {'lon': lon, 'lat': lat})
    print(json.dumps(result, ensure_ascii=False))

def cmd_alert(loc):
    """Weather alert"""
    coords = parse_location(loc)
    lat, lon = coords.split(',')[::-1]
    result = api_request(f'/weatheralert/v1/current/{lat}/{lon}')
    print(json.dumps(result, ensure_ascii=False))

def cmd_air_now(loc):
    """Air quality"""
    coords = parse_location(loc)
    lat, lon = coords.split(',')[::-1]
    result = api_request(f'/airquality/v1/current/{lat}/{lon}')
    print(json.dumps(result, ensure_ascii=False))

def cmd_air_hourly(loc):
    """Hourly air quality"""
    coords = parse_location(loc)
    lat, lon = coords.split(',')[::-1]
    result = api_request(f'/airquality/v1/hourly/{lat}/{lon}')
    print(json.dumps(result, ensure_ascii=False))

def cmd_air_daily(loc):
    """Daily air quality"""
    coords = parse_location(loc)
    lat, lon = coords.split(',')[::-1]
    result = api_request(f'/airquality/v1/daily/{lat}/{lon}')
    print(json.dumps(result, ensure_ascii=False))

def cmd_sun(loc, date=None):
    """Sunrise/sunset"""
    if date is None:
        date = datetime.now().strftime('%Y%m%d')
    coords = parse_location(loc)
    lon, lat = coords.split(',')
    result = api_request('/v7/astronomy/sun', {'lon': lon, 'lat': lat, 'date': date})
    print(json.dumps(result, ensure_ascii=False))

def cmd_moon(loc, date=None):
    """Moonrise/moonset"""
    if date is None:
        date = datetime.now().strftime('%Y%m%d')
    coords = parse_location(loc)
    lon, lat = coords.split(',')
    result = api_request('/v7/astronomy/moon', {'lon': lon, 'lat': lat, 'date': date})
    print(json.dumps(result, ensure_ascii=False))

def cmd_cache_list():
    """List cached cities"""
    cache = load_cache()
    if not cache:
        print("📥 缓存为空")
        return
    
    print("📝 已缓存城市列表：\n")
    sorted_cache = sorted(cache.items(), key=lambda x: x[1].get('queryCount', 0), reverse=True)
    for city_id, data in sorted_cache:
        print(f"  🏙️  {data['name']} ({data['adm1']})")
        print(f"     ID: {data['id']} | 坐标：{data['lat']}, {data['lon']}")
        print(f"     查询：{data['queryCount']} 次 | 最后：{data['lastQueried']}")
        print()

def cmd_help():
    """Show help"""
    print(__doc__)

def main():
    load_env()
    
    if len(sys.argv) < 2:
        cmd_help()
        sys.exit(1)
    
    cmd = sys.argv[1]
    args = sys.argv[2:]
    
    commands = {
        'lookup': cmd_lookup,
        'now': cmd_now,
        'forecast': cmd_forecast,
        'indices': cmd_indices,
        'storm-list': cmd_storm_list,
        'storm-track': cmd_storm_track,
        'storm-forecast': cmd_storm_forecast,
        'minutely': cmd_minutely,
        'alert': cmd_alert,
        'air-now': cmd_air_now,
        'air-hourly': cmd_air_hourly,
        'air-daily': cmd_air_daily,
        'sun': cmd_sun,
        'moon': cmd_moon,
        'cache-list': cmd_cache_list,
        'help': cmd_help,
    }
    
    if cmd in commands:
        try:
            commands[cmd](*args)
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(f"Unknown command: {cmd}", file=sys.stderr)
        cmd_help()
        sys.exit(1)

if __name__ == '__main__':
    main()

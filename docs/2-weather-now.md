# 2. 实时天气 (Weather Now)

> 查询当前天气状况，包括温度、体感温度、天气现象、风向风力等。

---

## 🔧 API 请求

```bash
curl --compressed \
  -H "X-QW-Api-Key: {apiKey}" \
  'https://{Host}/v7/weather/now?location={cityid}'
```

## 📝 参数说明

- `location`: 城市 ID 或经纬度（如 `101010100` 或 `116.41,39.92`）

## 💡 使用示例

```bash
curl --compressed \
  -H "X-QW-Api-Key: {apiKey}" \
  'https://{Host}/v7/weather/now?location=101010100'
```

---

## 🚀 使用 Python 脚本

```bash
# 查询北京实时天气
python bin/qweather.py now 101010100
```

---

## 🔗 相关文档

- [1. 城市搜索](1-city-lookup.md)
- [3. 天气预报](3-weather-forecast.md)

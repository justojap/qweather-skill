# 3. 天气预报 (Weather Forecast)

> 查询 3/7/10/15/30 天天气预报。

---

## 🔧 API 请求

```bash
curl --compressed \
  -H "X-QW-Api-Key: {apiKey}" \
  'https://{Host}/v7/weather/{days}?location={cityid}'
```

## 📝 参数说明

- `days`: 预报天数（`3d`、`7d`、`10d`、`15d`、`30d`）
- `location`: 城市 ID 或经纬度

## 💡 使用示例

```bash
# 查询北京 3 天预报
curl --compressed \
  -H "X-QW-Api-Key: {apiKey}" \
  'https://{Host}/v7/weather/3d?location=101010100'
```

---

## 🚀 使用 Python 脚本

```bash
# 查询北京 7 天预报
python bin/qweather.py forecast 101010100 7d

# 查询 30 天预报
python bin/qweather.py forecast 101010100 30d
```

---

## 🔗 相关文档

- [2. 实时天气](2-weather-now.md)
- [4. 生活指数](4-weather-indices.md)

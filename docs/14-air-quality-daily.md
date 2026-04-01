# 14. 空气质量每日预报 (Air Quality Daily Forecast)

> 查询未来 3-7 天空气质量每日预报。

---

## 🔧 API 请求

```bash
curl --compressed \
  -H "X-QW-Api-Key: {apiKey}" \
  'https://{Host}/airquality/v1/daily/{纬度}/{经度}'
```

## 📝 参数说明

- `纬度`: 地点纬度
- `经度`: 地点经度

## 💡 使用示例

```bash
curl --compressed \
  -H "X-QW-Api-Key: {apiKey}" \
  'https://{Host}/airquality/v1/daily/23.13/113.26'
```

---

## 🚀 使用 Python 脚本

```bash
python bin/qweather.py air-daily 101280101
```

---

## 🔗 相关文档

- [10. 实时空气质量](10-air-quality-now.md)
- [13. 空气质量小时预报](13-air-quality-hourly.md)

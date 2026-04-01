# 13. 空气质量小时预报 (Air Quality Hourly Forecast)

> 查询未来 24 小时空气质量小时预报。

---

## 🔧 API 请求

```bash
curl --compressed \
  -H "X-QW-Api-Key: {apiKey}" \
  'https://{Host}/airquality/v1/hourly/{纬度}/{经度}'
```

## 📝 参数说明

- `纬度`: 地点纬度
- `经度`: 地点经度

## 💡 使用示例

```bash
curl --compressed \
  -H "X-QW-Api-Key: {apiKey}" \
  'https://{Host}/airquality/v1/hourly/23.13/113.26'
```

---

## 🚀 使用 Python 脚本

```bash
python bin/qweather.py air-hourly 101280101
```

---

## 🔗 相关文档

- [10. 实时空气质量](10-air-quality-now.md)
- [14. 空气质量每日预报](14-air-quality-daily.md)

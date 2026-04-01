# 10. 实时空气质量 (Air Quality Now)

> 查询当前空气质量指数（AQI）及污染物浓度。

---

## 🔧 API 请求

```bash
curl --compressed \
  -H "X-QW-Api-Key: {apiKey}" \
  'https://{Host}/airquality/v1/current/{纬度}/{经度}'
```

## 📝 参数说明

- `纬度`: 地点纬度（如 `23.13`）
- `经度`: 地点经度（如 `113.26`）

## 💡 使用示例

```bash
curl --compressed \
  -H "X-QW-Api-Key: {apiKey}" \
  'https://{Host}/airquality/v1/current/23.13/113.26'
```

**返回：**
```json
{
  "code": "200",
  "now": {
    "aqi": "45",
    "pm2p5": "20",
    "pm10": "35",
    "so2": "8",
    "no2": "25",
    "o3": "80",
    "co": "0.5",
    "primary": "O3"
  }
}
```

---

## 🚀 使用 Python 脚本

```bash
# 查询广州实时空气质量
python bin/qweather.py air-now 101280101

# 或使用坐标
python bin/qweather.py air-now 113.26,23.13
```

---

## 📊 AQI 等级

| AQI 范围 | 等级 | 颜色 | 说明 |
|----------|------|------|------|
| 0-50 | 优 | 绿色 | 空气质量令人满意 |
| 51-100 | 良 | 黄色 | 空气质量可接受 |
| 101-150 | 轻度污染 | 橙色 | 敏感人群症状加剧 |
| 151-200 | 中度污染 | 红色 | 进一步加剧易感人群症状 |
| 201-300 | 重度污染 | 紫色 | 心脏病和肺病患者症状显著加剧 |
| >300 | 严重污染 | 褐红色 | 健康人群运动耐受力降低 |

---

## 🔗 相关文档

- [13. 空气质量小时预报](13-air-quality-hourly.md)
- [14. 空气质量每日预报](14-air-quality-daily.md)

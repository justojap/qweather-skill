# 8. 分钟级降水 (Minutely Precipitation)

> 查询未来 2 小时的分钟级降水预报。✅ **免费接口**（5 万/月）

---

## 🔧 API 请求

```bash
curl --compressed \
  -H "X-QW-Api-Key: {apiKey}" \
  'https://{Host}/v7/minutely/5m?location={经纬度}'
```

## 📝 参数说明

- `location`: 经纬度（如 `113.28,23.12`）

## 💡 使用示例

```bash
curl --compressed \
  -H "X-QW-Api-Key: {apiKey}" \
  'https://{Host}/v7/minutely/5m?location=113.28,23.12'
```

---

## 🚀 使用 Python 脚本

```bash
# 查询分钟级降水
python bin/qweather.py minutely 113.28,23.12
```

---

## 🔗 相关文档

- [9. 天气预警](9-weather-alert.md)

# 9. 天气预警 (Weather Alert)

> 查询当前生效的天气预警信息。✅ **免费接口**（5 万/月）

---

## 🔧 API 请求

```bash
curl --compressed \
  -H "X-QW-Api-Key: {apiKey}" \
  'https://{Host}/weatheralert/v1/current/{纬度}/{经度}'
```

## 📝 参数说明

- `纬度`: 地点纬度
- `经度`: 地点经度

## 💡 使用示例

```bash
curl --compressed \
  -H "X-QW-Api-Key: {apiKey}" \
  'https://{Host}/weatheralert/v1/current/23.13/113.26'
```

---

## 🚀 使用 Python 脚本

```bash
# 查询广州天气预警
python bin/qweather.py alert 101280101
```

---

## 🔗 相关文档

- [8. 分钟级降水](8-minutely-precipitation.md)

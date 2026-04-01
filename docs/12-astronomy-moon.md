# 12. 月升月落 (Astronomy Moon)

> 查询指定日期的月升月落时间和月相。

---

## 🔧 API 请求

```bash
curl --compressed \
  -H "X-QW-Api-Key: {apiKey}" \
  'https://{Host}/v7/astronomy/moon?location={城市 ID|经纬度}&date={日期}'
```

## 📝 参数说明

- `location`: 城市 ID 或经纬度
- `date`: 日期（格式：YYYYMMDD）

## 💡 使用示例

```bash
curl --compressed \
  -H "X-QW-Api-Key: {apiKey}" \
  'https://{Host}/v7/astronomy/moon?location=101280101&date=20260401'
```

---

## 🚀 使用 Python 脚本

```bash
# 查询广州今日月升月落
python bin/qweather.py moon 101280101
```

---

## 🔗 相关文档

- [11. 日出日落](11-astronomy-sun.md)

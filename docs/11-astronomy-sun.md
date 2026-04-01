# 11. 日出日落 (Astronomy Sun)

> 查询指定日期的日出日落时间。

---

## 🔧 API 请求

```bash
curl --compressed \
  -H "X-QW-Api-Key: {apiKey}" \
  'https://{Host}/v7/astronomy/sun?location={城市 ID|经纬度}&date={日期}'
```

## 📝 参数说明

- `location`: 城市 ID 或经纬度（如 `101280101` 或 `113.26,23.13`）
- `date`: 日期（格式：YYYYMMDD，如 `20260401`）

## 💡 使用示例

```bash
curl --compressed \
  -H "X-QW-Api-Key: {apiKey}" \
  'https://{Host}/v7/astronomy/sun?location=101280101&date=20260401'
```

---

## 🚀 使用 Python 脚本

```bash
# 查询广州今日日出日落
python bin/qweather.py sun 101280101

# 查询指定日期
python bin/qweather.py sun 101280101 20260415
```

---

## 🔗 相关文档

- [12. 月升月落](12-astronomy-moon.md)

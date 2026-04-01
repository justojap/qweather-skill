# 4. 生活指数 (Weather Indices)

> 查询 16 种生活指数，包括穿衣、洗车、运动、旅游等。

---

## 🔧 API 请求

```bash
curl --compressed \
  -H "X-QW-Api-Key: {apiKey}" \
  'https://{Host}/v7/indices/{days}?location={location}&type={type}'
```

## 📝 参数说明

- `location`: 城市 ID 或经纬度
- `type`: 指数类型（多个用逗号分隔，如 `type=3,5`）
- `days`: 预报天数（`1d` 表示今天）

## 💡 使用示例

```bash
# 查询北京今天穿衣指数和洗车指数
curl --compressed \
  -H "X-QW-Api-Key: {apiKey}" \
  'https://{Host}/v7/indices/1d?location=101010100&type=1,2'
```

---

## 🚀 使用 Python 脚本

```bash
# 查询广州今天所有指数
python bin/qweather.py indices 101280101

# 查询指定指数类型
python bin/qweather.py indices 101280101 --type 3
```

---

## 📊 指数类型

| 类型 ID | 指数名称 | 说明 |
|---------|----------|------|
| 1 | 穿衣指数 | 建议穿衣厚度 |
| 2 | 洗车指数 | 是否适合洗车 |
| 3 | 运动指数 | 是否适合运动 |
| 4 | 旅游指数 | 是否适合旅游 |
| 5 | 紫外线指数 | 紫外线强度 |
| ... | ... | ... |

---

## 🔗 相关文档

- [3. 天气预报](3-weather-forecast.md)

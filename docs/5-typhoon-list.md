# 5. 台风列表 (Typhoon List) 💰

> 查询指定年份的台风列表。**付费接口**（¥0.003/次）

---

## 🔧 API 请求

```bash
curl --compressed \
  -H "X-QW-Api-Key: {apiKey}" \
  'https://{Host}/v7/tropical/storm-list?basin=NP&year={year}'
```

## 📝 参数说明

- `basin`: 风盆（`NP`=西北太平洋，默认值）
- `year`: 年份（如 `2025`）

## 💡 使用示例

```bash
curl --compressed \
  -H "X-QW-Api-Key: {apiKey}" \
  'https://{Host}/v7/tropical/storm-list?basin=NP&year=2025'
```

---

## 🚀 使用 Python 脚本

```bash
# 查询 2025 年台风列表
python bin/qweather.py storm-list 2025
```

---

## 💰 计费说明

- **单价**：¥0.003/次
- **免费额度**：无

---

## 🔗 相关文档

- [6. 台风路径](6-typhoon-track.md)
- [7. 台风预报](7-typhoon-forecast.md)
- [0. 计费说明](0-pricing.md)

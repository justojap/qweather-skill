# 7. 台风预报 (Typhoon Forecast) 💰

> 查询台风的未来路径预报。**付费接口**（¥0.003/次）

---

## 🔧 API 请求

```bash
curl --compressed \
  -H "X-QW-Api-Key: {apiKey}" \
  'https://{Host}/v7/tropical/storm-forecast?stormid={stormId}'
```

## 📝 参数说明

- `stormId`: 台风 ID

## 💡 使用示例

```bash
curl --compressed \
  -H "X-QW-Api-Key: {apiKey}" \
  'https://{Host}/v7/tropical/storm-forecast?stormid=202501'
```

---

## 🚀 使用 Python 脚本

```bash
# 查询台风预报
python bin/qweather.py storm-forecast 202501
```

---

## 💰 计费说明

- **单价**：¥0.003/次
- **免费额度**：无

---

## 🔗 相关文档

- [5. 台风列表](5-typhoon-list.md)
- [6. 台风路径](6-typhoon-track.md)

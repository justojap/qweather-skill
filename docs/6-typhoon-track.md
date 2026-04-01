# 6. 台风路径 (Typhoon Track) 💰

> 查询台风的历史路径和实时位置。**付费接口**（¥0.003/次）

---

## 🔧 API 请求

```bash
curl --compressed \
  -H "X-QW-Api-Key: {apiKey}" \
  'https://{Host}/v7/tropical/storm-track?stormid={stormId}'
```

## 📝 参数说明

- `stormId`: 台风 ID（从台风列表接口获取）

## 💡 使用示例

```bash
curl --compressed \
  -H "X-QW-Api-Key: {apiKey}" \
  'https://{Host}/v7/tropical/storm-track?stormid=202501'
```

---

## 🚀 使用 Python 脚本

```bash
# 查询台风路径
python bin/qweather.py storm-track 202501
```

---

## 💰 计费说明

- **单价**：¥0.003/次
- **免费额度**：无

---

## 🔗 相关文档

- [5. 台风列表](5-typhoon-list.md)
- [7. 台风预报](7-typhoon-forecast.md)

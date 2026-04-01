# 1. 城市搜索 (City Lookup)

> 通过城市名称搜索城市 ID，支持中文和拼音搜索。搜索结果会自动缓存到 `city-cache.json`。

---

## 🔧 API 请求

```bash
curl --compressed \
  -H "X-QW-Api-Key: {apiKey}" \
  'https://{Host}/geo/v2/city/lookup?location={城市名称}&range=city&number=1'
```

## 📝 参数说明

- `location`: 城市名称或区县名称（如 `guangzhou`、`huangpu`、`北京`）
- `range`: 搜索范围，固定为 `city`
- `number`: 返回结果数量（默认 1，最多 10）

## 💡 使用示例

### 示例 1：搜索广州

```bash
curl --compressed \
  -H "X-QW-Api-Key: {apiKey}" \
  'https://{Host}/geo/v2/city/lookup?location=guangzhou&range=city&number=1'
```

**返回：**
```json
{
  "code": "200",
  "location": [{
    "name": "广州",
    "id": "101280101",
    "lat": "23.131169",
    "lon": "113.264435",
    "adm1": "广东",
    "adm2": "广州",
    "country": "中国"
  }]
}
```

### 示例 2：搜索黄埔区

```bash
curl --compressed \
  -H "X-QW-Api-Key: {apiKey}" \
  'https://{Host}/geo/v2/city/lookup?location=huangpu&range=city&number=1'
```

---

## 🚀 使用 Python 脚本

```bash
# 搜索城市（自动缓存）
python bin/qweather.py lookup guangzhou

# 查看缓存城市
python bin/qweather.py cache-list
```

---

## 📌 注意事项

1. **自动缓存**：搜索过的城市会自动保存到 `city-cache.json`
2. **支持拼音**：可以用拼音搜索（如 `beijing`、`shanghai`）
3. **支持中文**：也可以用中文搜索（如 `北京`、`上海`）
4. **缓存位置**：`city-cache.json` 在项目根目录

---

## 🔗 相关文档

- [2. 实时天气](2-weather-now.md)
- [3. 天气预报](3-weather-forecast.md)

# 🌤️ QWeather Skill

> 和风天气 API 查询工具 - OpenClaw Skill

[![GitHub](https://img.shields.io/github/license/justojap/qweather-skill)](https://github.com/justojap/qweather-skill)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![和风天气](https://img.shields.io/badge/QWeather-API-blue.svg)](https://dev.qweather.com/)

---

## 📖 简介

**qweather-skill** 是一个基于和风天气 API 的天气查询工具，支持：

- ✅ 城市搜索（自动缓存）
- ✅ 实时天气查询
- ✅ 天气预报（3/7/10/15/30 天）
- ✅ 16 种生活指数
- 💰 台风查询（列表/路径/预报） **⚠️ 付费接口（¥0.003/次）**
  - `storm-list` - 台风列表
  - `storm-track` - 台风路径
  - `storm-forecast` - 台风预报
- ✅ 分钟级降水预报
- ✅ 天气预警
- ✅ 空气质量查询
- ✅ 天文信息（日出日落/月升月落）

> 💡 **提示**：默认测试请使用天气查询、城市搜索等免费接口。**台风接口为付费接口，不在免费额度内**，使用时会明确提示扣费。

---

## 🚀 快速开始

### 1. 安装 Python 3.8+

下载地址：https://www.python.org/downloads/

### 2. 配置 API Key 和 API Host

> ⚠️ **重要**：API Key 和 **API Host 都是必填项**！
>
> **API Host 必须从和风天气控制台获取**，不同账号/项目的 Host 可能不同。

**方式：手动创建 .env 文件**

```bash
# 复制示例文件
cp .env.example .env

# 编辑 .env，填入你的 API Key 和 API Host
```

**.env 文件示例：**
```bash
# .env
QWEATHER_API_KEY=你的 32 位 API_Key
QWEATHER_API_HOST=你的项目 Host（从控制台获取）
```

### 3. 获取 API Key 和 API Host

1. 访问 [和风天气开发者平台](https://dev.qweather.com/)
2. 注册/登录账号
3. 进入「项目管理」→ 选择你的项目
4. **在项目详情页面找到 API Key 和 API Host**
   - API Key：32 位小写十六进制字符串
   - **API Host：类似 `xxx.re.qweatherapi.com`（每个项目可能不同）**
5. 复制并填入 `.env` 文件

> 💡 **提示**：API Host 因项目和区域而异，**必须以你的项目控制台显示的为准**。常见格式：
> - `xxx.re.qweatherapi.com`（区域项目）
> - `devapi.qweather.com`（商业版）
> - `api.qweather.com`（免费版）

### 4. 测试

```bash
# 查看帮助（注意：台风接口为付费接口，会有明确警告）
python bin/qweather.py help

# 查询深圳实时天气 ✅ 免费
python bin/qweather.py now 101280601

# 搜索城市 ID（自动缓存） ✅ 免费
python bin/qweather.py lookup shenzhen

# 查看缓存城市 ✅ 免费
python bin/qweather.py cache-list

# ⚠️ 台风接口（付费，会有明确扣费警告）
# python bin/qweather.py storm-list 2026
# python bin/qweather.py storm-track ID
# python bin/qweather.py storm-forecast ID
```

> ⚠️ **注意**：运行 `help` 命令时，台风接口（`storm-list`、`storm-track`）会标注为 **PAID**，使用时会有明确的扣费警告提示。

---

## 💰 计费说明

> ✅ **每月 50,000 次免费额度**！超出后按阶梯计费。

### 免费额度（每月）

| 接口类型 | 免费额度 |
|----------|----------|
| **常规天气**（实时/预报/指数等） | 50,000 次 |
| **空气质量** | 50,000 次 |
| **天文信息**（日出/月相） | 50,000 次 |
| **分钟级降水** | 50,000 次 |
| **天气预警** | 50,000 次 |
| **台风接口** | ❌ **无免费** |

### 阶梯计费（超出免费额度后）

| 月调用量区间 | 单价（CNY/次） |
|--------------|----------------|
| 0 ~ 5 万 | ¥0.0000（免费） |
| 5 万 ~ 100 万 | ¥0.0007 |
| 100 万 ~ 500 万 | ¥0.0005 |
| 500 万 ~ 1,000 万 | ¥0.00035 |
| 1,000 万 ~ 5,000 万 | ¥0.00015 |
| 5,000 万 ~ 1 亿 | ¥0.0001 |

> 💡 **示例**：月调用 150 万次 = 5 万免费 + 95 万×¥0.0007 + 50 万×¥0.0005 = **¥915**

### 使用量示例

**个人使用（免费额度内）：**
- 每天查 100 次天气 = 月 3,000 次 ✅ **免费**
- 每小时查 1 次 = 月 720 次 ✅ **免费**
- 每 5 分钟查 1 次 = 月 8,640 次 ✅ **免费**

**高频使用（超出免费额度）：**
- 每 1 分钟查 1 次 = 月 43,200 次 ✅ **免费**
- 每秒查 1 次 = 月 2,592,000 次 → 约 **¥1,543/月**

### 💡 建议

1. **监控用量**：定期查看项目后台用量统计
2. **设置告警**：在用量达到 80%、90% 时收到通知
3. **台风接口谨慎使用**：无免费额度（¥0.003/次），按需查询
4. **缓存数据**：避免重复查询相同数据

> 📊 **查看用量**：登录 [和风天气开发者平台](https://dev.qweather.com/) → 「项目管理」→ 「用量统计」

---

## 📚 文档索引

详细 API 文档请查看 [docs/](docs/) 目录：

- [💰 计费说明](docs/0-pricing.md) ⭐ **重要 - 使用前必读**
- [1. 城市搜索](docs/1-city-lookup.md)
- [2. 实时天气](docs/2-weather-now.md)
- [3. 天气预报](docs/3-weather-forecast.md)
- [4. 生活指数](docs/4-weather-indices.md)
- [5. 台风列表](docs/5-typhoon-list.md) 💰 付费接口（¥0.003/次）
- [6. 台风路径](docs/6-typhoon-track.md) 💰 付费接口（¥0.003/次）
- [7. 台风预报](docs/7-typhoon-forecast.md) 💰 付费接口（¥0.003/次）
- [8. 分钟级降水](docs/8-minutely-precipitation.md) ✅ 免费（5 万/月）
- [9. 天气预警](docs/9-weather-alert.md) ✅ 免费（5 万/月）
- [10. 实时空气质量](docs/10-air-quality-now.md) ✅ 免费（5 万/月）
- [11. 日出日落](docs/11-astronomy-sun.md) ✅ 免费（5 万/月）
- [12. 月升月落](docs/12-astronomy-moon.md) ✅ 免费（5 万/月）
- [13. 空气质量小时预报](docs/13-air-quality-hourly.md) ✅ 免费（5 万/月）
- [14. 空气质量每日预报](docs/14-air-quality-daily.md) ✅ 免费（5 万/月）

---

## 🔗 相关链接

- [OpenClaw 官网](https://openclaw.ai)
- [和风天气开发者平台](https://dev.qweather.com/)
- [和风天气 API 文档](https://dev.qweather.com/docs/api/)
- [GitHub 仓库](https://github.com/justojap/qweather-skill)

---

## 📄 许可证

MIT License

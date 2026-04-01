---
name: qweather-skill
description: 和风天气 API 查询工具，支持城市搜索、实时天气、天气预报、生活指数和台风查询
author: 汁汁
user-invocable: true
metadata:
  version: 2.0.0
  license: MIT
  tags:
    - weather
    - qweather
    - 天气
    - 预报
    - 台风

capabilities:
  commands:
    - name: qweather
      description: 查询天气相关信息
      usage: python bin/qweather.py <子命令> [参数]
      handler: python "./bin/qweather.py"
      examples:
        - "/qweather lookup guangzhou  # 搜索广州城市 ID"
        - "/qweather now 101280601      # 查询广州实时天气"
        - "/qweather forecast 101280601 7d # 查询广州 7 天天气预报"
        - "/qweather indices 101280601    # 查询广州生活指数"
        - "/qweather storm-list 2025      # 查询 2025 年台风列表"
        - "/qweather minutely 113.28,23.12 # 查询分钟级降水预报"
        - "/qweather alert 101280601       # 查询广州天气预警"
        - "/qweather air-now 101280601     # 查询广州实时空气质量"
        - "/qweather sun 101280601         # 查询广州日出日落时间"
        - "/qweather moon 101280601        # 查询广州月升月落和月相"
        - "/qweather cache-list            # 查看缓存城市"

---

# 🌤️ QWeather Skill

> 和风天气 API 查询工具

## 📖 简介

**qweather-skill** 是一个基于和风天气 API 的天气查询工具，支持实时天气、天气预报、生活指数、台风查询等功能。

## 🚀 安装与配置

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
>
> ⚠️ **注意**：不要将你的真实 API Host 提交到 Git 仓库，每个用户的 Host 可能不同。

### 4. 测试

```bash
# 查看帮助
python bin/qweather.py help

# 查询深圳实时天气
python bin/qweather.py now 101280601

# 搜索城市 ID（自动缓存）
python bin/qweather.py lookup shenzhen

# 查看缓存城市
python bin/qweather.py cache-list
```

## 💰 计费说明

> ✅ **每月 50,000 次免费**！超出后按阶梯计费（¥0.0007~0.0001/次）。
>
> ⚠️ **台风接口无免费**（¥0.003/次）。
>
> 📊 **完整计费表**：[README.md](README.md#-计费说明) | **查看用量**：https://dev.qweather.com/

## 📚 文档索引

- [0. 计费说明](docs/0-pricing.md) ⭐ **重要 - 使用前必读**
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

## 🔗 相关链接

- [GitHub 仓库](https://github.com/justojap/qweather-skill)
- [和风天气开发者平台](https://dev.qweather.com/)
- [OpenClaw 官网](https://openclaw.ai)

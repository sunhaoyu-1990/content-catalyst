---
initialized: false  # 首次使用时设为 false，触发 onboarding

account:
  domains: ["美妆护肤"]  # 内容领域
  target_audience: "年轻女性用户"
  persona_style: "亲切可爱"
  language: "zh-CN"

scoring:
  trending: 5      # 热度权重（小红书更重热度）
  controversy: 2   # 争议性权重
  value: 3         # 种草价值权重
  relevance: 0     # 相关性权重（小红书不强制相关）
  threshold: 7     # 入选阈值

# 小红书特定字段
xiaohongshu_fields:
  target_gender: "女性 / 男性 / 全部"  # 目标性别
  content_format: "图文为主 / 文字为主 / 视频"  # 内容形式
  post_frequency: "每天 / 每周 / 每月 / 不定期"  # 发布频率
---

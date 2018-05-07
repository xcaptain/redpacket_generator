# 红包样本生成器

采用正态分布模型生成红包样本

## 使用场景

核心是通过scipy带的截尾正态分布样本生成器来生成样本，通过自定义样本筛选代码筛出符合业务需求的样本

## 开发

flask没法热更新代码，每次部署都要重启服务
执行python test.py看生成的样本

## 测试

```bash
FLASK_APP=web.py flask run
```

## 部署

```bash
gunicorn -w 4 web:app -b 127.0.0.1:8001
```

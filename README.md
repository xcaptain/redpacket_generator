# 红包样本生成器

按各种统计模型生成对应的红包样本

## 模型

### 截尾正态分布

最早的版本是使用的截尾正态分布模型生成样本的，效果不错，控制好 sigma 的值可以调整游戏的趣味性。但是后来发现些问题，包括生成的样本容易有负数，对于红包份数分得很多的情况生成效率很低，所以在寻找更好的办法

### beta 分布

这个分布模型是从[universe1987/RedEnvelope](https://github.com/universe1987/RedEnvelope)这里看来的，这位作者说他试验了几种分布觉得还是 beta 分布适合用来生成红包，所以照着他的代码改了改

## 开发

执行 python test.py 看生成的样本，可以用 matplotlib 画直方图来大致分析每次样本分布的情况

## 部署

用 flask+gunicorn 开一个简单的 http api，可以对外提供计算服务

```bash
gunicorn -w 4 web:app -b 127.0.0.1:8001
```

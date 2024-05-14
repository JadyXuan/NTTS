# There is No Time to Sleep
### 没时间睡觉了
还在为ctrl+C时Traceback停在time.sleep()上而感到尴尬吗？在你的项目中引入这个包吧，它会把所有的KeyboardInterrupt输出traceback信息的最后一行替换成model.py，让你的代码看起来就像是在跑一个神经网络模型一样酷炫！

Clone本项目到你的工程目录下，然后在你的入口文件代码中import它，其余的什么也不用做！
```python
import NTTS
```

然后你的代码在ctrl+C时就会给出漂亮的输出

```
Traceback (most recent call last):
  File "d:/GitHub/test.py", line 14, in <module>
    a()
  File "d:/GitHub/test.py", line 5, in a
    b()
  File "d:/GitHub/test.py", line 9, in b
    c()
  File "C:/Users/admin/anaconda3/envs/torch/lib/site-packages/mindx/model.py", line 23, in c
    Model.inference(img)
KeyboardInterrupt
```

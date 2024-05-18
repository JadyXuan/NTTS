# There is No Time to Sleep
### 没时间睡觉了
还在为ctrl+C时Traceback停在time.sleep()上而感到尴尬吗？在你的项目中引入这个包吧，它会把所有的KeyboardInterrupt输出traceback信息的最后一行替换成model.py，让你的代码看起来就像是在跑一个神经网络模型一样酷炫！

你只需要：`pip install NTTS`, 然后在你的入口文件代码中import它，其余的什么也不用做！

或者，如果你想使用最新的版本, Clone本项目到你的工程目录下，在项目根目录下运行：
```
pip install -e .
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

如果你想实现自动导入而无需 `import NTTS`，你需要将项目根目录的ntts.pth文件拷贝到site-packages路径下。如/home/username/anaconda3/envs/conda_env_name/lib/python3.10/site-packages/

## Project Development
### build and upload pip package:
```
python setup.py bdist_wheel
twine upload dist/*
```
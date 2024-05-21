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

如果你想实现自动导入而无需 `import NTTS`，你需要将项目根目录的ntts.pth文件拷贝到site-packages路径下。如`/home/username/anaconda3/envs/conda_env_name/lib/python3.10/site-packages/`

#### NTTS 演示Demo

Demo位于 ./demo , 此Demo使用某500强企业同款语言&图片大模型，下载后运行 `main.py` 即可

# Time to Sleep

### 是时候睡觉了

明天就要demo了，而你还在纠结请求处理的异步和阻塞问题？在你的项目中引入这个附属包吧！它会把traceback信息的最后一行替换成`time.sleep()`，轻松解决`确定性时延😊`，让你和你的代码都能享受24小时充足的睡眠！
```python
import NTTS.tts
```

然后你的代码在ctrl+C时就会给出漂亮的输出

```
Traceback (most recent call last):
  File "/workspaces/main.py", line 11, in <module>
    write()
  File "/root/anaconda3/lib/python3.9/site-packages/mindx/__init__.py", line 57, in write
    time.sleep(6)
KeyboardInterrupt
```

## Project Development

### build and upload pip package:
```
python setup.py bdist_wheel
twine upload dist/*
```
## 感谢支持
[![Stargazers repo roster for @JadyXuan/NTTS](https://reporoster.com/stars/JadyXuan/NTTS)](https://github.com/JadyXuan/NTTS/stargazers)

## 感谢贡献者：
<!-- readme: collaborators,contributors -start -->
<table>
	<tbody>
		<tr>
            <td align="center">
                <a href="https://github.com/JadyXuan">
                    <img src="https://avatars.githubusercontent.com/u/35390572?v=4" width="100;" alt="JadyXuan"/>
                    <br />
                    <sub><b>JadyXuan</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/wufei-png">
                    <img src="https://avatars.githubusercontent.com/u/63766429?v=4" width="100;" alt="wufei-png"/>
                    <br />
                    <sub><b>Wu Fei</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/deanyxu">
                    <img src="https://avatars.githubusercontent.com/u/12771139?v=4" width="100;" alt="deanyxu"/>
                    <br />
                    <sub><b>DX</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/znsoooo">
                    <img src="https://avatars.githubusercontent.com/u/34830785?v=4" width="100;" alt="znsoooo"/>
                    <br />
                    <sub><b>Shixian Li</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/qhy040404">
                    <img src="https://avatars.githubusercontent.com/u/45379733?v=4" width="100;" alt="qhy040404"/>
                    <br />
                    <sub><b>qhy040404</b></sub>
                </a>
            </td>
		</tr>
	<tbody>
</table>
<!-- readme: collaborators,contributors -end -->

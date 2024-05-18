from setuptools import setup, find_packages

VERSION = "0.1.0"
URL = "https://github.com/JadyXuan/NTTS"

with open("README.md", "r", encoding="utf-8") as fp:
    long_description = fp.read()

setup(
    name="NTTS",
    version=VERSION,
    description="还在为ctrl+C时Traceback停在time.sleep()上而感到尴尬吗？在你的项目中引入这个包吧，它会把所有的KeyboardInterrupt输出traceback信息的最后一行替换成model.py，让你的代码看起来就像是在跑一个神经网络模型一样酷炫！",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    author="JadyXuan",
    include_package_data=True,
    author_email="",
    keywords=["NTTS"],
    url=URL,
    packages=find_packages(),
)

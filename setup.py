from setuptools import setup, find_packages

setup(
    name="pvv",
    version="0.1.0",
    description="파이썬 개인 유틸리티",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Andy Cho",
    author_email="soohwancho@korea.ac.kr",
    url="https://github.com/splendidz/pvv",  # 필요 시 수정
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # 원하시는 라이선스로 바꿔도 됩니다.
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)

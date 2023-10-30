---
title: 環境構築
layout: default
---

{% include header.html %}

{% raw %}

# 環境構築

## パッケージのアップグレード
```bash
$ sudo apt update
$ sudo apt upgrade
```

## 各種パッケージのインストール

※本チュートリアルでは、下記のパッケージすべてを使用しているというわけではありません。適宜、必要なもののみインストールして頂いて結構です。

### 基本
```bash
$ sudo apt install tree
```

### データ分析関連
```bash
$ sudo apt install libbz2-dev # pandasのインポートに必要
$ sudo apt install python3-tk # matplotlib.show()で画像を表示する際に必要
$ sudo apt install libffi-dev # scikit-learnのインポートに必要
# ...（5分程度）...
```

### GDAL関連
```bash
$ sudo apt install build-essential # GDALのインストールに必要
$ sudo apt install libgdal-dev	# GDALのインストールに必要
$ sudo apt install python3-gdal	# GDALのインストールに必要
```

### DB関連
```bash
$ sudo apt install postgresql
$ sudo apt install postgis
# ...（3分程度）...
```

### NLP関連
```bash
$ sudo apt install mecab libmecab-dev mecab-ipadic mecab-ipadic-utf8
```

## venv_recsys_django仮想環境の構築
```bash
$ python3.11 -m venv ~/venv_recsys_django
$ ls ~/venv_recsys_django/
```

## venv_recsys_django仮想環境のアクティベート
```bash
$ source ~/venv_recsys_django/bin/activate
$ (venv_recsys_django) $
# プロンプトが(venv_recsys_django) ...$となればOK
```

以降、プロンプトが`(venv_recsys_django) $`となっている行はvenv_recsys_django仮想環境上で実行することを表します。

## pipのアップグレード
```bash
(venv_recsys_django) $ pip --version
(venv_recsys_django) $ pip install --upgrade pip
(venv_recsys_django) $ pip --version
```

## 各種パッケージのインストール

※本チュートリアルでは、下記のパッケージすべてを使用しているというわけではありません。適宜、必要なもののみインストールして頂いて結構です。

### 基本
```bash
(venv_recsys_django) $ pip install ipython
(venv_recsys_django) $ pip install tqdm
```

### データ分析関連
```bash
(venv_recsys_django) $ pip install numpy
(venv_recsys_django) $ pip install scipy
(venv_recsys_django) $ pip install matplotlib
(venv_recsys_django) $ pip install pandas
(venv_recsys_django) $ pip install scikit-learn
```

### DB関連
```bash
(venv_recsys_django) $ pip install psycopg2-binary
```

### NLP関連
```bash
(venv_recsys_django) $ pip install mecab-python3
(venv_recsys_django) $ pip install ginza
(venv_recsys_django) $ pip install ja-ginza
(venv_recsys_django) $ pip install spacy
```

### スクレイピング関連
```bash
(venv_recsys_django) $ pip install beautifulsoup4
(venv_recsys_django) $ pip install requests
```

### Django関連
```bash
(venv_recsys_django) $ pip install django
(venv_recsys_django) $ pip install django-leaflet
(venv_recsys_django) $ export CPLUS_INCLUDE_PATH=/usr/include/gdal
(venv_recsys_django) $ export C_INCLUDE_PATH=/usr/include/gdal
(venv_recsys_django) $ apt list --installed | grep libgdal-dev
(venv_recsys_django) $ gdalinfo --version
libgdal-dev/jammy,now 3.4.1+dfsg-1build4 amd64 [インストール済み]
# libgdal-devのバージョンを確認する。
(venv_recsys_django) $ pip install gdal==3.4.1 # libgdal-devのバージョンに合わせる # GeoDjangoに必要
# ...（1分程度）...
(venv_recsys_django) $ pip install djangorestframework-gis # RESTful APIに必要
(venv_recsys_django) $ pip install django-filter # RESTful APIに必要
(venv_recsys_django) $ pip install markdown # RESTful APIに必要
(venv_recsys_django) $ pip install django-bootstrap5
(venv_recsys_django) $ pip install django-allauth
(venv_recsys_django) $ pip install django-cleanup
```

### インストール済みパッケージの確認
```bash
(venv_recsys_django) $ pip freeze
```

## venv_recsys_django仮想環境のディアクティベート
```bash
(venv_recsys_django) $ deactivate
$
# プロンプトが元に戻ればOK
```

{% endraw %}

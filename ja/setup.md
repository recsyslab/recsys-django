# 環境構築

## パッケージのアップグレード
```bash
$ sudo apt update
$ sudo apt upgrade
```

## 各種パッケージのインストール
```bash
$ sudo apt install tree
$ sudo apt install libbz2-dev # pandasのインポートに必要
$ sudo apt install python3-tk # matplotlib.show()で画像を表示する際に必要
$ sudo apt install build-essential # GDALのインストールに必要
$ sudo apt install libgdal-dev	# GDALのインストールに必要
$ sudo apt install python3-gdal	# GDALのインストールに必要
$ sudo apt install libffi-dev # scikit-learnのインポートに必要
# ...（5分程度）...
# sudo apt install mecab libmecab-dev mecab-ipadic mecab-ipadic-utf8
```

## rsl-django仮想環境の構築
```bash
$ mkdir ~/venv/
$ cd ~/venv/
$ python3.9 -m venv rsl-django
```

## rsl-django仮想環境のアクティベート
```bash
$ source rsl-django/bin/activate
```

## pipのアップグレード
```bash
(rsl-django) $ pip --version
(rsl-django) $ pip install --upgrade pip
(rsl-django) $ pip --version
```

## 各種パッケージのインストール

### 基本
```bash
(rsl-django) $ pip install ipython
(rsl-django) $ pip install tqdm
```

### データ分析関連
```bash
(rsl-django) $ pip install numpy
(rsl-django) $ pip install scipy
(rsl-django) $ pip install matplotlib
(rsl-django) $ pip install pandas
(rsl-django) $ pip install scikit-learn
```

### DB関連
```bash
(rsl-django) $ pip install psycopg2-binary
```

### NLP関連
```bash
(rsl-django) $ pip install mecab-python3
(rsl-django) $ pip install ginza
(rsl-django) $ pip install ja-ginza
(rsl-django) $ pip install spacy
```

### スクレイピング関連
```bash
(rsl-django) $ pip install beautifulsoup4
(rsl-django) $ pip install requests
```

### Django関連
```bash
(rsl-django) $ pip install django
(rsl-django) $ pip install django-leaflet
(rsl-django) $ export CPLUS_INCLUDE_PATH=/usr/include/gdal
(rsl-django) $ export C_INCLUDE_PATH=/usr/include/gdal
(rsl-django) $ pip install gdal==3.0.4 # libgdal-devのバージョンに合わせる # GeoDjangoに必要
(rsl-django) $ pip install djangorestframework-gis # RESTful APIに必要
(rsl-django) $ pip install django-filter # RESTful APIに必要
(rsl-django) $ pip install markdown # RESTful APIに必要
(rsl-django) $ pip install django-bootstrap5
(rsl-django) $ pip install django-allauth
(rsl-django) $ pip install django-cleanup
```

### インストール済みパッケージの確認
```bash
(rsl-django) $ pip freeze
```

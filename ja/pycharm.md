# PyCharm

## PyCharmのインストール

### ダウンロード
1. 下記からPyCharmをダウンロードする。
   - **[PyCharm](http://www.jetbrains.com/pycharm/)**
   - **PyCharm**: `pycharm-community-2023.1.tar.gz`
   - 2023/04/14時点の最新版

### インストール
```bash
$ cd ~/Downloads/
$ tar xvzf pycharm-community-2023.1.tar.gz
$ mv pycharm-community-2023.1/ pycharm-community/
$ mv pycharm-community ~/opt/
$ sudo ln -s ~/opt/pycharm-community/bin/pycharm.sh /usr/local/bin/pycharm
$ sudo ln -s ~/opt/pycharm-community/bin/inspect.sh /usr/local/bin/inspect
```

### 後始末
```bash
$ rm -f pycharm-community-2023.1.tar.gz
```

## PyCharmの実行
```bash
pycharm
```

以下、ホームディレクトリに、`recsys_django`プロジェクトが作成されているものとします。`【HOME】`を、自身のホームディレクトリに置き換えてください。

### プロジェクトのオープン
1. 初回起動時は「Welcome to PyCharm」画面が開くので、**Open**ボタンをクリックする。
   1. Djangoプロジェクトディレクトリ（下記の場所）を選択する。
      - `【HOME】/recsys_django`
   2. **OK**ボタンをクリックする。
   3. **Trust Project**ボタンをクリックする。

## 設定

### Python Interpreterの設定
1. **File - Settings**を開く。
   1. **Project: recsys_django - Python Interpreter**を開く。
      1. **Python Interpreter**の右側の**Add Interpreter - Add Local Interpreter**をクリックする。
         1. **Virtualenv Environment**を開き、下記を設定する。
            - **Environment**: `Existing`
            - **Interpreter**: `【HOME】/venv/rsl-django/bin/python3.9`
         2. **OK**ボタンをクリックする。
      2. **Python Interpreter**に`Python 3.9 (rsl-django)`が設定されていることを確認する。
      3. **OK**ボタンをクリックする。

### runserverの登録
1. **Run - Edit Configurations**を開く。
   1. 左上の**+**ボタンをクリックし、**Python**を選択する。
      1. 下記を設定する。
         - **Name**: `runserver`
         - **Script path**: `【HOME】/recsys_django/manage.py`
         - **Parameters**: `runserver`
         - **Environment Variables**: `PYTHONUNBUFFERED=1;DB_USER=rsl;DB_PASSWORD=【DBパスワード】`
      2. **OK**ボタンをクリックする。

### runserverの起動
1. 右上のプルダウンリストが`runserver`になっていることを確認し、**▶**ボタンをクリックする。
2. ブラウザで下記にアクセスし、実行画面が正しく表示されればOK。
   - http://127.0.0.1:8000/



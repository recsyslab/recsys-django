# PyCharm

## インストール

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

## PyCharmでプロジェクトのオープン
```bash
pycharm
```

1. **Open**ボタンをクリックする。
   1. Djangoプロジェクトディレクトリを選択する。
   2. **OK**ボタンをクリックする。

## 設定

### Python Interpreterの設定
1. **File - Settings**を開く。
   1. **Project: myproject - Python Interpreter**を開く。
      1. **Python Interpreter**の右側の歯車アイコンをクリックし、**Add**を選択する。
         1. **Virtualenv Environment**を開き、下記を設定する。
            - **Existing environment**: 選択
            - **Interpreter**: `【HOME】venv/rsl-django/bin/python3.9`
         2. **OK**ボタンをクリックする。
      2. **OK**ボタンをクリックする。

## runserverの登録
1. 右上の**Add Configuration**ボタンをクリックする。
   1. 左上の**+**ボタンをクリックし、**Python**を選択する。
      1. 下記を設定する。
         - **Name**: `runserver`
         - **Script path**: `/home/rsl/recsyslab/django/myproject/manage.py`
         - **Parameters**: `runserver`
         - **Environment Variables**: 
           - **DB_USER**: （DBユーザ名）
           - **DB_PASSWORD**: （パスワード）
      2. **OK**ボタンをクリックする。

## runserverの起動
1. 右上のプルダウンリストが`runserver`になっていることを確認し，**▶**ボタンをクリックする。
2. 下記にアクセスし、「The install worked successfully! Congratulations!」と表示されればOK。
   - http://127.0.0.1:8000/

## makemigrationsの登録
1. 右上のプルダウンリストから**Edit Configurations**を開く。
   1. 登録してある`runserver`を選択し、**Copy Configuration**ボタンをクリックする。
   2. 下記を設定する。
      - **Name**: `makemigrations`
      - **Parameters**: `makemigrations`
   3. **OK**ボタンをクリックする。

## makemigrationsの実行
1. 右上のプルダウンリストから`makemigrations`を選択し、**▶**ボタンをクリックする。

## migrateの登録
1. 右上のプルダウンリストから**Edit Configurations**を開く。
   1. 登録してある`runserver`を選択し、**Copy Configuration**ボタンをクリックする。
   2. 下記を設定する。
      - **Name**: `migrate`
      - **Parameters**: `migrate`
   3. **OK**ボタンをクリックする。

## migrateの実行
1. 右上のプルダウンリストから`migrate`を選択し、**▶**ボタンをクリックする。

## inspectdbの登録
1. 右上のプルダウンリストから**Edit Configurations**を開く。
   1. 登録してある`runserver`を選択し、**Copy Configuration**ボタンをクリックする。
   2. 下記を設定する。
      - **Name**: `inspectdb`
      - **Parameters**: `inspectdb`
   3. **OK**ボタンをクリックする。

## inspectdbの実行
1. 右上のプルダウンリストから`migrate`を選択し、**▶**ボタンをクリックする。


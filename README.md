# PassMain
一個基於python的密碼管理軟體

### 📝簡介

使用AES256對用戶密碼的json進行加密，以實現密碼保護。

## 📥部署

使用python3.8.10

```python -m venv <路徑>/```

創建python虛擬環境

```<路徑>/Scripts/activate```

激活環境

```cd /passmain```

移動到passmain資料夾

```pip install -r ```

安裝必要套件

```python main.py```

運行

## 🛠️建立可執行檔案

windows環境中使用

```pip install PyInstaller```

安裝 PyInstaller

```cd /passmain```

移動到passmain資料夾

```pip install tinyaes```

要加密原程式碼可以用(可選)

```python.exe -m PyInstaller -i ico4.ico -n PassMain.exe --onefile --noconsole --key abc main.py```

以下這些可以改

``` 
-i <主程式icon>
-n <名字>
--key <密碼> (前面安裝tinyaes才能用，最多14位)
```

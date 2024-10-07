# PassMain
基於python的密碼管理軟體

### 📝簡介
PassMain 是一款基於 Python 開發的密碼管理軟體，旨在幫助使用者安全地保存和管理他們的所有密碼。隨著互聯網服務的普及，使用者需要記住的密碼數量不斷增加，且這些密碼通常複雜難記。PassMain 提供了一個本地離線的解決方案，讓使用者能夠以加密的方式集中保存所有重要的密碼資訊。

#### 技術細節
軟體採用了高強度的 AES-256 加密算法，對用戶的密碼資料進行加密保存，確保資料的安全性。具體而言，它使用了 AES-256 的 CFB 模式，對密碼的 JSON 數據進行加密。使用者只需要記住一組高強度的主密碼，即可管理和訪問所有儲存在軟體中的密碼。

PassMain 的主要特點包括：

- 本地離線運行：所有密碼資料都保存在本地，無需擔心網絡攻擊或資料被竊取的風險。
- 高安全性：採用 AES-256 加密，並使用使用者提供的主密碼進行密鑰生成，防止未經授權的訪問。
- 簡潔易用的界面：基於 PySide2 構建的圖形用戶界面，提供了直觀的操作體驗，使用者可以輕鬆地添加、編輯和管理密碼資訊。
- 資料完整性：密碼資料以 JSON 格式存儲，方便進行資料的序列化和反序列化，同時也便於未來的擴展。

儘管無法完全避免**碰撞攻擊**等安全風險，但 PassMain 提供的加密保存方式，大大提升了密碼管理的安全性。與直接將密碼明文保存在電腦上相比，使用 PassMain 能有效降低密碼洩露的風險，保障使用者的隱私和資料安全。
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

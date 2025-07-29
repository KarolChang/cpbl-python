# CPBL Python API Server

本專案是一個以 Flask 為基礎的 API 伺服器，負責爬取中華職棒（CPBL）官網的各類資料，並將其轉換為 API，提供給自己或其他服務使用。

---

## 專案目的
- 自動化爬取中職官網的賽程、球員、戰績、即時比分等資料
- 將資料標準化後，透過 RESTful API 提供查詢
- 方便自己或其他應用程式存取中職相關資訊

---

## 專案架構

```
cpbl-python/
  app/
    apis/         # API 資料處理
    crawlers/     # 爬蟲模組
    errors/       # 錯誤處理
    routes/       # 路由 (Blueprints)
    templates/    # 前端模板
    utils/        # 工具函式
    static/       # 靜態檔案
    __init__.py   # Flask 應用工廠
  datas/          # 原始資料檔案 (json)
  .github/
    workflows/
      deploy.yml  # CI/CD 自動部署
  main.py         # Cloud Functions 入口
  run.py          # 本地啟動入口
  requirements.txt # Cloud Functions 依賴
  Pipfile         # 本地開發依賴
  Makefile        # 開發指令腳本
  scripts.py      # Python 開發腳本
  README.md       # 專案說明
```

---

## 快速開始

### 使用 Make 指令（推薦）

```bash
# 查看所有可用指令
make help

# 安裝依賴
make install

# 啟動開發伺服器
make dev

# 執行測試
make test

# 清理快取檔案
make clean

# 更新 requirements.txt
make requirements

# 本地測試 Cloud Functions
make deploy-local

# 部署到 GCP
make deploy-gcp
```

### 使用 Python 腳本

```bash
# 查看所有可用指令
python scripts.py -h

# 啟動開發伺服器
python scripts.py dev

# 安裝依賴
python scripts.py install

# 執行測試
python scripts.py test
```

### 傳統方式

```bash
# 安裝依賴
pipenv install

# 啟動開發伺服器
pipenv run python run.py
```

---

## 本地開發

1. 安裝依賴：
```bash
make install
# 或
pipenv install
```

2. 啟動伺服器：
```bash
make dev
# 或
pipenv run python run.py
```

3. 開啟瀏覽器：http://127.0.0.1:5000

---

## Cloud Functions 部署

### 自動部署（推薦）
1. Fork 或 Clone 此專案到你的 GitHub
2. 在 GCP 建立專案並啟用 Cloud Functions API
3. 建立服務帳戶並下載 JSON 金鑰
4. 在 GitHub 專案設定中加入以下 Secrets：
   - `GCP_PROJECT_ID`：你的 GCP 專案 ID
   - `GCP_SA_KEY`：服務帳戶 JSON 金鑰內容
5. 推送程式碼到 `master` 或 `main` 分支，GitHub Actions 會自動部署

### 手動部署
```bash
make deploy-gcp
# 或
gcloud functions deploy cpbl-api \
  --gen2 \
  --runtime python312 \
  --source . \
  --entry-point cpbl_api \
  --trigger-http \
  --allow-unauthenticated \
  --region asia-east1
```

---

## 主要功能
- 爬取中職官網各類資料（賽程、球員、戰績、即時比分等）
- 提供 RESTful API 查詢
- 支援 Blueprint 模組化路由
- 錯誤統一處理
- 自動 CI/CD 部署到 Google Cloud Functions

---

## 聯絡方式
如有問題或建議，歡迎聯絡作者。 
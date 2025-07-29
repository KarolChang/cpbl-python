# CPBL Python API 開發指令

.PHONY: help install dev test clean deploy-local deploy-gcp

# 顯示所有可用指令
help:
	@echo "可用指令："
	@echo "  make install     - 安裝專案依賴"
	@echo "  make dev         - 啟動開發伺服器"
	@echo "  make test        - 執行測試"
	@echo "  make clean       - 清理快取檔案"
	@echo "  make deploy-local - 本地測試 Cloud Functions"
	@echo "  make deploy-gcp  - 部署到 Google Cloud Functions"
	@echo "  make requirements - 更新 requirements.txt"

# 安裝依賴
install:
	pipenv install

# 啟動開發伺服器
dev:
	pipenv run python run.py

# 執行測試
test:
	pipenv run python -m pytest test/ -v

# 清理快取檔案
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete

# 本地測試 Cloud Functions
deploy-local:
	pipenv run functions-framework --target=cpbl_api --port=8080

# 部署到 Google Cloud Functions
deploy-gcp:
	gcloud functions deploy cpbl-api \
		--gen2 \
		--runtime python312 \
		--source . \
		--entry-point cpbl_api \
		--trigger-http \
		--allow-unauthenticated \
		--region asia-east1

# 更新 requirements.txt
requirements:
	pipenv run pip freeze > requirements.txt
	@echo "requirements.txt 已更新" 
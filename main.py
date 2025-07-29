"""Cloud Functions 入口，包裝 Flask 應用。"""

import functions_framework
from app import create_app

# 建立 Flask app 實例
app = create_app()


@functions_framework.http
def cpbl_api(request):
    """Cloud Functions HTTP 入口點"""
    # 使用 Flask app 處理請求
    with app.test_request_context(
        request.url,
        method=request.method,
        headers=request.headers,
        data=request.get_data(),
    ):
        try:
            response = app.full_dispatch_request()
            return (
                response.get_data(as_text=True),
                response.status_code,
                dict(response.headers),
            )
        except Exception as e:
            return f"Error: {str(e)}", 500

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel # pydanticからBaseModelをインポート

# フロントエンドから受け取るデータの方を定義
class RoadmapRequest(BaseModel):
    goal: str
    current_status: str


app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "バックエンドサーバーは正常に起動しています"}


# ロードマップ生成のための新しいAPIエンドポイント
@app.post("/generate-roadmap")
def generate_roadmap(request: RoadmapRequest):
    # ここにGemini APIを呼び出す処理を書いていく
    
    # 現時点では、受け取ったデータとダミーの応答を返す
    print(f"受け取ったデータ: {request.goal}, {request.current_status}")
    
    return {
        "goal": request.goal,
        "current_status": request.current_status,
        "roadmap": [
            {"step": 1, "action": "基礎学習", "estimated_time": "2週間"},
            {"step": 2, "action": "簡単なアプリ作成", "estimated_time": "3週間"},
            {"step": 3, "action": "目標のアプリ開発開始", "estimated_time": "5週間"},
        ]
    }
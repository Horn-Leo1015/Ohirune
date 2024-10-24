import random
from datetime import datetime

def super_fortune_telling():
    print("🔮 超運勢占い 🔮")
    
    # 現在の日付を取得
    today = datetime.now()
    print(f"今日の日付: {today.strftime('%Y年%m月%d日')}")
    
    # ユーザーの名前を入力
    name = input("そなたの名前を入力するがよい: ")
    
    # 運勢のリスト
    fortunes = ["超大吉", "中吉", "小吉", "吉", "末吉", "凶", "大凶","宿題を出すと吉","よく眠ると吉"]

    
    # ランダムに運勢を選択
    fortune = random.choice(fortunes)
    
    # ラッキーアイテムのリスト
    lucky_items = ["金のリンゴ","銀のオノ","赤いずきん", "青い鳥", "黄色い傘", "緑の帽子", "紫のスカーフ"]
    
    # ランダムにラッキーアイテムを選択
    lucky_item = random.choice(lucky_items)
    
    # ラッキーナンバーを生成（1から100までのランダムな数字）
    lucky_number = random.randint(1, 100)
    
    # 結果を表示
    print(f"\n{name}さんの今日の運勢は...")
    print(f"【運勢】: {fortune}")
    print(f"【ラッキーアイテム】: {lucky_item}")
    print(f"【ラッキーナンバー】: {lucky_number}")
    
    if fortune in ["大吉", "中吉"]:
        print("\n今日はとてもラッキーな日じゃ。思い切った行動を取ると良いぞ。")
    elif fortune in ["小吉", "吉"]:
        print("\n穏やかな一日になりそうじゃ。小さな幸せを見つけられる予感がするぞ。")
    elif fortune == "末吉":
        print("\n普通の一日じゃ。良くも悪くもないの。慎重に行動すれば良いことがあるぞ。")
    elif fortune == "宿題をすると吉":
        print("\n普通の一日じゃ。良くも悪くもないの。宿題はしっかり出そうぞ。")
    elif fortune == "よく眠ると吉":
        print("\n普通の一日じゃ。良くも悪くもないの。よく寝ることが大事じゃ。")
    else:
        print("\nいかん。今日は気を抜いてはならぬ。落ち着いて行動した方が身のためじゃ。")

# 占いを実行
super_fortune_telling()
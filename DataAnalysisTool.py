import pandas as pd
import matplotlib.pyplot as plt

# ================================
#  データ（CSVを使わずPython内に直接定義）
# ================================
data = [
    {"date": "2024-01-03", "method": "クレカ", "amount": 850},
    {"date": "2024-01-05", "method": "現金", "amount": 500},
    {"date": "2024-01-10", "method": "PayPay", "amount": 620},
    {"date": "2024-02-02", "method": "クレカ", "amount": 1200},
    {"date": "2024-02-11", "method": "現金", "amount": 450},
    {"date": "2024-02-18", "method": "PayPay", "amount": 980},
]

# DataFrame に変換
df = pd.DataFrame(data)


# ================================
#  基本集計
# ================================
def basic_summary(df):
    print("\n=== 基本集計 ===")
    print("データ件数:", len(df))
    print("合計金額:", df["amount"].sum())
    print("平均金額:", df["amount"].mean())


# ================================
#  支払い手段ごとの集計
# ================================
def payment_summary(df):
    print("\n=== 支払い手段ごとの集計 ===")
    summary = df.groupby("method")["amount"].sum()
    print(summary)
    return summary


# ================================
#  月ごとの集計
# ================================
def monthly_summary(df):
    print("\n=== 月ごとの集計 ===")
    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M")
    summary = df.groupby("month")["amount"].sum()
    print(summary)
    return summary


# ================================
#  グラフ表示
# ================================
def plot_monthly(summary):
    summary.plot(kind="bar", figsize=(8, 4), title="月ごとの支出")
    plt.xlabel("月")
    plt.ylabel("金額")
    plt.tight_layout()
    plt.show()


# ================================
#  メイン処理
# ================================
def main():
    basic_summary(df)
    payment_summary(df)
    monthly = monthly_summary(df)
    plot_monthly(monthly)


if __name__ == "__main__":
    main()

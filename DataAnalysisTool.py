import pandas as pd
import matplotlib.pyplot as plt
import logging

# ================================
#  ログ設定
# ================================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# ================================
#  データ
# ================================
data = [
    {"date": "2024-01-03", "method": "クレカ", "amount": 850},
    {"date": "2024-01-05", "method": "現金", "amount": 500},
    {"date": "2024-01-10", "method": "PayPay", "amount": 620},
    {"date": "2024-02-02", "method": "クレカ", "amount": 1200},
    {"date": "2024-02-11", "method": "現金", "amount": 450},
    {"date": "2024-02-18", "method": "PayPay", "amount": 980},
]

df = pd.DataFrame(data)


# ================================
#  集計関数
# ================================
def basic_summary(df):
    print("\n=== 基本集計 ===")
    print(f"データ件数 : {len(df)} 件")
    print(f"合計金額   : {df['amount'].sum()} 円")
    print(f"平均金額   : {round(df['amount'].mean(), 2)} 円")


def payment_summary(df):
    summary = df.groupby("method")["amount"].sum()
    print("\n=== 支払い手段ごとの集計 ===")
    print(summary.to_string())
    return summary


def monthly_summary(df):
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M")
    summary = df.groupby("month")["amount"].sum()

    print("\n=== 月ごとの集計 ===")
    print(summary.to_string())

    return summary


# ================================
#  グラフを1つの画面にまとめて表示
# ================================
def plot_combined(monthly, payment):
    """
    月次棒グラフ・折れ線グラフ・支払い手段円グラフを
    1つのウィンドウにまとめて表示する
    """
    plt.rcParams["font.family"] = "IPAexGothic"

    fig, axes = plt.subplots(1, 3, figsize=(15, 4))

    # --- 月次棒グラフ ---
    monthly.plot(kind="bar", ax=axes[0], title="月ごとの支出（棒）")
    axes[0].set_xlabel("月")
    axes[0].set_ylabel("金額")

    # --- 月次折れ線グラフ ---
    monthly.plot(kind="line", marker="o", ax=axes[1], title="月ごとの支出（折れ線）")
    axes[1].set_xlabel("月")
    axes[1].set_ylabel("金額")

    # --- 支払い手段の円グラフ ---
    payment.plot(kind="pie", autopct="%1.1f%%", ax=axes[2], title="支払い手段の割合")
    axes[2].set_ylabel("")

    plt.tight_layout()
    plt.show()


# ================================
#  レポート生成
# ================================
def generate_report(df):
    print("\n===============================")
    print("         支出レポート")
    print("===============================")

    basic_summary(df)
    pay = payment_summary(df)
    month = monthly_summary(df)

    print("\n=== レポートまとめ ===")
    print(f"最も使った支払い手段 : {pay.idxmax()}（{pay.max()}円）")
    print(f"支出が最も多い月       : {month.idxmax()}（{month.max()}円）")
    print("===============================")

    return month, pay


# ================================
#  メイン処理
# ================================
def main():
    logging.info("レポート生成開始")

    monthly, payment = generate_report(df)
    plot_combined(monthly, payment)

    logging.info("処理完了")


if __name__ == "__main__":
    main()

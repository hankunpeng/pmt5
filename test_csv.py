import os
import time
from datetime import datetime
#import matplotlib.pyplot as plt
import pandas as pd
#from pandas.plotting import register_matplotlib_converters
#register_matplotlib_converters()
import MetaTrader5 as mt5

# ====================== 可配置参数 ======================
SYMBOL = "XAUUSD"          # 目标品种
TIMEFRAME = mt5.TIMEFRAME_M1  # M1 周期
BARS = 100                    # 每次抓取的 K 线根数
CSV_PATH = "xauusd_m1.csv"   # 输出文件
SLEEP_SECONDS = 60            # 抓取间隔（秒）
# ======================================================

def init_mt5():
    """初始化并连接本机已开启的 MT5 终端。"""
    if not mt5.initialize():
        raise RuntimeError("MT5 initialize() failed — 请确认 MT5 已启动并允许外部程序连接")

def shutdown_mt5():
    """断开 MT5 连接，释放资源。"""
    mt5.shutdown()

def fetch_bars(symbol, timeframe, bars):
    """从 MT5 获取指定品种的 K 线数据。"""
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, bars)
    if rates is None or len(rates) == 0:
        raise RuntimeError(f"未能获取 {SYMBOL} 数据, 请检查该品种是否已订阅。")
    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')  # 将时间戳转为可读格式
    df = df.sort_values('time')  # 升序排列，方便追加
    return df

def save_to_csv(df, path):
    """将 DataFrame 保存到 CSV 文件"""
    if os.path.exists(path):
        df.to_csv(path, mode='a', header=False, index=False)  # 追加模式
    else:
        df.to_csv(path, mode='w', header=True, index=False)  # 新建文件

def main_loop():
    """循环抓取数据并保存到 CSV 文件里"""
    init_mt5()
    try:
        while True:
            print(f"抓取 {SYMBOL} 的最新 {BARS} 根 K 线...")
            df = fetch_bars(SYMBOL, TIMEFRAME, BARS)
            save_to_csv(df, CSV_PATH)
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — 已保存到 {CSV_PATH}，等待 {SLEEP_SECONDS} 秒后继续...")
            time.sleep(SLEEP_SECONDS)
    except Exception as e:
        print(f"发生错误: {e}")
    finally:
        shutdown_mt5()

if __name__ == "__main__":
    main_loop()

from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import MetaTrader5 as mt5
# register_matplotlib_converters() 让 pandas 里的时间序列可以被 matplotlib 识别
# 时间序列金融数据 → 想要既能算又能画 → 需要 pandas+matplotlib → 两者在“时间索引”上的兼容靠 converter

# connect to MetaTrader 5
# 尝试跟本机已打开的 MT5 终端建立“管道”，如果失败就立刻 shutdown()，避免残留的“半开”连接。
if not mt5.initialize():
    print("initialize() failed")
    mt5.shutdown()
# 任何外部 API 先 handshake（握手），再干活；握手失败要优雅退出，防止资源泄漏。

# request connection status and parameters
# 返回终端的安装路径、登录账户、服务器等环境信息
print(mt5.terminal_info())
# get data on MetaTrader 5 version
print(mt5.version())

# request 1000 ticks from EURAUD
euraud_ticks = mt5.copy_ticks_from("EURAUD", datetime(2025,7,7,7), 1000, mt5.COPY_TICKS_ALL)
# request ticks from AUDUSD within 2025.07.08 13:00 - 2025.07.09 13:00
audusd_ticks = mt5.copy_ticks_range("AUDUSD", datetime(2025,7,8,13), datetime(2025,7,9,13), mt5.COPY_TICKS_ALL)

# get bars from different symbols in a number of ways
# 从给定时间点 向前 抓 1000 根 1 分钟线
eurusd_rates = mt5.copy_rates_from("EURUSD", mt5.TIMEFRAME_M1, datetime(2025,7,9,13), 1000)
# 从“最新一根”算起的偏移 = 0，抓 1000 根 M1。
eurgbp_rates = mt5.copy_rates_from_pos("EURGBP", mt5.TIMEFRAME_M1, 0, 1000)
# 在时间区间里抓 Bars
eurcad_rates = mt5.copy_rates_range("EURCAD", mt5.TIMEFRAME_M1, datetime(2025,7,7,13), datetime(2025,7,9,13))

# shut down connection to MetaTrader 5
# 全部抓完后关连接，这一步必须，否则 MT5 进程会一直被占用。
mt5.shutdown()

#DATA
print('euraud_ticks(', len(euraud_ticks), ')')
for val in euraud_ticks[:10]: print(val)

print('audusd_ticks(', len(audusd_ticks), ')')
for val in audusd_ticks[:10]: print(val)

print('eurusd_rates(', len(eurusd_rates), ')')
for val in eurusd_rates[:10]: print(val)

print('eurgbp_rates(', len(eurgbp_rates), ')')
for val in eurgbp_rates[:10]: print(val)

print('eurcad_rates(', len(eurcad_rates), ')')
for val in eurcad_rates[:10]: print(val)

#PLOT
# create DataFrame out of the obtained data
ticks_frame = pd.DataFrame(euraud_ticks)
# convert time in seconds into the datetime format
ticks_frame['time']=pd.to_datetime(ticks_frame['time'], unit='s')
# display ticks on the chart
# MT5 Tick 返回的是结构体数组，直接塞进 DataFrame 就能变成表格。
# Tick 里的 time 是“自 1970‑01‑01 起的秒数”，转成人类能看懂的日期。
plt.plot(ticks_frame['time'], ticks_frame['ask'], 'r-', label='ask')
plt.plot(ticks_frame['time'], ticks_frame['bid'], 'b-', label='bid')

# display the legends
plt.legend(loc='upper left')

# add the header
plt.title('EURAUD ticks')

# display the chart
plt.show()
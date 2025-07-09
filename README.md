# [Python MetaTrader5](https://www.mql5.com/en/docs/python_metatrader5)

Python is a modern high-level programming language for developing scripts and applications. It contains multiple libraries for machine learning, process automation, as well as data analysis and visualization.
Python 是一种用于开发脚本和应用程序的现代高级编程语言。它包含多个用于机器学习、流程自动化以及数据分析和可视化的库。

MetaTrader package for Python is designed for convenient and fast obtaining of exchange data via interprocessor communication directly from the MetaTrader 5 terminal. The data received this way can be further used for statistical calculations and machine learning.
MetaTrader Python 程序包旨在通过处理器间通信直接从 MetaTrader 5 终端便捷快速地获取交易所数据。通过这种方式接收的数据可进一步用于统计计算和机器学习。

Installing the package from the command line:
从命令行安装 MetaTrader5 软件包：
```
pip install MetaTrader5
```

Or updating the package from the command line:
或从命令行更新 MetaTrader5 软件包：
```
pip install --upgrade MetaTrader5
```

Add matplotlib and pandas packages:
添加 matplotlib 和 pandas 包：
```
pip install matplotlib
pip install pandas
```

Functions for integrating MetaTrader 5 and Python
用于集成 MetaTrader 5 和 Python 的函数
| Function | Action |
| --- | --- |
| [initialize](https://www.mql5.com/en/docs/python_metatrader5/mt5initialize_py) | Establish a connection with the MetaTrader 5 terminal |
| [login](https://www.mql5.com/en/docs/python_metatrader5/mt5login_py) | Connect to a trading account using specified parameters |
| [shutdown](https://www.mql5.com/en/docs/python_metatrader5/mt5shutdown_py) | Close the previously established connection to the MetaTrader 5 terminal |
| [version](https://www.mql5.com/en/docs/python_metatrader5/mt5version_py) | Return the MetaTrader 5 terminal version |
| [last_error](https://www.mql5.com/en/docs/python_metatrader5/mt5lasterror_py) | Return data on the last error |
| [account_info](https://www.mql5.com/en/docs/python_metatrader5/mt5accountinfo_py) | Get info on the current trading account |
| [terminal_info](https://www.mql5.com/en/docs/python_metatrader5/mt5terminalinfo_py) | Get status and parameters of the connected MetaTrader 5 terminal |
| [symbols_total](https://www.mql5.com/en/docs/python_metatrader5/mt5symbolstotal_py) | Get the number of all financial instruments in the MetaTrader 5 terminal |
| [symbols_get](https://www.mql5.com/en/docs/python_metatrader5/mt5symbolsget_py) | Get all financial instruments from the MetaTrader 5 terminal |
| [symbol_info](https://www.mql5.com/en/docs/python_metatrader5/mt5symbolinfo_py) | Get data on the specified financial instrument |
| [symbol_info_tick](https://www.mql5.com/en/docs/python_metatrader5/mt5symbolinfotick_py) | Get the last tick for the specified financial instrument |
| [symbol_select](https://www.mql5.com/en/docs/python_metatrader5/mt5symbolselect_py) |  Select a symbol in the [MarketWatch](https://www.metatrader5.com/en/terminal/help/trading/market_watch) window or remove a symbol from the window |
| [market_book_add](https://www.mql5.com/en/docs/python_metatrader5/mt5marketbookadd_py) | Subscribes the MetaTrader 5 terminal to the Market Depth change events for a specified symbol |
| [market_book_get](https://www.mql5.com/en/docs/python_metatrader5/mt5marketbookget_py) | Returns a tuple from BookInfo featuring Market Depth entries for the specified symbol |
| [market_book_release](https://www.mql5.com/en/docs/python_metatrader5/mt5marketbookrelease_py) | Cancels subscription of the MetaTrader 5 terminal to the Market Depth change events for a specified symbol |
| [copy_rates_from](https://www.mql5.com/en/docs/python_metatrader5/mt5copyratesfrom_py) | Get bars from the MetaTrader 5 terminal starting from the specified date |
| [copy_rates_from_pos](https://www.mql5.com/en/docs/python_metatrader5/mt5copyratesfrompos_py) | Get bars from the MetaTrader 5 terminal starting from the specified index |
| [copy_rates_range](https://www.mql5.com/en/docs/python_metatrader5/mt5copyratesrange_py) | Get bars in the specified date range from the MetaTrader 5 terminal |
| [copy_ticks_from](https://www.mql5.com/en/docs/python_metatrader5/mt5copyticksfrom_py) | Get ticks from the MetaTrader 5 terminal starting from the specified date |
| [copy_ticks_range](https://www.mql5.com/en/docs/python_metatrader5/mt5copyticksrange_py) | Get ticks for the specified date range from the MetaTrader 5 terminal |
| [orders_total](https://www.mql5.com/en/docs/python_metatrader5/mt5orderstotal_py) | Get the number of active orders |
| [orders_get](https://www.mql5.com/en/docs/python_metatrader5/mt5ordersget_py) | Get active orders with the ability to filter by symbol or ticket |
| [order_calc_margin](https://www.mql5.com/en/docs/python_metatrader5/mt5ordercalcmargin_py) | Return margin in the account currency to perform a specified trading operation |
| [order_calc_profit](https://www.mql5.com/en/docs/python_metatrader5/mt5ordercalcprofit_py) | Return profit in the account currency for a specified trading operation |
| [order_check](https://www.mql5.com/en/docs/python_metatrader5/mt5ordercheck_py) | Check funds sufficiency for performing a required [trading operation](https://www.mql5.com/en/docs/constants/tradingconstants/enum_trade_request_actions) |
| [order_send](https://www.mql5.com/en/docs/python_metatrader5/mt5ordersend_py) | Send a [request](https://www.mql5.com/en/docs/constants/structures/mqltraderequest) to perform a trading operation |
| [positions_total](https://www.mql5.com/en/docs/python_metatrader5/mt5positionstotal_py) | Get the number of open positions |
| [positions_get](https://www.mql5.com/en/docs/python_metatrader5/mt5positionsget_py) | Get open positions with the ability to filter by symbol or ticket |
| [history_orders_total](https://www.mql5.com/en/docs/python_metatrader5/mt5historyorderstotal_py) | Get the number of orders in trading history within the specified interval |
| [history_orders_get](https://www.mql5.com/en/docs/python_metatrader5/mt5historyordersget_py) | Get orders from trading history with the ability to filter by ticket or position |
| [history_deals_total](https://www.mql5.com/en/docs/python_metatrader5/mt5historydealstotal_py) | Get the number of deals in trading history within the specified interval |
| [history_deals_get](https://www.mql5.com/en/docs/python_metatrader5/mt5historydealsget_py) | Get deals from trading history with the ability to filter by ticket or position |

import streamlit as st
from time import time
import yfinance as yf
import pandas as pd
pd.options.plotting.backend = "plotly"

st.sidebar.title("仮想通貨")
st.sidebar.subheader("このアプリは仮想通貨可視化ツールです。以下のオプションから、表示日数、価格を選択してください！")
st.sidebar.title("表示日数選択")
date = st.sidebar.slider("日数", 2, 100)
st.sidebar.title("価格の範囲指定")
price = st.sidebar.slider("価格帯", 0, 8000000)
st.title("仮想通貨価格可視化アプリ")

choices = st.multiselect("通貨を選択", ["BTC", "ETH", "全部"], default='BTC')
st.write("## 過去", date, '日間の', choices[0], 'の価格推移')

st.subheader("価格")


# 引数情報
btc = "BTC-JPY"  # 仮想通貨の銘柄を指定
eth = "ETH-JPY"
period = "max"      # データ取得範囲を指定
period1 = "1d"

# データ取得
Ticker1 = yf.Ticker(btc)
data   = Ticker1.history(period=period)
dataToday = Ticker1.history(period=period1)

Ticker2 = yf.Ticker(eth)
data2   = Ticker2.history(period=period)
data2Today = Ticker2.history(period=period1)

Ticker3 = yf.Ticker(btc, eth)
data3   = Ticker3.history(period=period)
data3Today = Ticker3.history(period=period1)

df = pd.DataFrame(data["Open"])
df2 = pd.DataFrame(data2["Open"])
df3 = pd.DataFrame(data3["Open"])


if choices[0] == "BTC":
	st.line_chart(df.iloc[: date])
	col1, col2, col3 = st.columns(3)
	col1.metric("今日の始値", dataToday["Open"], "5%")
	col2.metric("昨日の終値", dataToday["Low"], "-8%")
	col3.metric("今日の最高価格", dataToday["High"], "4%")
	st.write("%の部分は適当です")
	agree = st.checkbox('詳細のデータも見る')
	if agree:
		st.balloons()
		st.table(data)

elif choices[0] == "ETH":
	st.line_chart(df2.iloc[: date])
	col4, col5, col6 = st.columns(3)
	col4.metric("今日の始値", data2Today["Open"], "5%")
	col5.metric("昨日の終値", data2Today["Low"], "-8%")
	col6.metric("今日の最高価格", data2Today["High"], "4%")
	st.write("%の部分は適当です")
	agree2 = st.checkbox('詳細のデータも見る')
	if agree2:
		st.balloons()
		st.table(data2)

elif choices[0] == "全部":
	st.line_chart(df3.iloc[: date])

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
defence-news.py

■ 指定キーワードで Google News RSS を検索し、
  ・キーワード一致チェックした記事を取得
  ・SINCE_DAYS より古い記事は除外
  ・取得元ソースを限定
  ・不要なキーワードを含む記事を除外
  ・GitHub Pages用にMarkdown形式で出力
"""

import re
import sys
import html
import time
import hashlib
import requests
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from datetime import datetime, timedelta, timezone
from bs4 import BeautifulSoup
from urllib.parse import quote_plus


# ───────── 検索キーワード ──────────────────────────────────
KEYWORDS = [
    # 基本・横断
    "防衛省",
    "防衛産業",
    "防衛装備",
    "防衛装備品",
    "防衛関連企業",
    "防衛力強化",
    "日米同盟",
    "日米安保",
    "日米防衛協力",
    "自衛隊 米軍",
    "安保三文書",
    "安保3文書",
    "武器輸出",
]


# ───────── 除外キーワード ──────────────────────────────────
EXCLUDE_KEYWORDS = [
    "Mrs. GREEN", "Mrs.GREEN", "ミセスグリーン",
    "プレスリリース", "PR TIMES", "PRTimes",
    "イベント", "セミナー", "講演会", "展示会",
    "求人", "採用", "募集中", "アルバイト",
    "占い", "星座", "運勢", "今日の運勢",
    "レシピ", "料理", "グルメ", "食べ物",
    "エンタメ", "芸能", "アイドル", "タレント",
    "スポーツ", "野球", "サッカー", "競技",
]


# ───────── フィルタ対象ニュースソース ────────────────────
FILTER_SOURCES = {
    "日経", "日本経済新聞", "日経ビジネス",
    "共同", "共同通信",
    "時事", "時事通信", "時事ドットコム",
    "朝日新聞", "朝日新聞デジタル",
    "読売新聞", "読売新聞オンライン",
    "毎日新聞",
    "産経", "産経新聞", "産経ニュース",
    "NHK", "NHKニュース",
    "ブルームバーグ", "Bloomberg",
    "東京新聞", "中日新聞",
    "東洋経済",
    "日刊工業","日刊工業新聞",
}


# ───────── 設定 ──────────────────────────────────────────
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125 Safari/537.36"
)
JST = timezone(timedelta(hours=9))
SINCE_DAYS = 15
RSS_URL = "https://news.google.com/rss/search?hl=ja&gl=JP&ceid=JP:ja&q={}%20when:15d"


def strip_html(raw: str) -> str:
    """HTMLタグやHTMLエンティティを除去する"""
    return BeautifulSoup(html.unescape(raw), "html.parser").get_text(" ", strip=True)


def contains_exclude_keywords(text: str) -> bool:
    """除外キーワードが含まれているかチェック"""
    low_text = text.lower()
    for exclude_kw in EXCLUDE_KEYWORDS:
        if exclude_kw.lower() in low_text:
            return True
    return False


def clean_title(title: str, source_name: str = "") -> str:
    """Google News RSS由来の余計な文字を整理する"""
    title = html.unescape(title)

    # タブや連続空白を整理
    title = re.sub(r"\s+", " ", title).strip()

    # Google News側で混ざることがある角括弧を外す
    title = title.strip("[]").strip()

    # タイトル末尾の「 - ソース名」を削除
    if source_name:
        title = re.sub(rf"\s*-\s*{re.escape(source_name)}$", "", title).strip()

    # 「印刷画面」を削除
    title = title.replace("印刷画面", "").strip()

    return title


def escape_markdown_text(text: str) -> str:
    """Markdownリンクの表示テキスト用に特殊文字をエスケープする"""
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()

    # Markdownリンク構文を壊しやすい文字をエスケープ
    text = text.replace("\\", "\\\\")
    text = text.replace("[", "\\[")
    text = text.replace("]", "\\]")
    text = text.replace("|", "\\|")

    return text


def fetch_hits(keyword: str):
    url = RSS_URL.format(quote_plus(keyword))
    headers = {"User-Agent": UA}

    xml_data = requests.get(url, headers=headers, timeout=30).content
    root = ET.fromstring(xml_data)

    for item in root.iterfind(".//item"):
        raw_title = strip_html(item.findtext("title", default=""))
        descr = strip_html(item.findtext("description", default=""))
        link = item.findtext("link", default="")

        source_elem = item.find("source")
        source_name = source_elem.text if source_elem is not None else ""

        # ── ソースフィルタ ──
        if not any(src in source_name for src in FILTER_SOURCES):
            continue

        # キーワード実在チェック
        low_kw = keyword.lower()
        low_txt = (raw_title + " " + descr).lower()
        if low_kw not in low_txt:
            continue

        # ── 除外キーワードチェック ──
        if contains_exclude_keywords(raw_title + " " + descr):
            continue

        # タイトル補正
        title = raw_title

        if "印刷画面" in raw_title:
            try:
                page = requests.get(link, headers=headers, timeout=30).text
                soup2 = BeautifulSoup(page, "html.parser")
                meta_og = soup2.find("meta", property="og:title")

                if meta_og and meta_og.get("content"):
                    title = meta_og["content"]
                else:
                    h1 = soup2.find("h1")
                    title = h1.get_text(strip=True) if h1 else raw_title
            except Exception:
                title = raw_title

        title = clean_title(title, source_name)

        # ── 補正後のタイトルでも除外キーワードチェック ──
        if contains_exclude_keywords(title):
            continue

        # 発行日時フィルタ
        try:
            dt = parsedate_to_datetime(item.findtext("pubDate", "")).astimezone(JST)
        except Exception:
            continue

        if dt < datetime.now(JST) - timedelta(days=SINCE_DAYS):
            continue

        yield {
            "dt": dt,
            "date": f"{dt.month}月{dt.day}日",
            "source": source_name,
            "title": title,
            "url": link,
        }


def main():
    news = []
    seen = set()

    for kw in KEYWORDS:
        try:
            for hit in fetch_hits(kw):
                uid = hashlib.md5(hit["url"].encode()).hexdigest()

                if uid in seen:
                    continue

                seen.add(uid)
                news.append(hit)

        except Exception as e:
            print(f"[WARN] {kw}: {e}", file=sys.stderr)

        time.sleep(0.6)

    # 新しい記事を上にしたい場合は reverse=True
    news.sort(key=lambda x: x["dt"], reverse=True)

    print("# 防衛ニュースモニタリング")
    print()
    print(f"更新日時: {datetime.now(JST).strftime('%Y年%m月%d日 %H:%M')}")
    print()

    if not news:
        print("該当記事なし")
        return

    print(f"取得記事数: {len(news)}件")
    print()

    for n in news:
        title = escape_markdown_text(n["title"])
        source = escape_markdown_text(n["source"])
        print(f"- {n['date']}（{source}） [{title}]({n['url']})")


if __name__ == "__main__":
    main()
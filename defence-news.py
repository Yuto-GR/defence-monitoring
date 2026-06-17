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
    "「防衛装備品」",
    "防衛関連企業",
    "「防衛公社」",
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
    "日刊工業", "日刊工業新聞",
    "ロイター", "ロイター通信", "Reuters", "Reuters Japan",
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



def escape_html_text(text: str) -> str:
    """HTML本文用に特殊文字をエスケープする"""
    return html.escape(html.unescape(text), quote=True)


def render_page(news, updated_at: str) -> None:
    """GitHub Pages向けに、GR Japan風の落ち着いた政策レポートUIで出力する"""
    article_count = len(news)
    latest_date = news[0]["date"] if news else "—"

    print("""---
layout: null
---
<html lang=\"ja\">
<head>
  <meta charset=\"utf-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
  <title>防衛ニュースモニタリング</title>
  <style>
    :root {
      --ink: #14233b;
      --navy: #1f3a5f;
      --blue: #2f5f8f;
      --red: #b73a36;
      --gold: #c7a057;
      --paper: #f7f5ef;
      --card: #ffffff;
      --muted: #68758a;
      --line: #e4ded0;
      --shadow: 0 22px 60px rgba(20, 35, 59, 0.12);
    }

    * { box-sizing: border-box; }

    body {
      margin: 0;
      color: var(--ink);
      background:
        radial-gradient(circle at top left, rgba(199, 160, 87, 0.18), transparent 34rem),
        linear-gradient(135deg, #fbfaf7 0%, var(--paper) 48%, #eef2f6 100%);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans JP", "Hiragino Sans", "Yu Gothic", sans-serif;
      line-height: 1.75;
    }

    .page { width: min(1120px, calc(100% - 32px)); margin: 0 auto; padding: 48px 0 64px; }

    .hero {
      position: relative; overflow: hidden; min-height: 300px; padding: clamp(32px, 6vw, 64px); border-radius: 28px;
      background: linear-gradient(135deg, rgba(31, 58, 95, 0.96), rgba(47, 95, 143, 0.9));
      box-shadow: var(--shadow); color: #fff;
    }

    .hero::after {
      content: ""; position: absolute; inset: auto -12% -35% auto; width: 420px; height: 420px;
      border: 1px solid rgba(255,255,255,0.22); border-radius: 50%;
      background: radial-gradient(circle, rgba(199,160,87,0.18), transparent 62%);
    }

    .eyebrow { display: inline-flex; align-items: center; gap: 10px; margin: 0 0 18px; color: #f0dca6; font-size: 0.82rem; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; }
    .eyebrow::before { content: ""; width: 34px; height: 2px; background: var(--red); }
    h1 { max-width: 780px; margin: 0; font-size: clamp(2.1rem, 5vw, 4.4rem); line-height: 1.12; letter-spacing: -0.04em; }
    .lead { max-width: 680px; margin: 20px 0 0; color: rgba(255,255,255,0.84); font-size: 1.05rem; }

    .stats { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px; margin: -36px clamp(18px, 5vw, 54px) 36px; position: relative; z-index: 2; }
    .stat { padding: 22px; border: 1px solid rgba(228, 222, 208, 0.86); border-radius: 18px; background: rgba(255, 255, 255, 0.92); box-shadow: 0 12px 34px rgba(20, 35, 59, 0.09); backdrop-filter: blur(10px); }
    .stat span { display: block; color: var(--muted); font-size: 0.78rem; font-weight: 700; letter-spacing: 0.08em; }
    .stat strong { display: block; margin-top: 6px; color: var(--navy); font-size: clamp(1.25rem, 2.5vw, 1.85rem); line-height: 1.2; }

    .section-head { display: flex; align-items: end; justify-content: space-between; gap: 24px; margin: 24px 0 18px; border-bottom: 1px solid var(--line); padding-bottom: 18px; }
    h2 { margin: 0; color: var(--navy); font-size: clamp(1.35rem, 3vw, 2rem); letter-spacing: -0.03em; }
    .note { margin: 0; color: var(--muted); font-size: 0.92rem; }
    .news-list { display: grid; gap: 14px; margin: 0; padding: 0; list-style: none; }
    .news-card { display: grid; grid-template-columns: 132px 1fr; gap: 20px; padding: 22px; border: 1px solid rgba(228, 222, 208, 0.9); border-left: 5px solid var(--gold); border-radius: 18px; background: var(--card); box-shadow: 0 10px 28px rgba(20, 35, 59, 0.06); transition: transform 160ms ease, box-shadow 160ms ease, border-color 160ms ease; }
    .news-card:hover { transform: translateY(-2px); border-left-color: var(--red); box-shadow: 0 18px 42px rgba(20, 35, 59, 0.11); }
    .meta { color: var(--muted); font-size: 0.88rem; font-weight: 700; }
    .date { display: block; color: var(--red); font-size: 1rem; }
    .source { display: block; margin-top: 6px; }
    .news-card a { color: var(--ink); font-size: 1.05rem; font-weight: 700; text-decoration: none; }
    .news-card a:hover { color: var(--blue); }
    .empty { padding: 42px; border: 1px dashed var(--line); border-radius: 18px; background: rgba(255,255,255,0.72); color: var(--muted); text-align: center; }

    @media (max-width: 760px) {
      .page { width: min(100% - 20px, 1120px); padding-top: 20px; }
      .hero { border-radius: 20px; }
      .stats { grid-template-columns: 1fr; margin: 14px 0 28px; }
      .section-head { display: block; }
      .note { margin-top: 8px; }
      .news-card { grid-template-columns: 1fr; gap: 10px; padding: 18px; }
    }
  </style>
</head>
<body>
  <main class=\"page\">
    <section class=\"hero\">
      <p class=\"eyebrow\">Policy Intelligence Monitor</p>
      <h1>防衛ニュース<br>モニタリング</h1>
      <p class=\"lead\">政策・防衛産業・安全保障領域の主要報道を、落ち着いたコーポレートトーンで一覧化します。</p>
    </section>
""")
    print("    <section class=\"stats\" aria-label=\"更新情報\">")
    print(f"      <div class=\"stat\"><span>UPDATED</span><strong>{escape_html_text(updated_at)}</strong></div>")
    print(f"      <div class=\"stat\"><span>ARTICLES</span><strong>{article_count}件</strong></div>")
    print(f"      <div class=\"stat\"><span>LATEST</span><strong>{escape_html_text(latest_date)}</strong></div>")
    print("    </section>")
    print("    <section>")
    print("      <div class=\"section-head\">")
    print("        <h2>Latest Coverage</h2>")
    print("        <p class=\"note\">Google News RSSから取得・フィルタリングした記事です。</p>")
    print("      </div>")

    if not news:
        print("      <div class=\"empty\">該当記事なし</div>")
    else:
        print("      <ol class=\"news-list\">")
        for n in news:
            title = escape_html_text(n["title"])
            source = escape_html_text(n["source"])
            url = escape_html_text(n["url"])
            date = escape_html_text(n["date"])
            print("        <li class=\"news-card\">")
            print("          <div class=\"meta\">")
            print(f"            <span class=\"date\">{date}</span>")
            print(f"            <span class=\"source\">{source}</span>")
            print("          </div>")
            print(f"          <a href=\"{url}\" target=\"_blank\" rel=\"noopener noreferrer\">{title}</a>")
            print("        </li>")
        print("      </ol>")

    print("""    </section>
  </main>
</body>
</html>""")

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

    updated_at = datetime.now(JST).strftime("%Y年%m月%d日 %H:%M")
    render_page(news, updated_at)


if __name__ == "__main__":
    main()
---
layout: null
---
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
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
  <main class="page">
    <section class="hero">
      <p class="eyebrow">Policy Intelligence Monitor</p>
      <h1>防衛ニュース<br>モニタリング</h1>
      <p class="lead">政策・防衛産業・安全保障領域の主要報道を、落ち着いたコーポレートトーンで一覧化します。</p>
    </section>

    <section class="stats" aria-label="更新情報">
      <div class="stat"><span>UPDATED</span><strong>2026年08月10日 12:14</strong></div>
      <div class="stat"><span>ARTICLES</span><strong>33件</strong></div>
      <div class="stat"><span>LATEST</span><strong>8月9日</strong></div>
    </section>
    <section>
      <div class="section-head">
        <h2>Latest Coverage</h2>
        <p class="note">Google News RSSから取得・フィルタリングした記事です。</p>
      </div>
      <ol class="news-list">
        <li class="news-card">
          <div class="meta">
            <span class="date">8月9日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE8xRzhxMkdvbDFGcks1b09oYnRfdS1RazgwWlRVUklXUTR6MTNxd092Qkd3Q0x3alhVemctZ3dJdFNuQnh6aGdfdmJ3QWEyNmhnRUcteUd2aEhva2k0MXF3cldreVNlYlNIOVpxTw?oc=5" target="_blank" rel="noopener noreferrer">防衛装備品にサイバー防御ソフト 空自レーダーなど27年にも導入</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月9日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE0yZDFTMVlyRi0xTng0bXR0LW1pUmRIdFBIMkVoSU5yQjViWnFqekxEQU8zWjBwTEJYYzJqTGxYTDJlajNXdXNaVGVEU1hRX0RKTkFkaVMxR3JYNzNObVN4T1BnSExISHpwaFR2Vw?oc=5" target="_blank" rel="noopener noreferrer">パケ駐日EU大使、日欧安保「かつてなく密接」 防衛産業の協力期待</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月7日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE5vUW0tU0RTLWJ6WjBmeFRWSTNuX3VfbGhSbFlBYm5ZOGl5dHB1cGRrUnVlMGFRSlZIRWU4TUozbTZ4UjFibDQtSEUtOFhaWHU3d1hMNkRMNUVWeFk0VGFGN2RfbHNJWnFnZDNtQQ?oc=5" target="_blank" rel="noopener noreferrer">護衛艦や戦闘機の取得に遅れ 防衛省、物価高で単価上昇</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月7日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE96ejlzaUFTS0hqRS0xSmhkTHlZNmZneEI2WHRJNHlWbXRJSllWRGhyaWRYQzR1azgzT09EUnhQRTE3QmMwTHpaTTd1SlJLb1M5UkUxMU9FdmlwcVZrcDNLUlFvZDA1Zw?oc=5" target="_blank" rel="noopener noreferrer">防衛省、反撃能力向上へ攻撃型無人機を導入・太平洋側の防衛「監視能力は不十分」…安保３文書改定の骨格</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月7日</span>
            <span class="source">東洋経済オンライン</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiUkFVX3lxTE54YjJiS2VDdjM3VjR2S1RxLVVOamg3OGlEenRuNnp3dUVXYmhreHFLblZfZ0hCV1FJS3ZCWjZqa2hoUXFqOGFqQWtVdmp1WWVRQUE?oc=5" target="_blank" rel="noopener noreferrer">災害支援で賞賛される防衛省･自衛隊､その陰で放置された組織防衛と無謬主義という罪､防衛費を倍増すべき組織なのか</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月7日</span>
            <span class="source">東洋経済オンライン</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiW0FVX3lxTE5uNGFDT2V6cE05ZGgzeDRJbjB2Z1pRMnNiZ3hlNzVkY29YR1pFMjFDNFE3bkFMeTVyQ2NDVnQwNnVwNVcxdXlrM1htbmZNVnQ4TmItMHZlc18tdEE?oc=5" target="_blank" rel="noopener noreferrer">災害支援で賞賛される防衛省･自衛隊､その陰で放置された組織防衛と無謬主義という罪､防衛費を倍増すべき組織なのか</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月7日</span>
            <span class="source">東洋経済オンライン</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiW0FVX3lxTE45Nm9MREtKOGZUWGFUd1hmeVBpemVrYVRLbTRyUEhOUDZKSkpSQUdHcmhnY0doN055eWlIdHdHc1dtbHBfY0NoZHNYMy1FQUxCVUNPdmx3YmpqSmc?oc=5" target="_blank" rel="noopener noreferrer">災害支援で賞賛される防衛省･自衛隊､その陰で放置された組織防衛と無謬主義という罪､防衛費を倍増すべき組織なのか</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月6日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiVkFVX3lxTE1hdVRnZWV3UUw0bzlsV2V0VU1VZDZNZEQ3Sm5tcUU5TzRQX2hOemJHd0trUGVrM1R0TWJjREZKVDNESkp2VkZ5cnE2TWxoSkRfUWhKekVR?oc=5" target="_blank" rel="noopener noreferrer">高市首相「我が国は非核三原則堅持している」安保3文書改定で見直すかについては明言避ける 広島「原爆の日」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月6日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE44VXRYc092VjRUb1drTXVNLWtFUFl3M2s3VE9JajBYRkdxT1lmc1dmaTdydG9RaFlqLV9Kc2t4NnNRVlJxTUlsUkxOU1JQMmptaFZ3SHNSRmlqbTdBMzZHRmZ6aVR6aElrcDJfUA?oc=5" target="_blank" rel="noopener noreferrer">防衛省、装備品調達数を事前通知へ 企業に設備投資促す</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月6日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE9HYkRMdFlCQ1NqYUxHT04wTmRVcmxKR0xMWWxQQ3JkYkhnYi1lU0pBVHR5S3J3RE9McXJ2TVQ5MnpQTUtWVWppbTMtWUpibGhCd2x6QXZJOHgyamF6VDhra093bw?oc=5" target="_blank" rel="noopener noreferrer">防衛省「日本周辺に影響なし」 北朝鮮ミサイル：時事ドットコム</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月6日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTFA0TWJSZllGalktSnpnX2ZVQ1JwMUJ1NnJVQVlBUEFnOXlxUWtzOGxEWllUNVlGSGhPbHFZRGF4WUNSV2RFLTJoUUs4UnBuRk1VZS10U251VUszMUx6REVVM3NVX3RWNk0?oc=5" target="_blank" rel="noopener noreferrer">北朝鮮が弾道ミサイル発射か 防衛省関係者「EEZ外に落下」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月6日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMigAFBVV95cUxPUG1SNmQxZHJua3c1UUplSEw1b1otS0lMME55SGVkbkJDMlMzak9rWlp5eGxGWUpmVWRQUHFhejl5YzQyQzRlUXZGV3pOTFVIelFvb3ZsZkVmV0YwZURzU0JmR2lEVDJmbEtETWp5bDlzVkNrakZiRnNzOF81NXFrRQ?oc=5" target="_blank" rel="noopener noreferrer">画像・写真：防衛省「日本周辺に影響なし」 北朝鮮ミサイル：時事ドットコム</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月6日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE5La1FQcS1jb01WTm92bENaV3UxVi1iVm5wbFl1WWFabjVuWkFKQlFhQzVOek40VzBoRWQwYnlqZ0hISkI4WmRvUThKVE83UEstQ0V6X2pfTWJKN01mUDFvZHkycDJadw?oc=5" target="_blank" rel="noopener noreferrer">【速報】防衛省によると、弾道ミサイルの可能性があるものは既に落下したとみられ、日本周辺への影響はない</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月6日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE14THowcUw2ZUxib2ZWQTJrdFcxeEduS2IxVWdzY05kZVBLR1I5MzRmT3RWTHliR1lTTlFlV2lKSzlLQmdRY28xUmZrZld3amFlVzVlYkxWdnd1MWNmbVR6WDZHRTBBQQ?oc=5" target="_blank" rel="noopener noreferrer">【速報】防衛省によると、北朝鮮から弾道ミサイルの可能性があるものが発射された</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月6日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE11ZFdzNXZpMnNiNU1XaDlOQ2x2RHZZUFRFeWpXM3JxVUVCUzFidlZqMEpHTjhmWXVZTXM5aHFPUWs5QWktS0JSNk9YMkJWWm5OcXQ3bEJZcGNXMkpGS0tzQTdrRk5PNEtr?oc=5" target="_blank" rel="noopener noreferrer">安心はどこに：京丹後・米軍基地 発電機騒音 防衛省「重く受け止める」 専門家入れ対策検討へ ／京都</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月4日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE1MTGh3OHpmX291amJuU0ZIZGtoOUktTWJXaTF2d205d0Q2cWc5YkRiWHgtN1BFRm1HOTdCTFhraElPMXoxck53ejA2czdnYWVxZGhERFZ1VWdVbG9YMVo0?oc=5" target="_blank" rel="noopener noreferrer">安保3文書の有識者会議 経済的威圧に対処 法整備求める意見も</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月4日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE4yRUdSUjZZck5hNlBGNUFNUE5Pc3FPZEJjcUFtaEIzLXhxQjRDQ21aYWY1RFkySUVxNGdqcEpMam1pMV8wOU1QdUdpMC0wYllHY0ZlSzlzeUJoUG9ObzJYSGF4blo5YXFxUWZiWQ?oc=5" target="_blank" rel="noopener noreferrer">「経済の武器化」対抗へ同志国と連携 安保3文書改定へ有識者会議</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月4日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1IejJ5RWlaeU5GNlE1eG43MWVubUZ5b2I0a21ORmRGaHU1ZnNzUENVcGlwWkpZcHhVaFhTbmRnVnlkYXY1dXNfN1pNWU1IWnlIajB0ZU5YOW84NmNfNklwdzNLSUZ4dG8?oc=5" target="_blank" rel="noopener noreferrer">「生産力こそ抑止力」安保3文書改定の有識者会議、経済安保を議論</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月4日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE5KQzI3d19tN0x4Q0FfRDUzdTRUR3d5NVhmNXRkYXZILWt1cFR6c21wUDdrcjBMaXZ1LWp4Mk1Va0d0QlpJb29TQmhsUGhnY2VXbUYxNXptdWlNRVMxOE5Vbks1VHVXdw?oc=5" target="_blank" rel="noopener noreferrer">熊本の被災地にあすから「病院船」、防衛省の船舶活用し初の取り組み…内科診療や熱中症治療・薬の処方も</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月3日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTFBUTERuckRMQlNKaGEwWFBHUFk3bHBwQzRMVDlBZnIzZE5BcThGMWpVOHdxRER1b3FjN1VrQ1Bld2VhT2gtNkZEV0RmSjBuQmk3eHVVdkpJN1VyQQ?oc=5" target="_blank" rel="noopener noreferrer">防衛装備、日本の政策はどう変わる？ 元統幕長・前装備庁長官に聞く</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月3日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE9hc1N4ZmN6d2FXSlVXNmdRUjFhWi1KZ1M2dmpWODdsOUlhWFBmN3I4UkJPRXRabEJmNnJmSmRwa01LQ0N1MUZNS1RlbTZIM00zUk1ZWmF4djl5WmFFRUgyNmhhTQ?oc=5" target="_blank" rel="noopener noreferrer">インド、イスラエルに武器輸出２５００件超 「虐殺加担の恐れ」と国際人権団体</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月2日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE5OZk96QUp5X29GVjBCbFlwU2NKWHU0ejhleGphcUt4MlRueEI0SmtyYk5xV1VYV2dHZ20zWkM3TFU5TE56Ml9LVEFON3Q3QlUxLXdnYVBFVy1DVmowM2Zn?oc=5" target="_blank" rel="noopener noreferrer">防衛省 国際連携関係の政策を担う局の新設を調整</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月2日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMia0FVX3lxTFBMNVNSbkNCa0JsX2dlQjB4V3l5R014NWJ1Q3p0bXBZNVlHNmtDZ2c0dHdxczd5VlpINDdBTE5ZRFk2T1F3MkRnSGlhTWtScjl0NkNOYzA2UzZONmliSmhrd0RwN3h1dmhHalRj?oc=5" target="_blank" rel="noopener noreferrer">［地球を読む］日米同盟 相互防衛の意思 隙間なく…ハーバート・マクマスター 元米大統領補佐官</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月31日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE40SDdkaG5vUW9kU0tUWWQzbEUwZkNCT0ZleXQwVHA1ckkxVG5MQWtfekdqU0M2TTRwRDd2MWxEeDRacExvRWJQcGxPZnF3SHhPWDRPWndWbDZzQWY5V0JaS09nZ19nQm9aaENXYQ?oc=5" target="_blank" rel="noopener noreferrer">迎撃ミサイル成功9割超 韓国防衛産業、UAE導入で脚光 25年、輸出シェア世界4位</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月31日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE5HMk16NDNzNlVQVEo0OXdFOVlIdDd1ZFBpMk5Ld3hDdTNycHRyM04tdjhxUHVFdkktdDR2U1Z1ZkVJdFlZdlFIMmI4YWctbDhiUEJ6S3R5cjkzTUMxUVZXa3AtLTRqaEl1TG9IXw?oc=5" target="_blank" rel="noopener noreferrer">防衛審議官に安藤敦史氏 防衛装備庁長官は今給黎学氏</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月30日</span>
            <span class="source">東洋経済オンライン</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE1GXzNCLVNuTzlpZmZMRGJJSVJLbWVZOVBJaGhhcEg1bW9aOFJaNlRRcXdScmlkdTZtdEYyeWQ1UnBqNlU0QlNpYzlOUWlQMy1nY3lVT0NQY1NsY0ZIODM4?oc=5" target="_blank" rel="noopener noreferrer">自動車の次は建機､そして防衛産業も…セレンディップが｢1000億円ものづくり企業｣に向けて構築した斬新な仕掛け</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月30日</span>
            <span class="source">ニュースイッチ by 日刊工業新聞社</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiQkFVX3lxTE15ZkVacGo3OTljSTh2Y0UwSzg5MjA1WUhWdmxST1lrMVZMMXlncGphVWJSMVZnaGhjYmM4cWtWakNKUQ?oc=5" target="_blank" rel="noopener noreferrer">豪次期護衛艦向けソナー、三菱重工に供給…OKIが初の海外への防衛装備品移転</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月29日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE10dkVDQ2FyeGdxdDZvTnRWbEc5SFRzeVJWaEVlR3NaZkZ6WGNxS3doME9VeVRDQlRCT0ZGTUlSN0lWa1V6TmlxMzFmbk9Oejk4S3VmUDdmWXdPS3lMY01r?oc=5" target="_blank" rel="noopener noreferrer">ゼレンスキー大統領 米防衛産業大手幹部と会談 連携強化を協議</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月29日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE0xQU4xX0o0Wi1YRWhMSmJwS29ILW16Q0dacWJEb0N0bVJoZmpETzh0RDltN3NRMmctTWdvVlZpUFZnelY2bEFheW94TW1xZHVYaVRZdWFNWXZXd1BxVVJ6RzBLM3F4SzBPVmwxcw?oc=5" target="_blank" rel="noopener noreferrer">AI開発のプリファード、作戦支援システムを実証 防衛装備庁から受託</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月28日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTFBiOG43dHp5Um1YdWxXZVZVT2xLc2FlYW56YjhIQ2pySnFQWUh3bjQ4c1NxTnR6Y1NaTDV4R3lTUV8xT2JpZWJIQ3d3RmpYMzZTTmxuYm5vb2RfdWdQWldLVnNXZkR4RXRpUWFjdQ?oc=5" target="_blank" rel="noopener noreferrer">OKI、防衛装備を海外移転 豪護衛艦向けに</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月28日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE9MM1hCZlZDdlBTWVhWLTdxRURvWW1Wa21ES1F5ajYyMHBvUkR0bDNSWmEtZmdrS01hVjVUYk84bE5VamZhWkpQR0lvck90QkxCRVJGTmJkRDJ0Vmd4NGkwVVd4cmpSNVdncmcyZQ?oc=5" target="_blank" rel="noopener noreferrer">オーストリア、兵役期間を3カ月延長 ロシア対抗で防衛力強化にかじ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月28日</span>
            <span class="source">東京新聞デジタル</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiU0FVX3lxTE8zR00wdG55MlJLU3dhNWVzbUNoMk90enA1aFlBUlZwbkRlaXdoX25MVVFfTGs1T0cyYXl2bGJ5LW8wMWh5a09pRkZlejJLaXVzY2Zn?oc=5" target="_blank" rel="noopener noreferrer">「核戦力に触れざるを得ない」小泉進次郎防衛相の発言が波紋 安保3文書改定を前に踏み込んだ意図は何か</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月27日</span>
            <span class="source">NHK</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMickFVX3lxTE0tbE96RHB3ZUpGVVpSODMwcENUaWRMMUsyZm5RNnd6WjBiRzAzOE5QNGx1bVg0NWNabzJ2R3JibkhodmdQZDRtYmNMcTJMZlJCUWhnWmp4RlVlVElmQTRsTjRYNXFsVEYzVnFiVS1OMlExUQ?oc=5" target="_blank" rel="noopener noreferrer">月曜6時台前半 ニュース・気象情報/存在感が高まる韓国防衛産業/何の日 - マイあさ!</a>
        </li>
      </ol>
    </section>
  </main>
</body>
</html>

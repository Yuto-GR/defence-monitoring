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
      <div class="stat"><span>UPDATED</span><strong>2026年09月23日 14:44</strong></div>
      <div class="stat"><span>ARTICLES</span><strong>42件</strong></div>
      <div class="stat"><span>LATEST</span><strong>9月23日</strong></div>
    </section>
    <section>
      <div class="section-head">
        <h2>Latest Coverage</h2>
        <p class="note">Google News RSSから取得・フィルタリングした記事です。</p>
      </div>
      <ol class="news-list">
        <li class="news-card">
          <div class="meta">
            <span class="date">9月23日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE5yT0xta3lXTUJZdzR3RWctM1ZQR0h2NnVPLWZNRXpGS0JYaFZ1NDNiTnVERXd0enJ1cU5SWE9hU01UalNwRC1XRHdDNmhxSlpfTlhfNWlleGppcW1QSGZGc1oxWlZfdw?oc=5" target="_blank" rel="noopener noreferrer">高市首相、トランプ氏との会談「中国巡る諸課題でタイムリーに意見交換」「日米同盟の強さ世界に示すものに」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月23日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE1STF9jRTZ3UV9abHRZRGg2eUh4UzdaZVpVWjNxYVFLN1NjdHg4dUdUX014b1RRY3ZmVUNjeW5EYVNMb1g0clVuMmNZNkg3dGtOanlkajNaQURuMVlKUXRZ?oc=5" target="_blank" rel="noopener noreferrer">高市首相 記者会見“日米同盟揺るぎのないものに”</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月23日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE9ESzNBckJlNjRhZE5vYTlKS2N0THg3SThzdWhJMFRxeVpXWFlzM3RmSV9IWm9CeHdIUDd5UVdiNlZCTjZVLXdGU0RqTmhuWDFFMHNoNFE2d3hKOUhJV2JubmlsblZLQQ?oc=5" target="_blank" rel="noopener noreferrer">高市首相とトランプ米大統領、約３５分間会談「日米同盟の強固さを世界に示せた」…ＩＣＣ巡る率直なやりとりも</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月23日</span>
            <span class="source">Reuters</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE5NYUp1RWRrY2RZaWpxTGVYMy1WZDYwcGVDRWo1bHYzclNtVDkxUjJXOEozY0c1SVVwc0J2MFlFVm1BOWFtMlJkNGtwWFZkWnRfVVFFc0QxQTVialpZTHRaSzl6N2VwbXNJLVRCUHFvMVdadzIwTm5iV3o1c3NFZm8?oc=5" target="_blank" rel="noopener noreferrer">日米首脳が会談、高市首相「日米同盟の強さ示す」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月23日</span>
            <span class="source">Bloomberg.com</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMid0FVX3lxTE9STm05VGx0VGg1a3IyMGxMUmxVMkhTWm9uU3docVk1MTVkOUdxM2ZOMTJMWUJ5ZjN2Vnhmc1JmQUtSUnF5d1QwMWZuRTBZWUJET2lyeXNjcVliRnptQlJFeHFzMWtmQkdHY1ZBbnhZVHZUVEdPemZJ?oc=5" target="_blank" rel="noopener noreferrer">高市首相がトランプ米大統領と会談、「日米同盟の強さ示す」と強調</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月23日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE40bkJUSzlBQVlmeUo1SkRBZEpHa2paRGt2WWFqc1U5M254LWs3WlpWUDlMYTlza2NnWWRVOGZIZGtPUHhWcFNvWjVqMl85QmVWWUNFNEtidE1Ec0RucVdyVGNDVXo0dw?oc=5" target="_blank" rel="noopener noreferrer">【速報】高市首相は、日米首脳会談について「世界に向けて日米同盟の強さを示すことになる」と述べた</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月23日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE04bTFtV1d2ckh5UWxYRDlvT0xsdmFEanBCVUktYkpHWTE5Mjl1Y0MwcWN6d3UzWWR3SXl4d19EMGZXNy1tZklYQ3pFd2M0cDRVOWxCZ0JKbWdDRy16MWpzNVdDSGlnNFFP?oc=5" target="_blank" rel="noopener noreferrer">日米同盟の強化を確認へ ICC制裁への言及焦点 日米首脳会談</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月22日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE9idDJkTXVST3ozUGczdE1ySlFma0VPenNHZ1VsemF4OEkzWEo4VVhNdFZyWXlyNHBSTUJRc3pQVFotYUlqcXJyNVFDV19OSzFoN3pHR0Vya0MtcEpBMGNKRjFpUDJXQU96?oc=5" target="_blank" rel="noopener noreferrer">激動期の安保：防衛産業融資、惑う金融 業界「平和国家」信用にリスク／政府「成長戦略」盾に増す圧力</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月21日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE1TWWplc3BtRGt3MjVWZmtYU3d5M3oydlRkUjVfMG5Ud0p0MmFyVVppcW1HOFdGT2VBdFg2eHMxRnJhTzhpZzc0aGdhTjlsbWlFak8yVDBDNDVrRTZaN290eElmRWJ2SVU2?oc=5" target="_blank" rel="noopener noreferrer">激動期の安保：防衛産業強化 政府と金融機関に温度差「融資はセンシティブ」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月21日</span>
            <span class="source">東洋経済オンライン</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiUkFVX3lxTE96cFJxcmliSV9MZjFtWC15ZkdtY0tQdjJRVHhGUlFUUGQtOTF2YkdSZE1rb0x2em0tT0ptalVGV2lmZUxENmpyUGNSNkpfWXF5Z3c?oc=5" target="_blank" rel="noopener noreferrer">【検証･防衛記者クラブ（前編）】国民の知る権利を空洞化させる―防衛省で露呈した権力監視の放棄と当局癒着の実態</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月21日</span>
            <span class="source">東洋経済オンライン</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiW0FVX3lxTE51c1BlR0k0cFQydUR5elBrWms4emhZcGpuX3FpNmV4LUJIb093VmJUZ0tyd1IyWXY1QVlpU0dmU3pVbWJXU05RdlBPUTZIOFBBUDRYaExQMnhJUW8?oc=5" target="_blank" rel="noopener noreferrer">【検証･防衛記者クラブ（前編）】国民の知る権利を空洞化させる―防衛省で露呈した権力監視の放棄と当局癒着の実態</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月21日</span>
            <span class="source">東洋経済オンライン</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE9mSnVnU2g0TXJfUUFBSE8tNDBSVmNqSjYtMmNKc2dKMHJCbjU2NDhXNlVoY1VsNGQ3LVNmb2JfRHRqcmJQQXdsbk5uaHgza0FmTWxvRldxdGo3dkNLeS1R?oc=5" target="_blank" rel="noopener noreferrer">【検証･防衛記者クラブ（前編）】国民の知る権利を空洞化させる―防衛省で露呈した権力監視の放棄と当局癒着の実態</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月20日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE9ZUVlyMFhHT0sxUWZXM2MzYUpJU1kwVkxoamlxcnVqZk9oeWI5aUxUSkFNVGRqV2h3V0pSOU96aFdFWnJmb1JlTjhqMlZLSTJXMFU0aWx5dS1jSGFFUV8zbTNySDNHdw?oc=5" target="_blank" rel="noopener noreferrer">【速報】防衛省によると、北朝鮮から午後６時すぎに発射された弾道ミサイルの可能性があるものは日本のＥＥＺ外に落下したとみられる</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月20日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE1ESVo3QWhtRmlLVHViTW9EMVVqaFBHaTVDd3BwMmFaWnUzZjBSQW5IUkFuQkF0R2RLa00yR1UzZk9FYmFsTkMta20zalpzUlhud29xY2dGdGFDTnA4dmhEVGYyNl9NZw?oc=5" target="_blank" rel="noopener noreferrer">北朝鮮が「弾道ミサイル」発射、すでに日本のＥＥＺ外に落下か…防衛省発表</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月20日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE5wNzNwd09ONmdLSDc4TEJIU0NIMVI1OENVVHFtMDNYMlVjTjNmT0E4dU5hTEJwak92TmI4QTZtbndIV0VOYnVQZ2hjOFNZb3BDNkZKMHFCeTV2bWRuR0tadmlER2JWZw?oc=5" target="_blank" rel="noopener noreferrer">【速報】防衛省によると、弾道ミサイルの可能性があるものは既に落下したとみられる</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月20日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE04T1pMeUtocm1BU0JVRndNZV9LejYzZmJvY3RGQ1hjN29IdFMtejdHa3duWTFjbnJpR3VDOE5lbEZDNUR6NEk4UFFwcERNb0RRR05sVUVfMU4wOFB4QVVzNnFjTEdFdw?oc=5" target="_blank" rel="noopener noreferrer">【速報】防衛省によると、北朝鮮から弾道ミサイルの可能性があるものが発射された</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月19日</span>
            <span class="source">時事通信ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiVEFVX3lxTE1oR0trUnFJMU9QSWhiVFpncW1XczhQajg2N2NPMGp3ZjNmNlY2TVhRSXljUE9pNDEzQUlieHJ3aGhsRjBVblZZMXpUMzl5NVJsdXRpZQ?oc=5" target="_blank" rel="noopener noreferrer">◎日米同盟強化へ連携</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月19日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE0wWEZUbFM1NkNaeGdNNFFxSS1UMUhxTmI5TnMyV0ZzVVFldi1nTGZ0QlNxeGVLcWg2NlFoVFRjUXNCWEN0YUF3SWxtUGdiVlFKRlF0QUhmZ3BxX1p2WE5aQWxzLW5DRGxv?oc=5" target="_blank" rel="noopener noreferrer">武器輸出の原則容認 国民の不安解消に政府がやるべきこと</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月19日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTFBwZndqdXplZW9BMDVETjRTbnVPQXE0WG44VWM4dWdCaTF1QUZTcGhfM2dpczlPU1h0YzQxWU1iMHBPNGhWMk9PUzRRcWNxaFRBUjNTdk5OX1k1c3U0NmpCZk5ERQ?oc=5" target="_blank" rel="noopener noreferrer">日米同盟強化へ連携 防衛相電話協議：時事ドットコム</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月19日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiggFBVV95cUxQMmpheVV3QW5TSUg0NmpHaEpKLU41X1dSOUdNbHBWX1BEMDlWVU5DSzhUV1BBLU1KZmsxZ3lybVRvTlV0S0laUlljaTlSVTl5bng2MW8wUFlDZ0ppUTB4OGtWdVJVV3ZfSjBNcDNIUjE0emxqZm8zMl9ONzN4ZFdDODJn?oc=5" target="_blank" rel="noopener noreferrer">画像・写真：日米同盟強化へ連携 防衛相電話協議：時事ドットコム</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月19日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE83ZjBqQzBoSm1veW92eFJnZi1CeW1kREtkWExTcGFvQXRQRkxucXdaVUZnMzJuNjlld0ptcVhrd25QdXJtZktlZEt5NnNLWk1jYWJqU1FONnViYWo5X1YxbE9xSnNHbElmZ3ZtUw?oc=5" target="_blank" rel="noopener noreferrer">低価格のドローン迎撃ミサイル 英新興、防衛省に提案 1発数百万円</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月18日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE11X0t6NE9EMHU1VFpONUJHMTcwVFpoRmE0VDlMNEZBZVgzcXlFX05lZ2o0SDJ6QURmbWxFdFZJZjBadDRMbW95Wi1NUlE5TkJhX0VBVkx0WWphdTAxUXVaNTFGaFVBei10elQ1Mg?oc=5" target="_blank" rel="noopener noreferrer">英新興、低価格のドローン迎撃ミサイル 1発数百万円で防衛省に提案</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月18日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTFBCMkpfUE1RSExFRDdTbDRDSVZRMlZCMVZsb0xpcUwyTkFwWU5yUGo3YTktSHBVUUNNUVBzRzFVRzFXUlpTNk85aGM4aU5wcGVPdE1JSnV5Q3BTenB0RGlFNEhnMEhJSWhGcUhDWQ?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相「防衛産業の成長への一歩」 三菱UFJの融資基準新設方針</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月18日</span>
            <span class="source">信濃毎日新聞デジタル</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMia0FVX3lxTFBnV1M0Vkk5Ukd6WFhUS0JlMzBQSzJnRkpsaW9oZENVRVZKUVhCVm51LWh1SndocXlCSDlDeERUTmFfUDNjU0s1RTZYOVFIaVVGbkhKZ21FNmsxRTZCZUplU1FmTnRvY29qNWY4?oc=5" target="_blank" rel="noopener noreferrer">安保3文書「未来を左右」 留任小泉氏、改定へ決意</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月18日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE0wVzNQR2xmZjROQUh4aENSdG03OU1FRlhHR2JNN2RoZFNlU3JkM1AxVl90ZVd0Uk0tQ1hzSTJGTHpObWY3emtVQ19VN2tkeHV0VWpQNEt4aVNvSWZfSWptMWFTYWZndmZ2ODdOag?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相、3文書改定「日本と地域の未来を左右」 防衛省で訓示</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月17日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE4wRFlYOE5zUU1mcy1vNzRCQkVybUtoU18wR3FWc29CRXdoMnVwcDVBTUpxX21QNXBuOEZFMjNodmxNRTB2M3R2eGtEcmt5WVhjMTB1bUFvM292VTRnMXR3?oc=5" target="_blank" rel="noopener noreferrer">防衛産業への投融資 全銀協・加藤会長「個別に判断」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月17日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE1uR0hMbmVuVlIyaWM5ZUN6MEp1WU96bENuMmIwbGpLTm5zaTVoMHg5NUNEMkVkSW02dDc3R0ZZNzJqY2QtSlZ4bi1rYTZPTEJPS2VpRUlUbmM2SnZScGhZ?oc=5" target="_blank" rel="noopener noreferrer">安保3文書の改定に向けた有識者会議 AIの研究・開発求める意見</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月17日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE9TbEJ6ZVN1S2FfNlp3UWRhWG9fQlZTaENhWUFXX2NHY1BITzlRaW1pSFVua1FPTVh5MGRsdUhDUmVVUjQ5TkNWdWlPdTZQZXFPeEVjOWxERERrbjF4VnUtNF9xX0lfSmNmVHEtVQ?oc=5" target="_blank" rel="noopener noreferrer">三菱重工業など防衛関連株が高い 「防衛産業に融資」報道に期待</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月17日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE9IenZpQUxnM3JCeTNlcGk4SjEybmVPNVZsOXBGbDNVVExOeFRxd1lsNnBQa0xONGNSc2dMdHRER05leFI5cE5WbEtHcHJkRFBPRElna25OckZuckZCZ3A2SFVELTE4UGlm?oc=5" target="_blank" rel="noopener noreferrer">記者の目：武器輸出の「5類型」撤廃 不安視する国民 説明尽くせ＝竹内望（政治部）</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月16日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE9GZEtuNTV2VTJPZnNMcEpuS0QxQ0JiMGk0TkVGeGhqVGtvVzIzOEpxRXBHWEwxTi1hNzFSbkZ3RTlmdTBaZmlTMmZkX2JRRWZvRkFUczg4bFZBNlBvX1NrV19aRjRaTHV2?oc=5" target="_blank" rel="noopener noreferrer">防衛関連企業の融資、三菱UFJが慎重姿勢を転換 審査進めやすく</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月16日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTFAxaWYwemF0ekxjM3JuTkVFRDVMSTIwUFU2Y1hQdGRaR0Z2b18yajBORUFITWxiTWh6SnJKSWVXRS1LejBCNlpwRWRkOVVFT0dxWGxQbjNwNDNTRnZPdUFON0VNMkR1VHo5c3QxNA?oc=5" target="_blank" rel="noopener noreferrer">三菱UFJ銀行が防衛産業に融資 慎重姿勢を転換、安保政策を軸に判断</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月14日</span>
            <span class="source">Reuters</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMigwFBVV95cUxOZ3BzcndjOEJWc3EtelI4NDBCLWFaWWttWDRvbm01ZjlVZnVvdU1BVTJBREtiUnRfZUVlWjNXNHFwRmZ4amIxb1hFdGJtUVF2Q1lXUkhaU1MwOXFETHdWRWotSVh6UGNnT1NKYWFLVEtsZ3p1UGRWWHM0MjhLTDZLX1o2cw?oc=5" target="_blank" rel="noopener noreferrer">日本への侵攻を遠方で阻止、安保3文書にドローン防衛構想＝関係者</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月13日</span>
            <span class="source">ニュースイッチ by 日刊工業新聞社</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiQkFVX3lxTFAwVENtWFh1U1JNaVJLSHVMUjNkMzU1Z2ZiTGZ3V2M5YlkwRC1xa3pyV09jZXJ1akpkZUdpaXk1ZnVRZw?oc=5" target="_blank" rel="noopener noreferrer">無人機・AI「新しい戦い方」変化、防衛省が分析まとめ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月12日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTFBoSDlTenhkaUNnSVo4TXpabHBtVjZDOFBGaGZXMFRReDlwQWRqcVlNcjcwYmF1UHpqbmlzT0tsb29Jc1lPclJZYVdySWhhSzhfcGVua2ctSTRrbXIydXFqUTBaYm5od09v?oc=5" target="_blank" rel="noopener noreferrer">防衛装備品企業、来春選定 呉拠点 4者協方針、施設整備は28年度以降 ／広島</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月11日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiYkFVX3lxTE5PVHQxbjVYZlk5TVVhYUFvWGpHNXRiU0VLRVhKaDJQaWlCSXgtOXVWdjBoeHNFTElncnktSEdyREcxN3hhZ3lDV1hBZDhoZ0VCN0p4cU9LMGRyMkNZVzFzZmVR?oc=5" target="_blank" rel="noopener noreferrer">カナダ首相、ウクライナの防空能力強化へ３９０億円拠出…迎撃兵器を供給・防衛産業の協力拡大も</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月11日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiYkFVX3lxTE4wWi1iVmZNSXV4cHdvd28zV0V4dktqYVNFRGw3NzJEcjNSRy1UTGFMZXhteTFnMU16TU1JZDFVbF9ILUFQdE9RamFQUDY2QW43VkpxWDRvOFNuVWw0QmdzUlRn?oc=5" target="_blank" rel="noopener noreferrer">中谷元・前防衛相がＮＡＴＯ事務総長と会談、防衛産業協力で意見交換「欧州と安全保障はつながっている」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月10日</span>
            <span class="source">Bloomberg.com</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMid0FVX3lxTE5qS014c2paNWducDhmUHBzWE9CZldjRWp1UHJzbHBuUDBLOFNzeXJQN0NhdFJpZjBkUmZxQnEtSmhWWDk4VVo1eEJLZVVHSElwSnZ0MExhVElhU3FiNUNxRnBma0xqYm1oWnAyOWc2TXEtMnE5dnhN?oc=5" target="_blank" rel="noopener noreferrer">沖縄の関心は「基地」より「経済」、県知事選で薄れる防衛力強化への抵抗感</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月10日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE15Ujl3aHFHUEo3MEpEenpPeUNtdG5fTHJ0US1kZXNxUWN1djg2eVRoRmppNWdjMjlOYnd3SzZ3bnMwVXN6UVFIX3QtT2dna1loSnRrNmFqN3dPV01ZUHdxNThHYk9BZjA2ZzZ1Rw?oc=5" target="_blank" rel="noopener noreferrer">中国、ウズベキスタンに国産戦闘機「J10C」売却 武器輸出先を拡大</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月9日</span>
            <span class="source">東洋経済オンライン</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE8zb1VCZ0lFRS1PVVhIZnU0cE5WQjZJdFNxNDRSY3BYc2N4QWw2NHZTeFNjWWVjbXQ3c19PYU1YUUl4U3ROYkNMcmh5OVlIN2Z5QWdTb0w0dW55SnlGSVRV?oc=5" target="_blank" rel="noopener noreferrer">防衛省による国民の目を欺く前例なき160超の事項要求､｢事項要求｣で10兆円に膨らむ防衛費と文民統制への重大な疑問</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月9日</span>
            <span class="source">ニュースイッチ by 日刊工業新聞社</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiQkFVX3lxTE1HU3N6amZ6dHFISG9jX0t4WW0xc3luQ1NCdUxSMHZUVVFkdWN2UjN1R3RBQ3dkRnJoWTM5eXQ0NnhKQQ?oc=5" target="_blank" rel="noopener noreferrer">防衛省施設にペロブスカイト太陽電池…積水化学など、防水材一体型で実証</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月8日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE8wWVlBSF9CdGtZMl92ZDBJYmxLaFNfVGZ4XzgyNUVKN1FIVXZ4SEFreklPOHRMc3RPTEdPNFprVUxxQ1NMYVJ2N2RKRkZUUGRYczl1NEVfcE9DeXh6YVkzNnB3a2NXak0?oc=5" target="_blank" rel="noopener noreferrer">社説：防衛装備品供与 同志国との連携強化に繋げよ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月8日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMickFVX3lxTFB0aVFlbTdQUmh3Z19LQ2Z3NnVjWnRuNGhtdUUtNDh1SVNqeTZta3hrUTA1OXpQYVVtczI4NnBfcTFOVHY1aFdDalo4YkZSUkVET1BDWlY3bzNPeVNRMnBfYnNvNU04d243YU1ZWUxZQVp3QQ?oc=5" target="_blank" rel="noopener noreferrer">南西諸島の防衛力強化・南西シフトに「一定の理解」「さらなる強化は不要」…沖縄県知事選挙でも注目の争点に</a>
        </li>
      </ol>
    </section>
  </main>
</body>
</html>

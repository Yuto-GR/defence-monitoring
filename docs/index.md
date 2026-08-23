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
      <div class="stat"><span>UPDATED</span><strong>2026年08月23日 11:25</strong></div>
      <div class="stat"><span>ARTICLES</span><strong>46件</strong></div>
      <div class="stat"><span>LATEST</span><strong>8月22日</strong></div>
    </section>
    <section>
      <div class="section-head">
        <h2>Latest Coverage</h2>
        <p class="note">Google News RSSから取得・フィルタリングした記事です。</p>
      </div>
      <ol class="news-list">
        <li class="news-card">
          <div class="meta">
            <span class="date">8月22日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE9hRFhvSGsxZWROZ2M5U3BZZjNLM0VCMWVmWXAwMG95S0FOdGY2WEV6NXpLeGhOSEdwX0MzTXJNMmRkdTBKWEZfVnA3ZDlGWHpoc0UzWXBwRXFxQ0NKdFhFWVpRWmlUUQ?oc=5" target="_blank" rel="noopener noreferrer">通常は数年要する防衛装備、「迎撃用無人機」は公募から３か月で納入へ…大量ドローン攻撃への対処急務</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月22日</span>
            <span class="source">日刊工業新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMib0FVX3lxTE4yU3FocV9MOUR4VFdaOGoyWk9Ua2Ftc21GV2V2aGZTb1RtQWVPbzFnZVJGTUVFMTR6Yml1WTk1X0FXVTljV19xYU5nZ1RpQUVaRjRSVmh5bElUMXRrWE84YkJkM3lXdktPdmZTczBxVQ?oc=5" target="_blank" rel="noopener noreferrer">【電子版】渋る防衛省、首相が押し切る 韓国レーダー照射映像公開</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月21日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE5WeTFDRDRobWFWalktZTlfenhHQkwxeUFPNG4yT3A2UlBCS19MSlpHWlpIRHVwSWFUZF9KY3pmR0NfWVJfb1EycERFdENiSTYxZWx5Y0NJMXBSX1FlOXFpdWJmYTA2VEFnYlEzMw?oc=5" target="_blank" rel="noopener noreferrer">防衛省、AI指揮統制へ政府クラウド導入 27年度概算要求</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月21日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE95MGM3S25YbEowb0szdXoyRUtsVTdQbmtTUG9vbGtEZzliTzNtTG9nS1drMTNwOFNKZHlGUXpLVXlmOVpYeFBqbkNDMWxqNk01Y2ZYWFpSeldYVzRhWkk3YkUzaGpFTEdM?oc=5" target="_blank" rel="noopener noreferrer">海外製AI依存にリスク 安保3文書改定へ「国内開発力維持を」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月21日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE91Tm5XLXpkc1R5b1kwaWZWa1dOaUE5TnZ0aUNwQjJCNjFDMWRpYTZaSlluR3pGQlBNdkI5ZjVMRS1kSnNYeVZ0bGN0VE1ZcFg3WDJiaDF4VzZjeEYwYzJxTzhpNVVZYVU?oc=5" target="_blank" rel="noopener noreferrer">経済安保やAIの海外依存リスクを議論 安保3文書の有識者会議</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月21日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE1sRmtZMUgyR1djT0UxM2pCdC15RXRFY2syZ1NBLTVhWER6RzFmRVpqLU5LN0gxN051d1lBTEpMWTEydGZUbDVDWnY4MHp0dzNrWEM4bGdIX0RvZTk0ZUFPQTRoQ1JSaUkyT2NHMg?oc=5" target="_blank" rel="noopener noreferrer">「同盟・同志国と供給力確保を」 安保3文書会議の議事要旨公表</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月21日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiWEFVX3lxTE5vR0M1S1hvVjRyeENxc2EtLUs1ZFY3eGJOSDRkdy1nQ0QyY2ttWXdLOUVSZTN4X0JpQnZQRkpDYlMwVm84enRpTlZBWE5OdnRhTU9tZDJqSzE?oc=5" target="_blank" rel="noopener noreferrer">京都 舞鶴市に防衛省から新たな防衛施設の整備申し入れ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月21日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTFBFbzVJdnJtQUt0TjZ4aDktOVM1RW1JT1dHWDVpTjlkeF9ta0lLRGY1UXlDREM3YUE3dWlPc21Nc0t3b0l2QnlWRTE2ZVZJbU4yejRCQk9UdnhKb1RTZC1vQXhEdlQtZw?oc=5" target="_blank" rel="noopener noreferrer">防衛事業を再編する企業に国が出資、「継戦能力」確保へ業界効率化や生産体制拡充図る…防衛省</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月21日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTFA2TkdKUGVwZFc3WkZQLTh2cWRPNXpWQ2F2YlA0RE5jUEtuZU9iQkowSHVpZzhrWnFiOTVEVFpwOEx1SUZvUHBmcExMbUN2MnhpSUtNM2J3RmhYMWpqT01nb0YyZw?oc=5" target="_blank" rel="noopener noreferrer">日印海洋安保 覚書署名 防衛装備品 協力深化で一致</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月21日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiakFVX3lxTFB6T1pYUVk1a1owNVNZNGRYbEJQbG5IS25qZlg4emtCR05oZmlUeFZibko3RXYwTVNkMEM4UjcwWlkxVzVOT2dnVTUtNG5mNW8yRHhhcVFzeWlIbF9OMURtTmlPMXEzOWNsR3c?oc=5" target="_blank" rel="noopener noreferrer">日印海洋安保 覚書署名…防衛装備品協力深化で一致</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月20日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE8xV2RjRVV6dWdLR1BTYXJnQWFmLXlkOUNOakZiS216MnZZZVZ5ZjVwamc2c0VEakFkTm9UbUhrZTdocHNVTlUtVDlqc3B3MmpkMDllaTZwaVdzUGVUc21hLTkxTk1PVGVaNEx4akoyM0xGYzRBWXc?oc=5" target="_blank" rel="noopener noreferrer">北朝鮮の弾道ミサイルすでに落下か 防衛省発表</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月20日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE9tQnhOWVRfNzl2ZkN5YkNiUlpYcmhQUzBoMko0ejUzdlRYaFJVMUszUFdtUDlJYkUtS25VcWpVTVpDUXQ3Tk9tZ0tEeTFfUWM5N3EySmxINVFLUkJzREM2RVFub0M5UQ?oc=5" target="_blank" rel="noopener noreferrer">北朝鮮の「弾道ミサイル」、すでに落下と推定…防衛省発表</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月20日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTFBVcTg2U0EzT3BMVlBhVnVHUU9zLXlhSVgwOGpKbnNjd2xQVlBvazJDYUtYX1hOc08tMC1fTXZyUmhUZUpYRHpvWWt2VU5OMXRnYjVpRXloRE5uREFiS0RwcDA5OWhwZw?oc=5" target="_blank" rel="noopener noreferrer">【速報】防衛省によると、弾道ミサイルの可能性のあるものは既に落下したとみられる</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月20日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMihgFBVV95cUxOamc3bUxGZ2pTUnFScnZ0eFhHTlptZ01YYk1YcjF4SEg3bzJLM1p2T0htRzg1RmVWTXZHQWJNS0NQWmpWRy1McTc5MkR0S3l5WVhEeHBkXzVNTkFOOHZhQzJWQmU3d3RSbTBxYjU3ZElVMVBRTTVJSUZuYmUxREp6TnlZT21HZw?oc=5" target="_blank" rel="noopener noreferrer">北朝鮮が弾道ミサイルの可能性のあるものを発射 防衛省発表</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月20日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE1Nai12VHJCZElKaGxHd1lsSXZiaFV2MjBFbmpvLV9YUTJUSFhiS055R3ZIalRydFU0YWxkbkRHQ0ZoNE9fQ2hOc1lnOWxDSHpWR1RaeE1JUXJMeWxIazhOTE5fanBmdw?oc=5" target="_blank" rel="noopener noreferrer">北朝鮮、弾道ミサイルの可能性があるもの発射…防衛省発表</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月20日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTFBHaElSUmFBaklyTzlXQzhldkNnQVpHR1Y1X1ZlMXV2Sjl0ZVl1NGU1cVZxaWtpMEdOSC16d0JHRjZPQ0RRT1h6WG9jWXZ6cnJfS3N2WF9PMklHWGZWcWF5TEUtNi02MFNNTWlYTWpYM2ZmNG95WVE?oc=5" target="_blank" rel="noopener noreferrer">北朝鮮が弾道ミサイル発射か 防衛省発表</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月20日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE5HeWdoXzhPVlFMS0s4V1RKei1YVWZkUjl2ZFoxSjdydHoySjRKS2hnd0xOd0pvVDVQdmdYNWUtYU5vXzdMM1ptQldlczc0WGVLaHM4MFo4ZEFMTGZQQWNn?oc=5" target="_blank" rel="noopener noreferrer">北朝鮮が複数の弾道ミサイル発射 日本のEEZ外に落下か 防衛省</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月20日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE95Vko1UTExSzNUaGhLOWlIdm9LX0NJeEF3Y21fUmVMclRZVmNFM1Q0MUdGaXNXYi1DMnd2ODZlc2Q2ZV9FczQ2Y1oyYzFaMFpLdHM5cVBnVVdRQ2V1SEVEbHBtTk5rWFJ3TlUwVg?oc=5" target="_blank" rel="noopener noreferrer">北朝鮮が弾道ミサイルを発射、日本のEEZ外に落下 防衛省</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月20日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE9SMWZXdF9xQlViVkl4a2Z5MkR1TFYzbFU2eE1MaENNYlB5YXdLVHNPSHdBMS1pbG0zVDRrUngzd2I1aWRjXzVJS0lfYzNNNTJha3haLVZSdTM0MVN0YWdnS2JNcUpJdw?oc=5" target="_blank" rel="noopener noreferrer">【速報】防衛省によると、北朝鮮から弾道ミサイルの可能性があるものが発射された</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月20日</span>
            <span class="source">ニュースイッチ by 日刊工業新聞社</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiQkFVX3lxTFBYRkQyUnJLYzVTeG9tTkd4QTNwNXB1ZFg5dUIwVy1ObWRiWUxFVFBiaDNUMk1mdkp6ZHRRVlA0SGd4UQ?oc=5" target="_blank" rel="noopener noreferrer">防衛装備庁と開発…NEC、軍民両用の水中音響基盤構築へ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月20日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMimgFBVV95cUxNTElMbWtKNktzcU5nczl4YXZuR0NZYko1aEtWNHFQZW1rUVIycXlkNnVCT09WNVAwOV91Z0doZXZfMGQzYXVIQzlpekJySE5kWHM0TGh4bUNHaVZPWTRfZ3ZQc3pTbTlDbVJ1OXBuSkwweWQ5MEdzZGd1Z202cFNFUmh4V0U3WHRHWlNOV3BvekZQV1UwQVlQeXFn?oc=5" target="_blank" rel="noopener noreferrer">防衛省が組織改編、退職自衛官らの「支援庁」や3局増設を概算要求へ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月20日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTFBVZmw5dl94bURSSTJVZWdKM0pMSFRXN2F6Y1FaNndPX0Y1d0lmNVMzNkRDZU45RjlYYWI0d2dqYjJwaXFxVVdQUnM3ZnJtNHRpS3JQVGVwWkdKTE1NRTdEUm9qajROLXdk?oc=5" target="_blank" rel="noopener noreferrer">揺らぐ「平和」：武器輸出で影響強化 戦前戦後に通じる狙い 色濃い米国の影響</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月20日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTFBtRjI0UWNWcmMtODFpZVZaREZ1cDJJaWl4SGVJZ2tyZ0Y2VEUyMW9DTlNpRGw3eHpzWWUxOFp4bk1WV3otWUFEZGRxd2VtUm01cVRWRkoydHF4bUwyWnpEUkd1WUlhdw?oc=5" target="_blank" rel="noopener noreferrer">防衛省の来年度予算概算要求、過去最大８・９兆円…長距離攻撃できる無人機の開発盛り込む</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月19日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE1FWHpRajlZdWZDYUpkcC1heC02RHRNRHVzWVFtbDVIVnIxdmpjQ0NlVHlqY1AtTGxIY0VLZkdsZXMtR1B1X3dNdXFwQzlLZVd5ZmM4TEx5aUtnSlBrWnhF?oc=5" target="_blank" rel="noopener noreferrer">防衛省 令和9年度予算案 過去最大 約9兆円要求の方向で調整</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月19日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE1RTzBiejB0LUNJSERiWVFqU3pzdm40ZXpEdmJsM29TQkkzcGU5STNvSUI4WDJMU3ZNYUVCUm5ETzRnVkt0ek0yQ3BLX2oxV0hxT1FLWEVpT2xxdjQzVWJqbmROTWFYczlL?oc=5" target="_blank" rel="noopener noreferrer">水中発射型ミサイルを開発へ 防衛省の概算要求、全容が判明</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月19日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE5IWTloVDFmNTMzVHlIZkZWR1BsazZIVXl4X0J4Q21RcXluNWFpUWl3ZUJITjluTkNmdGFCTjJuMFpQaksxRHQwNmJNTGtjeXpscFBKb0RrY2NqcEpJcnhUTnVzdzc4WGM?oc=5" target="_blank" rel="noopener noreferrer">防衛省、過去最大8.9兆円概算要求へ 水中発射型ミサイルの開発も</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月19日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE4zb1BCMG1kcU9HeHpJcmxUNllERVR4d1gwMkYweDJnWGxxRFd6ZnVhd3VzRGpEWlJxdVNtMXUtQ3Y0cFZJOGxIcXA0N0RDSGdSU1I4RkI0aHlWM1J5d3BQanpuMk9LaXhnNVI4WQ?oc=5" target="_blank" rel="noopener noreferrer">防衛省、27年度8.9兆円予算要求へ 長距離飛行の攻撃無人機開発</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月18日</span>
            <span class="source">やさしい朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE9uNXFfLW9rV2RnYUJkZWtQaEZDZE9Tc1VNTl95RHpuUkkxWjdJOW5PcUFfeGhYeWtsdWRWRzhNS3hTcnFjNVBPQ1lKTkhjX0h6R0UyNUx5UEhVN2dvSVdNRGtUNkNxSEE?oc=5" target="_blank" rel="noopener noreferrer">楽天、ドイツの新興企業と攻撃用ドローンで提携、防衛省への納入を目指します</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月18日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTFBOd25JS3k2LV9rTi11YmduRU9CQ0FxOFBJQzBqQUk1QUNpbUdjZlQ3ellHM2xCQnNPb183a0N5TUlYSTRYNHQ1d2FPbkRTRzZKaEZFR0doWVphVFlwUkVzWlphSkFLTzg?oc=5" target="_blank" rel="noopener noreferrer">防衛省が最大3局増を検討、小泉氏の肝いり構想 実現は不透明</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月17日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTFAyTUJrdzJ3MG1ZM1BXNmFnSzZRRXFkTnd1Nm1YOGJFT3NnVmd1UjJqY3lwWjdZYTlIV2NSZ05iTWRXczI2UzBWcnlDNDBXaUw4OEdyZHhVeVFlYmNOREJKZUpOYw?oc=5" target="_blank" rel="noopener noreferrer">楽天、独ドローン新興と提携 攻撃型、防衛省納入に向け</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月17日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMigAFBVV95cUxQSmtaZ3ZnNTBoXzhYQ1I3QjM5QmFVdGF2QVhaeGpZS3R5R0MydUhDcHlXd19ZQlloNTRSN3VGRHcyX0I0ZlVsdEYxRGVGdkRzbEl3RkJ0UUZWM3Q0MHZPYURCV2VpbDJfRzBIQnFFNlRDLU05SWxwcnlxVzRYSmFfcA?oc=5" target="_blank" rel="noopener noreferrer">楽天、独ドローン新興と提携 攻撃型、防衛省納入に向け</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月17日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZEFVX3lxTE5uQXhraFBFNDRkRVE4d2djWGJZaV9tM3Q5SGNyOEsxc2NRQm1weHdWWjdaWUtqUDJWZjF5d3V6NURmTTB0QThuTU5tbTlENDFwaTdhbzg3bGIwdnV3bTZNaWh2bVY?oc=5" target="_blank" rel="noopener noreferrer">楽天、迎撃用ドローンを手がけるドイツ新興企業と提携…防衛省への納入や国内での量産化も視野に</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月17日</span>
            <span class="source">時事通信ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiVEFVX3lxTE5MSTc1VVgyLThGUThERGdRdm5Gd0l2LUY4ZWNaeDlza0xpR0ZRN09yVzV0Z2pfQ2w4bXBQVzFwUjltLWhvYlZIMGZEQ1dodE5aVnVXag?oc=5" target="_blank" rel="noopener noreferrer">楽天、独ドローン新興と提携＝攻撃型、防衛省納入に向け</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月17日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE14LVZpdklSS3ZqaTgta0hxbGNzVjZmVEMyOGtDS1p4cUMwM0RnaXM5U0ktNlh3MzN2TkhCQzJoZnNaTDV2bDczU1dIZ1U1b3h2TXpXT0JnX0pSZFR2OXdvUW5TbnRiVDA?oc=5" target="_blank" rel="noopener noreferrer">楽天、ドイツの新興企業と攻撃用ドローンで提携 防衛省への納入目指す</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月17日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE9FTXlkeUF2d3hQSXF6LUpHRTJtcUZkYkhRSGFSSEdoZW5fd21USzAyblFCQ0EtSHJnblEycFFLTE53UXdHYWdiMmI1a2xsZGFMbXFSaEo1cFBBVFA1ZEdIdUtGRQ?oc=5" target="_blank" rel="noopener noreferrer">退職自衛官支援庁、２７年度にも 成り手不足解消狙う―防衛省検討</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月17日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiggFBVV95cUxOelhXTTFjVWU2ZE1fLUpRMHBORGg0VVAta0pxLUdic3RKQ1NTTjBIY2dnejZCTGFqUldOeklzRVN5cXFfY2VPLXFnMTNVWUx4aEtVZVRnSHVsM2ZQY2NsNXREVDVxU3JCbXJTanMzZ1IwSlI5dVFwWDdnVDlkcl94R19n?oc=5" target="_blank" rel="noopener noreferrer">退職自衛官支援庁、２７年度にも 成り手不足解消狙う―防衛省検討</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月17日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTFAyZU1fNVp3ZTYxNldZWXF3LU12RGVJYTcwYTFmT2tuUFg3NU5lbV9DZjJiWjFhR0tSZGlFN1Z1UU5ZdnlQdlM3V21tLXhBN2pDdHBrcW1TU1dlV0xoZVp4WWs1bEtLNW5Ib0VJeQ?oc=5" target="_blank" rel="noopener noreferrer">日米同盟、老いとの戦い 中国台頭がさらす安保体制の弱点</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月17日</span>
            <span class="source">東京新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiU0FVX3lxTE1lS0RyS3plbDdNbnpka3haOUFtMHV3ZmtXSkE3dDJEUE1FTF9VNFJZaHgzeTRJSm82SEtHV0xONWJwNlhHT2t5TVk2Vm85WFUtel9v?oc=5" target="_blank" rel="noopener noreferrer">武器輸出解禁が転換点…歴史学者・藤原辰史さんは「戦争はもう始まっている」と日本の無自覚を問う</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月16日</span>
            <span class="source">信濃毎日新聞デジタル</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMia0FVX3lxTE50NG56N1gtOFpFazh1enBGQUNjUEFFZW9zc3lVcmstV3Y4TkZOU3IxcUZSOXhyY0lGdnpwSFk5STlBUVdINUJGaU9iWDdWc0RjbVVBZjdpT3NQMWoyRzJPa1FMaTBHZTExcXBR?oc=5" target="_blank" rel="noopener noreferrer">【高市首相初の終戦の日】防衛力強化、にじむ思い 靖国参拝、保守派は期待</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月15日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTFBldWp5TGdvcHJGX1BrM3NTMWgyMlR3VF9MSTZwQ05LWmtyWTZmQVh6NWtEd0stVFpDQlRNX2c4UkNwcXM3bGhLWjVSVzZIaHRFWjI1Tnl0SlpvQWVSa1FxVjFBVVZMeVVS?oc=5" target="_blank" rel="noopener noreferrer">揺らぐ「平和」：軍拡の時代に 防衛産業、活況と葛藤</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月14日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE13eS0tWUQ1ZkJsUHktNWlZcDV4d0Y3UFk4alc2dExUWkFPNVNaTThVYUhaMW5HMUhaTjhTTEhyZkpad0U3cUNvOTFHX1ZJS0JPQlk0b0EtVG5KU2NiS3lZQmJFbkpDd0la?oc=5" target="_blank" rel="noopener noreferrer">「平和都市」か「防衛産業」か 揺れる長崎が選択した道</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月10日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE0zSC1jVE54Z3QwR0NRcC1vVmw2UjZGRUR0U281cUlNbjlVT3RJTUVBS2ZvN3dMUHA1b0ZKSFBlRnhSWmNHUnBVT0RTOUVKQ0xBa3ZHREFuUXllVkhOVmR6elhic0NlWDhYd1QxUw?oc=5" target="_blank" rel="noopener noreferrer">パケ駐日EU大使、日欧安保「かつてなく密接」 防衛産業の協力期待</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月10日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE8ta3NfQ1p4dGpjT0JVTHRpSVhGZDA0WFhKbEpKOUd2V1NOSUxLZ0xBTElST2dZSUlxOVVTd1FfcVE3dkNuTjBaUmpjNnR5SU9hZ3BEOWRPdzRJV2FlREFrUUQ5NEdpUQ?oc=5" target="_blank" rel="noopener noreferrer">［政策点検 高市政権］＜３＞防衛装備品の輸出、抑止力向上に…同志国とネットワーク構築</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月10日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE5hSVhlR2pJVF9HOVhxUXVGUVljV3BuTmFacHJwcTkwOWNTbXBoQTNoNXpjR05OMG5lUWlrdldYUXZMX21SeFJHTDBWWUd4STN5LXlPRHNMQTEtcEdvblZ2SGIzWi1fdw?oc=5" target="_blank" rel="noopener noreferrer">在日米軍が熊本で支援活動開始、グラス駐日大使「一瞬の迷いもなかった」「日米同盟は鉄壁だ」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月10日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTFBPQzc3T2hramdaSDZic2VCN3dkbjRhRVZJdWVvYzBxQlgwajctaU9vYS12Sm5EekFMX2xtWlgwWG1zcE9DZWNkdTVvMWtBNURGOVgyWkZVLTFSVmtvSVBKakg3UWh5NWh0M0JvcA?oc=5" target="_blank" rel="noopener noreferrer">円安防止の日米同盟に組み込まれる日銀 27年春にかけ金利1.5%へ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月9日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE8xRzhxMkdvbDFGcks1b09oYnRfdS1RazgwWlRVUklXUTR6MTNxd092Qkd3Q0x3alhVemctZ3dJdFNuQnh6aGdfdmJ3QWEyNmhnRUcteUd2aEhva2k0MXF3cldreVNlYlNIOVpxTw?oc=5" target="_blank" rel="noopener noreferrer">防衛装備品にサイバー防御ソフト 空自レーダーなど27年にも導入</a>
        </li>
      </ol>
    </section>
  </main>
</body>
</html>

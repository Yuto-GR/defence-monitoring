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
      <div class="stat"><span>UPDATED</span><strong>2026年09月03日 14:36</strong></div>
      <div class="stat"><span>ARTICLES</span><strong>20件</strong></div>
      <div class="stat"><span>LATEST</span><strong>9月2日</strong></div>
    </section>
    <section>
      <div class="section-head">
        <h2>Latest Coverage</h2>
        <p class="note">Google News RSSから取得・フィルタリングした記事です。</p>
      </div>
      <ol class="news-list">
        <li class="news-card">
          <div class="meta">
            <span class="date">9月2日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMickFVX3lxTE9Ra3g5eWJZZFYwZlJ3c0FQdElVVHlXVjNPSmxiNXZMaXo5QXhQZVVfTE90WlpGbE1KRlpBUnZ4ODhra1duTE55UHd2QkVvT1Fwd2FuaFAwRml0TTR5bWZHaEpEeHBoNWc3MmpFbkNCVlV0dw?oc=5" target="_blank" rel="noopener noreferrer">馬毛島工事遅れ漁業制限延長要請 防衛省、4.9億円追加補償も提案 [鹿児島県]</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月2日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMi-AFBVV95cUxPZ3RqSXo3aDlLWUFwNU53YWpEbUJiaEo0bWNoR1FJeUxlNEt2ckdURFJLMlBzQmZ1YU5SMDZSdlBDOXdWaVRKYzJrNjVRYlp1RTF6bFY5dEZEc0t6U0dMWjRiYTY3dS1tWUJaeEU4ak40bjdlRmx2VnA4U295Tks0dlVPeF9rSmpCdHJZQkhvRGwxVFZFeENqV0s1RWFWRjlUSHV4LURvQ1ZaU0szZlQzbURKclJ6TC1pY3piZUNKX2VVY1hGdTJKRWItYmxXZGNMSVBmX19fNVV3ak5OUkJxbFBJdXdwR3FJTmhTMTVVZjAzaV9MMC1EVQ?oc=5" target="_blank" rel="noopener noreferrer">三菱重工とNEC、防衛分野で連携強化へ AIと防衛装備の技術融合 [AIの時代]</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月2日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE5jMXloN2drSjJ1NWV0LTdlSE5kbi14LTNQVEx2a0RoYzlvd1JGbXpablgyaUVHYnVVMW5oNDJyX3AyeDhIbHh1bW9YSlFCbGRJN3Mzd2ZHT3dhdmdoU2IwdDhVSQ?oc=5" target="_blank" rel="noopener noreferrer">高市首相、防衛力強化へ「変化恐れず」 自衛隊幹部に訓示</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月2日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiggFBVV95cUxQdkU4VzByR3Rqek5QaFh4cUxRSVVGbE93MmdUQkpRMTNZNGFjaUg0NnRBNnJXOXFaUjVOOFFlakxlc1lEbEUzOGxIWXpEVTFBcFIwUjZrbUJvc3ZOVTVvRW5Qd2ZfNzVVYWdUVzlTUHdiM05kVWdyR1V3LUhfYjQwOGt3?oc=5" target="_blank" rel="noopener noreferrer">高市首相、防衛力強化へ「変化恐れず」 自衛隊幹部に訓示</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月2日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiXEFVX3lxTE9ndG13R0NDYVhGRU82aDBJVjh0RGx0dWJjWWJJbnVwdHFYUURHZ2M2UE5DRnBBMlBGX3g0eXZJZVpCNk1ock5vblA4TG95cEtvRURSWmtfQXlZUGJW?oc=5" target="_blank" rel="noopener noreferrer">（社説）防衛省概算要求 現計画の検証欠かせぬ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月1日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE5CcFpNdTBtVkdLU05VSWhlZ1pqb3g3dDVWTUZhVmlGUnZEQmp6LVI2Y0lwWkllU3ZLLXlOWTk5MEFtQ0t0OW1jWTFzbHJQNVFGTzZDcmpoUTZEbEZXUDlWZms5VzRBQQ?oc=5" target="_blank" rel="noopener noreferrer">防衛省概算要求 「新しい戦い方」備え 過去最大８・９兆円 ＡＩ・無人機</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月1日</span>
            <span class="source">日刊工業新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiWEFVX3lxTE1IbE5OWGRhTWxYbEtnZzVPRUR2SVVPczZkSGxraEtrRnAwTzcyVWhCT2ZLU3dhQnpaLXhKT0NJeG5CeVFJcEI1ZVdvOWlDN0hhOU51bmNQM28?oc=5" target="_blank" rel="noopener noreferrer">概算要求2027／防衛省、AI・無人アセット重点 総額9兆円</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月1日</span>
            <span class="source">東京新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZEFVX3lxTE9saTVwMTM3a0NoUGFKd1ZiX1lqa2lDd1pmQ3RxclYzdUxwNjgwc09FTVNfYjl3Rnh0ZEJEQk5VZ1Uzdm5vN3Y2RHMtdkNaZDJZRXJ2SGpjSlRmUkdNZEVuLWt4ZlM?oc=5" target="_blank" rel="noopener noreferrer">防衛省が描く「AI活用」、指揮統制部門の支援まで広げる方針 海外では多くの命が「誤判断」に奪われる中で</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月31日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMia0FVX3lxTE1kNlM3NFlxRzBHR1lsZzVBTWRxbzF5YVhmM2JmRW9PU3c2bG16VmJsZmtaQjRnbHlpclRKOVZZN3BRRG5vTzVxWXlxMXVNZkRiOHluVno2OHF6TTdkc2JEZF85TXVIZlU0N0ow?oc=5" target="_blank" rel="noopener noreferrer">【SIGNATE】防衛装備庁主催のシミュレーションコンテスト「第5回 空戦AIチャレンジ」を開催</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月31日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE13T2h0WjcxMnFvNHk3dkM0UUdVb2wxRmRrQTY2dkdjSUJjWHY2UWlKVy1SZmk3N3VhSW5MWGtsQ0pNVTFleHlGYnhXc0F5MXg5VzUwWS0yV2JxQ09PQ2s4?oc=5" target="_blank" rel="noopener noreferrer">防衛省 来年度予算案 過去最大8兆8900億円余の概算要求決定</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月31日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE9ua09QdWZvRFlJaTExbjdHTUhFMm5YNHlZYnR6RV81RWdlZlZQOUdwWkZOcTN4dmprTHM2M1dpeklUTTJ4c2lFT2NFdzRVTGlkRUM3c0ZsVGlPZF9DaG1XcXF3WUFITUc5OUJ6Tg?oc=5" target="_blank" rel="noopener noreferrer">防衛省の概算要求は8.9兆円 事項要求で最終的に上振れ見通し</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月31日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE9tMGt4MkF1NE9sUjZIZGRWRDZxMjBHUWNUNXBiV3ZETTFnNHhScEEwOHF4eFpwdkhVc2p1QnphQlB0RW9aV2RENWpwYXgtQlNSb2xZLUpkUGt3bDZHWmxwQWFkVWZVWVk?oc=5" target="_blank" rel="noopener noreferrer">自衛隊の指揮統制にAI活用、多様な無人機開発も 防衛省概算要求 [高市政権の安保見直し][安全保障関連3文書][AIの時代]</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月28日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMipAFBVV95cUxNcm8yb2pHM3ZiVmJGSlhHTDdKZzR6REt1bXhkRWYzUV9ZZ0tqR2xsT1VkUkZ1UmZka1BKSnhMTW5PT2NjUXRRQTlpLW0wWTdNNkFXZXRLTUVQVnhXT3pvdE9pTmF1WF9qM2hOYkMtVlJWUjBZRS1QX1lOcVlFRDliWEh5M2VMNHBTVG82V21zN2drUWJVd0JDSVhWbWhqUjNDZm5IdA?oc=5" target="_blank" rel="noopener noreferrer">防衛拠点整備へ防衛省が土地を取得 広島県呉市で無人機など製造案</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月27日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiggFBVV95cUxOMUk1dV9LM2xFamdScUZWSnhMTXRqT2ZUWkp1X3Nxc3ZXTDRsdGNLYkxPZEFCcjhISkpBdXA2bFJSdDY3YTVGMXF3c0E2amc5V1RaM3I4eEd6VFBfT3RmeFpNMkFQTnVwUmV6Q01wUzJSVWZIQjV0Vnd3VUlEcFZOME5R?oc=5" target="_blank" rel="noopener noreferrer">防衛力強化反対に高市首相反論 障害者団体から手紙受け取る</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月25日</span>
            <span class="source">日経クロステック</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMickFVX3lxTE44RlB6MVN1bnhmRnVhT1NuaVJtZTVJYy1oQkNUV2RGbFd5ekgxRFM0d3RmVDFZNE9CbTJPSV9WdUtmUUlZQmQtQ0VQRzlYTFJCc0Q5WkRjS3BZcDNTaTA0a29JdzZaaFZNMExHQkFjMVhnQQ?oc=5" target="_blank" rel="noopener noreferrer">防衛費増で増える防衛産業への転職、40代で年収増の事例も（2ページ目）</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月24日</span>
            <span class="source">日刊工業新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMib0FVX3lxTE54UExBeWR2Q3c3emtvTERwcE0wU2FMR3NuYkw2ZXZwNVNLT1BjODk0cmZPUl9ETV95a1NibXFnY1JZUzhDeEtGUXlMOEIxM1RNMUV5QW5sazYtSzBzY1FUSDMwcHVGaWNpWGhPeUlORQ?oc=5" target="_blank" rel="noopener noreferrer">主張／防衛装備品、官民で情報共有 JISDA最高経営責任者・国井翔太</a>
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
            <span class="date">8月19日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMijgFBVV95cUxQQzhlSGFFMjFSaHlGbjNBNUZEdmktOGpsMlJzNUdobzFyRVFubHhyOU1DbFpfR1FtNzdSdk4tNTM5MzAtSlg1eXdPZDRTRHMxOTNTaXlYWHJpOXRVQkZ0T3N1b0tqLVVlenNYbWFyZ1B5N3JZcFZ5Z25vQnlJQjBwNU1DMlR1ZGswSm9IYUNR?oc=5" target="_blank" rel="noopener noreferrer">防衛省が組織改編、退職自衛官らの「支援庁」や3局増設を概算要求へ</a>
        </li>
      </ol>
    </section>
  </main>
</body>
</html>

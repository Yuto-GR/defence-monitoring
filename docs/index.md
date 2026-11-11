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
      <div class="stat"><span>UPDATED</span><strong>2026年11月11日 16:38</strong></div>
      <div class="stat"><span>ARTICLES</span><strong>63件</strong></div>
      <div class="stat"><span>LATEST</span><strong>11月11日</strong></div>
    </section>
    <section>
      <div class="section-head">
        <h2>Latest Coverage</h2>
        <p class="note">Google News RSSから取得・フィルタリングした記事です。</p>
      </div>
      <ol class="news-list">
        <li class="news-card">
          <div class="meta">
            <span class="date">11月11日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE5Fa0VQMzZuNWwybXRyX21mYVd4NVZ3MFlUbEN4bU5PVEVfQUJDT1JGa2RJV01OMXVLTXRXWkhEUThCRy1XSkg4UGtwOXdfdHRHMmNrVnBnVWlTSGp1OVo3c2ZEYw?oc=5" target="_blank" rel="noopener noreferrer">有事に備え防衛装備品増産 政府「国有民営」推進―安保文書改定</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月11日</span>
            <span class="source">信濃毎日新聞デジタル</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMia0FVX3lxTE5VQlVYaE9BaUNaN3VKYmRQWC0wY0Q5dWpTOHUxd2J3Z3RMVGxLYW9CZnh2cTBGdUpwZEJNbFFiYmVwaEoyVkE5bEFvT0pKcnByeUFZSmt5TzJhcUhDWGlYbWZQa3o2YTJCblU0?oc=5" target="_blank" rel="noopener noreferrer">自民、原潜の保有検討求める意見 安保3文書改定、核共有の議論も</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月11日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiggFBVV95cUxNUHNGZ2JaVWtsaVN0WnVVaHRnNEJPWmw4NE1INnZoS3R0cEZRR2J0T3NiY2o1M0FVcWxIV1BPbmwyVjVnQVJlOUVLTHpjaWRMeDVUb3dhUnFkR1p5X3p4UGM3MXdkRlRINGFibllYcHVMWDFFVHI3X1JpU3FxUEdVWXV3?oc=5" target="_blank" rel="noopener noreferrer">有事に備え防衛装備品増産 政府「国有民営」推進―安保文書改定</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月11日</span>
            <span class="source">ニュースイッチ by 日刊工業新聞社</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiQkFVX3lxTE1kb2dEamJXYTRzNlNYS2dvejBPNjRIRkRVSy1US1h6eU44ajhDN0Rpbjh1MjIyTHJTVmVXeGRvdlJZdw?oc=5" target="_blank" rel="noopener noreferrer">受注額は５億円…ACSL、防衛省から小型空撮用ドローン受注</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月10日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE1ocWkwcmdBMzVEd1dCaHZqanpobnNGelpBNnZEUm05M0dNUGt6dzV4ejJfbXZ3WWNqOUVBSk81OF85SENvaWRvcHlXZ0pWTkJWbU1lcHNhR01oSmZLaEh4dlRKY1FjVjMtOFdyZw?oc=5" target="_blank" rel="noopener noreferrer">安保3文書に「核持ち込み」の例外明記案 非核3原則巡り政府高官言及</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月10日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE1sUDBleG80VkxEaUxaOWtiWnlqRm9BaHFUS0dwVE1fbzhqTFZRbXRiUnFjR3h0TGljM3lXdXRWSDd3VFBHUklMMy1NR0J1eVUwUzVnLUN3b2laYk1mbGFOUk9Cb1ZoakxTVV9PTGlMbmZrelNTSEE?oc=5" target="_blank" rel="noopener noreferrer">ガラパゴス化の代償、武器輸出解禁も遠い世界市場 販路拡大へ「専門人材」確保待ったなし 岐路の国防～防衛産業の今</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月10日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiogFBVV95cUxNVDV5a1g4N1QzQXl2eFpkWHFBZEd1Z1dhbzg4cVZmeWppSUFjYnJXMzRNMVlXT25aVXhLZ3hEWDZaa0ZzcTgwbjdrSTUxM1ZKVnhzQmdXTEN5aWVkQlFVRXFacVQ2cUJBLU4tNHl0T1AtdDhnV0h4RENCRjVBdmdaNVRJTnRRNzZudWlzc3hhbGFXMmdiSHJXXzEwM19MNlBaSGc?oc=5" target="_blank" rel="noopener noreferrer">ガラパゴス化の代償、武器輸出解禁も遠い世界市場 販路拡大へ「専門人材」確保待ったなし（写真・画像 1/1）</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月10日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTFBHeFJXNUZmNV9vTWxTVW9tV0hxR1BnT0NiNFhJOTdsYm44TmdGd0hKX2RnNFhpM3JPdy1mV2NMR0N2bE5rY1hBeXhwT0dTWjRMU3YwN0dWcjVfWEh3cG1PUDRuVThjOEVpMHlLamxwcU9BTnl6Unc?oc=5" target="_blank" rel="noopener noreferrer">自民と維新、原潜と非核三原則で隔たり 安保3文書改定へ協議開始、官邸意向も行方を左右</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月10日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE44RVJrMkQ4cU5HdHdaVGN0ZFROQXNBTkZTeU5DY1V3OFZueEh4QnJNQnZENV9zbkVrd1BBUk55elR1cXJVSFFSNjc3cm45LWJQYjFXZDEzQ0xwVzVIcjR0akJoNEJDTEFW?oc=5" target="_blank" rel="noopener noreferrer">激動期の安保：政府、「拒否力」高める方針 継戦能力など重視 安保3文書改定</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月10日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTFBLcUlkM25KNzlGNk5UYVhDdVZ6d1lRbzQtNm55VGg1d1VvdTRNem5WcTBYNDZidGJKOXkzTWliV0pQSEtGVjV6R3RHZkJ2Z3NrTzdGUjllVi1QQjBVeno0?oc=5" target="_blank" rel="noopener noreferrer">安保3文書改定 AI活用への政府の考え 海外事例や懸念は</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月10日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE5HdVYyVExscFFZM0U1ZmNjampmTWtjZ2xRZTBYQU5aU3J3SDlIRjJjbFNpeU5Zd1E5emhmTS1jRXZaRlBZVHAzOE1yNnZyRDFmLTdmRGptUVBBZDRSU0VhdzFpaldzd2J4OEhuUg?oc=5" target="_blank" rel="noopener noreferrer">安保3文書、侵攻抑止へ「拒否力」明記 対中国で米と戦略共有</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月10日</span>
            <span class="source">東京新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiU0FVX3lxTE1pY3VpSmF3TzBVM1A4cGdNQU42ZFhCMWZsZXpwSWxrSi1lRW16UTBoUWowZ0JXMjJVLTJfQnRIV1l1bElSbXRyREdSYS16OFZ3clNR?oc=5" target="_blank" rel="noopener noreferrer">どうなる非核三原則、原潜、防衛費 自民と維新が安保3文書改定をめぐる協議を開始</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月10日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMijAFBVV95cUxQNzdSeW5kekpkbjVETGtGX05VOHhjLWthMHpRTjdiYzZyV3JwemxDVkVmbDhyVVk1VEZ3a3ZnbWVqN29nUGlUU3hIMFRrUVBrSk9rVUZ2N1I0YkFESVU1YmZwckZPd2xwOGNKX2pBVGdDSW04UGtENmxtYUxZdnBCSDF4bFZoV3VzUjdfYQ?oc=5" target="_blank" rel="noopener noreferrer">＜独自＞安保3文書に民間力強化明記へ 自衛官減少見据え委託拡大、企業や退職者を活用</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月10日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE00NHl3S2loRUt4dlg3RldrNTBKYm0zMmhOMHVBbFA0UVhLS1cwdml1MGNPcHA0MDVIblNpZ1d5YmFzZkZXdUFqMkpadnI5WTlBOUdOVllNZ3pjSExoUkF5RXgyc3FZT2U1?oc=5" target="_blank" rel="noopener noreferrer">激動期の安保：最大の焦点は防衛費の増額幅 安保3文書改定、80兆円要望の壁</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月10日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE1iajdGanU2R192SXdzOXlDc25wUGhCaTNDNkVhZUx5QXZIZmE4NnJuY1VUdW1PR1J0b3Y0U1JZYVAxRjJrQWd3ODFyLTA0bHZRb2hZWURUakhXYzUyZTNBdmZ1RjJybUh5?oc=5" target="_blank" rel="noopener noreferrer">激動期の安保：安保3文書改定「原子力」明示の可能性 原潜導入に山積する課題</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月10日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE5KazM0TDBZNzNHZ09VM2hfUmU4Wk5tNHhZdEpUbmpXMW1SZG1wS3c5OE5pcWRoejJDYkRNZ2ZuZnNFX2RUVjVMeC1iMXp2WVVaalRjbFR1dVhCendoT3BkbkYtaUtKSk1TLTFxVHBoNmdVazhVLVE?oc=5" target="_blank" rel="noopener noreferrer">防衛省ファンド応募が過去最多に…軍事研究の推進は平和を守る 論説委員長・榊原智の眼</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月10日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTFBJamFtRkIzUXI1UFB1MEljNGVDZmgxY2luOXA3WlduOC1udm9kVHU4TE81MFFERE5kMmV2dzlDRzBqTFhaMExIVHpGakRFQ1FkZDZ5VEJDOTIzXzBNanpTVmRPOG54OVU1?oc=5" target="_blank" rel="noopener noreferrer">与党、日米同盟の強化で一致 安保3文書改定へ実務者協議</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月10日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMijAFBVV95cUxQUTJNYXlZSkJpelMxRm9yR0tDY081eklRTXFRNkFVTGlzRFVhbzFwR2tKRV9DaGFuSlRBY2YzaURlSThnaVI0UU9PNXBib0NBdG5PRmlDa1RMOEFmTEp1b1pRaTRYcE9jaDRmeTg5WVNMU1NjWjladzRhUS0zUmQ2M243RlBqTDR4MlJLZg?oc=5" target="_blank" rel="noopener noreferrer">安保3文書改定へ、自維与党協議開始 日米同盟強化で一致「非核三原則」「原潜」など焦点</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月10日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTFBkd2ZUdUIxa2NnNGJkUXVoek5JY3RxcUppeVlpUFFPRnNVenhvYnhCNVloWlA0UHZ5Ti1RVXNDMXNWYk9SZmtBQkNIU3dKM2xJSmxHYm9ObmExMXNNN2dJ?oc=5" target="_blank" rel="noopener noreferrer">安保3文書改定へ 政府側が防衛力強化の方向性を示す</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月10日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE5IcjNtRTNpeUpnQjNlT2NrbmIxUzZUZjFsQ3hxRUZCaDFLUTJnQkNvLUExeU9PbGRPMEFGTFJYWDVCZjZPZWNfYzUtdHlCS0hnRHpKRzdJaEhZWDJubjc2T1ZRRHZzRFBf?oc=5" target="_blank" rel="noopener noreferrer">自民と維新、安保3文書改定への実務者協議 与党内調整が本格化</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月10日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTFBXaXFBUHd6Tjg1NUQ3ZmZpcU11bWxqM0I4NHVQQ1hBNkxER1F1akh1SVd0UVFsS2V5SlpLTk9DaDNnU3VnRmU5cXBYcHVrLVhtRXh1dW84RXRUaTl5ajhWaFRRVQ?oc=5" target="_blank" rel="noopener noreferrer">日米同盟強化を確認 中間選後初の外相協議</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月10日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiggFBVV95cUxQSEJVdnFuQmNZN0lZS3FGbGhOd0YyNDQtVENpTlhOV1JEUE9YSkdRY0E1UTR6cU52MENKOGNqcHZKUUpDUWpkZVhVNzZlWEFvZ1Zoc0lzeXF0MG9xWGh4V1o4b29GVW1iWUlfdWJvWkxXcUxHRWhQRWpXXzlwTVpmSzJR?oc=5" target="_blank" rel="noopener noreferrer">日米同盟強化を確認 中間選後初の外相協議</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月10日</span>
            <span class="source">Reuters</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMigwFBVV95cUxNOE5JbmhwV2YtakJySjFZdDNRbG5JTGtCb0t3OFlnOU5tS2J5TEIxaHBZNWJSOUpLMTdVTXdLLXhDblZRRDE0RHFnai1FZTJoemNmckpyd0UyZ1RueVZTYlNlT0VUWE5taTJhbEd5NnRILV9ka0ZVMEdJa2FNMm5kRm9QQQ?oc=5" target="_blank" rel="noopener noreferrer">自民・維新が実務者協議開始、安保3文書改定に向けて議論</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月10日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE5ic2ZjakJ1Q000RTlWUnhCV0d2cjBTXzJKazhETkE1ZmJtMlFhV2x4c01oOUhtbXZTWHJVMkdTYmlXaHFqRDlQUDFmeFVjTHkxbEpmUG5VY2JJQUlLS3RHZTlKeThyTFBETERqQzZQRVVua2NMZmc?oc=5" target="_blank" rel="noopener noreferrer">自民と維新「安保3文書改定」実務者協議 「非核三原則」「原潜」が焦点、調整本格化</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月10日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE8xcFYtQ2pLT2I4OUJMOVZFYk9rcjAtTDFrdjJlWTFvVmoxdFcyRkRfVUg3Ql9KSlpBdW5OXzZ3WXkxZDhPOWlMV0YydktxbFJ3NjRNMXdxb2JxWExEbHN3UXdQM2pGSzVVaUd1Q20xRFlocnRCNUE?oc=5" target="_blank" rel="noopener noreferrer">武器生産につきまとう根深い「評判リスク」 国際情勢直視しない軍事忌避の風潮なお 岐路の国防～防衛産業の今</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月10日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTFBmNDRqLVc1RUxhd2JNWUJWLXhsUXREWEZSZlVDTDBDQjFCeG5YMHA2ZWRDTVFTbXp6MXc2NzVOTlh2VXlqY2dEdHoySHFmV0J4RUpYdnVKMkxabXpiaUlLcjhVRFBLZE0?oc=5" target="_blank" rel="noopener noreferrer">「ブレーキ役」不在の影響は 安保3文書で自民・維新が与党協議へ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月10日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiekFVX3lxTE5neGVndW5UMXVJVURZNXdTOGtGODdua0JfeDFtcl9ZVGQya05GQ2huTWgzcmEzemNFZEtMd2FvRmhDRU9zakNZZmstaFh2Mm9wR1JBRjdTeUcxTDVRLUN6S2NoWFZZZTdOckJKX0I0RGFSbWJsQ0JpaHZn?oc=5" target="_blank" rel="noopener noreferrer">防衛省、AI活用の基本方針改定へ 「AI主権」盛り込む方向 [AIの時代]</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月10日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE5mSTdNMzk4VFdiRGtHY3UxbWhrNndPR3JUOTVrTUFYN3o0d18ydFEzNUQtbHBUdC00eGpjSzQweHQ5bGNfa1V1Mm9WNFZfTUNXRnhodUY3TEVFUWJUT1dTWkZmTQ?oc=5" target="_blank" rel="noopener noreferrer">比に沿岸監視レーダー ＯＳＡ初 完成防衛装備品</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月9日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE8yR2VuTEIzaEhDWG5WSVZ4ZWtEbWFCb0VTYXcwMEJxbGplUkk2cHFYUXJnUDM4TjBSWHhGeEZ1bnhBTmxSM29HQkJwT0dqWXJCajhNUmxCekltaS1CWFhuSm91d2xHZWdKd1JiYzhDM3JKM2FVc0E?oc=5" target="_blank" rel="noopener noreferrer">防衛装備品の技術協力巡り協議、日越防衛相が会談</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月9日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZEFVX3lxTFBIOW9WZGpWb2ZfSEV4OWhMeXRJSkxUaU5DZjRUWU1NNzBDdF9kaUN0d0FpcHg4SnhkOWJqYS1YVlVZVFhjLUNiVDRRVGU3RnprbnNrcndXVjVKbmpjT0lGVjZoWjQ?oc=5" target="_blank" rel="noopener noreferrer">画像・写真：防衛装備完成品を初供与：時事ドットコム</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月9日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE5abDFkbU5tMGk3Z0lIY0JFemNyWG1hRURkUnE5aWtNcURSRFBnUl9nblZSbFFuZHY0eWpMeUgyWFFkVjNJREIzcnh0QW5PaTJrNWtTdnpUWXJLcnd6Nl90YUUwcGZVd2FF?oc=5" target="_blank" rel="noopener noreferrer">フィリピンに沿岸監視レーダーを供与 OSAで初の防衛装備移転</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月9日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE4yemxIV1QtY2VyVzBCLVhJcUtDdlpoQXBzLXhSakxKQjBnM0FMUUJqX2VYczF4RWNraGFQeGtobnAyT0Z5RDREY3daOFRtbnk5XzdvcWk3UGIwWmtSMVpHdjNnQQ?oc=5" target="_blank" rel="noopener noreferrer">防衛装備完成品を初供与 政府、フィリピンに監視レーダー：時事ドットコム</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月9日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiggFBVV95cUxPb2JaT3Nqb1I0eHdnM3pMNTNRVDU5RW02bDhRLWNsMkJNbzFyak5DdG5IS2ZHeVp1VUZtMXA0RG0zQ0x2NE90NFZycjJnVzJpaFppZzFab0pqMkkxbTdBNk1oTVZaY1pjeUpFbXY0WWdycHRqTVpSeWFGVHFyVW00ZnJ3?oc=5" target="_blank" rel="noopener noreferrer">防衛装備完成品を初供与 政府、フィリピンに監視レーダー</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月9日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE8zc244N1VpekE4RTFxTEhMR0h5UWpxQ0F3ZzIxMFJuOGtkQVlWckZOenhHVlV5ano3dU1veXo3QlBhOFJFYS1ZaHk4cUUzUWM1REVfa2t2WDI2M2t6aWZ5VFNlV1VCZ0E?oc=5" target="_blank" rel="noopener noreferrer">フィリピンに軍用監視レーダー供与 OSAで初の完成済み防衛装備品</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月7日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTFB0RVRJNFlNOUlLdjZXZVEydmlRSVZMNnpGYnhmSFVLcGIwZHhobVhjMll4V2pUbDNlU3Y2cjNTZzNJQkRsckwtMWVRZXNDOE1Da2huaFZ0VVl0bmZpTWtUV0dzeFprMzQ?oc=5" target="_blank" rel="noopener noreferrer">安全保障、夫婦漫才で政府広報 防衛力強化へ国民の理解拡大図る</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月6日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE1zT2ZWWndyVlktU0dyaDBwaTl6QzBwck5aN1VFaTRUZVB4WUI5WFcxSnNUb3Q4QWM5SFByUDNvNHNKQVc2YkpVTzB0czViaVdsWVFFdjRqOFdVbUI3d0JGMHlnaW5PWmxzcUozRA?oc=5" target="_blank" rel="noopener noreferrer">今夜のNEXT トランプ氏が狙う「外交レガシー」と日米安保の行方</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月6日</span>
            <span class="source">東京新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiU0FVX3lxTFBxbGFVWTdxYnJWWDNmQVNPNHNYbHByV1Rvc2l1ZzdnZHRmOUpkUTJyZnlReGMxWnZyVXBMOURmYms3NTdHTXBZMGgwSHAxMEdPUU9B?oc=5" target="_blank" rel="noopener noreferrer">安保3文書改定で防衛費80兆円超え？ 「国力に見合わぬ軍事力増強は国を滅ぼす」識者は警鐘</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月5日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE9wazhyN2JmTzhmSExnUm0taDdQTkFvNENkdnNtOVFfQldTLWtfNlJqM2RlUjFjWU5hZVhJS2x5N2l4S0lRUTRPQTVaaTZvTDltdWhxSG04XzFTT0JaUWtB?oc=5" target="_blank" rel="noopener noreferrer">財政制度等審議会 防衛力強化では安定財源の確保を</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月4日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibkFVX3lxTE80Qm5DZjJud21lTDBHaDlIblY2NFJmNHphWFYwN0hlUWRDMTN1Uno4N0E4YlZ4dUZBUEJXTUF0bUltbUJtS0ZSaW5yUFhnOGJfdnBZWFZvX1lKdjA0ZnZvTkI5V1BpTktxVGFYbURR?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相、赤沢経産相が防衛産業と意見交換 産業基盤の強化めざす</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月4日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE0zS2hpVVN6RTlRd2JCMFFTNGFIMU1jekY0c1pHdnpIZHBIYUtPMi1ZVWxoV3FoY3p6dlktWGJfaXlMSE9uX3g0U1BtVi1BT1FuTnI1MjNBR01scDBaN0VZ?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相 防衛産業基盤の強化に向け企業に協力呼びかけ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月4日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE1Ta1JoaEF2REdwU3FncVUtbWo2Z2JKVUdKUUhubEt6cGo2UmFfNjBBLUtzaC1lUTVPSUtGRUhLV3IyWGtvTzdwSDBDN3FESjZRTWFPN3B5eTZ6a3lGRU5MM05nM0dTY210WW5qZw?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相、防衛産業「有事見据え予備生産力を」 新戦略の策定で</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月4日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE5zQXBFbXBiTlE5VUxjM0FfaUU3NndpVWZXMzdIcmRIblpFMDU2VThzWV9BRWlWYk5aYi1zcmpZQW1xQS1GOWJINTJ5aUczbmlJRk0yMzFwQVJvNXdSYUJESHZpV0ZKeU9s?oc=5" target="_blank" rel="noopener noreferrer">激動期の安保：無人機市場に「黒船」続々 防衛省が40億円投じた6機の実力は</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月4日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE9aTVNTNzlYRWdWbFpMS0V1NjhaLTlSVnd2S2c2V0hpZ1dkUnU4bTRYVVJGYzVVLXl2cTJpbFFQNHJYM043azBYUjI4bERsY0ZLd0FCNXFoczNPTlZtUUxDRk8yeUo2N2NQX19kSw?oc=5" target="_blank" rel="noopener noreferrer">防衛ドローン競争加速、スタートアップが変える日本の防衛産業</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月3日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTFBUTXA0OGZLZEhXRkxHdERUVVZqNVYtcnhiQ2NHYjF1Ul9RV3BmYUlWM29yUEUxY1RRLUZ6ZUJHTE1ubXE4MlRvOXQ5SVBuWnZoODFvMXV0S3JzS2ZUMWtJ?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相 防衛省のAI活用に関する基本方針見直す考え</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月3日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiXEFVX3lxTFBpUTE5UnlCSklHdHNGT2U0c2hXVGZPTEcxLW15elRITndRRmZTZkNiRGs4Q2VUMHF4TElkSUtHUzEzTjY1ZG8wOVZTX3A4RHJvU2ZGak1nWWxJSy1T?oc=5" target="_blank" rel="noopener noreferrer">武器輸出へ政府前のめり 「何でもかんでも候補」自衛隊不満も</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月1日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMijAFBVV95cUxPY0trTUIxN1dUNVI1aUdRQ0NSTGJpd0lFbkFjbld1a01tNnNVR1dZSTVFRG0yNGZlTVh2VUlyY3oxQWFrMEdDWjFqdnNGZDBhd0VjdXdzU2xEVXpIRm1fOGhic0Nvem5oT3g4S3I3djd2dGdDcUNOdmdwNmxQOVFzSDMtTG1paUJMaHdGbQ?oc=5" target="_blank" rel="noopener noreferrer">防衛産業強化へ新法人 防衛力の持続性確保図る 産業基盤戦略を年内策定、財政効率化狙い</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月31日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE5BeS1DR0Z6cGR1dWxwbFpMOEs0WU1tM2ZWQ1l5ancwd01OOXg5YmgxLWkyZGVnYUJFY2RQMmpObF9QUVE5RG9HYkJoNERZa0NBYnl2Q0tJRDUwR2ZVZExj?oc=5" target="_blank" rel="noopener noreferrer">安保3文書改定「防衛と経済の好循環」を重視 新法人設立も</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月31日</span>
            <span class="source">東京新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiU0FVX3lxTFBNUkFfOTRUTDNJTzNhTm9ITHlDVWV0VHJqRHRUZ2w5NkdnbktndEpWN2hXa0x0NlVJU3FVdnZmbEFOYzl0ZGNJbTBidTB5RkhWYkV3?oc=5" target="_blank" rel="noopener noreferrer">赤字路線が「防衛インフラ」に？…安保3文書改定で明記の案に透ける「国民生活の軍事化」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月30日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE9uZHdpbURBM2xzRVZqV2ZiOGhmTUZ3ZThXTHhYOVFfSy1ueHlPdVpWOFhfRnhkWHotMEJ4dEdYZm0xUm1fbVJOb0RkS0ZMdmRRd2swVVdtTU5kbkV2VWZHdk9LdnIxWWc?oc=5" target="_blank" rel="noopener noreferrer">「イケイケ」で売り込む日本の武器輸出 足元の自衛隊からは不満も [高市政権の安保見直し][安全保障関連3文書]</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月30日</span>
            <span class="source">日経ビジネス電子版</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE5zMDI1NERHT2s1azJEb2d3TE5EaGxuT3FFZUR6WW93UHZ0em42VlZ6V2pYVVMzU0Q5aWw4WGVUdWJLZUxwX2c1bzgyamxjTDNEUUd0NzdJaVFmUQ?oc=5" target="_blank" rel="noopener noreferrer">「新しい戦い方」が呼び起こす防衛産業の地殻変動</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月29日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiU0FVX3lxTE5keVAzOXFIWnNqLUZHbkdqcVJFQWxnRjNNMkQxLWVPMmx0NE1qb0tUYUZhOFVKY212WF9BX1BWbVlhWWM0Z3NheXgtdHFWSnVOZWI4?oc=5" target="_blank" rel="noopener noreferrer">EDITORIAL: Universities must maintain a strict separation from defense research （社説）防衛省ファンド 大学と軍事 危うい接近</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月29日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE1FQUdTeUI1cjI0YlNBbnc1RVo1QkpUcHlaR3JzT3BkUmJjWlhaTmVja3c2QnoxbXc4emR5MVBVXzFuMDJHNk9RazhENGVlWjdHMXVhT1dZUzA0aGRETmcxS2kyaHJWZw?oc=5" target="_blank" rel="noopener noreferrer">【速報】防衛省によると、北朝鮮から発射された弾道ミサイルの可能性があるものは既に落下したとみられる</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月29日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE0ySUc0SmlvYXJhWFpBdWZFQ19QUEE1SVU4QVJLVkFTTnI3WEhFVEhObi01cmpiV25rS3lrMnBZYVIwMUZ3WWxrRmlybUNLMTdveFE3UHFZRllYYVE1amlUWGp5SlBnZw?oc=5" target="_blank" rel="noopener noreferrer">【速報】防衛省関係者によると、弾道ミサイルの可能性があるものは日本の排他的経済水域外に落下したとみられる</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月29日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMifkFVX3lxTE8xS1JFcXN3ZWNSWjlHdlpDNFZLZXNtZE9OcjhrWmNJakdfZFh3RWFKUi1Yb3ktQV9BUElyTTVaQ1drSjlYMUU2S2NOWVJ5dzIzOGFqb0ZyZjZpX2V3OHNqR0ctQTdCbm41ZTM3S1dSWXVXcFVTSFlqQXlXZnM3QQ?oc=5" target="_blank" rel="noopener noreferrer">370兆円ノルウェー基金、防衛産業に投資解禁へ 大旋回を探る - 日経ヴェリタス</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月29日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE5XRG8zcU1MeXFsX1BTQnpjNlV5T25pUS1nWVdoNnphazM0YUNUTDNhZ2k0M2R6ZGZubEpiV1Q4QUJUTmZiSUVTenk4YjQxUTNYUEl2dTA3WGtRVXRsYkdXeHpmRmp0RFk?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相、防衛力強化も「専守防衛は変わらず」 フィリピンで訴え</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月29日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiXEFVX3lxTE1FRkoyeE84MkNQMG5zYmJQYzJMTzF4UEVNSFJPVndtR3VKVEJ2MmlqREZGM29nR01qTTEtNEg4Y3hzMXI0UjZMQlBNYnZ0cl9ZcjJjX0ZKLVItWVlw?oc=5" target="_blank" rel="noopener noreferrer">日米で防衛力強化姿勢 中国念頭、歩調合わせる 防衛相会談</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月29日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiakFVX3lxTFB2Y1dPS1FDMWxhTGhxcDNxUTcyb2tQcnFaQm43cndvX3N1Z21KOTRKOEN3UXU1UllzNFF2TFlybmZmbWphTG9faTBlVlFBYXJNTVgtMXBRcU12YWNOemFSVWJ1cnRnc3pYS3c?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相、防衛力強化も「専守防衛は変わらず」 フィリピンで訴え</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月28日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE9rb3FCUlNGSHBVNlNvWS0welNPTVRuZmItdFB0cWZmeW9fWEZkTzF6SDdiN3JIQzVQQ1VtaUFDODl2NVZrU2Ntc1lKOHd5S2FMQ1M0Q0s5bi1RbmtOOTlUMmw2QQ?oc=5" target="_blank" rel="noopener noreferrer">中国海警船、海軍艦艇と同行 防衛省が初公表―鹿児島県沖</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月28日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMigAFBVV95cUxOcXgwbnRxUFV3dDg5R1AxWmN4QlJSQ3lCTGEtVWZ4TXBhSmtZZ3d0OVlKektlUk9VNnJqN25ITTE5VVFOb19la2ZLXzhnRkM1NHRJTkViY2I5ZEpaRFlxUGd1YUhGcFlmanJaQk1rd3lvX1ZyeXlURnliZmQ2Ml81OQ?oc=5" target="_blank" rel="noopener noreferrer">中国海警船、海軍艦艇と同行 防衛省が初公表―鹿児島県沖</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月28日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTFBDMml2VUFsSndQYVZXVlNfSm9aZGpnU1R0WnlwNDYwWlBjN19PLUZXUndyWW9WRi04TzBrRUVodzhsRWFOSVR5a0NOZzNpVFcxWm5lT19Tdy1UQWQ3RW45cFQtSVJRTmFv?oc=5" target="_blank" rel="noopener noreferrer">日米防衛相、第1列島線の防衛力強化で一致 中国念頭、抑止力重視</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月28日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE5iM28tV2xqRWUycUlwbUtXaTk1V1NvQmdmY0NTVS1oQmtRajlOWHVJdnhFbHBnZE5DWnNkVFktNk9fZUg5ei10cXdxOVlWRkZYZ19hMEcyRVpLUi1BOGxELVhQTQ?oc=5" target="_blank" rel="noopener noreferrer">防衛力強化、恒久財源見えず 消費減税・積極投資と奪い合い</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月28日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE9tNUFyTmFaRkRvckY2TGthdUlfRVp3Nk8wWnZ1SVEzVHVUUVNrLTZnZGs2M085WWk5ZFBRd3JmSktiRkNLaFFPcWRpOGZVSXh0cWxvT3QxTS0tSWlRWDYyaGRCS1V4R0k?oc=5" target="_blank" rel="noopener noreferrer">日米防衛相が会談 安保3文書改定控え、日本の防衛力強化を議論</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月28日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiggFBVV95cUxPcTdKSEtJaTVWS0ZwNFc4ellrdzJPcjd5aTZPelB0TUItelJjU0dUYndxRGNaa2NBeDdVUk5ZLVpHSk5sTFBRdHVtcFpPd09NY1FDYklyRlpONW94aUprbEc3bHFodkxKTk9DNlI3OVV4OE4xYmJnV0ZWVkpHSGdRZUln?oc=5" target="_blank" rel="noopener noreferrer">防衛力強化、恒久財源見えず 消費減税・積極投資と奪い合い</a>
        </li>
      </ol>
    </section>
  </main>
</body>
</html>

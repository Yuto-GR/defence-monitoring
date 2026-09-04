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
      <div class="stat"><span>UPDATED</span><strong>2026年09月04日 14:41</strong></div>
      <div class="stat"><span>ARTICLES</span><strong>36件</strong></div>
      <div class="stat"><span>LATEST</span><strong>9月3日</strong></div>
    </section>
    <section>
      <div class="section-head">
        <h2>Latest Coverage</h2>
        <p class="note">Google News RSSから取得・フィルタリングした記事です。</p>
      </div>
      <ol class="news-list">
        <li class="news-card">
          <div class="meta">
            <span class="date">9月3日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1RazIySExvS1paTWxLRWRwWVRId0M1VjB5YklSSW5mRTQzMXFIRmYtdXRsSDl4OW1kZlByZzNfZ2J3dnhSVGk0aV9OS1RPSDhXU2dLNUlJX1hSWk9VaU5oWTlWVWNkbms?oc=5" target="_blank" rel="noopener noreferrer">自衛隊に「外国人の登用」検討を 安保3文書改定見据え研究会が提言</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月3日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE9GaVZBLVhHQXVqb2NqSGowVXdIamlRZHdMUFRpVERUM3pKSGo1aEJId295U2VEbDhMdmRLckwyb2htRUZrVUxSRGZ3X1JHMGI5QUxaSFpRUGo2RUdncHd5eGh6d0xjNWZO?oc=5" target="_blank" rel="noopener noreferrer">安保関連３文書：安保3文書改定「変化を恐れず」 自衛隊会同で首相訓示</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月2日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTFB6UktFMlc3R2ZiTGNBTWNTSkxjUm5RZnJERzVGLVlMemh4NHBDZ1JyenBVeW1tX1VGUTZhS0hqdGRWQ3p0STY0QU9UZjUtUHBuZWxVNlhpTXAtNEZWSEIteGdja1JsdjQ?oc=5" target="_blank" rel="noopener noreferrer">馬毛島工事遅れ漁業制限延長要請 防衛省、4.9億円追加補償も提案 [鹿児島県]</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月2日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTFA1U1NlZHFCNVIxNVc2QkhscGZ6dUQxYUEwT1R4bVF4WHRLSFBXejdhWFVFaHpQbnMxZW1Bb0EtWXBLcGo0QkdWcmVaRFR5dE5POFJocFBNQnFpUWcyWWIxNWNIaktFVUU?oc=5" target="_blank" rel="noopener noreferrer">三菱重工とNEC、防衛分野で連携強化へ AIと防衛装備の技術融合 [AIの時代]</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月2日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTFBYRl9LNkk3am9rdzUwS1pTak1Mb2dqS2dJdU1XOUNfMnktY2MweGdWMlA4SUhoeXUtRDVpTnViZnhaaEV4dTgzV0dISEUxWHlfNXUxaVp3alVUaFV0QUVMckxwMHFyX0JXWG5tMA?oc=5" target="_blank" rel="noopener noreferrer">防衛装備の国内製造強化へ提言 笹川平和財団、自衛隊の外国人登用も</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月2日</span>
            <span class="source">中日新聞Web</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE81eGFzMHk2QVdBZ0lvTmE4dFgyck5qZ2FoQm93MjhVaUxTTUg3MkE5NjFNYXpsSkJjeUZ3LWpWZmx5cnB5YkwyTkFDWGdlV2RLVmh6MWgzR0R5aUM2eGlSNmV2by1NZw?oc=5" target="_blank" rel="noopener noreferrer">国民の理解得て防衛力強化 首相、自衛隊幹部に訓示</a>
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
          <a href="https://news.google.com/rss/articles/CBMiggFBVV95cUxPamo2ZlpPdGVDQjdleTNRODBqckVwRlAtcjVaZjl2NlZNWTN0MFJLLXdidXpheHQ2RW11ZU10MzhWRndnYjJxTjE0amUzYnh4V0g0cGViNVV6Q0Y2YUdhMlZhNkJjZEV6S1M1WmdXX1VnR3ktTGZDa282WjZDUElCTnRB?oc=5" target="_blank" rel="noopener noreferrer">高市首相、防衛力強化へ「変化恐れず」 自衛隊幹部に訓示</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月2日</span>
            <span class="source">ニュースイッチ by 日刊工業新聞社</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiQkFVX3lxTE1tOEdUU0UxVkplbUZDMGxhY3ZnN254Ry04YkVkc0tXQWVDNkZJSmdob1lBaXlZNV9Nd19pdlB4b3JLZw?oc=5" target="_blank" rel="noopener noreferrer">AI・無人アセット・統合防空ミサイル防衛能力に重点…防衛省の予算要求、総額9兆円</a>
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
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibkFVX3lxTE1VWDJBNDF2MlZ2YjRWWXVGb1FsazBhc3AwNFZ0UDQ4QTZVYWlDc3o3NnotamhObkZ4cmNCWVEtOVpuSjRielY4SFlGaGNwbjRjdVIzR2o1ZUJYUHJDTzh4R2l6T05ONFc2MTdUZXBR?oc=5" target="_blank" rel="noopener noreferrer">【社説】総額が見えぬ防衛省の概算要求 現行計画の検証が不可欠だ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月1日</span>
            <span class="source">東京新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiU0FVX3lxTFBPR0ZhT2pFRGZOdTM3WnlBQjg3NElmc0Z2NFdMc2tmelpjN1lka0dfVjMzNkd4S2xyX2h6WjlRM0pnSy1hblcwMl9ZOGhISmJ4VEhV?oc=5" target="_blank" rel="noopener noreferrer">防衛省が描く「AI活用」、指揮統制部門の支援まで広げる方針 海外では多くの命が「誤判断」に奪われる中で</a>
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
            <span class="date">8月31日</span>
            <span class="source">Bloomberg.com</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMid0FVX3lxTE9uRF9FWWQ1SHVrd09LeUFYVDlyQjQxc1N0c2MwRXNZSDRvMUNxVDEzcUJiVmprNzJ2UjhybmotYXVNckFlcUFIbTRtU1VrSG9VTEI0YWRneEFpRm5tUm1NM2RnbHo4aXlwMmQzRE13aS1CdVF4Y3RV?oc=5" target="_blank" rel="noopener noreferrer">防衛予算は過去最大8.9兆円を要求、安保3文書改定でさらなる増額も</a>
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
            <span class="date">8月31日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTFBHd2JZbDVhUHVTeW9iX1BXNUN5LV81TFhzb3cxeTgzM1o0TVI0YXdTUlhneXM2T0pvbEhCMU5WZU1zekdQNUxHZEszQnVVV1dqbWc5MGdxUzBSb1g5NGhJVk1DOGNQMHlr?oc=5" target="_blank" rel="noopener noreferrer">防衛省の概算要求、過去最大8.9兆円計上 AI幅広く活用へ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月31日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE85TGw2bHVkRThRazFiQzl4Z1poZUlZTW9mNFR5WmY0QklBVTJiRXdvTmlfSUlGYkFfVXJUUXN5U3JKTzVSS3hzYW9tN01JY2VrU05QLXJseUMyMV9pRXZDaTExVXRkRmc?oc=5" target="_blank" rel="noopener noreferrer">防衛省、過去最高の8.9兆円を要求 「事項要求」多数でさらに膨張 [高市政権の安保見直し][安全保障関連3文書]</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月29日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE5MTS1XcVFGOHlERXZnNVl3Z1NCTE14SHlRb0xTd2ZWekl1YkVnLUJWaDZQY29ld0U2UVVHcU81S0RKTUs1Y3lkVHM5VmYwM2dXR0JKdUNxclpmLTZnUEZ3YllsU3kzRmp6?oc=5" target="_blank" rel="noopener noreferrer">ポッドキャスト：日本の防衛政策はどこまで変わる? 安保3文書の改定とは</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月28日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE0yMUgybFBubU5uUVRtLXI5MktrbXRvOEZGM2M3V3R3dnN0dk5HemVqeWtDQ0JaQU11UkVub090ajlJWlNHYVJWdklBYzFTREV5WjBWMF9PaWkzMXlfTVg5NjBVOWpLODltVWhUTw?oc=5" target="_blank" rel="noopener noreferrer">防衛省、日本製鉄と呉跡地の売買契約を締結 装備品製造の複合拠点へ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月27日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE1tQW80dzRDeEg4SURoRTNod0pOcTFNQlRfcW9lbGtKbnA5YXNLSnFCVHNZclZvbEdLZFFHU2RIUTYzRHJyY0RMZXBUaERDd21MZTRsODA3cUVielF5Q1ktWGtnaw?oc=5" target="_blank" rel="noopener noreferrer">防衛力強化反対に高市首相反論 障害者団体から手紙受け取る</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月27日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiggFBVV95cUxOcUZSMXByVnd0YjdsUUFHRHNmZEtkZHFqZHQ0am55SVdrQldvUFlUMEp5V0Y4Yy1BbmVhSHdkX0ZCWHVZOF9EM0RYY2JLb2gxTklqV1c0emRBb19SelpfWmRLUDY5NVB6dk9PazBwQUJvdl9CeFp2SzJfOTRpQVpxWlpB?oc=5" target="_blank" rel="noopener noreferrer">防衛力強化反対に高市首相反論 障害者団体から手紙受け取る</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月27日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiggFBVV95cUxPbE9KVTEzd1hWbVlmVXBaaXAzOXlTSWFVa1lOYTVxLWlzVFF6SVZvWDgzNUMtbVpBUEtmTXo2OVY2Y0lqSmpPay1jdnJyTjdSODE4ZkVEMkhsWkJjYmRLMG0wM3E5Q29qV2xtY1c5bUR1ZmNDX0VMUUFXLU4xdkZlZHVn?oc=5" target="_blank" rel="noopener noreferrer">防衛力強化反対に高市首相反論 障害者団体から手紙受け取る</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月27日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE5PLWVXTGFScE5qTkVOSnJjal81WUlyV2ZsVTM4MUJrcFptOUstRm80YVpmd0ZzMVJ2TmNCNktpU1BxbW56cmRObFV2cHZRS08taEJ2Z1k2Z3p4NjRXYUV2Ym5EQUZrTU9kZUZQUw?oc=5" target="_blank" rel="noopener noreferrer">防衛装備品の供与先、新たにベトナムやパラオ シーレーンを補強</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月27日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE5nRUpLT3A3OEgzSk1qWWN1ZVVWVll6UjBjVEh3OG5fcXVQa2g1SGhMZ0NtNnhKbnBTeDBQazNJNUlDR3RPR2lXNVo4cS0xUGQtUS1nTF9FQWgyTDl4TzlWUUdManEySG5JRFFhUw?oc=5" target="_blank" rel="noopener noreferrer">日米同盟不信は国益にあらず ICC赤根所長制裁で浮かぶ最悪シナリオ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月26日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE13M1lPcXlnb1dsUlZ5TGxqS1FoTFdGNGZpQlExSE1ORWg4ZHNjTkpROTVWbEJYSXNueTFLOUlFZzB2WU95Y2pacUpxWnNxZHRzbWpZWjRzdnhJWFhTVGNWQ0JGUFgwb3NBS1M5SA?oc=5" target="_blank" rel="noopener noreferrer">高市戦略17分野、国産ドローン8万台狙う 防衛省が大量調達へ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月26日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTFBQRk13SE0yS0NLeGZtSFpBZ3dGQlFKbURqckJzR3lqZDBTRGlMQkpMUmRwWTFWVDhrODdUT2VPSlZMRGg3LXQ4NWdqY2NjU2htZ2dwTk1iNzhRaDFmdDZiM0c4R2ItV3A3?oc=5" target="_blank" rel="noopener noreferrer">揺らぐ「平和」：軍拡の時代に インタビュー編 戦前回帰の武器輸出 他国への影響力拡大図る 纐纈厚・山口大名誉教授</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月25日</span>
            <span class="source">日経クロステック</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE1POGJyZVBkbWVFUkN1V01YMENmZjkwbjNTYklSbnJ4NlRvUUFoSVExYUFxQTVfRDFIWmZmci1lS2kwT2s3bDBmN1p6ZnJiYmlXbnhuY3R1MzVxcFNzTVVQenl3Unc3N3F4dERPMg?oc=5" target="_blank" rel="noopener noreferrer">防衛費増で増える防衛産業への転職、40代で年収増の事例も</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月25日</span>
            <span class="source">Reuters</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMifkFVX3lxTE1oVDdLU1kxd2liZFNvS2E5bG9xUmU2ZXgzaGVySF9LLWdXSWxNOW05aXR5U25CVEtEZ1FmeTVuMzJBTTA2VmxkY212Ymx2YmZsTUV5LXlnbWtyZEFia0tHYXBNeW5ORHVNSnY0ZF94blF3ZFZtV3FrVnI1MHdfdw?oc=5" target="_blank" rel="noopener noreferrer">防衛装備庁、迎撃ドローンでテラドローンと量産調達契約</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月23日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE1EVEhfNUJTQXdKUUNySUh5dF94NmZFemhtTExpYlVaazJiWDVlS0hfTURxRnVCemFzWG1vT0NvRDB4elVQYmhJSzFzNWtQN3lPVzR5bGQwN2J6RVZFRDVwTmFNT2JpNTg5SHJPUA?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相「日米同盟が機能」 熊本地震の被災地視察、支援に謝意</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月22日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE9hRFhvSGsxZWROZ2M5U3BZZjNLM0VCMWVmWXAwMG95S0FOdGY2WEV6NXpLeGhOSEdwX0MzTXJNMmRkdTBKWEZfVnA3ZDlGWHpoc0UzWXBwRXFxQ0NKdFhFWVpRWmlUUQ?oc=5" target="_blank" rel="noopener noreferrer">通常は数年要する防衛装備、「迎撃用無人機」は公募から３か月で納入へ…大量ドローン攻撃への対処急務</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月21日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE5obmxWY1BGZTFKMnRxNV9jZXFFaWJTTWxQVGtEcEl5QzhkMnE3TVNyb196TXFnOTJDeUFYY0tRQzQ5dndwX2JWWXNkQzdZUG1iSVJHSUhoaTlpWWxJcFFwSFpPTFNtdw?oc=5" target="_blank" rel="noopener noreferrer">日印海洋安保 覚書署名…防衛装備品協力深化で一致</a>
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
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE91Tm5XLXpkc1R5b1kwaWZWa1dOaUE5TnZ0aUNwQjJCNjFDMWRpYTZaSlluR3pGQlBNdkI5ZjVMRS1kSnNYeVZ0bGN0VE1ZcFg3WDJiaDF4VzZjeEYwYzJxTzhpNVVZYVU?oc=5" target="_blank" rel="noopener noreferrer">経済安保やAIの海外依存リスクを議論 安保3文書の有識者会議</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月20日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTFBVZmw5dl94bURSSTJVZWdKM0pMSFRXN2F6Y1FaNndPX0Y1d0lmNVMzNkRDZU45RjlYYWI0d2dqYjJwaXFxVVdQUnM3ZnJtNHRpS3JQVGVwWkdKTE1NRTdEUm9qajROLXdk?oc=5" target="_blank" rel="noopener noreferrer">揺らぐ「平和」：武器輸出で影響強化 戦前戦後に通じる狙い 色濃い米国の影響</a>
        </li>
      </ol>
    </section>
  </main>
</body>
</html>

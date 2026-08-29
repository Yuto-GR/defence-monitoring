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
      <div class="stat"><span>UPDATED</span><strong>2026年08月29日 16:46</strong></div>
      <div class="stat"><span>ARTICLES</span><strong>52件</strong></div>
      <div class="stat"><span>LATEST</span><strong>8月29日</strong></div>
    </section>
    <section>
      <div class="section-head">
        <h2>Latest Coverage</h2>
        <p class="note">Google News RSSから取得・フィルタリングした記事です。</p>
      </div>
      <ol class="news-list">
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
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE9RbFJ4WWk2d0hvM1FvbHdTZkphSnJ5R0t5S3lJb3V5bXBSX0pxQ25xM3ZNUkJUaTAxU2NoZVJxQmRReUd2NlRmVFl1LVRzSWdHZlFiNklKc2RvT0h0UE40?oc=5" target="_blank" rel="noopener noreferrer">広島 呉の日鉄跡地 防衛省が売買契約締結 複合防衛拠点整備へ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月28日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE9vTUNQN3FIdFo1dVdnaXhWZjZnLWwtajc3Y2lSb2FHeERFWmdEdGY2Z0VmR084ekJ5Mk5JekpIeUcwa2NzQ2pvTWhaSklUNDZfTE5fcWlVSEhBcU9RajBEbEp4R1N2ems?oc=5" target="_blank" rel="noopener noreferrer">防衛拠点整備へ防衛省が土地を取得 広島県呉市で無人機など製造案</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月28日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiWEFVX3lxTE9DelY5QlBDbWJqWHByUzN1YzNQay1QVFpuUm5ibDRyc1NITzJhamNOdU9JUXp4RHoyV3d3SEczdXZTazkxdlI3N2dwSW11dWxsN3VoVlFtYk0?oc=5" target="_blank" rel="noopener noreferrer">呉の製鉄所跡地 防衛省が売買契約締結 複合防衛拠点整備へ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月28日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE80elpwa2lCa0V0bVJhMjFoR2J3MFNMQUR0YjNDNGpzcVBSOW1QMmFZNjhHTGdwUGdOeERoWTU1Sk9ZRVBGZTd0cTVkOTUwcGs5elhiOFQwNkZSMm9LYzhIdTNSazNqWWNr?oc=5" target="_blank" rel="noopener noreferrer">防衛省、広島・呉の日本製鉄跡地を取得 「複合防衛拠点」に</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月28日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTFByQ1hPZEhtTFFTU3FOZVQ0OUR5WlQxQTQ4aHRyN0lVS2FkY1pBVFlwQ0ZiTXRPcDlJR3lZX0VacnJncEpIOC1oNVVLQjhLVjBIX3VVMi04SmJRUWtNdFJra1M4Yw?oc=5" target="_blank" rel="noopener noreferrer">防衛省、呉の日鉄跡地取得 「多機能拠点」整備へ</a>
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
            <span class="source">日刊工業新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMib0FVX3lxTE8wWmZxanJ4U01ST0paNEJVelRNblFwSzBFdEVMOEFUcllFVV9HTGo0MnFLMXRGSmVkZzJKZWlpcXVfaVBxWG5mVjlvZ0tfMS14TWtGM2dyNjlHYkhDUVN4ZGdjdHhBcHk5VGNJeUR0MA?oc=5" target="_blank" rel="noopener noreferrer">富士通・防衛省、予備自衛官の管理効率化 オンラインで手続き</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月27日</span>
            <span class="source">日刊工業新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiWEFVX3lxTE85Q1FydzRHOFg1bmVubjNOWlQ3NkFDbGRnRVpLT1FUMWl3LXF0cFlHdGszNnZKOEIxY0tPcWtHN0E4VzRmN25ENHlGV2RnTTRiZzBfMmwxQkg?oc=5" target="_blank" rel="noopener noreferrer">防衛省幹部人事／防衛審議官に安藤敦史氏</a>
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
            <span class="date">8月27日</span>
            <span class="source">日刊工業新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiWEFVX3lxTE80Qi05YmZ5VVA2cGIxd2dubHBXWkkzcFZmUXF3S0N3bklhRHo0b29sVW1qS3UxWWZfd3VNYVNuS3QyTEdfREVPVk1BQVg4OEFRQVB4c0kzRlM?oc=5" target="_blank" rel="noopener noreferrer">政府、防衛装備品の輸出緩和 移転三原則・運用指針改定、「5類型」規制撤廃</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月26日</span>
            <span class="source">日刊工業新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiWEFVX3lxTFBwZU9GRnRpWUhkSmd6T1FTcy1tUG5LQnNsUEJtd2lpSjlTMVJqUXVJNW5TNFVqWk1LYmd3dXFvdHhKbXVJTHdmM01yNzh4OGZVeEVTNDhjR3g?oc=5" target="_blank" rel="noopener noreferrer">令和8年熊本地震／防衛省、自衛隊員の投入5100人体制</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月26日</span>
            <span class="source">東京新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiU0FVX3lxTFBiZU9paWlZaWZNZ0xmQVY5NGpOT29XdlFyYjc5Y2tHTUpGWkJEdHU4ZUZYUXhHdk9IeFFKanl6TWgwYXZWVVVJb242b1FfQzVfdDBr?oc=5" target="_blank" rel="noopener noreferrer">米軍ヘリ基地 撤去要請 防衛省と都に 港区、アンケート結果受け</a>
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
            <span class="source">日経ビジネス電子版</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTFBGYlRhTW9zbVg1OUZENnVKcTFKa3hVTUFEMmpBMGhEZW9LWGVkNUtvLXp4TW9pTm12Y2NmdUNEZ2V2UVN5N0ZPU282SHR6OVRwRWI4OWdVd0lVaXN5dC1EcmRKLUtUdjg?oc=5" target="_blank" rel="noopener noreferrer">国民民主が代表選、橋本候補「防衛省を総合安全保障省に発展的改組せよ」</a>
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
            <span class="source">ロイター</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMifkFVX3lxTE1oVDdLU1kxd2liZFNvS2E5bG9xUmU2ZXgzaGVySF9LLWdXSWxNOW05aXR5U25CVEtEZ1FmeTVuMzJBTTA2VmxkY212Ymx2YmZsTUV5LXlnbWtyZEFia0tHYXBNeW5ORHVNSnY0ZF94blF3ZFZtV3FrVnI1MHdfdw?oc=5" target="_blank" rel="noopener noreferrer">防衛装備庁、迎撃ドローンでテラドローンと量産調達契約</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月25日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTFBSblFqQ2JZTzJJTm5mMmkxdVpuRzB0YWstTFBOdmdRTk1HZk9mdzhOWjRwZWZobzZVZ2llQl9YbmpkdlBzaHdMYy01ZHRLMnJKYUVzX2s4X1h6cTZEMEdSOHZ3aXh5cm8?oc=5" target="_blank" rel="noopener noreferrer">防衛省、概算要求で「新しい守り方」の表現を見送り 自民の反発で [高市政権の安保見直し][安全保障関連3文書]</a>
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
            <span class="date">8月24日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTFA2eXRBeWhnalFMQzMxdk14NUNiSlkxQUczMTlmVC1UVndQSmdSNHcydmtLdDZTSGNmOW44RWFkbHljNkJZZlhxZlAxd3dfYlFBclhVclZZcEZDbVZHNkhka2xVZWF4LWc?oc=5" target="_blank" rel="noopener noreferrer">防衛省、「認知戦」の対策強化で部署を新設へ 政府対応には課題</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月24日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE1QQ0hSRjYwVEhaMV9sT2pBaWNMc0hfOFVaaS0xLU5JNlQ5dmtqdEg1QXRsNEFXalBmcnlFbWJpNTRZX3ljY2NoR3QtNThzUEpyZ0pObzAwR3R2bFBOSy1tc3RsNEVMQUV4aVA5Tw?oc=5" target="_blank" rel="noopener noreferrer">防衛省、情報分析のAIシステム導入へサカナAIと実証事業</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月24日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE91VEh5d3Z1alJMU1l3Tk50ZDZfWkQyUW5RT0pGc21WZjJ3R0dmWUxhN3RFQWNCcF9BOVZmSXhKSTBZWU12Zkh0dE1zbnhGdVFCbEZHb0g2cFFOVDhBbEJJRGxiOXFBUQ?oc=5" target="_blank" rel="noopener noreferrer">大量の無人機・ミサイルに対処する「新迎撃システム」、防衛省が開発へ…機関砲やレーザーなど使い分け</a>
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
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE5WeTFDRDRobWFWalktZTlfenhHQkwxeUFPNG4yT3A2UlBCS19MSlpHWlpIRHVwSWFUZF9KY3pmR0NfWVJfb1EycERFdENiSTYxZWx5Y0NJMXBSX1FlOXFpdWJmYTA2VEFnYlEzMw?oc=5" target="_blank" rel="noopener noreferrer">防衛省、AI指揮統制へ政府クラウド導入 27年度概算要求</a>
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
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTFA2TkdKUGVwZFc3WkZQLTh2cWRPNXpWQ2F2YlA0RE5jUEtuZU9iQkowSHVpZzhrWnFiOTVEVFpwOEx1SUZvUHBmcExMbUN2MnhpSUtNM2J3RmhYMWpqT01nb0YyZw?oc=5" target="_blank" rel="noopener noreferrer">日印海洋安保 覚書署名 防衛装備品 協力深化で一致</a>
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
            <span class="date">8月20日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTFBtRjI0UWNWcmMtODFpZVZaREZ1cDJJaWl4SGVJZ2tyZ0Y2VEUyMW9DTlNpRGw3eHpzWWUxOFp4bk1WV3otWUFEZGRxd2VtUm01cVRWRkoydHF4bUwyWnpEUkd1WUlhdw?oc=5" target="_blank" rel="noopener noreferrer">防衛省の来年度予算概算要求、過去最大８・９兆円…長距離攻撃できる無人機の開発盛り込む</a>
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
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTFBHaElSUmFBaklyTzlXQzhldkNnQVpHR1Y1X1ZlMXV2Sjl0ZVl1NGU1cVZxaWtpMEdOSC16d0JHRjZPQ0RRT1h6WG9jWXZ6cnJfS3N2WF9PMklHWGZWcWF5TEUtNi02MFNNTWlYTWpYM2ZmNG95WVE?oc=5" target="_blank" rel="noopener noreferrer">北朝鮮が弾道ミサイル発射か 防衛省発表</a>
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
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE8xV2RjRVV6dWdLR1BTYXJnQWFmLXlkOUNOakZiS216MnZZZVZ5ZjVwamc2c0VEakFkTm9UbUhrZTdocHNVTlUtVDlqc3B3MmpkMDllaTZwaVdzUGVUc21hLTkxTk1PVGVaNEx4akoyM0xGYzRBWXc?oc=5" target="_blank" rel="noopener noreferrer">北朝鮮の弾道ミサイルすでに落下か 防衛省発表</a>
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
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibkFVX3lxTE5MNVZVTGxqTVF6d0dBYmt6Z0hfelZFMjlCellIemtUZWhKXzVLTUJ3N2pIMnFfZFVlVUVoajNILWZlWGZ3MWsyRlJnaHNVNUdhUlIzbmVFT3ZaOVkwZ0tBSDY4VmxoRk1Nb1FXZ1J3?oc=5" target="_blank" rel="noopener noreferrer">防衛省が組織改編、退職自衛官らの「支援庁」や3局増設を概算要求へ</a>
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
            <span class="date">8月19日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE1FWHpRajlZdWZDYUpkcC1heC02RHRNRHVzWVFtbDVIVnIxdmpjQ0NlVHlqY1AtTGxIY0VLZkdsZXMtR1B1X3dNdXFwQzlLZVd5ZmM4TEx5aUtnSlBrWnhF?oc=5" target="_blank" rel="noopener noreferrer">防衛省 令和9年度予算案 過去最大 約9兆円要求の方向で調整</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月17日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTFAyTUJrdzJ3MG1ZM1BXNmFnSzZRRXFkTnd1Nm1YOGJFT3NnVmd1UjJqY3lwWjdZYTlIV2NSZ05iTWRXczI2UzBWcnlDNDBXaUw4OEdyZHhVeVFlYmNOREJKZUpOYw?oc=5" target="_blank" rel="noopener noreferrer">楽天、独ドローン新興と提携 攻撃型、防衛省納入に向け：時事ドットコム</a>
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
      </ol>
    </section>
  </main>
</body>
</html>

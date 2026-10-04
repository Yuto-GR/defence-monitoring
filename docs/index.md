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
      <div class="stat"><span>UPDATED</span><strong>2026年10月04日 15:42</strong></div>
      <div class="stat"><span>ARTICLES</span><strong>35件</strong></div>
      <div class="stat"><span>LATEST</span><strong>10月3日</strong></div>
    </section>
    <section>
      <div class="section-head">
        <h2>Latest Coverage</h2>
        <p class="note">Google News RSSから取得・フィルタリングした記事です。</p>
      </div>
      <ol class="news-list">
        <li class="news-card">
          <div class="meta">
            <span class="date">10月3日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTFBKSzRKQmVDWUVraEx0ZDh3bGV0M2phMnRuazlJZW9Cb0R5dUFSV2t4VERuWC1LMEkxSVlPa3hqMERnRjJoY05zeFctWElTcmFqR3ZlTE50Z2E1V0M1aU9TS2pQQVNCdw?oc=5" target="_blank" rel="noopener noreferrer">北朝鮮が弾道ミサイルの可能性があるものを発射、すでに落下…防衛省発表</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月3日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE5uczhaNENueWFVT2x3T1puZV9VQTdqRXNKLXBfLUZISnBNR1RUaGxwZ3JaZElRMWxOLUNQWFVGa3dET0toSi0yYUFqNmtNbUJtcUh5OFlqc3c1MmY3LXB2OWhmaDdDUQ?oc=5" target="_blank" rel="noopener noreferrer">【速報】防衛省によると、ミサイルの可能性があるものは既に落下したとみられる</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月30日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiWEFVX3lxTE1jd1pHSmFTell2azA3WG5NZU5TSWlLbVpXd05VcGwyRkJBakcycDIzMU5MUUZzZ2d1U0w0c284M05DdFZSUUhyQVUxV2IzcVVfMmxfYTE0M3A?oc=5" target="_blank" rel="noopener noreferrer">自衛官贈収賄事件 防衛装備庁下北試験場を警察が捜索 東通村</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月30日</span>
            <span class="source">ニュースイッチ by 日刊工業新聞社</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiR0FVX3lxTE5mWjdmRW5IRTl3TGtNUENlVkhFV3R2dHd3Vi1xWGJLdldOb2hhS3ZOd1pnOVU3a3RDSUZUbV9MbWVnZWxISV8w?oc=5" target="_blank" rel="noopener noreferrer">垂直ミサイル発射システム搭載潜水艦、防衛省が開発推進…長距離防衛能力を向上</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月30日</span>
            <span class="source">日刊工業新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiWEFVX3lxTE82YUJUM3A4R2lLeG9pMkFVRmRsbFotQ1B1QTlLOHB2NHRMTFprdGtFS2h6aU9ub3RKamFPbTF5YjVYU1dvMC12bFd4R3l1VVhXbEktcm5KUjc?oc=5" target="_blank" rel="noopener noreferrer">サンテック、山形に新工場 防衛装備品・宇宙関連部品増産</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月30日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE9QRmdkdk5KZkNvbzVUMU5ZWjd5Y2xNdGFuYkNHS2J5eDQyRG80SGZORXB4ZDZPYXBFSS14RS05Y1hVUmNhOTRFNFBzVUszNExyOWtuRjFOdkVDOE1EaklnVGtpa3IxdDh1YXRfMA?oc=5" target="_blank" rel="noopener noreferrer">対外有償軍事援助 同盟国に防衛装備品</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月29日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE1tTHZIa0xOTTdGZkJjQnZxNXNZT0haSUJZdDhQMno3T1E0S3VxeGpNUjlWcGFlam9DV3Q3S3ZTenRiWDZhRk5BaU8zcUFmVFJHOEhSb3o2WElJQ0d1bVFFa0JUOA?oc=5" target="_blank" rel="noopener noreferrer">２５式地対艦誘導弾を初展開へ 日米共同演習、反撃能力向上―防衛省</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月29日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiW0FVX3lxTE90aW90aGRNSWxsOGNkdTRJa2dpQWNYQzVHWFBhTGNCaVZWcy05cm1iOGVxbWFDWkJqT2Fsb3FXdzNlVUNIeDctOVdBMGVuUUhYaFBLcmJ3dWhlMVU?oc=5" target="_blank" rel="noopener noreferrer">中国軍とどう向き合うか 安保3文書改定、日本の選択を専門家と解説</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月29日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTFBScTVGZDZ0aUxhSkY3cUFKTXZtazE4cW9KMEo2dWZEdklWcS1vZVhOc0tCVFFqc2p6eXZVTzNRMkxsM0d5YTlCMGJBNjVJT3ptNFlQQnh5cng4Y082V1I5cDV1czQtVHFsdWFVMQ?oc=5" target="_blank" rel="noopener noreferrer">振るわぬ米ドローン株、中国製締め出しへ 日本は防衛産業優遇で好調</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月29日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE1XTzljbjk2YnlWT3ZzeTN1eExLcFNCQ2YzbFFDUjgwMHFTSkQwWi1QblhwdUNQTElQbjRPR1RxM09ERHNuQ2RjMjBPNFM0YkY2NWhRUnJXbXpmZlN0N2JqN01INk9FVl9raVRobQ?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相、タブーなく核兵器・原潜保有を議論 安保3文書改定巡り</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月28日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE1sa2w3M1V5bG5Kd2dfM2dKZ1pGQm5aVEVZa2wtVm9JVVVTd2lzZDRnX1I2eWpiVGhPOEJQeXJ3SnppYVJiZG1oXzFFc2N1WERhaS1xRHJHOVNkdmRvVndHWmIyc1k4QQ?oc=5" target="_blank" rel="noopener noreferrer">防衛省 装備品に新興企業技術 新支援制度 公募開始へ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月27日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE5hM0lCVVdqcWtjMzlhVHFYZkNpTzF2Y3Vyejdteml5Um93ckZFLUg0Rlc5NHZyUW1iRVNaeDlkeWRweW95TmlMNW5PekVCbS1WaWcwQW9hLWxEeDFZQXNFQ0FBdk5DRXQ1RnpoQVpmR29ETHRuWFE?oc=5" target="_blank" rel="noopener noreferrer">防衛産業報道に必要な視点 新聞に喝！ 国防ジャーナリスト・小笠原理恵</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月27日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiogFBVV95cUxOLUpYaGZzWkVlM3ZlNlVZd1ZUb0lEUExZOFdFRklhQy1rSVo3aDlCZUlPcURNbTg3Z1RrTUR3T0hYT3hGVTJ1dGVzQ1BPWGxTR1liclotZktBQnFaZkc4OV9LZU00eS0zdkIyWjRwdjhfVUJyMk5fQXdkajJGQ1VQSUdJSzV4Rlh6WU1OM0g4VFNHUkVYUkQxVWJIUExQTWFzbkE?oc=5" target="_blank" rel="noopener noreferrer">防衛産業報道に必要な視点 新聞に喝！ 国防ジャーナリスト・小笠原理恵（写真・画像 1/1）</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月27日</span>
            <span class="source">東京新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiU0FVX3lxTE1lWUVXUkZ1VXE4OS1RdWhoWHQ5MXdZYnRxcUlYaDRIWFEwUkZiR3hxcWI0Yl9rQnZTUVFTbkhoRDdnUWliRnNZdG53eV9qakNjaHlj?oc=5" target="_blank" rel="noopener noreferrer">アメリカ企業の無人機「シーガーディアン」一挙大量購入計画 防衛省、2900億円超要求の「事情」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月26日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE9tamJIOE1KWnhFMW9vWWg5XzEtcnhObUdad0xXMlBkSHVqeEt6c0NDV1V0NGJmNDZXQmNXX3ltTnZjSmFoVHlEa0U3SmJDWUkwcjVFQ2ExMm8ydldsTFRtWXE2MXNTSDNHeTZ1aVV1U3Rkak9hdnc?oc=5" target="_blank" rel="noopener noreferrer">「日米同盟ともに強化」小泉進次郎氏、米中「同盟」演出の日に強調 対中象徴の米司令官と</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月26日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTFBBYlppU3dsdjZyU3VWWXdad2tuVndhU0YwVUhkSHh6bE1RUlJfb2tzb2ROVWh0eGU3bEdPbHdIckVVeUFfaEVhUVdfbl84UmFLekE3bzV5OXgzbzZFZElwYTVNVjM5cWJhdlBFc0N1dmRiUm9KU0E?oc=5" target="_blank" rel="noopener noreferrer">長射程ミサイル「25式」日米演習に 敵基地攻撃、10月初投入 防衛省方針、熊本配備</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月25日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE16VC1xNVdVcmR1Wnc1QzVJaUR4aWVURHY5bTUwSzllN1o0TmlybjQ1TFh2Ym1sV3Azc19jcGJqaXBJZzh6ZU9mZkNXdVU2MnYwTjhIUHNIT1oxUFZhcjJrTURLcEREaHFFcnRTXzZFaHBqWU1VaHc?oc=5" target="_blank" rel="noopener noreferrer">先端技術取り込みへ防衛省が新たな調達制度 スタートアップの育成狙う</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月25日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE9CQ00xZm90TDRyN21DdHFjZGIzSHE3Nk1GclRCNW50QkpqZmtFUTRUZlJSclZxS1hCbGl3Z0RvLXlJSG5tNmk5MVBUU0RGWVZ2Uncyb0l4bF9EQ3ZXRDBTbUdITXFreGZTUF82QQ?oc=5" target="_blank" rel="noopener noreferrer">防衛省、10月に無人機開発へ新興企業の公募 早期に量産体制構築</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月25日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE1YNmdhRmxGYU1sVm5YaHVuYkswZ0ljaFlheU5IVm5kd0t6MmVsZ19zcUk2UVJnQ181a1huZHlSaHNvS2x4MVVYaW5GRGdzR1FoMzZ6WldWa1A5S3I2TTFabGZubw?oc=5" target="_blank" rel="noopener noreferrer">無人機開発へ新興企業支援 防衛省、資金配慮の新制度</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月25日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiggFBVV95cUxNWGhGWjE2Snppek9Id0JrVlB5VlIwTUZzWDd3S2kyR3BMWU81YVl4cUVWRkVzZnhPajhmUVhyRXVjTUR2eDFwWVNfbmtIUFMxN3RnQ1E4OW0xWk5RZ2hHNzg0RnZhVjluYVY1bGtHbDJFWk55RzF0U0JOMHFXaWRrdkFB?oc=5" target="_blank" rel="noopener noreferrer">無人機開発へ新興企業支援 防衛省、資金配慮の新制度</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月25日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMic0FVX3lxTFBINEFRU0hHT0R2TGxIdmJPemM5WlNFNDJOdnZFR1liMGF4TnU3VXM4UWNTbE9XblFGcmc4Sm5MTmI1SkZGaG5UNjFWdGo1RW5XM2g3ZTFseEdFcUVKUlhmODU0OFVsTnFZMHRKSERKREhNaHc?oc=5" target="_blank" rel="noopener noreferrer">鳥取：防衛省、情報提供遅れ謝罪 無人偵察機墜落で知事に ：地域ニュース</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月24日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE5rR0h3MEVnSDBJMnJYR2pfWUJCZHJibldHRDdWLThaWFctTTg2WkFFUGFBcEl3WUlVdnBTTWwzWExuQWdKeUVrek1ZZnFNUUp3dGRGb0V5c0x4UTlmb2pKNnVZZzllUQ?oc=5" target="_blank" rel="noopener noreferrer">日米首脳会談、対中国で「緊密に連携」一致…ＡＩ・重要鉱物の協力で日米同盟「さらなる高みに」引き上げ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月24日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTFBxdkZndWQ1QmxManNaZUZUMElpQllDOUdVSUtyeEFNU2k3ZlBMQ3IzblNscktGYUx6VlBUR0l3aUZkMjFYckJNQVBXM1VwcFBsNUJLMTRVc2FXWFdWY2ZYZ3dVWDliQQ?oc=5" target="_blank" rel="noopener noreferrer">［スキャナー］強い日米同盟誇示、米中会談前の「布石」に手応え…日米首脳会談</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月23日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE9NaXZYLXprb3ZkbnlDYUVoZTlFMXhJNmdjdm5qbVk5em5VOEl1YXVlcldTRkdZcEtGOG9hSnF6SGUzUFNGWUpqUGp2SVpiZ2FsNTZQOVFTSk5jb2FMUmdsTmsyWlVqS09hTElXNg?oc=5" target="_blank" rel="noopener noreferrer">［社説］日米同盟の深化と法の支配ともに追求を</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月23日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE1STF9jRTZ3UV9abHRZRGg2eUh4UzdaZVpVWjNxYVFLN1NjdHg4dUdUX014b1RRY3ZmVUNjeW5EYVNMb1g0clVuMmNZNkg3dGtOanlkajNaQURuMVlKUXRZ?oc=5" target="_blank" rel="noopener noreferrer">高市首相 記者会見“日米同盟関係さらに揺るぎのないものに”</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月23日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTFA0UXB6T1Y0cnJ0em95WmlPOGtZVUxLMXdLenNpRW5Yd0VlRWtrRDRhQ1dqYjVWWmtiOW4tQkptVmJBMlNoRlFPbHlhVU84N2NVVUZuOWdiNEtEbDVWSGYwSjgwVVZDQXpLS0RwUEVkVzJabkdiUkE?oc=5" target="_blank" rel="noopener noreferrer">高市首相「日米同盟の強さを世界に示す」米中会談2日前の日米会談、対中連携で示せた収穫</a>
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
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE40bkJUSzlBQVlmeUo1SkRBZEpHa2paRGt2WWFqc1U5M254LWs3WlpWUDlMYTlza2NnWWRVOGZIZGtPUHhWcFNvWjVqMl85QmVWWUNFNEtidE1Ec0RucVdyVGNDVXo0dw?oc=5" target="_blank" rel="noopener noreferrer">【速報】高市首相は、日米首脳会談について「世界に向けて日米同盟の強さを示すことになる」と述べた</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月22日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTFA5UTEwaWxSSWR5OFBJQTEtSGxuLXhjVU1UV1hxNzZKaHd5eUFoN2UyUGpFMVJkcEN6UlZyUUFlbEV0cVAxNjRvUkFtNjVMODQ3NkFscF9QSlR3WWRtYjFCTGtiUHlENDJUNGVRN3VlVmVpTEVZWUE?oc=5" target="_blank" rel="noopener noreferrer">＜独自＞防衛大がAIリテラシー教育導入へ、来年度にも 安保3文書改定見据え PT設置</a>
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
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE04T1pMeUtocm1BU0JVRndNZV9LejYzZmJvY3RGQ1hjN29IdFMtejdHa3duWTFjbnJpR3VDOE5lbEZDNUR6NEk4UFFwcERNb0RRR05sVUVfMU4wOFB4QVVzNnFjTEdFdw?oc=5" target="_blank" rel="noopener noreferrer">【速報】防衛省によると、北朝鮮から弾道ミサイルの可能性があるものが発射された</a>
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
            <span class="source">時事通信ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiXkFVX3lxTE9Wd2RYME4xaC1XUmg5TWhxdlo3bTROR3E2dzlSem9WNTVPNFV1d3lmemxsdmkyNFBIekM2MTFrdDlJMUFTWFNGdVVJdDBVZ1FBOUJ2ckttZFFWdWtMRHc?oc=5" target="_blank" rel="noopener noreferrer">日米同盟強化へ連携＝防衛相電話協議</a>
        </li>
      </ol>
    </section>
  </main>
</body>
</html>

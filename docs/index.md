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
      <div class="stat"><span>UPDATED</span><strong>2026年10月09日 16:15</strong></div>
      <div class="stat"><span>ARTICLES</span><strong>42件</strong></div>
      <div class="stat"><span>LATEST</span><strong>10月9日</strong></div>
    </section>
    <section>
      <div class="section-head">
        <h2>Latest Coverage</h2>
        <p class="note">Google News RSSから取得・フィルタリングした記事です。</p>
      </div>
      <ol class="news-list">
        <li class="news-card">
          <div class="meta">
            <span class="date">10月9日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE5lLWlPQUNtLURZckxiSTl3TUFKWVlfWkJJQmNPdmI3UmtLamFobGhpYndLaDJRcEx4Z1c0MVRFbld1cW4wdVZkSjBnUklZQlU0dWNaQWlPNXktcG94c0ZaZ3lxV1JWc0NlYnBzOA?oc=5" target="_blank" rel="noopener noreferrer">防衛省、衛星の迅速な打ち上げ研究へ 故障時も監視機能の回復早く</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月9日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1rcEpsNlowVHNjY2J5RDRvOUw1QzVEd1hGVEVEOVVrdFJ5SU9zRnkzZEo4aGwwVEdNVWtrUGg4MW5ucmdRU1AtS2xzeWRKbm5XQVB2QW5PekswempnUlJrRVhuLUZvMkU?oc=5" target="_blank" rel="noopener noreferrer">防衛力強化へ特定利用空港じわり増加 都市部近接の神戸、懸念の声も [兵庫県]</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月9日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTFBPVG9KNzZ6X00tOXFybHFsQUhwTkdmcldfR0d2MlNya1RQdnR6eDhmM1ZTRW4wcVhBYVBaR1pmX3hEMFhkdkVnaVlaN3BIM3p3OUthelY2QkhaemRGMjhn?oc=5" target="_blank" rel="noopener noreferrer">防衛省 宇宙への輸送能力強化に向けた調査研究開始へ | NHKニュース | 防衛省・自衛隊、宇宙</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月9日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE1INDQ5VVlZQmp5amlYdm0xcS0xMF9hWVgyVjUtSnhfeEFZdlFzV0ZlODZhM1ZFTHVJLWpneUZINVB0eVFNeWZNeXBMdnh3VC1VYmQtdFFoZlZBNDdWemFtVU1wTHlQUQ?oc=5" target="_blank" rel="noopener noreferrer">衛星打ち上げロケットの短期製造、防衛省が調査研究へ…人工衛星への攻撃など有事に備え</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月8日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE5jeEFnSXdHV0FSVXRXRXY2cmt3N3BSQXFiZnR0XzdmbDVlaDRncjJJMkZtVmtjbXFaR0tIR0hBOXJjSUNxSXFQc2tkWmUwYkgxbGtDZVkxWjhKR2dJNHRrS0FXUU5tV1ZuR2t6Z04wMnY0SC1raVE?oc=5" target="_blank" rel="noopener noreferrer">安保3文書改定は「本質論で丁寧に議論進めたい」 自民・小林政調会長が記者会見</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月8日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE1kUzgxazZETTF1c2s4NU5waWJHSGV6WkhzeUVoN04xTGtpeW5SVDhyRU5OQ3MxRG1lUUdfRHg5Z0NqYTFaT3h0RTJOTnpKdDZETGd4T2NCbWhXRVpCT1l0Z3ZnTlhBV3NaMVRubjZKT0V1VUkycUE?oc=5" target="_blank" rel="noopener noreferrer">＜独自＞核持ち込み、緊急時の例外記載案浮上 安保3文書改定、非核三原則は維持へ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月8日</span>
            <span class="source">Reuters</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMihAFBVV95cUxPRzYwUThaOTNBWHgwYlVTcS1zbDBFaEpweHZqdFVGd2FkRDNFX044dnVLLVc5bWdLd29lM3dpZWl5TG9IRTZJa2VjUzA4VFN2MkdjeFZZcWs0UmVjTi11OERkUmpNWHhLVmlGWUNrbkJOODhSR0pWLXJEUFhPdDg1eHI4bEk?oc=5" target="_blank" rel="noopener noreferrer">米台関係、米中首脳会談後も強固 防衛装備の適時引き渡し重要＝駐米代表 | ロイター</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月7日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTFB1eEtYU2NvZXIyYUhNNlBmcVpIYThjaHVVc2MwZm5RcDBGa2YyTkkxc0dmcjBOclF6TjQ5OU9nV0o0b2tXQ1gyS2ZEWnJiREp0dlM0RW5wRG12aWdfdFBOZ2dKOVRIWFFXQ0pKTw?oc=5" target="_blank" rel="noopener noreferrer">スタートアップ参入促進へ5000億円 自民の防衛産業議連が提言案</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月7日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE96Uk1PRS1JUTJseFdGN2FKcnFmdGFlSlV1LTdyY1RqLU16TXJXdjc0dGowV1dxdUdmVE90X0VycTZzR1pldzc1T2MxdE9RM3BlOGk0b09zVFd1OHB4SlJV?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相 スタートアップ企業に防衛産業への参入呼びかけ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月7日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE1VeXhwZGdpd25MSXVONzhqMGtYY1VLSWdMb0ZUU2xPY3lEQXU2aF9odXlXTHZwdnZOdUNGX2NrVHEzZEhLMEpZV0pQTThJTEZKSTRNRm5wRHRIU2dzTURxVUlWWlZlVFh6T24tNUp4aTdua0JmU2c?oc=5" target="_blank" rel="noopener noreferrer">防衛産業推進へ「独法」新設要求 自民議連、安保3文書改定への提言了承 予算規模数兆円</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月7日</span>
            <span class="source">中日新聞Web</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE5GYWtvRmJpNkk1S1IzLWFvYmxVM3lxdEFLaTFPUmVOcTZ3bVQzYU5TOVlrSnpBZzJlSloxQkNtc2JkWXV6alN2SngtMGxIWDFSUnlHZ2NEMkRTa1hxY1RubHQ0RUVoZw?oc=5" target="_blank" rel="noopener noreferrer">防衛産業推進で独法新設を 来秋念頭、自民議連提言へ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月7日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE02VzhMZEhPMWI0OTJrYjZKQjREdzIxSDdxaTNTOTNyMmxBT01oYU9OQUZvRnhaZHRNUERQMUNzVGdPYzFLelFXYWEzLTc0SjEybHExVzRSdVF2a2Vfb20taTN0a0dudzQ?oc=5" target="_blank" rel="noopener noreferrer">「南西シフト」で巨額の税金 防衛省の概算要求、目立つ「事項要求」 [高市政権の安保見直し][安全保障関連3文書]</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月7日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMihwFBVV95cUxQQzI1M1B0c29hRFEybjNkSXZoTGdvUEhKb1lCdjYyRkJSQU9uOHpfZHludEgxTl92ZWxSSER6WlJzdVRZVFY5c2ltM1dhcHRjTGlCZHlNZFhSc1g3cWdNeUlrTU42SXhjcVlTLVEyUHZQMUdtOG9tdnJjWmxvSHJKcjc2NE9vdUE?oc=5" target="_blank" rel="noopener noreferrer">防衛ドローン加速、主役は新興 防衛省も早期量産へ本腰</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月5日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMicEFVX3lxTE54ejFGR2JRMWNILU9vcFpKZWJIOHRQeWdDQWpHYXhjR1oxWVBybmN6WjVQT0w1Mkd6YXN1TS1KdFpjaW5tdFd6R2RZa0VmWGhIVURsTThrUUhSWFNySVNieVFmbzJySzNldmhSVHVER3U?oc=5" target="_blank" rel="noopener noreferrer">防衛産業への投融資</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月5日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE53NngzcXc4cnFSbHpQdEpZcWtGaXZ2TVdsLUx4WHdCVlVJeHE2UUZBUFR2dkVqVXhoV3VKVUFIUktEbHJ0aGF6MXNCMXlURXVLMXI0dUhmT2N6a1RIbGE5MkpGczN3aVZSN0JkbndHTWNwZFY0ekE?oc=5" target="_blank" rel="noopener noreferrer">＜独自＞先端技術の防衛装備実装へ官民連携構想 安保3文書反映、米国の大学機関がモデル</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月5日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiogFBVV95cUxNaXlGRDBpR01DYk1wRVVGd0pSam80RkdFVmF1WG5VVEZNUTJrWFp2Vkl3NXczWDRsU1NuUGhLRkRGRVdRNGo4anFEX1ZUNU5BVzlCMVYxMmxEZlo3Y1VPbWwwSWNhVmU5R3FCMDJzbnU0Z0RYZHUtQUFfVkp3XzNzX1pCcDZSYXkxRXYxTWJoMzdPRVhyeHlVem1zVVVLUTVnQUE?oc=5" target="_blank" rel="noopener noreferrer">独自＞先端技術の防衛装備実装へ官民連携構想 安保3文書反映、米国の大学機関がモデル（写真・画像 1/1）</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月4日</span>
            <span class="source">信濃毎日新聞デジタル</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMicEFVX3lxTE5aZE5UMFBLR3R2YnlvamVVV0F4R3lveXdxaEVEU0djQW5Kcy1PWGFJUVJZM1VIVjlNdHJHSG95OFhKR1hEa2xoYTVqYldkT1BQN1h2NUhWSkYxMVVTbEYtZkg2ckhubnhBZ056TzRUZFI?oc=5" target="_blank" rel="noopener noreferrer">日米同盟と積極財政の行方 佐々木毅（東京大名誉教授）〈多思彩々〉</a>
        </li>
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
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE5HdXR6OHNFZ21GWDRILTUtUjFXTWxFcXlNeHdtU0NKNmpReEl0ZHhhQS1pak5jUUlsN0V5ZWpadXU4bm1Pd2QtU2tJQTEzRERvcFBLR0phbnBXY0xVTDhPeGxMYVF1azBy?oc=5" target="_blank" rel="noopener noreferrer">真相・ニュースの現場から：防衛省「懲戒処分公表時期を調整」 自衛隊に届いた1通のメール</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月30日</span>
            <span class="source">ニュースイッチ by 日刊工業新聞社</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiQkFVX3lxTFAtT0lWV29zV21xdWxHY1FIVVl5N2dUckxDRTRZSnBvMzdZRXNUZUM3UURxNU9SdU9lUU04RDhGdU83QQ?oc=5" target="_blank" rel="noopener noreferrer">垂直ミサイル発射システム搭載潜水艦、防衛省が開発推進…長距離防衛能力を向上</a>
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
            <span class="date">9月30日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE5VdmhXRXhrRk1lR1JiV1hZakU2Q1JRNW1iS1JOVEVGUzhjZi1BbXJIeVNRNnVFUndLZ0lOX3J2X043Q3VqbFNtTUU2ZW9oRTJsaVdjODRVMUczaDE0OGdMeXVrOGx4VDZYanJMVDZ1eUtUazM0Wmc?oc=5" target="_blank" rel="noopener noreferrer">防衛装備庁・下北試験場を捜索 青森県警、陸上自衛官が逮捕された贈収賄事件で</a>
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
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTFBScTVGZDZ0aUxhSkY3cUFKTXZtazE4cW9KMEo2dWZEdklWcS1vZVhOc0tCVFFqc2p6eXZVTzNRMkxsM0d5YTlCMGJBNjVJT3ptNFlQQnh5cng4Y082V1I5cDV1czQtVHFsdWFVMQ?oc=5" target="_blank" rel="noopener noreferrer">振るわぬ米ドローン株、中国製締め出しへ 日本は防衛産業優遇で好調</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月29日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTFBheXExT2JmSVZXN011amZVbnhFdG1EZzctTUtPLWNWQjV3MXBBQTVlbzEwRmNXN1pCczlaS2FTUHVrTVF0OHBXdGFNckx5N0oxdHVvdU9fUEVRSUtWV3R0VjBfR19mOTA?oc=5" target="_blank" rel="noopener noreferrer">陸上自衛官を収賄容疑で逮捕 防衛装備庁試験場の入札めぐり 青森 [青森県]</a>
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
            <span class="date">9月28日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE1sa2w3M1V5bG5Kd2dfM2dKZ1pGQm5aVEVZa2wtVm9JVVVTd2lzZDRnX1I2eWpiVGhPOEJQeXJ3SnppYVJiZG1oXzFFc2N1WERhaS1xRHJHOVNkdmRvVndHWmIyc1k4QQ?oc=5" target="_blank" rel="noopener noreferrer">防衛省 装備品に新興企業技術 新支援制度 公募開始へ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月28日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTFBsN0ZZeHFvbGJkZ2ZqMXZIODFKMzBibVVBLXFvaEVpUHVJSlRHMkdQUm9rSHNlYjhjNXViVG81LUZvcjZOcEtDT0xpTXFMNnFwN1BzcE5kVmgzMHMzZDZtbDFjdllGNGc?oc=5" target="_blank" rel="noopener noreferrer">隠す時代は終わった？ 防衛産業の積極発信に動く重工・電機大手</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月28日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTFB2VmpZenlyQWlRZHNPNjZqajR4TGhzLUVlUm5yYnZYYTFzTlptQUV4QTBsbnNkQk01Z1AtWGVmcVdpTkVzbnBUekJQay11QWpTRFFrX3lMU0NFVFh3dVp3Zk9TSUZBdWs?oc=5" target="_blank" rel="noopener noreferrer">防衛装備品にスタートアップの技術取り込み 参入促す調達方法を導入</a>
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
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiXEFVX3lxTE5vQmFiX2xjckpUMVdaSXRMNmt5ZHUzZDVqRDJUV1FndlcxMXk2bjdxUkMwU0Jqb3NwMkRyNFBxUjdGeHdyU0YzMS0yQ1RnLVFfamVGOUJsOUFWXy00?oc=5" target="_blank" rel="noopener noreferrer">（フロントライン 政治）日米同盟と法の支配 国連で直面した難題 米のＩＣＣ制裁、深入り避けた首相</a>
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
            <span class="date">9月26日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE9tamJIOE1KWnhFMW9vWWg5XzEtcnhObUdad0xXMlBkSHVqeEt6c0NDV1V0NGJmNDZXQmNXX3ltTnZjSmFoVHlEa0U3SmJDWUkwcjVFQ2ExMm8ydldsTFRtWXE2MXNTSDNHeTZ1aVV1U3Rkak9hdnc?oc=5" target="_blank" rel="noopener noreferrer">「日米同盟ともに強化」小泉進次郎氏、米中「同盟」演出の日に強調 対中象徴の米司令官と</a>
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
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE16VC1xNVdVcmR1Wnc1QzVJaUR4aWVURHY5bTUwSzllN1o0TmlybjQ1TFh2Ym1sV3Azc19jcGJqaXBJZzh6ZU9mZkNXdVU2MnYwTjhIUHNIT1oxUFZhcjJrTURLcEREaHFFcnRTXzZFaHBqWU1VaHc?oc=5" target="_blank" rel="noopener noreferrer">先端技術取り込みへ防衛省が新たな調達制度 スタートアップの育成狙う</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月25日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE54aGx3UkRqY1JJRjc5OERvMTRSN19ZWjZGOVBVYVFIbVdqcFdjYUdsSEM2VjZiUmtxaVBJN21fMDlTaXEzUGJQR2o2SEZSTHViY1JmRmFmQmttRzJsZTNVenZkYXBuSUU?oc=5" target="_blank" rel="noopener noreferrer">スタートアップ企業、防衛産業へ続々参入「新しい戦い方」の担い手に [高市政権の安保見直し][安全保障関連3文書]</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月25日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMikgFBVV95cUxNR0R4MHpfRG9jdnpJNHFwS2o5VUNOdGVFVmg4ZlhndUNWaWpBVml3SnhleWFQNlNPVnN3MmJDTV9oRlhLdHBTdXltby1BRUFTWUE0VDU1bld6bVMyZ0hVTDd6Vm81NVQ1ZlhlRHBiRXZwUGNTTTJwbGt6NE4yY2EyTVlYaDRxeVVfaGhqX2xhRzlOdw?oc=5" target="_blank" rel="noopener noreferrer">スタートアップ企業、防衛産業へ続々参入「新しい戦い方」の担い手に 動画</a>
        </li>
      </ol>
    </section>
  </main>
</body>
</html>

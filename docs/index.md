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
      <div class="stat"><span>UPDATED</span><strong>2026年11月17日 17:56</strong></div>
      <div class="stat"><span>ARTICLES</span><strong>70件</strong></div>
      <div class="stat"><span>LATEST</span><strong>11月17日</strong></div>
    </section>
    <section>
      <div class="section-head">
        <h2>Latest Coverage</h2>
        <p class="note">Google News RSSから取得・フィルタリングした記事です。</p>
      </div>
      <ol class="news-list">
        <li class="news-card">
          <div class="meta">
            <span class="date">11月17日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTFBFMklnYkdydVFIa1JVOE5iQWxETkl5eWZsWmhmQkNTbVItLXVxZjgwMjBneS1RWVZ3eExSTEFCSVA5eHFQMWloVFc0NEFTd2R3bGdrN2xyazRzUnp5d2xMRVl1S1JJQQ?oc=5" target="_blank" rel="noopener noreferrer">【速報】防衛省によると、ロシア機２機が福岡県沖ノ島北西の上空を侵犯した</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月17日</span>
            <span class="source">日経ビジネス電子版</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZEFVX3lxTE5vU1FXM3B4ZG5vNXlHQjgxLW5uZzdVd21aZmkzd3JLdEpDXzBXb0E1NDVqZjhYcTFlLUFSSTNWUVlRSTJ5R0c1MHdCek5LNHBQZEVHY1ZKSzBKekZtc29UZEV3WUY?oc=5" target="_blank" rel="noopener noreferrer">稼げる防衛産業 「安い・速い・賢い」で国を守る</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月17日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE9PQXdCTUFSaG4yV0MtVmxsRVczOUh1X2xRVDI4cXJ6TE1FZFdtOERJeXV4UnE4LTZQU05iUFV6QUV5ZWxWNnpFalRLRWRhQWhoV0Z2YUV6VWVOY3F2UlhJWThqSktfTEh6clVBaEN1eWEzRWM1R2c?oc=5" target="_blank" rel="noopener noreferrer">安保3文書改定 有事に「大量に緊急増産」体制 無人機など「予備生産力」戦略に明記へ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月17日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTFBUZ2JzQWtTREk4SUlmWUxQY0Q4WVU3YU9GQTkyREVlTTcyWG9UcFZTQk9VOEo1Rjd2d081YldrMV9MSVY5b214YldlZEZERnR2d1VobTBsVGEzakZxd3VF?oc=5" target="_blank" rel="noopener noreferrer">安全保障3文書の改定 防衛産業基盤の強化説明へ 政府</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月17日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTFBtODN5b1A1OFQtcXN2RElLWlYtNGc0UnczdWZ2TnpweWh0bm9PcS1SRVppOHVvQTBxNTdveW05ZlQ1RE1pS3BsZDlfcVlhZ3IzdXdzQ3pzVVVSbTQzd3dUVG40RW5rUQ?oc=5" target="_blank" rel="noopener noreferrer">防衛装備品輸出、官民一体支援の新法人が窓口…安保３文書改定に合わせ策定の「防衛産業基盤戦略」概要判明</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月17日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiXEFVX3lxTFBVbkluTF9vWXVwQkYyZy1mQmlKOFVvUmgyRndkQUVkdFZHMHd5QWJVdG5YRU1WM2pZMGdJLUZzSTRNZ1dab1IwWlhCZTVWa09tNnJIWGU1UC16T3Rz?oc=5" target="_blank" rel="noopener noreferrer">（安保３文書）「総合的な国力」増強へ舵 防衛力強化と経済成長、一体化</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月16日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE5oekthb21OdG1QRDRYajA3aENEdG05R1dSSGVKYk1fbUMxVHBZNWZsQ3RMbFY3OUM4NnBlQ19OWk9vLXBEdUQ3WElELWtHTXRlMWdFRmpXVG04d2NkcnF6QlhneXgtdmJfVng2Qw?oc=5" target="_blank" rel="noopener noreferrer">防衛費「安定財源を確保すべき」 安保3文書有識者会議の議事要旨</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月16日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE5aZHhpeFpOMV9UVEgxUGE1cUQyTW90YU5ZaEx1a2RfZEpNbGZGMWNwSVNMR0FRcVNpUG1RdEZ6Q0hGV09lVHEtMHJPcU50ZEZQOUEycWtLcmozV0NGY2R4bW1VMEtWS0E?oc=5" target="_blank" rel="noopener noreferrer">有事の備え「社会全体で」 協力企業へ補償も 安保3文書で政府方針</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月16日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE9vY2RlVnhmME0zZHVOYmsxLWJJZXJQOERtR3hqOTNOc2RzWncxR2JUNFkyYWppem02RjR1Y1FsaGE5RHFEVHZHTVJQNG1nZVNQbmlwYkJaVzNoa0JJQkU0?oc=5" target="_blank" rel="noopener noreferrer">【特集】九州・沖縄で何が 防衛力強化の10年</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月16日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE0yYV9nY2tJNHlDTW9EVkpyQ29CQkZDTndMdmR6UVdVRXpGYUxZeGJoRE5RTi1HWXNPVkp3S1F0dEtYMkpWZVdHZXJnekJUZ3BsdnBmTGdXOTljMkJIZXJzYlhXUkdVdw?oc=5" target="_blank" rel="noopener noreferrer">高市首相、防衛装備品を無償供与するＯＳＡ活用しフィリピンとの安保連携確認…マルコス大統領と会談</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月16日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTFBVOGMzejdsU09sR2lRaEhUcXNZMTdWeVJsVlZISXhjUkswRFpkN1BfZGNLNllRT09vMFM0UkhSdUQtYjNBYzRQaFRwMjVHXy0zNjZVazJ2T2JBZXg3Ym1WMnpBY3ZFVVZK?oc=5" target="_blank" rel="noopener noreferrer">防衛装備品の「国営工廠」 広島・呉に建設で調整 日鉄跡地</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月16日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE91N2pTVUZuZXcySDdwSjVUdGdFOXphQjk3dkRBNUJIbUQ1U0hCUFpRcXdnYnY0YWNIRHRYOGs3V0phTEhaSUhxeW04YktEdkVBelJuazJoNFVobkNHTWZPWmN3bk4tcW1PdjNKUA?oc=5" target="_blank" rel="noopener noreferrer">木原官房長官、米中ロ首脳会談「注視」 日米同盟は不可欠と強調</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月16日</span>
            <span class="source">日経ビジネス電子版</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMijAFBVV95cUxPYXFfdElnYTBjWHNqcDNPeXJ5RG54WFY2eXVOeTU5am5LSUVtTjVKUFNsYW9sQXRtYkNfWTRwa0p2bjh5TmNDUzNnc0FsNzVwSWJyQVFnazNtQ2VLRjFFVTQ2YlJBNHMtWTBrWDZHd1lsdWMzN3JpY3BXLVVVQlFTckRSRGVMU1NmQlFzRw?oc=5" target="_blank" rel="noopener noreferrer">渡辺元防衛装備庁長官「スタートアップは技術ではなく課題解決ストーリーを」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月16日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTFB5SFlHWnZtN21pMUNJOEFJeG9IUy1qc2JMMy1WdE5MZG9uSXNpc0FRTWVpVjZ0di1EZXZMY0ZSZU1kZmxBOE1EeFJfQ2taa2xJODlPeXF2d1hmRHd2T3RGZ2NpTQ?oc=5" target="_blank" rel="noopener noreferrer">［安保新時代］防衛省、ＡＩ活用新方針 月内に策定 空自警戒管制に導入も</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月16日</span>
            <span class="source">日経ビジネス電子版</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTFBuaHNjM0F5NzI2dDFUYVJ0OC1XY3NYd3dYTUNfTnJHN2x4SnVhelpOSVM5TVJMWkxpcXM1aHVlelExeHBCNGZDN0NQZUh3LTFDQVpzRm9IcGJUQi02Q255UVJVc2t5R1E?oc=5" target="_blank" rel="noopener noreferrer">渡辺元防衛装備庁長官「スタートアップは技術ではなく課題解決ストーリーを」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月15日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTFBYM3hXMEpGZlc0clVScF9QV1RtNDREeFJrYTJ2eEFpcVFzOGNnZ081QnFQb3g3UUZieDFiYzlsTlVvcVI1aXdUTzdlNlBWaGFtV3ZOaG5DMkxhWGdIUUdIS2wwV3Vtdw?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相、ＡＩ基本方針見直しを表明…「ＡＩとデータを実際の防衛力強化につなげる」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月15日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE9yQncxMkZDTEhDUFFqNTc5MnF2aDlfOWtPSXk4WGdVM1RhNDRFQjNnSFFSUEdzVXFoRUUxOGpRbkJKaVgwRWNjeHRRbXV6SlVqckpkMkk3SEg3WlBMNE40bDdSM0NsRkhPbEJ3QTRRYlR2YWlpdGc?oc=5" target="_blank" rel="noopener noreferrer">非核三原則「持ち込ませず」に緊急時の例外規定 安保3文書改定へ検討も…議論は低調</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月15日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTFAxMWh4MEZnN28yQUZ6MlhjVUV4Q0JMd29CSkxQTkFYU0d5QjJGaTRLakw2YXFMYTBrRHdxRXFtRXA5SVRKUTV5N1NyZzdRX204V0NIUHFGc0hBYnVzcmdCT0xiTQ?oc=5" target="_blank" rel="noopener noreferrer">防衛省ＡＩ指針、月末に公表 小泉氏「現場で使えるものに」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月15日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMigAFBVV95cUxNY2pPVzFxOGY1M0FfeUpuanVHZ0dRdXZmNlJ4OU9GV1NGdFMybDRQdVdWLTVBVUVzMTNxczIxbXIwcUl1X1lzR0xvTHBYVWhTYTQtN2FYdDFRUC1ITDNNel95VTVzVzN0OUg2OVJfMzhfOVFpdkQ3NkppeGJtbTB2Vg?oc=5" target="_blank" rel="noopener noreferrer">防衛省ＡＩ指針、月末に公表 小泉氏「現場で使えるものに」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月15日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE42ZnRNQlN2bm5VVjlwcEJnNzVyQlVXZkVpd0lnQVZWalZ4eTB2T3FSVnlXWE9NLWRsZVJJajBCUXBvMW1QMjZMaGFSbDV4dzMwNEdIX3pTMk9pSmItUm0xcVVrajlCY0ZTZGxVTA?oc=5" target="_blank" rel="noopener noreferrer">［社説］日米同盟の真価が試される外交の正念場</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月15日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTFB6ZVVGdFpXSVg2QzlLR2Y4c0ptbThoOTZXcWJEekl2Q1RYNnpreWswQksyR3J1aHRIN01DYTJmRUNnWng5U3dtY1BELUdpT2RkdG9iRkFpbW5XUzNMdXJmU1BtbGhkR1k?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相、防衛省・自衛隊の新たなAI活用方針 11月末に策定 [AIの時代]</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月15日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibkFVX3lxTE9kNzhQWlBuRzh5SkRORjVmZjFZRmFEZGY3RE0zQzNxdXZ5WVRSTVE3R3BXaEFMbGZFSXpxX2trWTBSaU5EcHpxMDdsNEJ0LWtlVGFxb3BlVk9hTmZUSTV4bW9EckdHM2NIdkl2Q1FR?oc=5" target="_blank" rel="noopener noreferrer">非核三原則「維持すべき」75% 武器輸出「反対」67% 朝日世論</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月15日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTFBFaGJJaC1DX05BY2NOS1hsTXZFOTFsLThLVy1kYzkwaDFRU1hzQ2oyZU9mQ29pbDU0WGF5UlhjOXpzVmE5WFFhbTdBM01LTi1pVUdEZG5vM3ZaWVFYaGJr?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相 防衛省の新たなAI活用基本方針 11月末めどに公表へ | NHKニュース | 防衛省・自衛隊、安全保障、ＡＩ・ネット・ＩＴ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月15日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE4xVXpYeUtncWZieUJ5Y0FkTG9oN1Z5UUtPRU9OaktUNzF2ZFNfTnJYeDlYbUZWQ2VrZmdReEljWl8wRjZUb0t3TE1SYm9KdjIzUWhpZWN1V3F2NnpDZkRWaUpKc1JKV2Z3U1JfRw?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相「データを日本守る力に」 防衛省が新AI方針を月内策定</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月15日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE9yNHBoNWpkVXEzYlBJTDJhQU53TGhtX1VaclpWNktDVk9iSTdua29EU0dIQnl6Y2pJNmJhNE9QMlY5U3RIaTVLN3dyeEwzNkstcVlNT1h5MkgtQnpuLThz?oc=5" target="_blank" rel="noopener noreferrer">政府 安保3文書に「歴史的かつ根本的な変革期」の認識で調整 | NHKニュース | 安全保障、防衛</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月15日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTFBvRXdFMWs3LTFRR2NwRkx1a1F0SzBXNTR1LTU5VGRhNnB3VzZTZ0lUTXVsQVZZdU1DQzY3aWtZSG9SZFh1M1B6c2F6SFdsaWhQczhBd0IyZmVpRmdLYklMdmQ2bVdmZklZeHVFWmRHWmphUi1xNGc?oc=5" target="_blank" rel="noopener noreferrer">＜独自＞防衛関連経費に「戦略分野」 AI、エネルギーなど 安保3文書改定で調整</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月15日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE5rYlhDc0JxclJoQ0JVMC1KU3VjSjBKNmp0VVVXUXhxS1hWa3NzMzVoOXdmZ2RGTDNPdzZKdnVGYTc0VlMxa1ZqOWxBbnJKaFVjbUJMNm5tQTh0M0I3bDRraVBLRDh6cDg?oc=5" target="_blank" rel="noopener noreferrer">社説：防衛装備の研究 大学との連携をさらに進めよ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月15日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE96dWR1VFg0UFZqSDdleTNqc2VKMG8wd016aE1qRUdIMHI4QUNSZGlaanFBcGNDcUNpbFFlN1llSFBzMlZiNmZuc0dWVmVJZ0xpTmhWcGkwVTQ5ZV9mOC1qeUw1MA?oc=5" target="_blank" rel="noopener noreferrer">［社説］防衛装備の研究 大学との連携をさらに進めよ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月14日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE5YeHlxdXAxSVV1N2hTR3owdG93SDducDRjVHpLSUxRbzdDQ2NXempjMUtTQTFXOUEwSjdzVEdlMlVhZHVxbF9PTTFoSDFRZnkxdkFXaXR1X0NVWUVlazJPMHFDVE02Zw?oc=5" target="_blank" rel="noopener noreferrer">米中露首脳会談は「冷静に見極める必要」と自民・小林政調会長、「どういう状況でも日米同盟が外交安全保障の基軸」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月14日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMijAFBVV95cUxNbFZPSnl0NTJpUmdYYnRGVEItOW5nTEFsTjRmZmZhN3J4Y1pSdFFwZ2VweFNWRUdfVU5hTnBWdThvUWJUUVVySUU4a01KZXVQel81dDFWNHJYR2tCRW1xdjFhT1NZN0dNUFJDSGc5OExTeE5BelBSRHMxTFNISFF3WWFnbS04d1R6WGwxeg?oc=5" target="_blank" rel="noopener noreferrer">安保3文書「同志国と実効的連携」集団的抑止力へ強化 防衛省、国家防衛戦略に方針明記へ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月14日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiogFBVV95cUxNV2pxS2NGb281NUVOS09rRWFsY3VIcTRsU09hVUl2aUctNjlGM2ZnV2c2VVBkRmNzY3R4aFlSdlFzdjl2MWZNc2J3UUJaRm5wYWM3ZkZIYUlxN2wtbHI5Q1FtX2x0N2Itek94TzA1ZzhJdGxucUpWcUtPR3VpMEljZFVONENlTEJBazMzS3hfQ2JUSWExbnAzMXhHYXNuWDE1aHc?oc=5" target="_blank" rel="noopener noreferrer">安保3文書「同志国と実効的連携」集団的抑止力へ強化 防衛省、国家防衛戦略に方針明記へ（写真・画像 1/1）</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月14日</span>
            <span class="source">信濃毎日新聞デジタル</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMicEFVX3lxTE5UNDh3Q29XZDF5S1JHYjBWakI4RndxREJCcTBucGlXdWU2RkxaU3hKMG4ySlRkbVVYbXAxdG5oMjVSTnRteUZaSnZkN3VWRGxyN1BGamR2ZjRybWw5ZXdxV0tESmJlQVB4aDFQNktyU1A?oc=5" target="_blank" rel="noopener noreferrer">〈社説〉安保三文書改定 地域の安定損なう危惧</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月13日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE5ZNjhkQm9lSjgzVHZ2aUFWY01tdkJqZWJtZWt0RjFaR0k4SERTcmNHVzVTOHBsZ25lc1ZXa29ZaU1DVUl6VEZFRWFkdk9zSTc5OHJqWGZGcmpsam54UzFXRFB2V09qWmM?oc=5" target="_blank" rel="noopener noreferrer">インテリジェンス強化の記述大幅増へ 安保3文書、国民監視の懸念も</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月13日</span>
            <span class="source">Reuters</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMigwFBVV95cUxPNERlTjN2OTV1Q21wREpLMGpPd3RVTmdsaV85ZE9UTDJfNkExUm5hRWk3dU4tNUFkSXVidHJ1dUlUS3UtVjV2WTRYME1EUUNPTEtTOHhPZXVnYlV1T1ZiYkRpSWJYRW5vZjJJLWVkSWxyV2hubW1xZXdjeW5nNUQtTzB2aw?oc=5" target="_blank" rel="noopener noreferrer">防衛費5年で50兆円台、財務省が提示 防衛省は調達削減を企業に伝達＝関係者 | ロイター</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月13日</span>
            <span class="source">日経ビジネス電子版</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiiAFBVV95cUxOZG5ZbFR2cXB4bzNnWWVSWnIxdHFSbkg4aEIwNF9UUHFzeS0wR2lzbE5VbTRaRVd5M2xSVUlfZzNla3lONVU4ZEhLd0FrRmUtOU44WkFheUVxbXR5TDdCZ2wyVUotb3RSTm1oRmRYYnM0d242RDRRNTk5UV9veG9nSEZJY0hPdDJ2?oc=5" target="_blank" rel="noopener noreferrer">［新連載］防衛産業「安い・速い・賢い」時代 テラドローンは参入5カ月で受注</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月13日</span>
            <span class="source">日経ビジネス電子版</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1LMjFJV1l2RjJqMUxSUW83eHRVX0FmUXdnUjgtQ2NSOHpnTXNja28tVlhPYm9MYWs4dUlCX2gzaFRsejNlSzFoWjFibVZQTm5FeW5nNnZrcXNvTUItajVfWF9OWmhnVjg?oc=5" target="_blank" rel="noopener noreferrer">［新連載］防衛産業「安い・速い・賢い」時代 テラドローンは参入5カ月で受注</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月13日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE4wdXRWekJsN2FIV1BqajBZY2xzQXQ4Z3dXcVpqN0NtXzZWbDZnYmlJNHdPWWEwX1hnVmlEUnlwZllsb0txeVRTRDVUZG5UZkJrU1pTWUNxYUtfSW8zTGJGX3VOUUxuUnFjVmZUSg?oc=5" target="_blank" rel="noopener noreferrer">安保3文書が映す世界の激変 改定の軸はAI・無人機、半世紀で急転</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月13日</span>
            <span class="source">日経ビジネス電子版</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiYkFVX3lxTFB3dXpwQnNUZTBfa2V5ZjZZYmFKU0hwaTNnejhnRFQxelQwOXFEUGEtVVVLZWJLSThRem8xbXVUV2VCay1QcDRsa3ZtZkVKMXNvdEQyWUplbGc3RWgtZjBvTmVn?oc=5" target="_blank" rel="noopener noreferrer">防衛産業育てる「資」と「志」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月13日</span>
            <span class="source">日経ビジネス電子版</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZEFVX3lxTFBrNm1Da0hmU1V3ZldNV3BwaTNFSi11WC1VZDJjeGtENnNsS0dQcGhUNDV2SjRLNmpJZUJiQ2o2R1BqMXA0akNGWjdKbXNKNDAtdmRDaDlPak5qYWRid1BBanpxcVY?oc=5" target="_blank" rel="noopener noreferrer">渡辺秀明・元防衛装備庁長官に聞く 「技術そのものではなく、課題解決のストーリーを」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月12日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE9rVk5uUEtQMm5TT0c5ZHJtM2QzVHlQNnJLZEdEQ2VMcVJWSWRra3BnUlFITG9nTDNQSkozN2psMXBjV1VoTVRLTTFONEtxRUNCZnBQclpiT1pKUUtuLU1J?oc=5" target="_blank" rel="noopener noreferrer">防衛力強化と暮らしのはざまで &quot;安全保障の最前線”沖縄でいま</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月12日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE9yd3pBLWZkRHlvQVFTUlFUc3g3UnEyU0NsUndkY3J3MDQta2RhU1N6UjFpRkw3WmZPZFdlTXJaekhDTHFQRkdNQzYzYTZVbEd1RVAtSEhzdVFYQXVjSVRN?oc=5" target="_blank" rel="noopener noreferrer">安保3文書改定 維新 前原氏&quot;自民との違いは与党協議で調整&quot;</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月12日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE9ySEJEMmZEeUc0TjhNeDVqQmVrVU9SVFpYY0YyUFNqbm5lNGFqbWVqTDlqUUdMQ0dQd25nN29VcEgwTV95eUNSN0pHM3gyV0RRazlnakp6OThzbEVvMG9N?oc=5" target="_blank" rel="noopener noreferrer">日本被団協 安保3文書改定 非核三原則の見直し論点に危機感</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月11日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE5oTk9aX1hCckloWkllaEpZcG9yQ05IUUNVTFlEUW1hT0JCa3psOVpfMnNNNS0xUkpURGwzUURmb0ZRbnhSTm16ajdtUWtRRUMtS2pMQk0ySTVteUVhSW1ETm5GaEpxQ0NaU0J3Tw?oc=5" target="_blank" rel="noopener noreferrer">安保3文書に「集団的強靱性」明記へ 同志国の経済安保力を強化</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月11日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE9yWXZ2MnJRWlp3RjBwdmxpWVdPMU50U05Ya3VzRHNSWUI2TUd4Mm5PbXdoOThWd25maENEek1LYUd2WVJlLVUxM1VtSnVueGxvUGpWZGNwU3VFWlh1ZGtsaEtNZDFKdFU?oc=5" target="_blank" rel="noopener noreferrer">非核三原則「持ち込ませず」に例外明記 政権が安保3文書改定で検討</a>
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
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE9sNVlNS3JaRF9uczJtZjNlRmNvV0MyWGMyOEFNTjgyZzFnZzFXb2hoUFU2dGZRbnp6M2VtRktwSVk0UzB6M2RCNHRHblhmZ0pzZEJEZU43ZF9sWGRBdGkwbUlHdXU4Z1k?oc=5" target="_blank" rel="noopener noreferrer">原子力潜水艦、導入視野に検討へ 政府、安保3文書改定で調整</a>
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
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTFBkd2ZUdUIxa2NnNGJkUXVoek5JY3RxcUppeVlpUFFPRnNVenhvYnhCNVloWlA0UHZ5Ti1RVXNDMXNWYk9SZmtBQkNIU3dKM2xJSmxHYm9ObmExMXNNN2dJ?oc=5" target="_blank" rel="noopener noreferrer">安保3文書改定へ 政府側が防衛力強化の方向性を示す</a>
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
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTFBmNDRqLVc1RUxhd2JNWUJWLXhsUXREWEZSZlVDTDBDQjFCeG5YMHA2ZWRDTVFTbXp6MXc2NzVOTlh2VXlqY2dEdHoySHFmV0J4RUpYdnVKMkxabXpiaUlLcjhVRFBLZE0?oc=5" target="_blank" rel="noopener noreferrer">「ブレーキ役」不在の影響は 安保3文書で自民・維新が与党協議へ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月10日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE9EeVZRQmRwOW9aeDJMMU9oZjdKeC1IVDljT2c2eXZ2cWRaZzROZDlpSkJvU3V6cm9GbDI0QU96LUF2TUc3UXdZc2lmRDFfLW15ZEZOZURVdE4wUXNSV0oyTUlUWDVnNVE?oc=5" target="_blank" rel="noopener noreferrer">防衛省、AI活用の基本方針改定へ 「AI主権」盛り込む方向 [AIの時代]</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月10日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTFB3MmxXQktMa1ZsbFNad1l4Uk5XbVNkVTBpZXhqRjdhRkN6czkzLU1UZUZiOXBaTkl6b2o2U1lkZ1ZEQmVXSFJnMkF2M3ZodUFiaDNLVnVRaHB4SXdUdUhtMWJvSjhkUQ?oc=5" target="_blank" rel="noopener noreferrer">比に沿岸監視レーダー ＯＳＡ初 完成防衛装備品</a>
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
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE4yemxIV1QtY2VyVzBCLVhJcUtDdlpoQXBzLXhSakxKQjBnM0FMUUJqX2VYczF4RWNraGFQeGtobnAyT0Z5RDREY3daOFRtbnk5XzdvcWk3UGIwWmtSMVpHdjNnQQ?oc=5" target="_blank" rel="noopener noreferrer">防衛装備完成品を初供与 政府、フィリピンに監視レーダー：時事ドットコム</a>
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
            <span class="date">11月4日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE1Ta1JoaEF2REdwU3FncVUtbWo2Z2JKVUdKUUhubEt6cGo2UmFfNjBBLUtzaC1lUTVPSUtGRUhLV3IyWGtvTzdwSDBDN3FESjZRTWFPN3B5eTZ6a3lGRU5MM05nM0dTY210WW5qZw?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相、防衛産業「有事見据え予備生産力を」 新戦略の策定で</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月4日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1yOG9jQUxRa3o2bEM0NE1YWW0xcXNZYzVVLVF4aHFQdUNWUmdVd2paNzlWQTVWQzFDM1ZNYlpfVzNxU0UzZ0g5MkpFUHJWUm1sUHhKZnhCN1o0U2plVlFzR1l5VFk0Q00?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相、赤沢経産相が防衛産業と意見交換 産業基盤の強化めざす</a>
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
            <span class="date">11月4日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE0zS2hpVVN6RTlRd2JCMFFTNGFIMU1jekY0c1pHdnpIZHBIYUtPMi1ZVWxoV3FoY3p6dlktWGJfaXlMSE9uX3g0U1BtVi1BT1FuTnI1MjNBR01scDBaN0VZ?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相 防衛産業基盤の強化に向け企業に協力呼びかけ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月4日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTFA0eFdWUVpBTzMtTXA5UXUyU2c2eHF1QkYweFNzVklfbUNnaFQ1bnFTQzI4YTd4UktPb0E5d25TdWNTZHlaZEFTb083anZnZ1FUNmcwZTRLdTFNeUhONDlR?oc=5" target="_blank" rel="noopener noreferrer">木原官房長官“米中間選挙の結果に関わらず日米同盟は基軸”</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">11月3日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiXEFVX3lxTFBpUTE5UnlCSklHdHNGT2U0c2hXVGZPTEcxLW15elRITndRRmZTZkNiRGs4Q2VUMHF4TElkSUtHUzEzTjY1ZG8wOVZTX3A4RHJvU2ZGak1nWWxJSy1T?oc=5" target="_blank" rel="noopener noreferrer">武器輸出へ政府前のめり 「何でもかんでも候補」自衛隊不満も</a>
        </li>
      </ol>
    </section>
  </main>
</body>
</html>

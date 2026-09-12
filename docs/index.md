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
      <div class="stat"><span>UPDATED</span><strong>2026年09月12日 14:32</strong></div>
      <div class="stat"><span>ARTICLES</span><strong>52件</strong></div>
      <div class="stat"><span>LATEST</span><strong>9月12日</strong></div>
    </section>
    <section>
      <div class="section-head">
        <h2>Latest Coverage</h2>
        <p class="note">Google News RSSから取得・フィルタリングした記事です。</p>
      </div>
      <ol class="news-list">
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
          <a href="https://news.google.com/rss/articles/CBMiYkFVX3lxTE5vSFVEQU1yS2REM2l1ejFuUkdDdW1Rai1McFJMV2FveDVVaVRpYW1waDU2dWlSOVZ1bUo1RFFYNUJ5N3d0N1RGYUFtSmltUGJPS3A1bmxKWWNJVGxOUXAwMnVn?oc=5" target="_blank" rel="noopener noreferrer">米国防総省傘下「災害対応・人道支援センター」所長「日米同盟の絆は、一段と深まっている」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月11日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE5sQ1lFQ1hJYjNkSFpmY0F0RlYwWWVOR25EdWNBWlZJYm9iSHQybXJ4aG5JWF9pZnRvVTBEUVVNQ2ZaMUY2ZXZHSHhzT2hLcWc0Z1ZzdXVfQVVWTDlKekxHcWFkeDMwTDQ?oc=5" target="_blank" rel="noopener noreferrer">防衛省「複合防衛拠点」イメージ図を提示 水上・水中無人機製造など [広島県]</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月11日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibkFVX3lxTFBGZ1NyN2huRjcyc3ZlRFJibUthOUV1MHFMZmtTdjZTNDhGMFN1NDNQVU5FWV92VEVQMU9hVzRhS1hGY2dzc0pOYTNjZHFJcUFZejdaM211S0VZTmgzSnpSSEdJN19pNENzb2FVdTFR?oc=5" target="_blank" rel="noopener noreferrer">防衛省「複合防衛拠点」イメージ図を提示 水上・水中無人機製造など [広島県]</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月11日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiWEFVX3lxTE1ya3pwSUZ6TjFOUnFqRktId3p0Q3F3dGN6U1FLZ0lLVHJURjVNSkF6RTJWaklXZ1VyVU10Nl9fU0ZKVEJLcnZvcEYydGJ6WEpfZm9oX29wU18?oc=5" target="_blank" rel="noopener noreferrer">呉の製鉄所跡地の「複合防衛拠点」計画 防衛省が県や市に説明</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月11日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiWEFVX3lxTFB4bFJFNXJIQ0k3SmZha21aU24zekRBcHdzNnloZm5yRzFnRE4xczVrWHJqa3pBRlg4VXhTRmdOVHNUaVg0cjc3eGQwR2Y5N2hwOUhfT0RxNlI?oc=5" target="_blank" rel="noopener noreferrer">製鉄所跡地の「複合防衛拠点」計画 防衛省が呉市議会でも説明</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月11日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTFBKQkM5UlpSR2M5cFNxSXNVS2N2cUNVbVdyZ2dhcXY0aWVNeG03VkViaUR4b0pZUFZNSTdCelYyWE9BSGc2b2xGME00ODdGN185RTdldkp0bmVzNGZiZWdkeFhrakZfMHg2RC1nTQ?oc=5" target="_blank" rel="noopener noreferrer">ドローンや弾薬、有事増産へ設備投資を助成 防衛省が法改正検討</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月11日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE9hSXZ3MjEwX0hkUEpjWUdyUGhPcmtyU18xaWRzV0ZBVkFjZUpMS1l3cUhnSEQzNXE5V05ubDMyUEgtX0ZqLXAtdlE2c05UTWlTYVZlUTJFdkFiVXJBVmg0TXRESVlUd216NW1ORA?oc=5" target="_blank" rel="noopener noreferrer">呉の日鉄跡地に複合防衛拠点、防衛省がイメージ図 28年度以降に整備</a>
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
            <span class="date">9月11日</span>
            <span class="source">Bloomberg.com</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMid0FVX3lxTE5qS014c2paNWducDhmUHBzWE9CZldjRWp1UHJzbHBuUDBLOFNzeXJQN0NhdFJpZjBkUmZxQnEtSmhWWDk4VVo1eEJLZVVHSElwSnZ0MExhVElhU3FiNUNxRnBma0xqYm1oWnAyOWc2TXEtMnE5dnhN?oc=5" target="_blank" rel="noopener noreferrer">沖縄の関心は「基地」より「経済」、県知事選で薄れる防衛力強化への抵抗感</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月11日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTFBub0t1MXJWZGtfaXhUTVVQSEtKRVNOTXM1a3puNHZfZW1helJyQnI1Zng3TUpBczdpQ3Bzd0dHN1dpRG10SER6RklBSG9HVVI4R2d4S05jNjFfOERjVWNWTDJ5TGNaNXpNdnNqeA?oc=5" target="_blank" rel="noopener noreferrer">ウズベキスタンに戦闘機売却 中国、武器輸出先を拡大</a>
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
            <span class="source">ニュースイッチ by 日刊工業新聞社</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiQkFVX3lxTE1HU3N6amZ6dHFISG9jX0t4WW0xc3luQ1NCdUxSMHZUVVFkdWN2UjN1R3RBQ3dkRnJoWTM5eXQ0NnhKQQ?oc=5" target="_blank" rel="noopener noreferrer">防衛省施設にペロブスカイト太陽電池…積水化学など、防水材一体型で実証</a>
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
            <span class="source">東洋経済オンライン</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiUkFVX3lxTE9TNlRCVzRDOHRMMkRGM096Qy1kMEpWMG5wYU1uVHRWQVp4U1phT2ZvdkhuRktKdkdUMC1OZFdDZDBKN1dmNEpDcjhGUExuNkpRdHc?oc=5" target="_blank" rel="noopener noreferrer">防衛省による国民の目を欺く前例なき160超の事項要求､｢事項要求｣で10兆円に膨らむ防衛費と文民統制への重大な疑問</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月8日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMickFVX3lxTFB0aVFlbTdQUmh3Z19LQ2Z3NnVjWnRuNGhtdUUtNDh1SVNqeTZta3hrUTA1OXpQYVVtczI4NnBfcTFOVHY1aFdDalo4YkZSUkVET1BDWlY3bzNPeVNRMnBfYnNvNU04d243YU1ZWUxZQVp3QQ?oc=5" target="_blank" rel="noopener noreferrer">南西諸島の防衛力強化・南西シフトに「一定の理解」「さらなる強化は不要」…沖縄県知事選挙でも注目の争点に</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月8日</span>
            <span class="source">Reuters</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMieEFVX3lxTE8wZDFmY1Z5ZWk2OFJWNXpsdkt5dEg2ei1ucFo4ZVVxd2pIWTVkdTlmZ2R6cTJfTTBJOFRHUy1NNXg4YTlvUER2bmtBTmZtVkgxSnFJdFF4YXd0Y1JTdlN4RUk1WTJaRDBHR012cHN3ZG1SUFgzWTRNRQ?oc=5" target="_blank" rel="noopener noreferrer">ＶＷ、オスナブリュック工場売却で暫定合意 防衛装備品生産に転換へ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月8日</span>
            <span class="source">日刊工業新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiWEFVX3lxTE03WkxTVGozdk5SSllsbDVwaHV4YUZzck53ZmxXaERRNGYwTlBkcnRIcFRKd3R1MDNJMWR3T1lyRzM3TjdjNHFSdGJvRy1Mb0lsRGhfU1NRbFo?oc=5" target="_blank" rel="noopener noreferrer">積水化など、防衛省施設で実証 防水材一体ペロブス電池</a>
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
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE5STm52MU9ZaHp4SmlGeFB0azE2aU9KOFp6WVBubXMtMWxkd19IWnotS0NkV2h0Q0o3dGF3eFhYUmF6OHlneDVQNFJJR0RPNkFkTlAtSHpxTTJ5TXVtLTNrUWc0aw?oc=5" target="_blank" rel="noopener noreferrer">［社説］防衛装備品供与 同志国との連携強化に繋げよ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月7日</span>
            <span class="source">時事通信ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiVEFVX3lxTE5BWmJaSzQ4QUhhTHI0c0Q5aHFiSms4ZHB1dWRFTnkxWS0yQVFYc05KQzV0VmdIQ2VnTFFIcC1oenA5U290LU9qVU1fb2U3b211WlZtMg?oc=5" target="_blank" rel="noopener noreferrer">独ＶＷ工場、防衛産業に転換＝イスラエル投資会社に売却へ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月7日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMigAFBVV95cUxQcDFTQ044Q280OTVzM0tXYW5IOVA2SWEyZm1nY3RTb0xBWkVseFVSN0MyYTJZMjNzZVRkUVNkVTF4OXdpOGkyUXpDQVFfa0Z1Y2JZY1JaMHVVSzJ2T0w3akFBMHRFQWMya1hjRmNORjFySFBjZXd3YVNZLTZ0bXNsag?oc=5" target="_blank" rel="noopener noreferrer">独ＶＷ工場、防衛産業に転換 イスラエル投資会社に売却へ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月7日</span>
            <span class="source">東京新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiU0FVX3lxTE1faWRZcHZFdkpKMlBtODRfZzhkNUx6Z0hONDdwSlZfd2l4YUpYcEpXeXp6VU1jakdRVkU5REo2YkVpUm9mWk5VZnBPTDdZTWpxalNz?oc=5" target="_blank" rel="noopener noreferrer">政府の武器輸出政策を問う 24日、明治大で公開シンポ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月7日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE1qYWVRdEs2QjF1RFNqQ1FuUEpEeG5KUFhYaUkyNWh6OV9JRWMyYkc4N1FQREpqcVgtNEVWT3d4OTd6cGg1N0ljNzkxbUtIZ2t4Q01XR1pWNzhpWGdYSjRPLU40VQ?oc=5" target="_blank" rel="noopener noreferrer">防衛産業へ投融資、銀行が苦慮 政府が要請、政投銀は制限撤廃も</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月7日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiggFBVV95cUxNVFVzZlpsdHFXdHlTZ3NLS1F4bE5UVzBTU1dEUnVyMXdSUnFzU1NXZTJuMkZNVE92T3UyTnNXQWt6aDJ0c1VjTk9QY1RqbzFZT1BKRVZUTnpZekRxejE3bVAtYjBYS05jTXBLOEZoR2FhQTc0V0NPWmthUlBSN3lsamdR?oc=5" target="_blank" rel="noopener noreferrer">防衛産業へ投融資、銀行が苦慮 政府が要請、政投銀は制限撤廃も</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月7日</span>
            <span class="source">日経ビジネス電子版</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE9wczZpNEpwdENvaFJ0U2ZjOXg4aURSbUJtS0NHaDUteGprZkhVRDhEczRfaW9DNEZsOHhXNGp2dkxfeVNRS1hCT2VuS2xxNTdWOWRueDlTYmk1RWxHTElNNVZNWVpxT3M?oc=5" target="_blank" rel="noopener noreferrer">笹川平和財団が提言 「防衛産業は防衛力そのもの」を具現化する法</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月7日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTFB2cHRVOUI0clNHV0VWT19WdE0xSjcyUTZFdnZGTmFIeVowMVZaLVozOWxKM1pBazRtQ1lQX3JIR1k2RkdkTFM4TmtzNXA1ZGtsbFluTnlQX05hRzN5eEc5VlBqWVVFSzFh?oc=5" target="_blank" rel="noopener noreferrer">「防衛」に新興企業（その2止） 「商機」に沸く防衛産業</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月6日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE9peWFzb25jZzRreVdwOE9ocThmWFBLTmlGZWhBOHB4ajJsUThRSTlXQzZxUW41bXd2by1IeWxaZnloOFpCVlJFSWlpWlVHMFdiUUkyX1lJRUZJTktKcGZpOHZxLUp3ai1heFk3ZQ?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相を続投で調整 内閣改造で首相意向、安保3文書改定を控え</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月6日</span>
            <span class="source">時事通信ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiXkFVX3lxTFBpM3h0RVQ1RjZHdTJMU0hwQVdLaTBSR3U2Y2xDYWNKaW1kQTY1cjRfaG1PYWlBenlNSHV5aWp5Z3A0Z2wwRUZ5RHNqZzlGenowRndxUGdRU1VydXRvOWc?oc=5" target="_blank" rel="noopener noreferrer">防衛産業へ投融資、銀行が苦慮＝政府が要請、政投銀は制限撤廃も</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月6日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTFAxcW9jMlQtOU1BMVZCOFkza05LNzI2Qm1ibU5CSGVjcGQtZnRxU21uek95dmQyLVZNbGNlZXJOTndieHk1aHNlLXpodWp4amhWT3AtMUpmRGhRSWh3b21WWGFqYThhbzg?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相を留任で調整 内閣改造、安保3文書改定を控え継続性重視</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月4日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE40M2lhZ1U2SEhvaWR0QWtUOFljdkNDVV9EOHpWX0thR2J3UXh1OXpHZWJsRE9VNFRON0VpUGpJTmFnSWp3Wk1SaWs5UGE3ek5CdTZDYXhaZHFjb2lRdTVSTzVRZ1RsWEU?oc=5" target="_blank" rel="noopener noreferrer">防衛省、イラン情勢受け「AI活用必要」 安保3文書改定に向け</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月4日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE5mWGtpaEZiV09uSzcwVXpfU3JYNldkN180ZEdCaHg1YjhMcUhyQTJGejVDbTk4MVlPdnpxd2lSTk90ZDZCdjk1b29XX0tVRXM5MllNcTVsVjZURmlZbFJKSm1EWmFSQThJLW1JMA?oc=5" target="_blank" rel="noopener noreferrer">防衛省が「AI衛星」開発へ 監視情報を宇宙で解析、迅速に反撃判断</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月4日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE9ic1J3UVF0aVA2LVBWWE9RQzRydXVSNGFDSnNyS1VMQXNFZEUxVzRmVmVwdWp5RE1VQ1BRWkQ0OHNYMENHVWNkMXNSVzhiLUNWWVpjNXdrVGFtSlQyeUJmTVlpYw?oc=5" target="_blank" rel="noopener noreferrer">防衛省、ＡＩ活用重要性訴え 米イランの戦闘分析</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月4日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE9IRXl3U0hndmo3MzNab19hU3JvQjFoeERGZDN2QzJxUlU2MlVkNU01SWFaZ01jRlB3cm1EdUQyTFlpT2xEYmZ4VGtCaUk1R3g0ZVVSZy1qZ3RFa2NRUzJUZG1RTFNVNUNVallSeA?oc=5" target="_blank" rel="noopener noreferrer">防衛省が米イラン衝突を初分析 「無人機と地理的特性を生かした戦闘」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月4日</span>
            <span class="source">時事通信ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiT0FVX3lxTE5TQ3F1bk96NDgyOFJlTGFwQzdGV3VFNWJaNU9JaUE4MkhISEIyR3NXZG44UWFPV1dZLVZ5Q3habFEyWTVQTWZuN2dFWmpIUEk?oc=5" target="_blank" rel="noopener noreferrer">【動画】【Archive】 高市首相、防衛力強化へ「変化恐れず」 自衛隊幹部に訓示</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月3日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiWEFVX3lxTE1nTklVVXpEYm9BOG9TeE5EblN1OFBFeGhLcEhtaGhXUzBCaDBNeFNYeTEteWVYZUJPelVORnRTZ0RnaHZHb0RWUkpILUU5TVRtaTNSYUV4OS0?oc=5" target="_blank" rel="noopener noreferrer">米海軍佐世保基地司令官が交代「日米同盟の絆さらに深める」</a>
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
            <span class="date">9月3日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1RazIySExvS1paTWxLRWRwWVRId0M1VjB5YklSSW5mRTQzMXFIRmYtdXRsSDl4OW1kZlByZzNfZ2J3dnhSVGk0aV9OS1RPSDhXU2dLNUlJX1hSWk9VaU5oWTlWVWNkbms?oc=5" target="_blank" rel="noopener noreferrer">自衛隊に「外国人の登用」検討を 安保3文書改定見据え研究会が提言</a>
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
            <span class="date">9月2日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTFB6UktFMlc3R2ZiTGNBTWNTSkxjUm5RZnJERzVGLVlMemh4NHBDZ1JyenBVeW1tX1VGUTZhS0hqdGRWQ3p0STY0QU9UZjUtUHBuZWxVNlhpTXAtNEZWSEIteGdja1JsdjQ?oc=5" target="_blank" rel="noopener noreferrer">馬毛島工事遅れ漁業制限延長要請 防衛省、4.9億円追加補償も提案 [鹿児島県]</a>
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
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTFBYRl9LNkk3am9rdzUwS1pTak1Mb2dqS2dJdU1XOUNfMnktY2MweGdWMlA4SUhoeXUtRDVpTnViZnhaaEV4dTgzV0dISEUxWHlfNXUxaVp3alVUaFV0QUVMckxwMHFyX0JXWG5tMA?oc=5" target="_blank" rel="noopener noreferrer">防衛装備の国内製造強化へ提言 笹川平和財団、自衛隊の外国人登用も</a>
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
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiogFBVV95cUxNSE9KWkg4TWMzdngzNWY5dHlOcnNUcFRjbjVFNUR5VkVfTVptS0d1UEpDdno3UG9ldDMxNW52bC05eDlVRlkyTFBBdmRpUGhnQUNHM3hlNjBXdHJmb3pfN2sxUmc0R0p2bTFBelpQelZ1Y3F4UVYwYTRBSmNTYllpUVpTNVgwbXM1T3VpZ3N3aG96VTQwRW1qLWo0eWM4SG1Yd2c?oc=5" target="_blank" rel="noopener noreferrer">ロシアがイランの超音速ミサイル開発支援か、英紙報道 武器輸出担当者ら何度も渡航（写真・画像 1/1）</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月2日</span>
            <span class="source">時事通信ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiXkFVX3lxTE5rQXhvc1ZzNEc3QU81VDRRbTd3cW9MMEdzS3hhTlJjZVpMNGJqU2VMeHN4YV81T1VYa2pGRkxsWFp1bXcwS1k3RmJtMFhVclVVSS1zbXFpTnlaRE1oR1E?oc=5" target="_blank" rel="noopener noreferrer">◎高市首相、防衛力強化へ「変化恐れず」</a>
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
          <a href="https://news.google.com/rss/articles/CBMiU0FVX3lxTE51ZnlyVEpFR0FlOHNVZHo2em96TXZ4VTNvWlgyY1psQzVWNWgtU0RzQWdfMEJmb2l6WXZuZnBSemxneGh0d2lRMFFsVEZzbVlkOElZ?oc=5" target="_blank" rel="noopener noreferrer">防衛省、新しい守り方記載見送り 自民国防族の苦言で</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月29日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiUEFVX3lxTFB2bThMZ2RxNE9QTDJSWFdIQzBXUGd0Yk9QQ3dFc09Mb3JuUVRCVnAtTUc5bjhPM25oSXZLZnRybm55dS02bXQ3WE4xSVYwNHNG?oc=5" target="_blank" rel="noopener noreferrer">ウクライナ戦争支えるドイツのドローン工場 防衛産業に参入するスタートアップ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月29日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE5MTS1XcVFGOHlERXZnNVl3Z1NCTE14SHlRb0xTd2ZWekl1YkVnLUJWaDZQY29ld0U2UVVHcU81S0RKTUs1Y3lkVHM5VmYwM2dXR0JKdUNxclpmLTZnUEZ3YllsU3kzRmp6?oc=5" target="_blank" rel="noopener noreferrer">ポッドキャスト：日本の防衛政策はどこまで変わる? 安保3文書の改定とは</a>
        </li>
      </ol>
    </section>
  </main>
</body>
</html>

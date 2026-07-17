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
      <div class="stat"><span>UPDATED</span><strong>2026年07月17日 13:12</strong></div>
      <div class="stat"><span>ARTICLES</span><strong>61件</strong></div>
      <div class="stat"><span>LATEST</span><strong>7月17日</strong></div>
    </section>
    <section>
      <div class="section-head">
        <h2>Latest Coverage</h2>
        <p class="note">Google News RSSから取得・フィルタリングした記事です。</p>
      </div>
      <ol class="news-list">
        <li class="news-card">
          <div class="meta">
            <span class="date">7月17日</span>
            <span class="source">日刊工業新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiW0FVX3lxTFB3U19KenUzLS1BX2RpQ1Y4cXZRZ0duakhqZ1NKWWdxaTZjWUNrOVMyclRyNElpLTRhYUlqdE1Qa1JKaklONUtPaVhzaHUzWGFZeDNMdmNUdFAxTTA?oc=5" target="_blank" rel="noopener noreferrer">防衛産業、官民で投融資 全銀協会長、新興活用を強調</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月17日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE5yWkdLYk1kR3VBNU1jNXcyUmJHUVlHNjNtdDNySVB1dmRzNVBMYUlEanhueU1KYnpDSUJZUXk2TTJWbk1jLV9JQ1ptTlN0WDk3MnBFeUVQXzhmM0R3TFZMeVNGbHF3cmR4b3ROVA?oc=5" target="_blank" rel="noopener noreferrer">韓国防衛産業、イラン紛争で脚光 湾岸で9割超のミサイル迎撃成功率</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月16日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE9QQkVfdHJPMERUQkpxY3dieUVYcDRCVWxNRUpOaHJvalhFNFNFMFFUT3d6aFBtX3V1T3JzNTBZWTJ6M1ItRmszMUlFVE5FRFJPb0RHQzBUX1E0cGJ0Ql9XWjlWQThpZ215d055OQ?oc=5" target="_blank" rel="noopener noreferrer">中国とロシアの艦艇、沖縄・宮古島間を太平洋へ通過 防衛省発表</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月16日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE9hcGVZeWdIS1RhWWFGODFoTE1US0JESFNPZnQwV2toNW1KcXdMWjFkYk5JUzVxcTk0dFlWb3N0c1JxWnFJdUxzUW5KcFFtajRvUDJ6dTVGUUdZSk5yaU5aY0xxM2NQZXBkZUY4Mg?oc=5" target="_blank" rel="noopener noreferrer">全銀協会長、防衛産業への投融資「国際条約を踏まえ判断」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月16日</span>
            <span class="source">ロイター</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiekFVX3lxTE40TXFrRDZQOUJWZ2N3VEJ5ZXMwcWNYQmdCeFJOc2pQMGRFUjBSdzkyVVUxaVh4bXB3TGJOUU5SLVc2TFpUN2MzMjNIc3lPYlZlMVFVTkZ4a3VvbEE5N1ljaE5vWGJZQjlvVGtRM25oeUVsWkVibUMwQXZ3?oc=5" target="_blank" rel="noopener noreferrer">トランプ米大統領、防衛産業首脳に兵器生産加速を要求</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月16日</span>
            <span class="source">日刊工業新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiW0FVX3lxTE10R0VYMHJrbFR2cE90ZHpWOFpRa1VOMHZES2xiS2t1dGt3OEtQSkU5TXdpZXpoZHRBOUJxakJNQzVqWFN4cFR5RnBjeGx6VmJzZ0hwYTNIYVdTTXM?oc=5" target="_blank" rel="noopener noreferrer">防衛省、新興技術活用へ金融系と協議</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月16日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE9fb2hqem1takpZeG1YMjhNQlhsXzBMT0dJUTRmSGpTQVl0a2VaNjQ2VUhpYTFVdV9CRzF4SW1ydllmZVpNV2JNMWMxQlRMVmRIWkZrS2wtbUVralVGN3pVZjN6THdIbDdXcVItNQ?oc=5" target="_blank" rel="noopener noreferrer">防衛相「防衛産業に融資を」 新興企業支援へ金融業界に要請 メガ銀は慎重に検討</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月15日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiWEFVX3lxTE54X1ByZ2g5OGRFS3ZvSWNkS1FJN1lvTG9JWG8zbHc1Z0N1OUxGUHFFUUVfbjF1RWVnREd0RWxWMjkzRFpXdGNjVlNLOHhkV2JPNldBX3l1d3M?oc=5" target="_blank" rel="noopener noreferrer">離任する在沖縄米軍トップ「日米同盟をさらなる高みに」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月15日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE9HbjNtMnVHdkl0djlvLTlfNDc2ZWx6VHhWVFZxRERqd01tTUFFNnB2RzFGSENvV1VzcGh0aFdBSXhaRzJOSUx3NTB6X0NSeTFGRkRmTkk5SnNBS3FWbXhFTkI1cU51d1E?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相、8月中旬にインド訪問を調整 防衛装備移転など議論</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月14日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE9PMWU5cXcxWnlQM19hOVhUaEYtUi05end6cjluMGFzNUtoTVVSSXJjNGZ5Q2hLWGs5WEtCSlBqNTRQaG1Vd0N3V0szU0hIYUstNGhDNlZYVDhlU05PS04yS053Q2w3OXVhZXNDaENTcndMaEhRMkE?oc=5" target="_blank" rel="noopener noreferrer">韓国防衛産業好調も「欧州の壁」に苦しむ 受注合戦で相次ぎ敗北…ウクライナ特需は終焉か</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月14日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE9EeVRORzhnRVdDeVlHM1BLVW12ak4zcWJQVDBWR2Rka0JSaFJNVGhjcnlKVk84bjktbEdyYXdJYllnS2g4cFhFR2FSV29OczFtMndXZkdEbXlwRVoycnRDYng4TDNUTHJ0eU9VczhYNWlhZnVwZ2c?oc=5" target="_blank" rel="noopener noreferrer">北朝鮮に「特需」、対ロシア武器輸出で年間GDPに迫る 戦後にらみ対中接近も</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月14日</span>
            <span class="source">時事通信ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiVEFVX3lxTFBEMlFqRTFEZUtiR2V1QzlRektRMDJPWkZnLW8zdFZJMGRnVWtxZmhFTXNXa2ZIcHlfdWdFbU9xNm1LUTVFWmNSNmFUSHJXcVpCQ3dRRg?oc=5" target="_blank" rel="noopener noreferrer">◎防衛産業で対日協力</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月14日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiggFBVV95cUxPZVNEYXZfbzk1OGt2SDdmaWYyV2JvbFhHamJmSTJmV3hNYklHcjhqazd5TGRjUWhxR29hQjVEMEFkekZfZzN3NWdUWlFEMU14SmticVhHS2d5b0VtSmVhZWhVcjVzeDZVX1ZsZHVDaVIzbDA1Vm9XenE1a3hIV0JsNGxR?oc=5" target="_blank" rel="noopener noreferrer">防衛産業で対日協力 「共同生産」にも言及―アゼルバイジャン大統領</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月13日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibkFVX3lxTFB3blhuZ0ZfOXN1Qk9Tc0VHcjdEWGMzT2Q4bUxPLXZVbnhJdTJidU55d1BVS056MDFuQV9FZXU3SDZwc1c0ZUpUOUdJd2tvSXVuQ2s1bU9ncFFqYUM1dFRIQ3RZUXJjNUZwZ20xRXlR?oc=5" target="_blank" rel="noopener noreferrer">日米安保条約調印 米ワシントンのホワイトハウスで…：安保闘争の時代 写真特集：時事ドットコム</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月13日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE0tdFR6VWM3SEZfdzJCcWhaXzdxM1NRQU9hWnNQSTMtWnpKdVZqRDlFdk90SEFxdmpPejhmRWtBWDMwSVpkcnRSamo5ZzE1dWVpVjdCTlRaOVI1WW9haHQ1cFRBRGp4WE0?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相、来日のベトナム国防相と会談 防衛装備などの連携を協議</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月13日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibkFVX3lxTE9VMjNiNFRTNDNoRHV4UklnVXcyVEdlN2U0M3lfWE82YlJ0NGxBZ2VzXzdPSEFnMm1FaFRDazNpQzZUV1EyTUwtRGdCN25Ca2ljWkRSblF2TFo4a1VEeU85MGZ3MEc5ZGg3OGhlM0xn?oc=5" target="_blank" rel="noopener noreferrer">７０年安保 首相官邸で日米安保条約の自動延長に関…：安保闘争の時代 写真特集：時事ドットコム</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月12日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiakFVX3lxTFBMa01UeUJzMlhZMkhrV0R4aFlhbW9QNGRfeXp3NWdrbjNoUWl1d3pHUlZVVlJINEw0TXJTdXBiMFhQY0FoYUpBTURENWg3bHRUZzFFd0EzM2FqRzdsQ2RtY0R6RnNrQjlCa1E?oc=5" target="_blank" rel="noopener noreferrer">防衛省、新たな局の増設検討 骨太の方針に組織の「抜本的強化」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月12日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE56ankxdzhmNjVBaHctM0FtLUZ6dHhNbUp0NnliaUx1SXFaYUhvMVhWSUtHcHZQR01HYm81UzlVVERpNmloYkstMjBjN2U1YURxSzJ1WDIycGo5VVVWejhWdHdqUTVHcDNDOFR5ckZZZmoyMmlwSFE?oc=5" target="_blank" rel="noopener noreferrer">日米同盟「再選択」の時 不確実な相手を見切る覚悟 元海上自衛隊海将の吉田正紀氏 インタビューズ 聞き手・有元隆志特別記者</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月12日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiXEFVX3lxTE5PdkN4Z2xDbUhHdDA0V3NmNGxuMWpsZWJPMWFPQXVOUnZiM3VubGhQV0R2Y1BqT2Q5ODZxNWpaMTRnZGtvN3Zha0RDdk1DVVpYYnQzZGpTQ2pNNmZQ?oc=5" target="_blank" rel="noopener noreferrer">救命キット、操縦妨げたか 他機から持ち込む？ 防衛省、事故調査結果公表へ 空自機墜落</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月11日</span>
            <span class="source">東洋経済オンライン</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiW0FVX3lxTFBqUE5uS05oTVNiTms0QXJVSXRYT1JBdGdMb2dHYW9pYWZERjhyMWJ4ZXp0UDJHVkNmYjNyenV3R3ZDa21JaDlseVpSTVYyR2xJck1RVm1HdHVTckE?oc=5" target="_blank" rel="noopener noreferrer">中国が日本を｢新型軍国主義｣と呼び始めた真意は？ 日本の防衛力強化を阻止しようとしている中国の｢認知戦｣</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月11日</span>
            <span class="source">東洋経済オンライン</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiUkFVX3lxTE82djhjQzV3UnVlb1ZZZnp5LVVsVy1GaFBJWHJHanJhb2dIa1ZkUHBfcEZTWXp6Rzh4THNaNkhFd2ZqUXd6TDRQLUdWTy1zaks5WHc?oc=5" target="_blank" rel="noopener noreferrer">中国が日本を｢新型軍国主義｣と呼び始めた真意は？ 日本の防衛力強化を阻止しようとしている中国の｢認知戦｣</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月10日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE1sVHdubWFnVnFhZXpmTWliZ1Q1WkxsWjBHaVNFdmFOZkQyMlR5Z0I3TkRidUNTTHU0U0NjOGxKakdQbXRNUUNMd1VyeWNreHc0dTJMZEEyMlJoMjFmQl9vVHltajg1WXJ0MmZLZHdFSldtVlY4Nnc?oc=5" target="_blank" rel="noopener noreferrer">米国は日本の憲法改正に期待 日米同盟深化へ安全保障の「国際的異端」解消を</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月9日</span>
            <span class="source">NHK</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMid0FVX3lxTE9rZ2lSZjgxSTNfZnhrZkVPQnpFb295RDh6NDhUbkp2VnE5TTZreWZpSFJ0UEI3ZEJseTlBMHg0MzdPOWw5SGtnbk5mMlh3SldsNW1aaVNXY0JXYU9OTkVwU3c1bUdaNXJINk1wUTVqcWl1clRPTDRJ?oc=5" target="_blank" rel="noopener noreferrer">存在感高まる韓国の防衛産業 ミサイル防衛システム・戦車など輸出 - 国際報道２０２６ 番組のお知らせ - 国際報道 2026</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月9日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiYkFVX3lxTE9WU2p2VWhxdm1VcV9rQS1ZOXNsWGp2cEpwLXJjMWEycWg1VG1YT2RPQm42enpqbVpVaGVwc1cxRThBdlRGdHdGUHFHbUpqN0hDY3RUSEM4UGc2V2NWZjd2OEVR?oc=5" target="_blank" rel="noopener noreferrer">韓国、ＮＡＴＯと連帯強調 李氏・事務総長会談 防衛産業で協力</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月9日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiXEFVX3lxTE9xS0JQejVmWjZJdUFycDBlNDh0eGdkTE5KYlY4Y0FCOTNlRFM2WThIeUpoVHMtNTN1SDd0bHVqQjA4RVhUOHJtdUFUNnNkbWRKQXQzcG1FaUdwTEpO?oc=5" target="_blank" rel="noopener noreferrer">防衛力強化、必要性訴え ゼレンスキー氏、トランプ氏と会談</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月9日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMid0FVX3lxTE1fcmlDdGtncW5EMDJuRDQ4QWdlNDJDUF8tSzJIY3AyWVVxclNBZWMtMXNhbDd4NTNUcGdtMTlDRTNyeWt2aWRoY1ZjZkJuRXljUWczTnBtTk9GekllOFR4SDVCUjZjQ1FPcW5ncWhWdDZ1NzJJTFpR?oc=5" target="_blank" rel="noopener noreferrer">防衛産業、新たなフロンティアは海中に（Lex）</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月8日</span>
            <span class="source">信濃毎日新聞デジタル</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMicEFVX3lxTE9Lall2RGJRUjM3VkdqZFFmM1NtTy11Y0pmakkyZVB3dFpnXzJhSURndlE4SURQdGR4RHhhQ05hUGFMMWY1cFpRaE00VGVDTjg3WWdmb0NWVXcybGY1YVYyMk9NWHFzMDNIZVlJRTNBaTg?oc=5" target="_blank" rel="noopener noreferrer">殺傷能力ある武器輸出の解禁 長野県弁護士会が反対声明</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月8日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE9RUVc0VkR1WGR3Yi1Ldm9Ta1RaQnN2OHF0a2g5Wmt3S21sTk9raFV2bjVIamFybWtXa2ZkbEZzMkFkU1VET1N6QWRZZThuM1BBbmVFM3owNE5HRGZleFc3VHpUcHpFQQ?oc=5" target="_blank" rel="noopener noreferrer">防衛省幹部が相次ぎＸアカウント開設、中国との「認知戦」に備え…小泉防衛相「黙っているだけではウソも本当に」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月8日</span>
            <span class="source">ニュースイッチ by 日刊工業新聞社</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiQkFVX3lxTFBDNDNmV1FIUTQzNW5oQ0tNSzcybW1jVkR1ZXdKVW50d1hyZ3JxdGM0VmNLWlNycmFUMWo0ZjQxRnZZUQ?oc=5" target="_blank" rel="noopener noreferrer">三菱重工が引き渡し、防衛省向け護衛艦「ながら」の仕様</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月8日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiXEFVX3lxTFBFTDZ1QmtzcHZJb1FXb2pMRkJ1X1RVdGhwaXBpbmdYZTJkS1p1aXp5WTBRbnVjWm1weFpNcDVBUnJ3elFtaFYxbjNMRlY2RnUyY0d3SFl5SVdaMGty?oc=5" target="_blank" rel="noopener noreferrer">欧州防衛、負担増応じる構え 米から圧力 防衛産業と大型契約発表 ＮＡＴＯサミット</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月8日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE1PUnRabzM3ci1lRzhpNVBpdFRoUzlHbVl0cXJwRnZXY0MzOUlfNVNld2ZDRGRyUGEtUUxfdXBqTmNpU1k3cjFuZDBGZmJfa0FOalZXR3lsUGdPRkJnQVhCanpCTQ?oc=5" target="_blank" rel="noopener noreferrer">韓国、防衛産業で欧州食い込み図る ＮＡＴＯの壁克服へ「パートナー」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月8日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE9kRGNHYmhQMUVzQ0JONFh6bWx4eFNjRGVuVFF3Y091WFA3TWd6VWtEUFlkYkptWGRjRnVFUWZoQm55ZVphYV9wSUZRazJmY3NxNWhfMUloYVlEd3hFbzR3VVhNdFZIRUVLREZpTQ?oc=5" target="_blank" rel="noopener noreferrer">「NATO＋インド太平洋」会合 防衛産業・サイバー分野で協力確認</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月8日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiggFBVV95cUxNa0x3OFZjRU1FTnNQbUlyT1MweHEwWVRERklCeXVUb1dPeWtYMTV1TEtzZE9SeDR2bnFwaEQ1eFdwemFJNzB5R1BZUFpJOUdabmZpdlFURGhDSEtmNTJYUXJ4T2hXQV9ESGtSNTlUa2NESndkamJiU01mU0J3UEtVTm93?oc=5" target="_blank" rel="noopener noreferrer">韓国、防衛産業で欧州食い込み図る ＮＡＴＯの壁克服へ「パートナー」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月7日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiggFBVV95cUxNOEYyZmtDRnFzdmlaLUQ4bHlwdVFaTnFHMEZRVEtKSXc5a3BhVVNQWXQwUTdta3YzOTVsanNIYjh1SmVnbVVFaUJMVTNlWkZpTFdSbVduU1NwcmVqZWZGWl9WMEw2NDZJVlBGRTlnWDV5X1AtM2lvaTJpZ28zWWs1OEpR?oc=5" target="_blank" rel="noopener noreferrer">ＮＡＴＯ、防衛産業を前面に 首脳会議開幕、増産へ官民結集</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月7日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE9ObzQtcFhxckVNaXZwN01EUWpaVTR0QWlqQThrbWhNc1hpQ3MtWnp5SHBrYUlScFRMSUtySU9mYjR6SE5ESWdkYkNvUG80VkZrVUtrN1RYWGtiNXdQZlREN09CZ1V3bTlTS0xfbA?oc=5" target="_blank" rel="noopener noreferrer">防衛省、局の増設を要求へ 骨太方針に「組織の抜本強化」明記</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月7日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE5HeW8yZnZPUUZUeDdGNldzbE5jY1lBTWtkVFJjaFNFcHlWMFUyQnl6YVRkSlFMTThSVzRxUE9Gc3F6T3BOMjV1X2hBSDVhY24yZXo3a3ZRMFEyUG80VkQzdy1GZ2pvRzg?oc=5" target="_blank" rel="noopener noreferrer">防衛省、新たな局の増設検討 骨太の方針に組織の「抜本的強化」 [高市政権の安保見直し][安全保障関連3文書]</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月7日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE5ldHhrODBsUjlwVTJwWFk4V2ZpZ1F2d3AtX0RUV2twSDdWenMzMnZDZVpCTFN5OHNNaDBVcndzbTctY1A3NUswRE1ZTDRYQ09ER0tSdlp2T2wyYU8zWGE3T2YxQQ?oc=5" target="_blank" rel="noopener noreferrer">防衛省の「局」、増設検討 国際協力所管、ＯＢ支援庁も</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月7日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE9oejlBdnVrVk44YmpqREozUVdtT0toTlNhdnNUS01hWWlMdmN2b3FBeTBKc0dfdHhXZlk1RGxuZjAtVVlRNzRLRFJNV1M0WHJwLXk3Z0oycWdTUWl5YjBMRGwyR2R0MFE?oc=5" target="_blank" rel="noopener noreferrer">防衛省報道官がX開設、「表のホットライン」中国主張に反論の狙いも [高市政権の安保見直し][安全保障関連3文書]</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月7日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiggFBVV95cUxNelRTTzlreFNBRVVSa2Q1TzR1QlotLUFTVXNQcXRZNnhILXZCdFRxcEY0Rl9WNEFsODBIYmM2SE41SFh2QzNZSUcwZFdrMHliYTFGRHZidGV2VzN0MVBUQXZuOUFRV0hwU2xONFJOeGd1Nmg5aUtHeFdIbjlySnBZdEV3?oc=5" target="_blank" rel="noopener noreferrer">防衛省の「局」、増設検討 国際協力所管、ＯＢ支援庁も</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月7日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTFA2ei1IdDVtZ2k0ZFkwc180eWc1Mk1ocjBsT2pjaGNnU01MV3U1NlNpRUozRTJ4NkRBNXJ5OURxMVQ4Nl92cjNNbHFLZlNkMzZZMUlDQ0x0dHZzSFU0c0JKV0owWQ?oc=5" target="_blank" rel="noopener noreferrer">ＮＡＴＯ、防衛産業を前面に 首脳会議開幕、増産へ官民結集</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月7日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiXEFVX3lxTFA1RDhmZ3FFbjR3cXB4NFJsVEpHdmxqbk9KMVNrdEp1OHBzbHM0el9MTnpkTU1MVUhDTGlocUJCVDRfMllhVGh3Uno4OW1SeFpQSXIxanY5bUVrMHRH?oc=5" target="_blank" rel="noopener noreferrer">武器輸出、台頭韓国・追う日本 韓…安くて早い、対北朝鮮で発展 日…高性能で高価、国民は抵抗感</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月6日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTFBhSHY2aG9XZjM1aWFGQ0RCS0NreGl6djZ0eEpQQjM5a0tFYlB1WkhXdmV1UmJkRjVMaE9oYmMyaGpSeHF3VDU0NWhmamdtUnpoMXBsUmlHcmNaZFJ2ek1vNFA2aUJPUQ?oc=5" target="_blank" rel="noopener noreferrer">防衛省に局増設へ、他国と防衛協力や交流する国際連携所管が有力…骨太の方針に向け政府・与党調整</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月6日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTFBfWUFoOGUzNXU0X3ZydWZYZFRad2F5cmdWWGRZcml6aWMyU2Z1Y1NQWTRoNDRiNXZHalFfX0dTVWpOQloyNlRySEQyeUlxUE9aZkFkbllna3JFRjd1dUhVSExUOA?oc=5" target="_blank" rel="noopener noreferrer">防衛省「ＬＵＵＰ」を導入 市ケ谷庁舎に、ＳＮＳで懸念：時事ドットコム</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月6日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiggFBVV95cUxQc3FPRHhTTlowZXJwNmZBaGxhckYxTHNaOWJ4Wmd6VUdER3Uxcndrdkd0V0sxaXlCU2xUTGJsZW5vaHJnQmNpdVJEZ1NDbTN2WXhoUlRnbnlxNUJGcW03UUJsdlJmenh6WmdCWHE2X3NWUVd1WEpBT3F5UHQ2UGpWSFBB?oc=5" target="_blank" rel="noopener noreferrer">防衛省「ＬＵＵＰ」を導入 市ケ谷庁舎に、ＳＮＳで懸念</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月6日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMid0FVX3lxTE9jWE1FdWNZcXlWX2lwLUpEZDBLOVJaZmNVVDUzUDZRLVA1aGNtZTl1NV93NnlaM0kzT0ZnWE52STdDOFlyLWZrTHRDajFhTDRlV2ZwNUhjb3NwTzVOTWFSeU8tczRQMjNBR1VHXzVVS250RVRmcVR3?oc=5" target="_blank" rel="noopener noreferrer">トルコ、急成長する防衛産業（上） 欧州の期待と懸念</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月6日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE1ubDdJaGhhSTZzOFlvWThCVmFXbVRnOVNjV1pwb1h0b0ZnR195MXByS1p5UW1XT01mVEZMQ2N3SWVpaFFDdlI4OHVfYzloanRnZzJaVUxiRzM4UWJ5TnFfWTNBcXZUTmlFaUlwaQ?oc=5" target="_blank" rel="noopener noreferrer">三菱重工業の株価、午後一段高 「防衛装備の工場『国有民営』」報道で</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月6日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE5peGp0Q0ozNzE1WktSODFuRXZ2RDBZaHUtWFpDSWo0SnVyaDZuM09pdFFIM3JGdjZYMHg2eno3MXdKUmEtWUFNbUVPX0VXM3ZfSGdmVmhPRC10TzZUc2RCbnlvNHk0VFE?oc=5" target="_blank" rel="noopener noreferrer">防衛費増の数値目標示さず 安保3文書の自民提言の裏側は……</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月6日</span>
            <span class="source">中日新聞Web</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiVEFVX3lxTFBQQkVPVmVxazlYV0N0YXAtUE5tbTRDUTFocHN0VkNlYlViU3JaSHlDR05lTGhNejhQMlVkcU82RF9XalNCRmdSVnVoYnd5Wk04V3lQdw?oc=5" target="_blank" rel="noopener noreferrer">加速する武器輸出 歯止めは？ 高山晶一・編集委員が聞く</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月4日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiXEFVX3lxTFBoMjJNaEhTRHQzZ2czTWRIdXMzNU43TzdjemJJMU5ZWHRyeXVLZk5OQWtwQUFBZkppczJFWDVkTDR5WFJvOUhaVmlXdm1DekNHUzdwSjY3b2VKdWgt?oc=5" target="_blank" rel="noopener noreferrer">防衛省、職員移動にＬｕｕｐ 東京ドーム５個分、市ケ谷庁舎で</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月4日</span>
            <span class="source">中日新聞Web</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiVEFVX3lxTFBHQjJLdVJsY21KeWFYbmZzMVNuLTlyOFN0T0o5VWpmbFlmLXVjT1J1bkx0emtYN2FrQWFSRjZKeGI1MDBkQll1ZEhNNGlEeTJqMW01Tg?oc=5" target="_blank" rel="noopener noreferrer">空襲の地で感じた防衛産業展の“熱気” メ～テレのドキュメンタリーが放送文化基金賞受賞</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月4日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE1LbUFWOXc2M01lZ25WcGxsaVYzbE1xWXNGWGIwWG1qYjAyOFpjZXJVVGhPSGRjblVSUEliMzNrbV9OU3VfUFNIeDI2SGhYRHl2cjJBQ3lrelhQN1hDX2kySkVGdWZRMWZDRU83eg?oc=5" target="_blank" rel="noopener noreferrer">防衛装備の工場「国有民営」 政府、法改正へ調整 有事の緊急増産に備え</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月4日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMimAFBVV95cUxNODRERUhsSU9NSC1WbV9ZQjZxWHBMSHdnTFU0SENVd2hjT1c4bVBkcGNNWndJUUVpZkgxTlJaXzJyUnJxbHVzYmlEeXptUDdMZERQT3FSaGFRM2JnNDktUlY1Q0NxLXBGSWFHZTZXRE1GanYxWUxsQU1CaE5BcXdxbXpnNm1lQkQwYUZHQWFkdkExTFp2WDhtTQ?oc=5" target="_blank" rel="noopener noreferrer">防衛装備の工場「国有民営」 政府、法改正へ調整 有事の緊急増産に備え</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月3日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE1XQ1hMU0FJNUpNc09yMTZqalZDNllTMGtKU2NKeGFKVXA4NkxrbHhiOFdna2lxTjJHQTJDbERLVXRiUlI3N3hpY2prdXFmVFNGMlhjekU3cHIwWXc4eG4wVi1mRHp3VXpLV29veENwVDhmcXhsWmc?oc=5" target="_blank" rel="noopener noreferrer">防衛省、広い敷地移動にLuup導入 位置情報流出の懸念に小泉防衛相「保全上問題ない」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月3日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE5DbTk0dTBDU0t3eU44eUVyWktqb1hreHdIdEZ1S2dta2YxOThUMFY3dGUtejhGOUNER1dmRlc0UUwyTk8tY1VYQ0pCNzVWZnQwZ2pLODZ4a0YxdmxpWTRMbVhhdFh0clU?oc=5" target="_blank" rel="noopener noreferrer">防衛省にLuupの電動キックボード 小泉氏「情報保全上問題ない」 [高市早苗首相 自民党総裁]</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月3日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiqAFBVV95cUxPd2dGdWZFckVIMTVTcHgxbEFIMFk5dzViZlpVa01WWlpyNno1Ry0ydXdUN0l3a1o2OE1aXzFuS0taNUNjV0xRM1ZGc3dBY253YVF4ZVVvbllrdExKMzNyR0dZVllsaW1pbXlBVTVFcWJhTDhCQllLYWExRXY0SUctSHQ2MFpfQUF4YUE4U1lZbUl1QWVVUGhRbEZqWW51Z2ZUS2ktekY3TUI?oc=5" target="_blank" rel="noopener noreferrer">防衛装備の生産能力維持へ｢公設民営｣ 法改正調整、輸出促進に新法人</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月3日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTFBzcXBYSGFqQ1ctbGNqeDl0d2o4MGtNck1PM3NoOEFMalhsRWI3SnlRa3g5cUtjTk45UG9PX1d4LUd4SzMyUFhUa1VIWlNyUFpIMUJnQ1M3RjM1UHdJSVpxT1ZFc0hGTm1E?oc=5" target="_blank" rel="noopener noreferrer">「当事者」台湾の視点を忘れるな 防衛力強化論の前にすべきこと</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月3日</span>
            <span class="source">東京新聞デジタル</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiU0FVX3lxTE91Q2tGX0dueVpyUHNXeUhhMHNTdk5hYVEzVmlzaF9iWG11Skd6dEJQaTlhRVRQWktZcE5MOEN2N21jeFQ2U2pjU0haMzRtV1FWTm1B?oc=5" target="_blank" rel="noopener noreferrer">「一切の武器輸出禁止を」署名約12万筆 高市政権が武器輸出ルールを緩和してから急増</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月2日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTFBoSWZibVhjRFVMTEdBbGoyLVo2Rkl3RGp6Z29tVEV2WEhTVmluSnpORXlacVo5cjlHRDVOT3h3b2FORjJzSlFER21uaEhldnAwVVhySTFHQXNuNVVlR25sMFVSQkdqMHpF?oc=5" target="_blank" rel="noopener noreferrer">大学祭の自衛隊ブース中止騒動 職員組合と防衛省 双方の懸念</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月2日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTFBGNzVaWnFxNWQ4UFlTdl9jaHI4bkZsU25QNFhiVHl2emZqMElZNGU3Nm5iSEpidXI2ZzcyR014NkZyNFJtSkVLTFp5RURIV0NLaGtHdWhpMXJYT2xUT0pDd2xkOA?oc=5" target="_blank" rel="noopener noreferrer">防衛装備協力の推進期待 武器輸出解禁「歓迎」―印国防研究所トップ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月2日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiYkFVX3lxTE9KeDlxYjNCMlk3U2pxMlhuejVGTGZ6UjY5Ylp4dnNZVGFMRUJkT0ZnSC1TMG1Sb0x4SEdwdWViaHl5aS1qa3dNWDhwWmFoRGptRHhrRldicDRaQ19tQUdVMmx3?oc=5" target="_blank" rel="noopener noreferrer">英、防衛力強化へ投資計画 日伊と戦闘機開発１・８兆円</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月2日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiggFBVV95cUxNZlh5UkRxSzVSNk9HNk44ckxjZE9QVm5pZVYwWVJOTWpoWUdIUUMxLVB0eTRjellOQW95Y1NSZ3ZoMzgxNjhfTDh0ZWQwV0x0eTk0c3FJMDZMWDJ0SzBXdWdGS1BxdWtVQTJCY0lDdVkyYzBNT205M19ta3lQSGlsNGhR?oc=5" target="_blank" rel="noopener noreferrer">防衛装備協力の推進期待 武器輸出解禁「歓迎」―印国防研究所トップ</a>
        </li>
      </ol>
    </section>
  </main>
</body>
</html>

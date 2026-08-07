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
      <div class="stat"><span>UPDATED</span><strong>2026年08月07日 12:53</strong></div>
      <div class="stat"><span>ARTICLES</span><strong>42件</strong></div>
      <div class="stat"><span>LATEST</span><strong>8月7日</strong></div>
    </section>
    <section>
      <div class="section-head">
        <h2>Latest Coverage</h2>
        <p class="note">Google News RSSから取得・フィルタリングした記事です。</p>
      </div>
      <ol class="news-list">
        <li class="news-card">
          <div class="meta">
            <span class="date">8月7日</span>
            <span class="source">東洋経済オンライン</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiW0FVX3lxTE5fOFdkMnJVaG5EbHRhT2tjQnZ3QXZocTU2U2Nfb3JTeDFnUGd2VXVCOEFVVDgtYXk2eWUzczFYYkNhQ3ZmMl9OVjFsRzg5cmxkSzFObEJGSng0aU0?oc=5" target="_blank" rel="noopener noreferrer">災害支援で賞賛される防衛省･自衛隊､その陰で放置された組織防衛と無謬主義という罪､防衛費を倍増すべき組織なのか</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月7日</span>
            <span class="source">東洋経済オンライン</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiUkFVX3lxTE54YjJiS2VDdjM3VjR2S1RxLVVOamg3OGlEenRuNnp3dUVXYmhreHFLblZfZ0hCV1FJS3ZCWjZqa2hoUXFqOGFqQWtVdmp1WWVRQUE?oc=5" target="_blank" rel="noopener noreferrer">災害支援で賞賛される防衛省･自衛隊､その陰で放置された組織防衛と無謬主義という罪､防衛費を倍増すべき組織なのか</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月6日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE44VXRYc092VjRUb1drTXVNLWtFUFl3M2s3VE9JajBYRkdxT1lmc1dmaTdydG9RaFlqLV9Kc2t4NnNRVlJxTUlsUkxOU1JQMmptaFZ3SHNSRmlqbTdBMzZHRmZ6aVR6aElrcDJfUA?oc=5" target="_blank" rel="noopener noreferrer">防衛省、装備品調達数を事前通知へ 企業に設備投資促す</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月6日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTFA0TWJSZllGalktSnpnX2ZVQ1JwMUJ1NnJVQVlBUEFnOXlxUWtzOGxEWllUNVlGSGhPbHFZRGF4WUNSV2RFLTJoUUs4UnBuRk1VZS10U251VUszMUx6REVVM3NVX3RWNk0?oc=5" target="_blank" rel="noopener noreferrer">北朝鮮が弾道ミサイル発射か 防衛省関係者「EEZ外に落下」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月6日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE9HYkRMdFlCQ1NqYUxHT04wTmRVcmxKR0xMWWxQQ3JkYkhnYi1lU0pBVHR5S3J3RE9McXJ2TVQ5MnpQTUtWVWppbTMtWUpibGhCd2x6QXZJOHgyamF6VDhra093bw?oc=5" target="_blank" rel="noopener noreferrer">防衛省「日本周辺に影響なし」 北朝鮮ミサイル：時事ドットコム</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月6日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE5La1FQcS1jb01WTm92bENaV3UxVi1iVm5wbFl1WWFabjVuWkFKQlFhQzVOek40VzBoRWQwYnlqZ0hISkI4WmRvUThKVE83UEstQ0V6X2pfTWJKN01mUDFvZHkycDJadw?oc=5" target="_blank" rel="noopener noreferrer">【速報】防衛省によると、弾道ミサイルの可能性があるものは既に落下したとみられ、日本周辺への影響はない</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月6日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE90OHRUeE9FWnFpQWQ0SW1BclBQZzY5aWJuWGRDdEx2eFplODJKUnlZTHE0Sm1MNUdfQlRpUmFDcmM5enpfdWt2TG12RmlSN2tpVURMcmZXRFVfZHNkUExCRGdqNlBrbGRLMEdoeGE4bFhRMm9iUVE?oc=5" target="_blank" rel="noopener noreferrer">北朝鮮が弾道ミサイル発射か 防衛省発表</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月6日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE14THowcUw2ZUxib2ZWQTJrdFcxeEduS2IxVWdzY05kZVBLR1I5MzRmT3RWTHliR1lTTlFlV2lKSzlLQmdRY28xUmZrZld3amFlVzVlYkxWdnd1MWNmbVR6WDZHRTBBQQ?oc=5" target="_blank" rel="noopener noreferrer">【速報】防衛省によると、北朝鮮から弾道ミサイルの可能性があるものが発射された</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月5日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTFAxWGFHUEVkak9RUGdwOG1uUFJVc2hLNDFHdjNTXzJIS0tWVWxBaVA5ZWdqRlpzZU84N3FieDV5b3doV0xHWXdGdGUzRHJ2VlB0YTJxdzlxYWhsNDFneUlYSWxlcENGdEl0Umw5NGktWkktX0tuZkE?oc=5" target="_blank" rel="noopener noreferrer">防衛省チャーター舶「はくおうⅡ」が入浴や医療提供 断水や猛暑に苦しむ熊本の被災者支援</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月4日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE1MTGh3OHpmX291amJuU0ZIZGtoOUktTWJXaTF2d205d0Q2cWc5YkRiWHgtN1BFRm1HOTdCTFhraElPMXoxck53ejA2czdnYWVxZGhERFZ1VWdVbG9YMVo0?oc=5" target="_blank" rel="noopener noreferrer">安保3文書の有識者会議 経済的威圧に対処 法整備求める意見も</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月4日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE4yRUdSUjZZck5hNlBGNUFNUE5Pc3FPZEJjcUFtaEIzLXhxQjRDQ21aYWY1RFkySUVxNGdqcEpMam1pMV8wOU1QdUdpMC0wYllHY0ZlSzlzeUJoUG9ObzJYSGF4blo5YXFxUWZiWQ?oc=5" target="_blank" rel="noopener noreferrer">「経済の武器化」対抗へ同志国と連携 安保3文書改定へ有識者会議</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月4日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMikAFBVV95cUxQVXVlTERSeGxUMlFwUUc0ZnpzVGVsV2QxR1lKbTNSMGpqNkNoTVZvYVdXVDAzS1pzbGhQcTVXSHhwZzZjcVRHVFZXekdnazFaRnlWV1A5YWhpblF3dmEzaFhiYWdTTDYtZVU4SzlyeUw3TlVxR3RBd0hVWmpCck1pdmhwYllwLTM4YTM3LWo3TWM?oc=5" target="_blank" rel="noopener noreferrer">「生産力こそ抑止力」安保3文書改定の有識者会議、経済安保を議論</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月4日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibkFVX3lxTE9TUlU1ZzhEZzNaMHh6YnVMeGlNVmZZckVzMEtZQUlZa2FzUVhibmk1cHpoTFMtdWt1TUo1ajNtc2JWbDRhUlpoNG9DbW5BUjZhNW95Sk51ZFVnZnBLT1prSUNZdTFzcDZnWXJkQ1VB?oc=5" target="_blank" rel="noopener noreferrer">「生産力こそ抑止力」安保3文書改定の有識者会議、経済安保を議論</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月4日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE1WbWk3S3FTa0dJd2pOSlhkLVEwY2RWcnhVcFExRGdSbWpXLU9NN0V2YllMZ2VFdExNN1djd1dURTdfZVlZSnlRZU9XU0NDeEt2VFg2Ty0zVkdzdjNVU3BYblVuOGlYNDZ2MmhneEhRaWlnOFUyd1E?oc=5" target="_blank" rel="noopener noreferrer">「経済を武器化」中国依存脱却論相次ぐ 安保3文書改訂へ有識者提言</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月4日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiogFBVV95cUxOMUQ5Z05rck5BQmtIQVk0dHNHSk9CMnVjV2hQZlFKbDNhamRybnBld2FFeFZNYjItaGRFQXlKTkFUVFZwQW16eWNrcTZ4aHVyRkVWN3VWTmN3QXQ2QkdHZDl2Q3JTR2t3dDVlNkNGbmp6bkk3Xy1yNDB0anFSc1NaUXl5a2JpMGgtR1V6TUxCQnlIUFZnclZYQmpkMzNjMWRhUEE?oc=5" target="_blank" rel="noopener noreferrer">「経済を武器化」中国依存脱却論相次ぐ 安保3文書改訂へ有識者提言（写真・画像 1/1）</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月4日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE5KQzI3d19tN0x4Q0FfRDUzdTRUR3d5NVhmNXRkYXZILWt1cFR6c21wUDdrcjBMaXZ1LWp4Mk1Va0d0QlpJb29TQmhsUGhnY2VXbUYxNXptdWlNRVMxOE5Vbks1VHVXdw?oc=5" target="_blank" rel="noopener noreferrer">熊本の被災地にあすから「病院船」、防衛省の船舶活用し初の取り組み…内科診療や熱中症治療・薬の処方も</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月3日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE9hc1N4ZmN6d2FXSlVXNmdRUjFhWi1KZ1M2dmpWODdsOUlhWFBmN3I4UkJPRXRabEJmNnJmSmRwa01LQ0N1MUZNS1RlbTZIM00zUk1ZWmF4djl5WmFFRUgyNmhhTQ?oc=5" target="_blank" rel="noopener noreferrer">インド、イスラエルに武器輸出２５００件超 「虐殺加担の恐れ」と国際人権団体</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月2日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE5OZk96QUp5X29GVjBCbFlwU2NKWHU0ejhleGphcUt4MlRueEI0SmtyYk5xV1VYV2dHZ20zWkM3TFU5TE56Ml9LVEFON3Q3QlUxLXdnYVBFVy1DVmowM2Zn?oc=5" target="_blank" rel="noopener noreferrer">防衛省 国際連携関係の政策を担う局の新設を調整</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月2日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTFBLSG0wbjQwWjFKY2FYQUtkazlKOEhrTEhpaWdiazd6SVBNNFNueHR6SmhjQXB1bW1aUmxjdlBHeGpPRWVEd2dEaVBWUDFQWUhZWjAzbm1YRThxT3laQlJDOG5aRQ?oc=5" target="_blank" rel="noopener noreferrer">［地球を読む］日米同盟 相互防衛の意思 隙間なく ハーバート・マクマスター 元米大統領補佐官</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月1日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTFAxeE84cUhDWnl2SlZSZXRHT3F4LWlMU3FVOHJGR0JLSWV3VXpaa2lnaE94OFlaUHFDU3hKRkZURkx4bWRuRmUxeEJyZFhfZS12dDBWYW5FLS1xcWE0U2duTVFoMElGdw?oc=5" target="_blank" rel="noopener noreferrer">防衛省人事（７日）</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月31日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiWEFVX3lxTE5tb1VvbTcwbUlmeGFHZ1BrbXlaUmctN3hZQ0Y0R2RtRXhoRWxPV21BemFiV3g0SjVkb3N4MEhqWHRPbWN2LS1VbmQzX3lBSjdQby1LMXNuMEM?oc=5" target="_blank" rel="noopener noreferrer">長崎 佐世保 防衛産業をテーマにシンポジウム</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月31日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE5HMk16NDNzNlVQVEo0OXdFOVlIdDd1ZFBpMk5Ld3hDdTNycHRyM04tdjhxUHVFdkktdDR2U1Z1ZkVJdFlZdlFIMmI4YWctbDhiUEJ6S3R5cjkzTUMxUVZXa3AtLTRqaEl1TG9IXw?oc=5" target="_blank" rel="noopener noreferrer">防衛審議官に安藤敦史氏 防衛装備庁長官は今給黎学氏</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月31日</span>
            <span class="source">日刊工業新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidEFVX3lxTE1IZzdUYWFjY1VtQlk5aktlODhpX2ZNTm1LNUZPcDBRQXliOHJ5cDRhR2hjdzJRVXRhcVZPRC02Z3paT3VaLWNDVnpXOTh4Zm02VnZIaVN6U0dNSWhaSUt5aVRDRGowR1J3dnFFWmZZWFY1ZXBs?oc=5" target="_blank" rel="noopener noreferrer">令和8年熊本地震／防衛省、自衛隊員の投入5100人体制</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月31日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE40SDdkaG5vUW9kU0tUWWQzbEUwZkNCT0ZleXQwVHA1ckkxVG5MQWtfekdqU0M2TTRwRDd2MWxEeDRacExvRWJQcGxPZnF3SHhPWDRPWndWbDZzQWY5V0JaS09nZ19nQm9aaENXYQ?oc=5" target="_blank" rel="noopener noreferrer">迎撃ミサイル成功9割超 韓国防衛産業、UAE導入で脚光 25年、輸出シェア世界4位</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月30日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTFA2X3psSjl0cE8zX3VWd180WFBsQW16bDVaTW1rUGY3Z1VwNnZNQ0ZiN2gtX0dTX0FYVXhrZkZiTjVFeVlDdkprY0x0WG14SmhTaExXSzl3WnJBY1d6VjJkVU41SQ?oc=5" target="_blank" rel="noopener noreferrer">トマホーク実射試験終了 海自イージス、米海域で―防衛省</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月30日</span>
            <span class="source">東洋経済オンライン</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE1GXzNCLVNuTzlpZmZMRGJJSVJLbWVZOVBJaGhhcEg1bW9aOFJaNlRRcXdScmlkdTZtdEYyeWQ1UnBqNlU0QlNpYzlOUWlQMy1nY3lVT0NQY1NsY0ZIODM4?oc=5" target="_blank" rel="noopener noreferrer">自動車の次は建機､そして防衛産業も…セレンディップが｢1000億円ものづくり企業｣に向けて構築した斬新な仕掛け</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月29日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE0xQU4xX0o0Wi1YRWhMSmJwS29ILW16Q0dacWJEb0N0bVJoZmpETzh0RDltN3NRMmctTWdvVlZpUFZnelY2bEFheW94TW1xZHVYaVRZdWFNWXZXd1BxVVJ6RzBLM3F4SzBPVmwxcw?oc=5" target="_blank" rel="noopener noreferrer">AI開発のプリファード、作戦支援システムを実証 防衛装備庁から受託</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月29日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE10dkVDQ2FyeGdxdDZvTnRWbEc5SFRzeVJWaEVlR3NaZkZ6WGNxS3doME9VeVRDQlRCT0ZGTUlSN0lWa1V6TmlxMzFmbk9Oejk4S3VmUDdmWXdPS3lMY01r?oc=5" target="_blank" rel="noopener noreferrer">ゼレンスキー大統領 米防衛産業大手幹部と会談 連携強化を協議</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月28日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE84X2h2Y25VU2E3eXV6NHRvaVlwdTd2ZVhrSmYwOGt0dWhtWENRbmg5cVNkQzJwMWRsVTljU2dyaFBsV2hCMDg3TzJ2a2tLTFpFSmdHaGZVa1BHMXlxWmdDNmRYNy01RHFBUWpEMg?oc=5" target="_blank" rel="noopener noreferrer">防衛省、JTカンパニーを13カ月指名停止 高機動車の不正輸出未遂</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月28日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTFBiOG43dHp5Um1YdWxXZVZVT2xLc2FlYW56YjhIQ2pySnFQWUh3bjQ4c1NxTnR6Y1NaTDV4R3lTUV8xT2JpZWJIQ3d3RmpYMzZTTmxuYm5vb2RfdWdQWldLVnNXZkR4RXRpUWFjdQ?oc=5" target="_blank" rel="noopener noreferrer">OKI、防衛装備を海外移転 豪護衛艦向けに</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月28日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE5ZOHJYNFNDeGNGUDhLQXc1d3ZBU25BSzctWWZrUk4xVEtWZXhJVTNKcGxIdmc2eE9ZMmlidXBZZFVxaUFjTlZtTS1CU0I1RzN4SmZZQUxON3pkRFhDcEw3TkptN1Zkckhkb2pSWm1kYno1bmllVnc?oc=5" target="_blank" rel="noopener noreferrer">「情報防衛力強化は待ったなし」外国勢力干渉に刑罰と自民提言、安保目的の通信傍受容認も</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月28日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE9MM1hCZlZDdlBTWVhWLTdxRURvWW1Wa21ES1F5ajYyMHBvUkR0bDNSWmEtZmdrS01hVjVUYk84bE5VamZhWkpQR0lvck90QkxCRVJGTmJkRDJ0Vmd4NGkwVVd4cmpSNVdncmcyZQ?oc=5" target="_blank" rel="noopener noreferrer">オーストリア、兵役期間を3カ月延長 ロシア対抗で防衛力強化にかじ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月28日</span>
            <span class="source">東京新聞デジタル</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiU0FVX3lxTE8zR00wdG55MlJLU3dhNWVzbUNoMk90enA1aFlBUlZwbkRlaXdoX25MVVFfTGs1T0cyYXl2bGJ5LW8wMWh5a09pRkZlejJLaXVzY2Zn?oc=5" target="_blank" rel="noopener noreferrer">「核戦力に触れざるを得ない」小泉進次郎防衛相の発言が波紋 安保3文書改定を前に踏み込んだ意図は何か</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月28日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMie0FVX3lxTE54a0RBZndWSjk0S2tYSmpORnhLc1lWWFh4MTYxeGJwc1pWczhNSkMxUG5KQzJELWNPNTl1WFhXcHVXNzRYWmRCRHNVbktlWHlSMjFUU081UTc1aG1raWpNZlJSTHU3TGdLUFJDbjh1SUtVeExWdmt4QThoYw?oc=5" target="_blank" rel="noopener noreferrer">NEXA、防衛予算と予算要求の「仕組み・時期」を解説する防衛産業参入ウェビナー第3回を8月10日に開催</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月27日</span>
            <span class="source">NHK</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMickFVX3lxTE0tbE96RHB3ZUpGVVpSODMwcENUaWRMMUsyZm5RNnd6WjBiRzAzOE5QNGx1bVg0NWNabzJ2R3JibkhodmdQZDRtYmNMcTJMZlJCUWhnWmp4RlVlVElmQTRsTjRYNXFsVEYzVnFiVS1OMlExUQ?oc=5" target="_blank" rel="noopener noreferrer">月曜6時台前半 ニュース・気象情報/存在感が高まる韓国防衛産業/何の日 - マイあさ!</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月27日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE9STnJvdzR2Q2syTktlM2YtdkdZNUs4ajBuck1HYmJjYnpmQnhnWWg2UXdJYVVVSUtRbnRUekJ6T0pvOGR4OHJ5QUI5cGhIVWgycU9ybEJoSVhzSW5hR0Vuek54eGZXSkUtRDZEeHhOa1NrSm1LMnc?oc=5" target="_blank" rel="noopener noreferrer">NATOで高まる日本への期待 武器輸出解禁では限界と課題も 世界を知るキーワード</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月27日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiogFBVV95cUxPdE10amVhbHUwOHA3Nkd6S3oyRlNDVk1PSC1kd24tcTZ4UUQ3emhPZnlNeXlUTmR6R2txUTROQ2ZpdWNHRThVaVNpNmU5aUlEUDVjLWlYaWZseTBYOFlwb0FsRlFHa3BYMENQQnBEVUJvLWZ1SDctckN4cEZWQmxLVXNMdnFadjJNTmdVQkx5Sk4yVzRQLU1DRmVkejdSN05FYVE?oc=5" target="_blank" rel="noopener noreferrer">NATOで高まる日本への期待 武器輸出解禁では限界と課題も 世界を知るキーワード（写真・画像 1/2）</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月25日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiYEFVX3lxTFBTVmRKdksyVTJZSlRPbjFkMVkwbEpRR0ZYa0pQSUdnUGQwbEVsVS1YMlJRRUE3ZjJMMUx1WlhJb1RvTzBQbFNGd0J6b1J0aGt3STI1RnBSTGpBNm83ZGlQZg?oc=5" target="_blank" rel="noopener noreferrer">防衛装備、日本の政策はどう変わる？ 元統幕長・前装備庁長官に聞く</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月24日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiYkFVX3lxTE5Zc1RqM2tGWkZvR1hSUFNfZ3M0SEc5WjZtSkR4QUt0U0E5aWNUZnZaWlA1cWd5WjNkWUxmWWFjdVYwN180V0Y0RDV6dzZnZE0xWEUwWWpFU2wxbG9tZXFrOWR3?oc=5" target="_blank" rel="noopener noreferrer">かつて「死の商人」の防衛産業、ロシアの脅威で「もはやタブーではない」…生産拡大・新興企業も参入</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月24日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE4wSjFVTVZ3TEg5Y08yanIwaVVhUVFIQ2hUdDJLZGlhdURueDdpMm5jbEo3ZW1YWEV1djV3bk9YUHA1SGlNbVVQeGJ3bnB2Y3B3YVlzaXdBaHpSZ3lYdWJNb2xZWkFaR0tqalRPTQ?oc=5" target="_blank" rel="noopener noreferrer">米ノースロップ・グラマン、日本の防衛装備品輸出に支援意向</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月24日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTFBheHVKaGhvdG5XQ3BxNnpWbG5rTE1xRmRLWWpUU0RzTUhRaDBPdUdKa0RMTlh2ZDJxUEtBbnEyRC0xMTV3QlpHcnNMSGc4a0lpRUxCRWtZbXZjLV9KNE1F?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛大臣に問う 防衛力強化のねらい 課題は</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月23日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTFAwOWlrbERZa1BpT0dISGI1aTk3RjNHcmdNYko0YkRZd3ZDZHVsa3Y5OFFCUTVRM2Noa2h0XzdEZWRqdFNiVkpxaFBuUVE3bzhZcmo5OEt3ZEtyb0tNcnNacFh4RFluN2tvbDhtTFlRMDRiSFhzeGc?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相が核で踏み込む「あらゆるタブーなく議論」 安保3文書改定の議論に影響も</a>
        </li>
      </ol>
    </section>
  </main>
</body>
</html>

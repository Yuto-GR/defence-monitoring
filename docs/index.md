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
      <div class="stat"><span>UPDATED</span><strong>2026年06月25日 14:10</strong></div>
      <div class="stat"><span>ARTICLES</span><strong>54件</strong></div>
      <div class="stat"><span>LATEST</span><strong>6月25日</strong></div>
    </section>
    <section>
      <div class="section-head">
        <h2>Latest Coverage</h2>
        <p class="note">Google News RSSから取得・フィルタリングした記事です。</p>
      </div>
      <ol class="news-list">
        <li class="news-card">
          <div class="meta">
            <span class="date">6月25日</span>
            <span class="source">Reuters</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMigAFBVV95cUxPdEVwWTRGV2V2cC1VVFd2bk9jdmhoUkR6b3BLYWtGdTNmdlhVMFVxNXQ0d1ZVdGdTYTdaWlBrc1J0SVU0bHl0T0pFNEtyUW9Oc1VhN3RNWjdjTk9PV1Vic3VBRy05aEdDWU9YTERrV3llMmlxV0pqSElVYnB4bVk0dg?oc=5" target="_blank" rel="noopener noreferrer">防衛装備の増産や輸出を主導、骨太の方針に「法人の設立」明記へ＝関係者</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月25日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTFA0cUk0SkpCRm5MQ1FWSjlmVXZOZi1qZUZ3SFZFUEdWbDlnMnFYUlpFcXplUE5WanM2eHdRUFJCSm41cHBDbWt4cUpadjVFN200MXNiSnR6cW5RTWlvU000?oc=5" target="_blank" rel="noopener noreferrer">安保3文書改定 防衛費の規模や非核三原則扱いが焦点に</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月24日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE9JNjVyRGhKcUhUc2k5eHJWWkphNGZVSDYyVTRvVTdqZk9QWHBiQm1JNzRJelNKRXBabWtFa1dYMEVuajduczNEanFUQTl4ZnFhQUNmV3ZuaE5yYlJjRFhkZlB6MV9qc1pOcmZFUy03Q05UWlNzQ2c?oc=5" target="_blank" rel="noopener noreferrer">安保3文書与党提言、核政策の見解相違埋まらず 自民は難題先送り 維新は現実的検討</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月24日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTFBMQnZMQkR2YjFIZ0hOYmRXdWNGOVJheVFCaG9SeV8taGpDUUlIaTBjdy1BbDR2TTFQTGdQaWg4ZFdudHYxVVFLaGlQa3pHYmhRNUl6T2lENmtlVlRVMzUwY2lBb01HaE0?oc=5" target="_blank" rel="noopener noreferrer">安保3文書改定の提言、自民と維新が提出 首相「これからが正念場」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月24日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE1qZWktc2YxV2U1dG5RZEMtcUxYM1d2VEVGdUZzdUt4aGdfaDRaUndUcTFiazVyU0JJLTVEbEFQMEZlakl5RmhzM1l2cjZhRlJ5RVBBUXdiREl5UUlDSGg3SVNwaWotREdMdFlrSw?oc=5" target="_blank" rel="noopener noreferrer">自民党、安保3文書改定に向けた政府への提言全文</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月24日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiogFBVV95cUxNeXUtQ3JTNWhtMkNBVGVjQ2lQNGZFeDF4TnVxLUFsai02a09Cd0g2UUwwcXRpTUhlTHNsWlpGc1I5bU50N29OdmFMN2hlZjl2clExNnJmSDB0Y25PSFZ0VUNZeTRZV25BN2F3aHJiLXhlMHQ5RGdKQmN2Sy04VTFjdVRLeERselFKNUFscEFwTEVFeFhEVU5CQ0ZpWFhrVi1iZEE?oc=5" target="_blank" rel="noopener noreferrer">自民党、安保3文書改定に向けた政府への提言全文</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月24日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1yWEZ6Y2VuSGV2ckdDejFmVlNNR0VIUHo5TTgxNDRFaF9vSjRQcnNwdU5YUzJKaE9ld2pmQ2FOcDlSNnZzQzN4d0pRMkZwOXYyRUdWeEdOV0o4OFVlRi1lMkxXX3l6QTA?oc=5" target="_blank" rel="noopener noreferrer">武器輸出の推進に新組織を設置へ 「継戦能力」確保でGOCOを検討</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月24日</span>
            <span class="source">東洋経済オンライン</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiW0FVX3lxTE56X0t3VVIwclBWdTR1a3czU2YyZjZkUmF2SmE4bU1vZnp2bkhSZ1VsZG5nSzB4V09ldDVpYWJId1hwc25QUGFLMkJpeF8weWg3bWh6QVBTdDJqdW8?oc=5" target="_blank" rel="noopener noreferrer">税金を投じても日本の防衛産業は強くならない ｢防衛公社｣｢国営工廠｣構想が見落とす統廃合と改革への意識の欠如</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月24日</span>
            <span class="source">東洋経済オンライン</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiW0FVX3lxTE13N1ROcnBUM0NSUkhldG5CUVlodFJxUGdxSzV5alI3ak5tTVEwTENESUhuc3UxMVVRNnhxX2w5bUQ2cTFkOWFMUXVzaDUtdVdVZDlQeUJrZmRFMU0?oc=5" target="_blank" rel="noopener noreferrer">税金を投じても日本の防衛産業は強くならない ｢防衛公社｣｢国営工廠｣構想が見落とす統廃合と改革への意識の欠如</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月24日</span>
            <span class="source">東洋経済オンライン</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiUkFVX3lxTFBVbEZxZjhMS1QzZTcyNC1lOGpRc1RIU3BNREtSNHpSYlZZU3V6aEVhNjZIQmpZUzdsSXFoNFlsSzRhVmVkNUgtVjkteUVJRXdFQnc?oc=5" target="_blank" rel="noopener noreferrer">税金を投じても日本の防衛産業は強くならない ｢防衛公社｣｢国営工廠｣構想が見落とす統廃合と改革への意識の欠如</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月24日</span>
            <span class="source">東洋経済オンライン</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiW0FVX3lxTE10elVHb3dzM29XRlRlcUVzc3hoQ2xZQWxTQ2JNcEdCMFdXVzcwNk5pVHlfRzNfNlJ1bkNiZnZHQS1LQ2ZNZzVRVS1hb3Q1b2t6WWtRTmFwa3ctY1U?oc=5" target="_blank" rel="noopener noreferrer">税金を投じても日本の防衛産業は強くならない ｢防衛公社｣｢国営工廠｣構想が見落とす統廃合と改革への意識の欠如</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月24日</span>
            <span class="source">東洋経済オンライン</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiW0FVX3lxTE80QmJQWG5lOGlUN0pITXFBR3hfVkNwRVpqX3R2M1lnNnVCb0N3YkVoaUJwd21xTkZpYXBNVWZNcVJHMHU1WWoxSjJvTElicllTOTh3eTZvdGF0T0E?oc=5" target="_blank" rel="noopener noreferrer">税金を投じても日本の防衛産業は強くならない ｢防衛公社｣｢国営工廠｣構想が見落とす統廃合と改革への意識の欠如</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月23日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMicEFVX3lxTFBKbHgzMHJFLWRDLVFqVF9xN3JjUDZlVWVhZVBrdkJaTExlYkpTc0ZVeHRzNkx5Qk1td25fN2lyQTgwMDdRTndsNThXWm1LQ242Tl9CMk1lRFNrM1U5ZGdmeHd2cjdKNU05d3R5V0VFdzA?oc=5" target="_blank" rel="noopener noreferrer">安保3文書、維新が独自路線</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月23日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTFBULXRhdW0yeGloQ19FUnQ2SkExd19xTTJJMUk3QWpfWnl2aGZUb2s0OC01MVJtUkNzd29VNUtmNHFKdVQ1clA4RFRraDRGZm9hZzh2dy1OYnZvanFYaTZkQVRjSkt0UHhXUWVPYg?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相、装備輸出・日米同盟を語る インタビュー全編を動画で</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月23日</span>
            <span class="source">Reuters</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMigAFBVV95cUxOREpIRWhjMGpFS1c3ZEZneVV6ZlFVQnVNUVJzQVFrZjI5QTBKb2h6M0d2TGt3cDBoTmFOOU9vMHhsWXFydzdVdzN6bENMbmRMUklsNk03VFRCZkhMQl9ONGlpSklrUU9RckZNbTkyeUJqLW1Mbk9HWV9jYTdZY3h3Yg?oc=5" target="_blank" rel="noopener noreferrer">印、ＵＡＥと防衛装備売却協議 超音速ミサイルなど＝関係筋</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月22日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE1vbHhkUzZLVV9rV25jaER0TDQtSlRGY3h5aUYyN1M4cUw3U0RYeU1EWm5mem9oOThfOFhsLUdrYnU5UkpxU1BwbkpWdEtXNmhXcnFmMmUtYkFxYTNfOE1Z?oc=5" target="_blank" rel="noopener noreferrer">中国海軍の空母 東シナ海に向けて航行 防衛省確認</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月19日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE5qMkw5YkFrVzJIUHJQT29iLTNWVC1KRHBPZWNzenJZVzVaa3ljaG5aRVlkeXdwNF95YklQcUltTHcwSXJSa29JUWRUUHIwcjN1TTJnYVFJT3VWQ2JJU2xsS1J3MWQ4cE0?oc=5" target="_blank" rel="noopener noreferrer">「形式上実施するだけ」 安保3文書の自民・維新の与党協議、形骸化</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月19日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE1sTDFwX2dxa09DZTRKbkt2dV80YTZ6ZXpkYzVMQXItdFhJQkRRc2NKc0d5V19tSlJCZWpJbloycUFsVDRvdXllZ0VZbUlFZ1ZWeTdkV0FjbV9FVGRfcnAw?oc=5" target="_blank" rel="noopener noreferrer">自民 維新 安保3文書提言 来週にもそれぞれ政府に提出へ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月19日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE52bnlNdy1ucmJUR0VzMjBTbWdRMlVzRHZSeGl6UFBPTTY5Z2FyVGtudTh1SGNNbmNZX0U4Z0JHbURSbWZpQkw3NVU5QU4xT2lRR3E1cmN6SlFwUFJhZ1J3ZjJhVk9aSDIxUTFsUQ?oc=5" target="_blank" rel="noopener noreferrer">自民党・日本維新の会、安保3文書提言確認 来週にも首相に手交へ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月19日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiW0FVX3lxTE5NVnphSFBQSVZBdlJ0Z0R2azJpVjVCYzlzeGFPLWxKN2JBZDhpS2dmUTJHQ3BoSmZmcGpzVnlfTjVONERTWngxdm8wYVJxUDlCbWlPM2oycUZtVnM?oc=5" target="_blank" rel="noopener noreferrer">AIデータ社、防衛産業向けAI基盤「AI Defense on IDX」において、組織をAI Native Enterpriseへと進化させる「3層構造 AI Data Platform」を発表</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月18日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE04UnU0emdzUng0TWhlMkxfeEpTYllYNHMzNW5XQ25jYUNSN1V5c2NEUVUxeDk4dkNSUnczQ1V3ZnBNU29kSWk5aEtOajNoZHJET1ZzcnF6ZTMyakFYOTdZYV9TZUpFWTQ?oc=5" target="_blank" rel="noopener noreferrer">名大学園祭の自衛隊ブース、職員組合から抗議で中止 防衛省「遺憾」 [愛知県]</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月18日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE5IWlFwOHU1ZUd1SlBjd0p4SHFRZGVSTHpSdWhkVWdacjlKR2NyLXNnZE5jNV9hc2k1UTdaZzIyTTBjOWRFMEszT0lWbmxJdlZuNnFiWG1FVE9hOWFSX202ZE1HaEdnMmc?oc=5" target="_blank" rel="noopener noreferrer">高市首相とEU委員長が会談 防衛産業や重要鉱物の供給で協力確認 [高市早苗首相 自民党総裁]</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月18日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE5iSGxaWDFZcjQxaWtrckZhaEpUSlFpQWlrRFFSenNxVUkwV2F3WGt3R3JwcnRKMWJPMWFJZHBoTmxyRXRQNWZHVUdVU0xtLVZEV1pBLWkzQ2lHLWZ4dHBN?oc=5" target="_blank" rel="noopener noreferrer">米自動車大手が防衛産業と提携 兵器生産の加速がねらいか</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月18日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiqAFBVV95cUxNaXViTDljLXhtRGp3c1F5NWV1eV9rVWhMTF9Kc3dndkhlV1FxRTdiVXEzVW9ZLTV2OWlJT0pNX1NKSGlxdkRCTVEtMnFSMnJpNk43Wm1YUVdpMmJvWE1Pc29XNzh1d0tHNGluN0pPUHo1cThxZjFXcVNvOFBGdGFUNjZtZ0JtRUxIX0JSZ3RQY1V6aFRUMTh0UFlZLW00UTFVazFXaDU3TFI?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相、防衛装備「欧州の国」が要望 もがみ型11隻に意義 平時の最適化に警鐘</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月18日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE43WGoyYWZTLXhHdUlyMWQ2Yy1aaFM2bFNMOFNHTGNUSjVva0g3ZDFMdGphVjBHbFlKQTdTcU5DaE5wV1pBX2N3Rm1QR2ZsRm8taUR6M2VqWEtqcVlydDE4Yk1DbVVleHFV?oc=5" target="_blank" rel="noopener noreferrer">検証：安保3文書、提言了承 維新、際立つ独自路線 非核三原則「持ち込ませず」 現実的検討を</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月18日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTFBkMldvMTJQTkt5Vzh1SE1TQWoxOU1qYUFnMDFjVVllMVBrbmlmbWdMWVZsVldlQXU4a1pfeDhxMUw5U3RrOXFKMUVNdmU1d3JwX1ZpNGhKQnFUdzhIeXIzUnhueExvQm5adlRhYw?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相、防衛装備「欧州の国」が要望 もがみ型11隻に意義 平時の最適化に警鐘</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月17日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE1valhZRzVqdmpMancxbWFsbEl5LXkxM0pSNlVXckhmM2JnakFmUW1KUVNTbmhrRG1CcE1tVE9faThJSC10bkUzQ1R0VC1tNG5GZWtYVUIweVJEb0ZpSUhV?oc=5" target="_blank" rel="noopener noreferrer">退職自衛官と家族の支援に向け 新組織含めた検討開始 防衛省</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月17日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1WWWhUODg5dHZNZ2JZbEFNRklVZFByN01PWlprU3JoUGp3T2lkNTh6N1Z0bmpQT1l0T3ZMN2tXWklwTFV1V0V2bzg0cUJDWXlZb3B0VFA3NlEwZ2tvYTlxY2UtUGhhWjA?oc=5" target="_blank" rel="noopener noreferrer">維新の安保3文書提言、非核三原則や原潜で独自色 実現性には疑問も</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月17日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE1kdW1GdlB2WF9IU3EwcGQ3RUFmUnExVnpZam5WNlllQkpncS11MU85M1I5RFJ6R2tDcmI3cjg1X2pzc0JjUzJNWFdPNVlqSmNycmVSc0dORUpabFlvcVY2b1RySVpQTk1hMjRKNV9hcmd5VWJYemc?oc=5" target="_blank" rel="noopener noreferrer">維新、安保3文書提言を決定 非核三原則の見直し検討、高市首相に提出へ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月17日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE1QdHA3M2dMbnk0a3NLWFpvMFdGRld2d1Vsc3dsd3BpYTJ4eFdsUjJQQmdpc2ptczZJRUQyTkVWY2ZDWEtqNTd2SFRhY2ZYV3cteUNGeXJ2Q1YzMHNlWlY4X0RSTTlKcnRP?oc=5" target="_blank" rel="noopener noreferrer">「独りよがり」「勇み足」安保3文書の維新案、自民から冷めた声</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月17日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTFBjQW5wWGxrdzBvWksweFRMalZGRG1BM01ac0VtYkdHVUM5RGpqSnZRdDFxOWh1c2dRd252c1BtcHN6OXFScWNWTXlWLWo1S2ZjRXlWXzZjWEEyTjN2OWdB?oc=5" target="_blank" rel="noopener noreferrer">維新 安保3文書の提言了承 非核三原則は“現実的検討を”</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月17日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTFA3MkpZSHZNNmlFZUZJZU5VTjl1SDBJYUhFd1lkaklRakY2bEtBd3lSRmU0UW5uZkoxbFRoVkJyNkFveHpBcGNRejd0V3MtSks4LU81Sy1UWW1pOTM3V0owTmhwMFFuN0xHRlpiVw?oc=5" target="_blank" rel="noopener noreferrer">ロングボトム駐日英大使「日本の防衛産業、国際連携に軸足を」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月17日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE03ZDYwQnEzY0tnLTFXWlNQUTZINGRId0NEazdYLS10MHI5U2hQZTJMM3VaYWlIVzVYM3c0WVdKc0VGR2lNUDBDUEtVNkJjSDFBazRxbmJfc1N4R0t5LWo5OXhtSQ?oc=5" target="_blank" rel="noopener noreferrer">沖縄・辺野古新区域に土砂投入 防衛省、普天間移設巡り</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月17日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMihwFBVV95cUxPNlNVLTRGMzM5cUVucjJ2S21TaS1keFhjNzAwamIyZ05LVnBLTHA4bXU4OEJubUJQN3BkZUZoYWZrWkpJMTR2RVp3d0hHUUhKaVVkNExObDJSMUpuWUN4dFlqNEZtME5vb2tZNWpnbjJmNmRXckhqcVpMX3I4SmZyWHZYRUZDcTg?oc=5" target="_blank" rel="noopener noreferrer">名大祭の自衛隊ブース中止、防衛省「極めて遺憾」 SNSで抗議 [写真特集3/3]</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月17日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTFBwTm9iVTBqYkpKOXpMSmc1ZUlJdDRPdW93S3kzcmhmOWRCRjBtZWFhNnowM3JPWGpXNU5nVS1UNk1WRUlyZ2ZJaXQ4MzRrNndmek93bXFSZjVPTDFadUZnT0hJUW0tbDY0c3RmbEFQai1nTWZ1ZFE?oc=5" target="_blank" rel="noopener noreferrer">防衛省「遺憾」名大祭の出展…職員組合反対で中止 小泉氏「災害派遣の紹介すら認めない」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月17日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE9xcjN6VGNlNTFrWklsTUJpbzhUVm5pbDg3ajRXOUY4Q1Rad0VFTkZpLWtZVlNQbW1nb3RwMTBUdk4yWjRtRzRQSUE2Q0tScWJsMmxVME1SWkdKV2FRV0p0WjZVNlhZTTg?oc=5" target="_blank" rel="noopener noreferrer">非核三原則のあり方「現実的検討」 維新、安保3文書提言を大筋了承</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月17日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTFB5aEZJTG1aLVlyX2NTQ0hPMVlIelViejBRR0JCbzFpeTNaR0pVay1DQTRMajduTUVUdFd2OUpRb2o2N3ZDV1NVX1N2bGgzc3RfVXMzTmdaT05zT0cxc2xxTzMzOFBBRlZwaVM1Ug?oc=5" target="_blank" rel="noopener noreferrer">重厚長大の三菱重工、急ぐドローン開発 ウクライナが変えた防衛装備</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月17日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE9HSjNHUnZLQVFNcXZNb2VSRkpYU1BMZFNoM0YzLWFEQmdVanBIV1dDWVJTcE1PRVNwUWlHWnVIeXc4b1dwVzZpQXN0cXFsUnpGNUh3R0JVQmJ0c05PWjNHemVCc0lmb29HN01GQQ?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相、日本の防衛装備品「欧州のある国から輸入求めるレター」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月17日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTFBxYkI1UGxuTXdGakF3TFdsdGlkbVFLcVpNeTU3VU1KWElwVURtVjF4TlBuUWVwSzA3OXA2QU5Bdkt2NE90R3Nnd2daeWtRckJDWlpaSGJsREdKWjA1T2hUMENoay1qXzhJa3ljUA?oc=5" target="_blank" rel="noopener noreferrer">オランダ国防相「日本の防衛産業と協力」 AI開発など念頭</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月16日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE5FMmhCRnMyX1RpLTJSdXlhR1hiVjFZMjhLelkzdGJIR09RRV95bmdfNWVDeUJYMzgtWVprUE9EeFJ4RTNnTUVRU09JSlRVTFMta3dzckdaV1pOUFQyeVluMF9wQnl4Q3I3VGNVNTV3QjBIZ1FveGc?oc=5" target="_blank" rel="noopener noreferrer">維新「安保3文書改定」提言 概要判明 核「持ち込ませず」現実的検討を</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月15日</span>
            <span class="source">ニュースイッチ by 日刊工業新聞社</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiQkFVX3lxTE9UaldHeUxCRXJTRGExWjZKUE00TWdSekhMOFhIWElfU0ZFTzZDZ0dFM3FCX2RYdGZjMDJaTmZhS090dw?oc=5" target="_blank" rel="noopener noreferrer">防衛省、「迎撃ドローン」提案公募…要求性能は？</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月15日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE5HdURNNFkxbkNmNjhQUUxKbmFaTG5tUEZvaXdyRmZxMFlSb2tFRlphbm1RejhRZ1BOdmNSWTNTTEF0LU1mNXRqc3dnZmNoQ0FUS2VncGlRNHA3Q1o4cmhLcWZNRjlBS1BrVHhTRmZicjFqS3JGaXc?oc=5" target="_blank" rel="noopener noreferrer">米作戦目標で振り返る対イラン戦 核、ミサイル、海軍、防衛産業の4本柱に「海峡」加わる</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月14日</span>
            <span class="source">東京新聞デジタル</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiU0FVX3lxTE8wRG9XUHJHMXhVT3JYbnNQRkRZWDkxWV9fQ2h0OVM4bTZfNkZuQUZ6UERiQkVaQlNWNFBJbTFDOWI0dlpCZTg0Sm9XWGwyVXVyY244?oc=5" target="_blank" rel="noopener noreferrer">なぜ軍国日本は武器輸出を進めたのか…その「論理」は令和にも繰り返される 「官民合同」の効率と危うさ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月13日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1XNGFYLVNkdWJOSDM3WEVZSTFWMjF5ZTFFYU1QdUt6dW5tM19SM0NySHBHM1NrbnpEUTAyNDRlVW5aaHpKanpFRE9KMnpqdVNhWFQyMlU4RnZBblZ1LXBFbmN6NGlpRE0?oc=5" target="_blank" rel="noopener noreferrer">【社説】自民党の安保提言 さらなる防衛力強化、財源後回しの無責任 [高市政権の安保見直し][安全保障関連3文書]</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月10日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE5IZzhmWV81TENSNEZKXzctTFRkanAyVFNHWFl4NDRrSXgwMzJZcW1Tazk1ZHZMMFl4NzZMdV9yUS1sbUVvS2dITW1vcS16YUIxQVpZb2pmNy1LeUtVdERZNTNJd2o3UQ?oc=5" target="_blank" rel="noopener noreferrer">「防衛装備品」輸出支援へ政府が新組織…企業に代わり窓口となる「日本版ＦＭＳ」や製造ライン国有化も検討</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月10日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiYkFVX3lxTFA0dkN5MlpMTnkyYW42aG83ZjdtbDRPVGtLVHRIRmplY3ZHVHpJU0dGbUIzUW9EUXU5RmFkTmNkWnRDQWFCTE52MElsTmhMYzBzZ19wVllqZFUtaFRSMWtnY0ln?oc=5" target="_blank" rel="noopener noreferrer">イスラエル防衛装備品の輸出額、過去最高の３兆円…イランなどとの戦闘で「国際的な需要を押し上げた」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月10日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiakFVX3lxTE1mekZ3UndwLU53Nms1MDNWRGs5YnlXR0RhX05zQ3IwamhxdTNBeHd0ZFdybThjaVdtU2hmeUoyLWdhUUlGN3ZlWHVTWHZXQmV0QTMxQWZHMDdNTVYwRGdGdVEwR1FNT2w2WEE?oc=5" target="_blank" rel="noopener noreferrer">「防衛装備品」輸出支援へ政府が新組織…企業に代わり窓口となる「日本版ＦＭＳ」や製造ライン国有化も検討：写真</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月10日</span>
            <span class="source">中日新聞Web</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiVEFVX3lxTE1fcm0xdks0Zlc5NXBVQmxSQ1hIcFZGczlsVkdJRm80c2VvMlQ0a1ZUYlZzNGVIUEJOallGYWE0eHFtdHRieU1TcFlMc1dfRTNjYm91eg?oc=5" target="_blank" rel="noopener noreferrer">静岡県牧之原市の富士山静岡空港、「特定利用空港」への追加を国が打診 防衛力強化のため</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月10日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1TOUNwSjRLWnpIaUxaVzczVlpMY2tnTFFYZjBlXzF3d3hTQ2ozLU50TkxPUV9wTFJ4QW40Z0oxNmRheFJKdW5sVXh4X3VZTGxIbmFkZ2paa09LS3dFZFA4bjJqYS1jYm8?oc=5" target="_blank" rel="noopener noreferrer">安保3文書改定、自民・維新協議は形骸化 「ブレーキ役」公明が去り</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月10日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE9wTEZzWHhkVlRnSWZ2X3k3UnFuYTk5UEJqaE9XZ0ZzbjFkY0Y0czZRNEZ5Tmo3d2RSNE5Ca2cxQnFJbkRIWHhUYUszUnpQa1h3TUtIbFkxOGhKclNHMnFz?oc=5" target="_blank" rel="noopener noreferrer">日米 外務防衛事務レベル協議 安保3文書説明 中国核戦略も議論</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月10日</span>
            <span class="source">信濃毎日新聞デジタル</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMia0FVX3lxTE5MTllHS1B6OXFMMm1haWRBLXA2NEtLdG9aWlA5Nnl5MWFXZXdKeU1OT2ZNZGJFM19NZFNrWVJBYmNCbzM3dnJKT2FvQVVQQU1wc256dl9OcmJzVVNHVjZKam1tRHdmaUQ2aUdV?oc=5" target="_blank" rel="noopener noreferrer">【自民、安保3文書改定へ提言】防衛費紛糾、明記避ける 「現実的対応」を優先</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月10日</span>
            <span class="source">信濃毎日新聞デジタル</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMicEFVX3lxTE9tRTZRMDRxNmpBUnI2c21nbmk1aTJscHY3OGxVa0VUUENndkw1RkN2cXRfcDBXbXZRcmdDMzU5S1FXLWJvMUNQOUlBTVE0bmZGcXpHWXNzT0tEWmJLSHo0cFhDS3dtT3I4RXVkcHZtZkk?oc=5" target="_blank" rel="noopener noreferrer">自民、安保3文書改定へ提言 長野県民の思いは</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月10日</span>
            <span class="source">Reuters</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiiwFBVV95cUxPNWlkXzhQbjV6TFYtcGFhQkV6ZnZXSnJmdDgzc1A2a05lVFVydklLMEU2eTB3cHB5MjVTZ3RJTnNxQlpTTnQxQmpTLW9wS0M1UE9MZ3otb3U2aDYxUmdUb09aVXZ5ZzhuVXRRR01fY2VIMmpBRVdPUkNaNThVY090Q0dxcWY3a2pUR3RZ?oc=5" target="_blank" rel="noopener noreferrer">Breakingviews - コラム：ウクライナ武器輸出は一石二鳥、欧州軍備近代化と経済てこ入れ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月10日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE5vY3AwZGQ5RVVVbTJHdHJCaEVQSVd4emozeFZwQkxTbkp0cGUxeFU1OXVjbzRiTld0dnB0dHlFMkZtdEpVUEk1MXJWSVJXVk9GNExCdU5yaUp1WHJ5aUk3VGRFVjVZTC0xZFBZbzdITW52RjRtQWc?oc=5" target="_blank" rel="noopener noreferrer">高市首相がマレーシアと首脳会談、LNG安定供給で一致 日本の武器輸出緩和を「歓迎」</a>
        </li>
      </ol>
    </section>
  </main>
</body>
</html>

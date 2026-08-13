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
      <div class="stat"><span>UPDATED</span><strong>2026年08月13日 12:28</strong></div>
      <div class="stat"><span>ARTICLES</span><strong>23件</strong></div>
      <div class="stat"><span>LATEST</span><strong>8月12日</strong></div>
    </section>
    <section>
      <div class="section-head">
        <h2>Latest Coverage</h2>
        <p class="note">Google News RSSから取得・フィルタリングした記事です。</p>
      </div>
      <ol class="news-list">
        <li class="news-card">
          <div class="meta">
            <span class="date">8月12日</span>
            <span class="source">Bloomberg.com</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMid0FVX3lxTE5nTFdqb1F3WVhkQUwzMGJocmxUVVAwaUFZMzV4dGMwWjhnUVROUGFFY1ctSG9Qdk1nbmdURktMUWdZeGFKRkJFVHZKMVlYQ3lOaURpREtMOFczZ2ZJcGR1cGF6QVJRanJqaW5WdmJtR29TcldOMzdZ?oc=5" target="_blank" rel="noopener noreferrer">金融庁が防衛産業への投融資を聞き取り、メガバンクや生保に実態照会</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月12日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE5yQXdLTmp6NnZORW9ua0dSZjdQMVRrZ19DdjBiYlk4YkxJNkRoT3lrajBZN0FvODNuZnVsSTVudDJmTzJiQU9SemZ4dXdBZmpobk1ZMU1JcUQzZVd0WWxF?oc=5" target="_blank" rel="noopener noreferrer">北朝鮮 弾道ミサイルの可能性あるもの EEZ外側に落下か 防衛省</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月10日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE5hSVhlR2pJVF9HOVhxUXVGUVljV3BuTmFacHJwcTkwOWNTbXBoQTNoNXpjR05OMG5lUWlrdldYUXZMX21SeFJHTDBWWUd4STN5LXlPRHNMQTEtcEdvblZ2SGIzWi1fdw?oc=5" target="_blank" rel="noopener noreferrer">在日米軍が熊本で支援活動開始、グラス駐日大使「一瞬の迷いもなかった」「日米同盟は鉄壁だ」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月10日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE93ZTExYlpmSlVrcUVqd1VZakM4YTByeWhJYnJnLVNOWlpIUlFHd0VVeFktSG8wQVIxRlcwS3JzODRVSmJTaUdwaV9tdDBzU1VfVTRJLTJfcE5WNXhqWUJrNWxCS19OclNJM0ZhdUFDR3ZwVktKZlE?oc=5" target="_blank" rel="noopener noreferrer">防衛省職員、無免許運転（免許証失効）で神奈川県警が逮捕 箱根で追突事故</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月10日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE8ta3NfQ1p4dGpjT0JVTHRpSVhGZDA0WFhKbEpKOUd2V1NOSUxLZ0xBTElST2dZSUlxOVVTd1FfcVE3dkNuTjBaUmpjNnR5SU9hZ3BEOWRPdzRJV2FlREFrUUQ5NEdpUQ?oc=5" target="_blank" rel="noopener noreferrer">［政策点検 高市政権］＜３＞防衛装備品の輸出、抑止力向上に…同志国とネットワーク構築</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月7日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE1icFUyS3Z6c2Rpd205WTJpc2JFSXA3c3JRNXNRX2hlZEFibC1DTEMxcklDY1dSWDl1cUdQaTVZUWFKQ1llNUFlck4zck82cHZka3VGQnlEdFMxOGFfOVRCWlFIelNrMHBjR0ptQ0JON3VSNXA2UFE?oc=5" target="_blank" rel="noopener noreferrer">防衛省が発信強化 報道官、統合幕僚長が相次ぎSNS開設 背景に中国が展開する認知戦</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月7日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE96ejlzaUFTS0hqRS0xSmhkTHlZNmZneEI2WHRJNHlWbXRJSllWRGhyaWRYQzR1azgzT09EUnhQRTE3QmMwTHpaTTd1SlJLb1M5UkUxMU9FdmlwcVZrcDNLUlFvZDA1Zw?oc=5" target="_blank" rel="noopener noreferrer">防衛省、反撃能力向上へ攻撃型無人機を導入・太平洋側の防衛「監視能力は不十分」…安保３文書改定の骨格</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月7日</span>
            <span class="source">東洋経済オンライン</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiW0FVX3lxTE5uNGFDT2V6cE05ZGgzeDRJbjB2Z1pRMnNiZ3hlNzVkY29YR1pFMjFDNFE3bkFMeTVyQ2NDVnQwNnVwNVcxdXlrM1htbmZNVnQ4TmItMHZlc18tdEE?oc=5" target="_blank" rel="noopener noreferrer">災害支援で賞賛される防衛省･自衛隊､その陰で放置された組織防衛と無謬主義という罪､防衛費を倍増すべき組織なのか</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月7日</span>
            <span class="source">東洋経済オンライン</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE5zTmw2cldBXy05TFVuQkZKbWhqTExXcGpNcUhoaXpYb2xGRE9aQUFBU3BOUzd6XzZPNDhXQXUyZXhnMFpIem5hNWNCaU9JczJxTjN3U1p4LVdMOVR5MUhN?oc=5" target="_blank" rel="noopener noreferrer">災害支援で賞賛される防衛省･自衛隊､その陰で放置された組織防衛と無謬主義という罪､防衛費を倍増すべき組織なのか</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月7日</span>
            <span class="source">東洋経済オンライン</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiW0FVX3lxTE5RbXBONDhnaTZRbHpuNVlSckM3RjdGRlJXYzhyZ1dEMEROQmRIb2d1U1BjdlQ3Nmx0cjJteWFPX3pldk1CdjZzd0g2ZGROYS14NWo4czdFejBhUGM?oc=5" target="_blank" rel="noopener noreferrer">災害支援で賞賛される防衛省･自衛隊､その陰で放置された組織防衛と無謬主義という罪､防衛費を倍増すべき組織なのか</a>
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
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE90OHRUeE9FWnFpQWQ0SW1BclBQZzY5aWJuWGRDdEx2eFplODJKUnlZTHE0Sm1MNUdfQlRpUmFDcmM5enpfdWt2TG12RmlSN2tpVURMcmZXRFVfZHNkUExCRGdqNlBrbGRLMEdoeGE4bFhRMm9iUVE?oc=5" target="_blank" rel="noopener noreferrer">北朝鮮が弾道ミサイル発射か 防衛省発表</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月6日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE11ZFdzNXZpMnNiNU1XaDlOQ2x2RHZZUFRFeWpXM3JxVUVCUzFidlZqMEpHTjhmWXVZTXM5aHFPUWs5QWktS0JSNk9YMkJWWm5OcXQ3bEJZcGNXMkpGS0tzQTdrRk5PNEtr?oc=5" target="_blank" rel="noopener noreferrer">安心はどこに：京丹後・米軍基地 発電機騒音 防衛省「重く受け止める」 専門家入れ対策検討へ ／京都</a>
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
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE5KQzI3d19tN0x4Q0FfRDUzdTRUR3d5NVhmNXRkYXZILWt1cFR6c21wUDdrcjBMaXZ1LWp4Mk1Va0d0QlpJb29TQmhsUGhnY2VXbUYxNXptdWlNRVMxOE5Vbks1VHVXdw?oc=5" target="_blank" rel="noopener noreferrer">熊本の被災地にあすから「病院船」、防衛省の船舶活用し初の取り組み…内科診療や熱中症治療・薬の処方も</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月4日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1IejJ5RWlaeU5GNlE1eG43MWVubUZ5b2I0a21ORmRGaHU1ZnNzUENVcGlwWkpZcHhVaFhTbmRnVnlkYXY1dXNfN1pNWU1IWnlIajB0ZU5YOW84NmNfNklwdzNLSUZ4dG8?oc=5" target="_blank" rel="noopener noreferrer">「生産力こそ抑止力」安保3文書改定の有識者会議、経済安保を議論</a>
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
            <span class="date">8月2日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMia0FVX3lxTFBMNVNSbkNCa0JsX2dlQjB4V3l5R014NWJ1Q3p0bXBZNVlHNmtDZ2c0dHdxczd5VlpINDdBTE5ZRFk2T1F3MkRnSGlhTWtScjl0NkNOYzA2UzZONmliSmhrd0RwN3h1dmhHalRj?oc=5" target="_blank" rel="noopener noreferrer">［地球を読む］日米同盟 相互防衛の意思 隙間なく…ハーバート・マクマスター 元米大統領補佐官</a>
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
            <span class="date">7月30日</span>
            <span class="source">ニュースイッチ by 日刊工業新聞社</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiQkFVX3lxTE15ZkVacGo3OTljSTh2Y0UwSzg5MjA1WUhWdmxST1lrMVZMMXlncGphVWJSMVZnaGhjYmM4cWtWakNKUQ?oc=5" target="_blank" rel="noopener noreferrer">豪次期護衛艦向けソナー、三菱重工に供給…OKIが初の海外への防衛装備品移転</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月29日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE10dkVDQ2FyeGdxdDZvTnRWbEc5SFRzeVJWaEVlR3NaZkZ6WGNxS3doME9VeVRDQlRCT0ZGTUlSN0lWa1V6TmlxMzFmbk9Oejk4S3VmUDdmWXdPS3lMY01r?oc=5" target="_blank" rel="noopener noreferrer">ゼレンスキー大統領 米防衛産業大手幹部と会談 連携強化を協議</a>
        </li>
      </ol>
    </section>
  </main>
</body>
</html>

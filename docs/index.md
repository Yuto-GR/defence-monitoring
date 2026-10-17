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
      <div class="stat"><span>UPDATED</span><strong>2026年10月17日 14:26</strong></div>
      <div class="stat"><span>ARTICLES</span><strong>59件</strong></div>
      <div class="stat"><span>LATEST</span><strong>10月17日</strong></div>
    </section>
    <section>
      <div class="section-head">
        <h2>Latest Coverage</h2>
        <p class="note">Google News RSSから取得・フィルタリングした記事です。</p>
      </div>
      <ol class="news-list">
        <li class="news-card">
          <div class="meta">
            <span class="date">10月17日</span>
            <span class="source">ニュースイッチ by 日刊工業新聞社</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiQkFVX3lxTFBSYW1zU0llNFhacEZMNEhJd2pFbThiaWNUNjBTZU5tSVdpXzZ6bkNJX2JXRV9jd2JibHZFaXZiOWFEUQ?oc=5" target="_blank" rel="noopener noreferrer">防衛装備品にスタートアップ技術取り込む、始動した新たな調達制度「防衛省版SBIR」の全容</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月17日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiYkFVX3lxTFBmLTlWc2I5clFPOWlVVHpSZ0RiOWhpRVNUUnFvcEx3OGZkcmpadnRwRGJVTzBwSWRIRjZuVUdLMVpiczdGMWdnSmU2bVQ4R1ktM0I3eDEtTE9CVlNHTWdXRmhB?oc=5" target="_blank" rel="noopener noreferrer">防衛産業 日欧協力に意欲 ＥＵインド太平洋特使</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月16日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTFB1SUhFZ2w3YjVZN09tcDh2S05XYXNtcWplc0RHTnQ1RlRBNUpUdkhWQUx4aW1oTzRVNXIxVmJtb2tVeEVJcVdXZk5pZHNLVl9mcGdzd0R1RE1MbDJzNHVjODRmRFNzWThx?oc=5" target="_blank" rel="noopener noreferrer">自衛隊に原子力潜水艦導入検討、安保3文書改定で盛り込む方針</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月16日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE9KUldnelAyemluZkl3dzZKZGNwZzZ6WUhOaVhDbVdEekgxdHpDVk12djI5UWNkaEpWRVFnSG9Ud3c5eWJGTjFZOHNwNzZvdVNlZURmSkFZTU1GQjZrZHl5QW5qcDlmUlhSNktqbA?oc=5" target="_blank" rel="noopener noreferrer">マクニカ、UAEのサイバー防衛関連企業を子会社化 事業拡大へ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月16日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE9JZVNoMkpsTktSSm9LZkpocFptZVhOaHVsRGI3WjlrMWhSeVVVbWVLRlJMZi1YNUVRQVU3MVF3SGlLMzUtUVJTQnladzh2aGl5U1c3aXJ3SDBMMUtDWjNSMTNfNzhmdldDT1p6bQ?oc=5" target="_blank" rel="noopener noreferrer">SHIFT、安保でのAI利用プロジェクトを開始 防衛装備庁の事業</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月16日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE04VXc2VG1mTUtiRUxVVHZPY3NsZXl2OVctbVgyLWZJbnVuZnZvbjNZTTB6bVo1VUdRbmhzSGFMdWxyeDYxOW9KejN1SlN0OEVDUExZV2RvQkJSdnA4aXFUTFNRem9IY2Vj?oc=5" target="_blank" rel="noopener noreferrer">原潜導入で「海自が変貌」 シンクタンク、安保3文書巡り提言</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月16日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiXEFVX3lxTE5Pek41UTZ2ajhUOUhESXl2a0QyYVJ4RVJqYXJrcndLVGZVYlN0aENFWHZIbUZZNlAyQ2p1WnNEVGZhcmdhMms0THFWMVZWYmliUzVITG41V2V3REw0?oc=5" target="_blank" rel="noopener noreferrer">日本とウクライナ、武器輸出で温度差 首相、米政権に配慮か</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月15日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE5OQ19POHMtUGY4dThudkp2Vm1TdWE5QUFtdHh4ajV6QWZlRmJIanN3SDMteWFmZG96eVlKV3ZOVXktQ1R1LTh0ZG1JTXZjLXJodno0Y2F3XzMzdHRzcG4xWHQ3TQ?oc=5" target="_blank" rel="noopener noreferrer">中国空母「遼寧」、南シナ海へ 石垣島南方で訓練実施―防衛省</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月15日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMigAFBVV95cUxPVlJjMTJUeWprWjJxaW1ITVRmOExCalp4T24ybEllbVdoUEoyTDJNU0VidDJtdkZTbVdJOXFtQ0phRUJGX0JRcDZnZVFGTzI4Uzd1dEQ0eFdGczd0Zl92ZTV6dWZRTFl1bGNjZjZSallvT3B6ak02QjBMWGFoWVFRMA?oc=5" target="_blank" rel="noopener noreferrer">中国空母「遼寧」、南シナ海へ 石垣島南方で訓練実施―防衛省</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月15日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE85aElrRDROUTVtcTZkMHFZN09LWWlrVkxCRjQ0SWtsYlJjRkx2NlcyZ255RkRRRlhjdTh6MmpjWktJaUg2eU1WZTdWeDk5VklndDNmUl9QWFI5Sk54b0lwWXV3eENpdGRyMlRBaA?oc=5" target="_blank" rel="noopener noreferrer">中国軍の空母「遼寧」が南シナ海へ航行 防衛省発表</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月15日</span>
            <span class="source">東京新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiU0FVX3lxTE14bTFWUEZLaWpiQWk5S2tETlU2NllfVGQ3WWdyQzY1ZFV6NEJSX1hkNm1wdEpobWt0ZEt4RUZqNUNtYXA3V3RCYV9SbklwcDB6VGpn?oc=5" target="_blank" rel="noopener noreferrer">核が持ち込まれたら「攻撃誘発の危険もある」…安保3文書改定でシンクタンクが警鐘</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月15日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiYkFVX3lxTE9CcDZjcHRsVm9BVlRsSGREcnFxMDlnekFRZWFXTXpnQm0wWFdfVVdUaV90NXBzdW1rZzNPNzlzVUNHNDlxX3RERG1kWVJXcmpWUFIxRFBfR0VSRXRubUNZdjR3?oc=5" target="_blank" rel="noopener noreferrer">北朝鮮、国連委で日本の防衛力強化を批判「敗戦国から好戦国に」…日本抑止のために「戦力を強化」とも</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月15日</span>
            <span class="source">日刊工業新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiWEFVX3lxTE9MWEE5S0RubzM4MmUxX3FIZkxEa2hRUHd3ckloMFhMaV9QSEcySk9hemFJc2NDdENYZXl4eEF4OVJyRndKSUhHdnNIblV2QkcyQUItQ3hvbW4?oc=5" target="_blank" rel="noopener noreferrer">点描／「防衛省版SBIR」始動 装備品に新興技術を反映</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月15日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE5tZjQteW1mV3p5U21lSTlhRmdZaTgwbHZmcXhibDVqVUhzaFZiRmVsVUFpc0hyWTBDNnR4c0hZamw2Njd5RVlBWW5LX2pZVXQxR2hiVU5LbnJXNVQwQUt0bFZOMF9WcmloRGJLTA?oc=5" target="_blank" rel="noopener noreferrer">安保3文書改定で非核三原則「表現検討」 首相が言及、環境変化で</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月14日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTFAxcjFJT21ReWN6dzZ1anJVOUd0WlhHcDdSXzF0elhXYWg0YXQ0ZXRhb2J4ZzIxSjN0ejZxeVdIdng1N2VaYVlaTUNSMkVLdjRZSFRPeFNweU50TS1nc2hrRllBajRSNEVqZmhua3lqZW83U3owZ2c?oc=5" target="_blank" rel="noopener noreferrer">中国空母「遼寧」が沖縄本島と宮古島の間を通過 防衛省が公表、戦闘機の発着艦も確認</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月14日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTFBJWWZwdFFrTE5YTUNMNmZmdVJiZmlrQ0U4M0NXd3JKZGZlLWQ5S2JSZE14ZW53QmxXZFI1bUdkcFVFWDRLczlrMklkY0FEWGg5Z25hZ09ZcEJxU2c2c1JqNXhWd28tQ0F1TGlPTQ?oc=5" target="_blank" rel="noopener noreferrer">原子力潜水艦、安保3文書に導入の明記求める意見 有識者会議</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月14日</span>
            <span class="source">中日新聞Web</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiVEFVX3lxTE1WY1JFQXF4Q3NmeU1pdDV4alh6M3FGZFR0WTZRd19VM1N5TkxqY0lxRXNxTk5Na05kOWNsWGpHa2VONThLOG1fbG1jZ3pKRG41NmRHdg?oc=5" target="_blank" rel="noopener noreferrer">小松基地の騒音区域見直し案、防衛省が地元に説明 住民らから分断懸念の声も</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月14日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE05TUlUVUhQUUROYXVFbGhudUhaQmxIcVF1a3drVXRBM3Z5X2xKLURuX1NHQ2VjWWxUeER6bGc0aVFUT3NFd3BhbW5IVFRYeFo0VDZJNmJybmFDb1EyVHo5Z1JLcw?oc=5" target="_blank" rel="noopener noreferrer">中国空母、戦闘機発着艦 沖縄通過後、石垣島南方で―防衛省</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月14日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE9jWFBQLVNrTFl6MnRVTnlfTHJpM2tBc3Q0bkxhdW9BLWg1YTdEdnBteTlHVHdsc1ctT1RDdFdOVUJTOElTQlM2Nml3aG82MmsxNEg1UHJaY2w1ekZSRjYyTjBGcVZDenc?oc=5" target="_blank" rel="noopener noreferrer">原潜「導入」「検討」の明記求める声 安保3文書の有識者会議で</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月14日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE80THJ1b1hwR3pfSDVTaXlCOGtXaEw2LWw0TzVLLV9OcnNXQXNyc2x5X3FLVnhiQVg5TWNmN2ZIVllzSHQyLUpNWEdkTmN2NFA3WHF3NGZ4Y1FCN3ViZjBDb21fVzN0VUk0MC1FSA?oc=5" target="_blank" rel="noopener noreferrer">安保3文書改定、原潜保有の「調査」明記論 建造1兆円の見方</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月14日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE9RWUxxUDhyTjdjZ2prdVpOM041a2F4eUl1WlhCR2x2SXVzYkNSS0laRUJvM1pCdHNmQjFMTG4wVmdpaWxmY2tmb0VXM1dVaTcyeDFKaEplZ09qMzZ1SUxvQ1lhb3hzcng0OXZXNkJEVC1Wam9DeEE?oc=5" target="_blank" rel="noopener noreferrer">非核三原則の例外規定「検討の余地ある」 高市首相、安保3文書改定をめぐり答弁</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月14日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE5oYmtFWklTNmRsT1BRWm1TZmE4cXFTUW5vS2N1WHp3TE80eTFTNElUN21Jd29VX05RWFFXY2x4NDBDMEp6bXlHMFlJM0pSRnNVM1RHZFM1LUQ2Ymh0YUZR?oc=5" target="_blank" rel="noopener noreferrer">防衛省が小松基地周辺の住民に騒音区域の見直しを説明</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月14日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTFAyb3dOQ19IS29ibnIwRlBZbDRWRm5YS1gtcGVxdXZqUDNRMkJsazZ6cUtnU194Q1lZR0dSc3BUcy1RUGo1TTJYZG1yRlNBM0tMODA4azV1bXd2dkltQndEakQtdlMtS05aeHlpYw?oc=5" target="_blank" rel="noopener noreferrer">高市首相、非核三原則「表現ぶりに検討の余地」 安保3文書改定で</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月13日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE5uQXpEcUppcG8zb0dLNnFJbTRPbUFseks4SG95VE5FX1E1d2FtLUYyQmttS3BvYzRHbDd2NFV4OEl5R0RnVlZtQ3Y1VzFmSmVxb01kNnN5S1NYUWxlaVpwVV91ZDlESTJJTUx3RjZrNjlIMnRkX3c?oc=5" target="_blank" rel="noopener noreferrer">退職自衛官の再就職支援、自民議連が設立総会 安保3文書改定に向けて提言へ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月13日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiogFBVV95cUxQMEZqaTU2TUdaWHNNRGVPdnppNjZpY2lvTFprdklmMVhpOE1JSkFuN1laQWNHVDBOM1VZWl9obVlCQVVLY3VTM3VMel9UYW9nNUVDV25jbGd4c0o2VUZrUGtGN0ZWUlBHT0lJRmlWNUJVZjRHQ2lTYTNzdGxnUGc3UzhpdTNoblpIeVUxenJIZ3FpVW44NV9lNlJSZFFJeXdSNlE?oc=5" target="_blank" rel="noopener noreferrer">退職自衛官の再就職支援、自民議連が設立総会 安保3文書改定に向けて提言へ（写真・画像 1/1）</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月12日</span>
            <span class="source">東洋経済オンライン</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiUkFVX3lxTE14Q29teG5fVXdwSVQ3TkhWYU8wWl9EdlgxcFk3N2pfSUZnZFlRNTAxTUpnUkh5QjZWTmlaUW0yRHdpVHdaMG9jYkN0VERtRWctWEE?oc=5" target="_blank" rel="noopener noreferrer">このまま戦争になれば自衛官は｢犬死｣しかねない！医官不足と時代遅れの医療体制を放置する防衛省の信じがたい実態</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月12日</span>
            <span class="source">東洋経済オンライン</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiW0FVX3lxTE42bWxGcjNXTEpGTUNjLXF4MGVnTk1zdzRiMk9QeWtMR2dIT254Z0tMQkRfM3R2OEJpZy16d1AtNHdqVlF4M00zSnVWUWw5MEhPOVJzeVpVY0M5Wms?oc=5" target="_blank" rel="noopener noreferrer">このまま戦争になれば自衛官は｢犬死｣しかねない！医官不足と時代遅れの医療体制を放置する防衛省の信じがたい実態</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月12日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE95VFhaZUZzQWhMbEFRa09wV19yRFp4dG1iQTBSQUNLLWNIRTNlQkZnY3lKM2VGdjhaRUZVQkY0SDZyZWF5Q3JjdVhqUXVZbFlPMndYZlFYT1M1LWN1UUNCWmVGSm9GMmpCTGRabm5qLTF2ejlhVUE?oc=5" target="_blank" rel="noopener noreferrer">北朝鮮が相次ぎ弾道ミサイル発射か、すでに落下 防衛省発表</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月12日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE42TnowUklUSmNYeXpkTVhfX2p5SE5sTjJTZWxZVnhBQmdFTG0xSWRtV1FtTkdLZlpxUnhWU1ViWVRtMGRIVGNaaFo3VDgtM2xpSEw0XzlabjZ0TFBkMUFjell6akg0NGF4NmpRZA?oc=5" target="_blank" rel="noopener noreferrer">北朝鮮が弾道ミサイル2発を発射 防衛省、EEZ外に落下と推定</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月12日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTFBPUGp0MllaaXQ2ZXRqUkoxNVkzTkFjSmJaZS1sQ3ZWUnlBeXQzMGtuVHdMM3U2Q0NSYjI2VDM2dHhvX1EtbXI4TVB2R3NDM1Nfd3JBS1FVYUtMSGR2X2x5YjlOaElSUQ?oc=5" target="_blank" rel="noopener noreferrer">【速報】防衛省によると、北朝鮮からミサイルの可能性があるものが発射された。既に落下したとみられる</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月10日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiYkFVX3lxTE1IcElnVXBCR0NRQkl0R3M1NVl1R2hZVlVjX3phUHcwVXVzajdXMjlDVkt0NzRoRGx0MWZ2MGdhN0F1bDFTX0dpMkZXcndyV00zSUdyWWlldjhaSHRhNHZOVnhn?oc=5" target="_blank" rel="noopener noreferrer">台湾総統、無人機など低コスト兵器で中国に対抗する考え示す…防衛力強化は「挑発ではなく戦争を抑止するためだ」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月10日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE1TT3E2X0tMWFVBWUIxUWFwWUk0TzBxZEZWaF9BZ25fZl9BS3ZxXzZfQnNwalFQeFdsazQ1Sl9tWmpyTDdZaXRYRm53MUJxaVZXZ2hpckVVd3NjTWFhRXZJ?oc=5" target="_blank" rel="noopener noreferrer">台湾総統「中国が現状変更」 防衛力強化強調し連携呼びかけ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月10日</span>
            <span class="source">東京新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiU0FVX3lxTE5iQlhLOTNOT3EwdVNCbzJIZ0NIaFdpWDJKelNSWHlxVjNoNzZ0OFR5MlRpYi10aTg0VnFsSnZYV3NCUWZ3MXpMRGRhNWhOemlKS3Jr?oc=5" target="_blank" rel="noopener noreferrer">台湾総統、防衛力強化を訴え 中国に対抗、双十節で演説</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月10日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTFBpUmhrRHVWeUhmMFgtYk9ybFZ5QjZRVmd0N1VYa3llUlZrLS1nU2xhMHA0OEpJR2xGLThkck5zcFd0U0YzdWpVMzg4bG5aN1NBeWpNN2VxSlhyZTByTzUwTlR6TlFRdw?oc=5" target="_blank" rel="noopener noreferrer">ロケット開発 事業者募集 防衛省 衛星迅速打ち上げ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月9日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1YOTkyOGxZb1dUS1pmd1FvRExTMGFseGRDcXFFQzJsZXFhV0JVSndCV1NSandOLTdwdE1vcHQ1QnZUY1A4elNUM2dlS1pYNUE5VFJWclhDX1RzYkxzdnF5YThsZEJIVzA?oc=5" target="_blank" rel="noopener noreferrer">防衛省がロケット開発を研究へ 有事を念頭、短期間で衛星打ち上げ [高市政権の安保見直し][安全保障関連3文書]</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月9日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE5jMTJsYk9hYkNXYWVUcktBSTlDSXZraVJ4SFhJc0R2anFOS3k4clJDZFh0dFZ3T1dpU0R4dUs3UzhKS3dTaVp2VkxLdVRhcU1UazhHWTJNR1pyNGhpd253ZThNWQ?oc=5" target="_blank" rel="noopener noreferrer">ロケット打ち上げ、迅速化研究 防衛省、衛星攻撃に備え</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月9日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiggFBVV95cUxPTTVmOXRFbHBTSVh1OVBuZWNrdEdVUm1ZUFRXd1lodU1iMXVGX0tfMVlyYUdYVzE5VnNKWjdUSEdsbDlnSVlTUFI4dFBxQUk3Y3FXblAzaThzY05MaXVUTUlDMWNWNFZRblJBb0wydDFlMzgzUkhnNU1KLVpfN09yN1Z3?oc=5" target="_blank" rel="noopener noreferrer">ロケット打ち上げ、迅速化研究 防衛省、衛星攻撃に備え</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月9日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE9EWXRqNXJISDZJMThvWXJwVFdzY3IzS3dSRjdNS2l6SmJnTWFvQktrMDhvX25aNk05akRwTHVrVjhEek1lZGlRdVV1QU1pRXdzcTd0bDdROXdBU1plajlSanMtV05Hdw?oc=5" target="_blank" rel="noopener noreferrer">硫黄島の発電設備点検業務、防衛省が誤って随意契約…「特殊性を考慮する必要はなかった」と会計検査院</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月9日</span>
            <span class="source">東京新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiU0FVX3lxTE9oWi1MbExwMkNxNDhXOFBPUHl4WU5HSG9vaTMyZDJXRkVBVmREQzhhQkpYRWh2Qm5POFV1cWVpNmdrZ0IyOHJPd05qVnBscFdkQU5R?oc=5" target="_blank" rel="noopener noreferrer">ロケット迅速発射へ調査 防衛省、宇宙輸送を強化</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月9日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE9nOU9LS1YzN2o4ZV94bUctbGVhb3o1ZjlHdnR1SEp0bEtEa2JUQlJmOHdpRXpwQTVzazRGZzJkQUxvNTRjaURMQmE4T1dxc0pIaXBVekRRd3JIM0ZSdGFIRWNHaDFIUmRFNGU0cA?oc=5" target="_blank" rel="noopener noreferrer">硫黄島の防衛省設備、随意契約4件「不適切」 予定価格9800万円過大</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月9日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE5tdmdJQ21vdnV0V1V0WHJpMWRwY3Byb0lha2d1U0U5bHN3cGNaa1VEQjR4djE5eU12QjYxZlZqT0xQcmdlNHJ3S2tvMWFnanJrOG9OUmJxLV93MTRlMFNhbmowRHZISlk0ZjUzZkdpMFEwTGdwSnc?oc=5" target="_blank" rel="noopener noreferrer">小泉進次郎防衛相、原潜保有「議論の必要性は国民も理解」 安保3文書改定</a>
        </li>
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
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTFBPVG9KNzZ6X00tOXFybHFsQUhwTkdmcldfR0d2MlNya1RQdnR6eDhmM1ZTRW4wcVhBYVBaR1pmX3hEMFhkdkVnaVlaN3BIM3p3OUthelY2QkhaemRGMjhn?oc=5" target="_blank" rel="noopener noreferrer">防衛省 宇宙への輸送能力強化に向けた調査研究開始へ</a>
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
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE1kUzgxazZETTF1c2s4NU5waWJHSGV6WkhzeUVoN04xTGtpeW5SVDhyRU5OQ3MxRG1lUUdfRHg5Z0NqYTFaT3h0RTJOTnpKdDZETGd4T2NCbWhXRVpCT1l0Z3ZnTlhBV3NaMVRubjZKT0V1VUkycUE?oc=5" target="_blank" rel="noopener noreferrer">＜独自＞核持ち込み、緊急時の例外記載案浮上 安保3文書改定、非核三原則は維持へ</a>
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
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE9DOUpYei1ybnEwUU9Gd1JqS1hCdURiWTA0bDZTckVGa2xuVlRwWmhiRlpIWVdxa0lsUkRpVzJfVWJCYzF4aGJRQUtvNTJwTDcwSk5PREhRTGJrLXZ6c1VF?oc=5" target="_blank" rel="noopener noreferrer">青森県への「シーガーディアン」配備は2031年度ごろ 防衛省</a>
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
            <span class="source">Reuters</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMihAFBVV95cUxPRzYwUThaOTNBWHgwYlVTcS1zbDBFaEpweHZqdFVGd2FkRDNFX044dnVLLVc5bWdLd29lM3dpZWl5TG9IRTZJa2VjUzA4VFN2MkdjeFZZcWs0UmVjTi11OERkUmpNWHhLVmlGWUNrbkJOODhSR0pWLXJEUFhPdDg1eHI4bEk?oc=5" target="_blank" rel="noopener noreferrer">米台関係、米中首脳会談後も強固 防衛装備の適時引き渡し重要＝駐米代表 | ロイター</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月7日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE9mQURRSXVJYmFlVFdmRVFXT2tEZjY5OGY5UGFtR1N4SGozbDhZaWhyV2tHQW5RaVZzUW5waHFqNUZpQlBocmFDakVrd0prelpXQkpvUF9JOVNyZw?oc=5" target="_blank" rel="noopener noreferrer">中国軍とどう向き合うか 安保3文書改定、日本の選択を専門家と解説</a>
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
      </ol>
    </section>
  </main>
</body>
</html>

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
      <div class="stat"><span>UPDATED</span><strong>2026年06月19日 15:24</strong></div>
      <div class="stat"><span>ARTICLES</span><strong>57件</strong></div>
      <div class="stat"><span>LATEST</span><strong>6月18日</strong></div>
    </section>
    <section>
      <div class="section-head">
        <h2>Latest Coverage</h2>
        <p class="note">Google News RSSから取得・フィルタリングした記事です。</p>
      </div>
      <ol class="news-list">
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
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE9qRjVKSVdEd1lWakV3ZDVFeFNXcHNrbVZ6WnpIRzZEcjRQbFdKTUs3d1JnMGRyd09IYXIzOEdsa21CcTEySU9FaWNaSG5KOGYzSnlNRVRJQkVmWjFMelV0LUF0eHZzUU5R?oc=5" target="_blank" rel="noopener noreferrer">名大祭 自衛隊出展中止 「極めて遺憾」防衛省投稿 妨害予告や抗議メールも ／愛知</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月18日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiqAFBVV95cUxQZ3FWZnl5QnZqRXoyWW91NWVFY2R0VkJMLWFaQUp6N0FfYnlRa05tSnBwR1F5NmFuaW1pTUktM0lEZ2R5QlJRRk9OTHcxNFk0U3RmMTVMNEdkMlBSVTQ4MGRiS2xBQWtRQUFZb2Nhbm9BLXNBcG93RWRmaEhna2lpc3oxd1owcF9kSTJCRjRrcE1SaV9mcFhHR09WZEJYejNMUjF1QVlCdjQ?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相、防衛装備「欧州の国」が要望 もがみ型11隻に意義 平時の最適化に警鐘</a>
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
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE80UTlKWF9NaUQ1TGp4eDJLYzlEd0xJSFlTRG9ub18tNnRmVFA2YXlHNTZ2YURhTEdFaG1UWTN5NExaVGIxNWpyNXA5UlhqeEFlamlRX3NpM2dWaXVnUmlzaHl1akZ4ZXE2THoxTg?oc=5" target="_blank" rel="noopener noreferrer">日EU首脳、防衛産業・重要鉱物で連携確認 G7サミットで会談</a>
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
            <span class="source">中日新聞Web</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiVEFVX3lxTE5CNlpNZm5iajdnSlhCeU5NZDNOU19zR3E2LUI2VFg0VnZDV2c4aTR3NkZxSkR2OFZXT2dtN0g5TDBwUVNYemhIeHFKSFA1VUFhSVhEUA?oc=5" target="_blank" rel="noopener noreferrer">名古屋大学が防衛省に謝罪 「名大祭」での自衛隊ブース出展中止で</a>
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
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiggFBVV95cUxQekZtRjVlQkE5eVFZb2drMmdWS1ZISHdWbFU1eFpaTkJaODlpRkxQX2R5NURrR3pKX2xoa0VPdXNvNlppbkg5ZVhPN0gwRVhBMjFvTWNRWFRDT0x0SHpaTEhWMFExbXExVWhTLTlKOFhGRGhQTjRKWEFJQkwtemI5YTV3?oc=5" target="_blank" rel="noopener noreferrer">沖縄・辺野古新区域に土砂投入 防衛省、普天間移設巡り</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月17日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMihwFBVV95cUxOUnExNkNGODlwMm11QXNVNU9nZlMxNVR1WkVzTlFvSUljTEd0LWZNTzduY0JObXowSXZpR0diVklrNGQwVWQyZUVodllkaTVTM3dhZVB6VHZjYmlfamRIM0ItbDlyS2s0R0FyMDByU0RDd2JwVFBTRThfUnU0MWtFV0NhNnlndjA?oc=5" target="_blank" rel="noopener noreferrer">名大祭の自衛隊ブース中止、防衛省「極めて遺憾」 SNSで抗議 [写真特集1/3]</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月17日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE8wSm9pOTJ1MkoteHdodFV2YU5ad0doTUZQcVJxOVdYT3dNV1IxLUpsSk1IdVNfZGhhVzZ3UXZQWUZLRWxFR1ZaVVVNRjd4WlVXb3NIZ1VsU3RZakVzOWNlUDhZRVNOMXo0?oc=5" target="_blank" rel="noopener noreferrer">名大祭の自衛隊ブース中止、防衛省「極めて遺憾」 SNSで抗議</a>
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
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTFBiVzZScU1UMl9vUmtwMWhtR2h4MGdjMVByc0F0SXlIdWpCUlJjd01HVEYwT2E1NHJ2ZlhkM0QzQzRCYWhIaTRfcjFUb21qeDByaGNWaG5WLWNWVkUyWTJURFg2ejZ5TkdT?oc=5" target="_blank" rel="noopener noreferrer">維新「非核三原則、見直し検討を」 安保3文書提言案で</a>
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
            <span class="date">6月16日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE8zMWNQYzlYRkNMcU5PQlNnY2RBTkpKd2d2UXp2by1wVG9xOUc2SXVlb3hSMW04aUZEQnN1QlI5V1lmQThWV3RNckEtME9hLXRZQ18xTV96bHNBYmhxMU9Z?oc=5" target="_blank" rel="noopener noreferrer">維新 安保3文書で論点整理案 “非核三原則は現実的検討を”</a>
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
            <span class="source">中日新聞Web</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiVEFVX3lxTE1fcm0xdks0Zlc5NXBVQmxSQ1hIcFZGczlsVkdJRm80c2VvMlQ0a1ZUYlZzNGVIUEJOallGYWE0eHFtdHRieU1TcFlMc1dfRTNjYm91eg?oc=5" target="_blank" rel="noopener noreferrer">静岡県牧之原市の富士山静岡空港、「特定利用空港」への追加を国が打診 防衛力強化のため</a>
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
            <span class="source">Reuters</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiiwFBVV95cUxPNWlkXzhQbjV6TFYtcGFhQkV6ZnZXSnJmdDgzc1A2a05lVFVydklLMEU2eTB3cHB5MjVTZ3RJTnNxQlpTTnQxQmpTLW9wS0M1UE9MZ3otb3U2aDYxUmdUb09aVXZ5ZzhuVXRRR01fY2VIMmpBRVdPUkNaNThVY090Q0dxcWY3a2pUR3RZ?oc=5" target="_blank" rel="noopener noreferrer">Breakingviews - コラム：ウクライナ武器輸出は一石二鳥、欧州軍備近代化と経済てこ入れ</a>
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
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiakFVX3lxTFBUX0dzRUhnS1lQOHNJeGhzVVh4LWhTZ2s0M1E0dk85dHRPV0lVUWhrWnpZWmpLWjJIU3RiZFdzd2ZHMkpCV09hRjJ0UU1xMDdVYUJwcm1GZTlXX3BwUVE0ZVoyd3VadDh5U2c?oc=5" target="_blank" rel="noopener noreferrer">「防衛装備品」輸出支援へ政府が新組織…企業に代わり窓口となる「日本版ＦＭＳ」や製造ライン国有化も検討：写真</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月9日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiYkFVX3lxTE02UWRJRUpiSEFuOGUzeGFsUU92QWNqS2JhTVNnM0VpR1Z2d0tEbFk4UFZwWlh5elNlQzUyQTNlQVVRdVl2eHFOX3JHLWJlcFJWV2M0cXJXb2Jxbk9oQXkzT0ZB?oc=5" target="_blank" rel="noopener noreferrer">中露朝改善、脅威連動も…防衛省防衛研究所中国研究室長 増田雅之氏</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月9日</span>
            <span class="source">Reuters</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiggFBVV95cUxQUFJ3UW1icTcxVGF5eWQwRFZuU0NCRDJ0djZMaHRTWUhCSFlObWFrY3U0MzZNZUU5Wl9TOElQaDRweFU3SmtCNnVkb1Z6YmVzS2MzRUtlSHhxY2Z5WmkyM0l4czFKaXhwWFdUX1RWaXB1VE1xSjN1cGhxYnp1Z1kyQUdR?oc=5" target="_blank" rel="noopener noreferrer">装備の生産基盤強化へ「防衛公社」の設立検討、武器輸出も支援＝関係者</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月9日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE9HX0JxemNhU0kwUmIzOS0wS3RmRjNTeU5fbjVmaHhTRVk0c2M3djRYRm5TRTgtaGp2T3FDWVlZa3N5RlBnM2dNYkYwck9iNDcyeXgtNm9ILVhiRlhFeFRqM3VkWGRPSUk?oc=5" target="_blank" rel="noopener noreferrer">無人機の「大量導入」要求 自民、防衛費大幅増へ安保3文書提言</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月9日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiqAFBVV95cUxOZjdZa2NqLVFhMVJleTdjUVlSQThPT0NNVHowUU5Vb3BUOUZEZmpqOW85Mk9PWHFnY1dITFNyTHdOY3gzM1lMUXZDLV9pdjRWSUJ3YkRoOHZlNGtLeVNiU0tlbEdoVVplc1ptOWpucFZvWUVqVGFmN3BuUkNaM3B0ei1DU1l4MzU3SWhuaDJTNEs3aDBqcmhINC1YUnRxdTliZ0NaZ3J1a1M?oc=5" target="_blank" rel="noopener noreferrer">同志国と「防衛協力網」 安保3文書改定へ有識者会議 非核三原則見直し賛否</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月8日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE9PS01OMGk0a2hIVEZUS0E5cldia01PbE55S3k4MVRZYWhudWVibDVkcVhKcGZCaDlCSmV4WTJWd1dFWHlyb2U4MEtKWFhEV1RweVRrR18tWldxbzBqc09sREdYSE1La2tEcEdMNTIydnM3WngtUFE?oc=5" target="_blank" rel="noopener noreferrer">安保3文書、第2回有識者会議で非核三原則を議論 賛否割れる</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月8日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE9wNE1fVXdPWEthdGZTTXB6UWVHS1Vkc2xTZndoMUo2MmRPNVdIMXU5Z3BDZFBJWk9TcTUxMm5TUGFhTW5XWm1tQlpNVUhDaWdZWHB3UGJDNmswRmdfc2k2VWV3S1dwYjQ?oc=5" target="_blank" rel="noopener noreferrer">高市首相持論の「非核三原則」見直しを議論 安保3文書有識者会議</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月8日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTFAwQVVzZkNYdVF2Xy1SWHVVRWdaekFkZnM4NmVMRFRfQTZoZlRWSHZZeWhGRmpoVndUYTJ6REJuMFphQTM2eHk1Z2JtVVhQR19CWHV6NWVKV1Q3M09MVkRDZWRxWmwzLVhm?oc=5" target="_blank" rel="noopener noreferrer">激動期の安保：維新の安保提言案、概要判明 業務従事命令を防衛産業に拡大</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月8日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE10emUxMElITjF0OGJyNUFmTm1HQ1pzTkJmSHNYaVZGSlBCaEFxdnJQNENQYWYxWDRNZF9oUjJuMTF3WWFTOTdvWkc4cUFnMTI1bmd5NkdOYUp1bFd3TGxYbW5mTUY4UQ?oc=5" target="_blank" rel="noopener noreferrer">防衛装備品輸出や技術開発でも同志国との協力強化求める意見…安保３文書改定へ第２回有識者会議</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月8日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTFBCeU1mM0lGZG9TWW52azhFanQyeXhMYS0tUnlnWXpYem5wT3dFUDFjdW53YmthdUNiUElyTVUza3JhWmdiTnN1RU1qWVQ1ZVNsNFRxc3VVMTJwQUlGdWdDUWNyQ0VSVUk?oc=5" target="_blank" rel="noopener noreferrer">平和国家の転換に？ 改定が進む安保3文書、知っておくべきポイント</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月8日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE5Gdi1QWUFEQmxRTUFhWjNLNzFJWDRDX1dRRlh4QnpBNHRCd0JDQ3BibnNqYXlmWFV6MTFNSnZtMHJmNE9fMHlNdnF6ZFdNdHRpTVVEWnByeFMzVFJmbzV6U2t1dHF6ZjA?oc=5" target="_blank" rel="noopener noreferrer">高市政権で安保3文書どう変わる？ 防衛費や非核三原則…8つの焦点</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月8日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTFBhaERBT3VCRWVVcUF3NVdfbVpENl9wbEM2TW93Vm9JOHZzSUtDVEJaQ0lIVUFSSFFnQVZmUHBUWXlhTjhjR2x4WmZ0TGozY2QxRUpNeS1JNDNldTRzZU5ZdThiNnBacVFDRzY4ZQ?oc=5" target="_blank" rel="noopener noreferrer">「非核三原則」見直しに賛否 安保3文書改定巡る有識者会議</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月8日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE00T2JnVVU4VmsyRG1qWnJMSGpOeEJjeHl2Sm94YWM4cGpvRldpTVRtNC00MDRIeDg0VkZpTmR6czdOeEdBbzVHY0U4Si1rWWl4QXVvVkJQMTlaUVdKR3IxU3FqaklLOW5s?oc=5" target="_blank" rel="noopener noreferrer">安保3文書改定で有識者会議 非核三原則の見直し巡り意見に相違</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月8日</span>
            <span class="source">Reuters</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiekFVX3lxTE5ZOW15akhMeFNOcGMyVW1wRGtHSmdOVExHR1EwZTdpLXFER3FSSTZJM1NkdWNWcHZ4UGczV2tMMzlyY3EwdGc5UEo3dU9kWDg1bzBzV1ZERmd6VGhfZEN5Nzd6ZzFvbThtaEl5X05HMXZjS1F6X0JpX0FB?oc=5" target="_blank" rel="noopener noreferrer">「安保3文書」有識者会議で非核三原則を議論 見直し必要との意見も</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月8日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE9XUlNoMW5sbW9Dc0tMak84Y25YV29fMHpxSUE2eHhGaHIzWmRhRlRENEh3UTI5aVJmUVNJX25MOExOb2tSZTZ4aGpqaTNxeWgxUG1HZC1ROVUwT29hQW80?oc=5" target="_blank" rel="noopener noreferrer">安保3文書の有識者会議 非核三原則の議論すべきか賛否</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月6日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZEFVX3lxTE1KVGc2OVZwQmxkRkNBUlpyNjBPVmt5SWpaekt6MjJUZmdRbHBUX0hUVDI1YTZyN05reU1PUEs0N3V0WnRHaldNY3A0TXhjeE1IRnZDVlpjVGp6N0dvU1hGVWdtNWQ?oc=5" target="_blank" rel="noopener noreferrer">画像・写真：豪ＮＺ、防衛装備協力を強化：時事ドットコム</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月5日</span>
            <span class="source">日刊工業新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiW0FVX3lxTFBDczBBMm5LSTl2NUFOLV9wOHM0enJkT1hxdlFSZ1JfbV92UU9ISFBXbGNqSHJPV2lXemtOejJvOUgwSUg2bGpFRDUySzNraU1jeXVNU3RwV3E4ems?oc=5" target="_blank" rel="noopener noreferrer">広がる防衛産業市場 民間企業の持つ技術や製品で国を守る新時代到来【PR】</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月5日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZEFVX3lxTE1PTHlHT0FvMlJxdDJBbXk0b200b2t4Ml9lOWZDTkt1Q3Fhdk5PTUlGUHVSckpROFBVRy0zeXpLSnVYbU9FS0d1R0VXNXdIYlBCTEVPWlF1ZVVLZ2xnbVA0NEwzczA?oc=5" target="_blank" rel="noopener noreferrer">日本の防衛産業１４社、ＮＡＴＯに製品アピール…事務次長「日本は技術とイノベーションの真の巨人」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月5日</span>
            <span class="source">時事通信ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiT0FVX3lxTE5SaFVPcExhbWNxMTlUM2NDNVkwRC1oMVF3TUFERXhuc3p6bV9KazdoLVRTLWc3Yk1MUVJkei1obUpmUHgtOXEzci1lWG1sVXc?oc=5" target="_blank" rel="noopener noreferrer">【インタビュー】「マスク氏に宇宙で依存せず」 防衛産業でも日本と連携強化 独ブレーメン市長インタビュー</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月5日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE5yUW82OWt5VWNwNFpHdUxyb2x3WjJELV9zZEJyNXQyQWxMSktaZDk4MTJQenR3VHNjcHYxZDVtdENjT0NNQ0Zoc0ZTaGlOQllWQUJPWmVmY0p3SEF3NVJlRlZzc01ZTm53?oc=5" target="_blank" rel="noopener noreferrer">社説：安保3文書改定の議論 防衛費増ありきを危ぶむ</a>
        </li>
      </ol>
    </section>
  </main>
</body>
</html>

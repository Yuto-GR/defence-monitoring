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
      <div class="stat"><span>UPDATED</span><strong>2026年10月03日 15:16</strong></div>
      <div class="stat"><span>ARTICLES</span><strong>44件</strong></div>
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
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE8wczA2cGZOMUFrRkRhbWZ2bFRIdDhIVDZaN0RBUlh3QkJpdlhQeFdXNkRCNDlZYk5LLTJFR2JfbVNvMHNDZ2FpVGs1Z1hrS2J1ek9pbDdiaUpSdTgwX1MyeFF4MWRZQnJjdzIzQw?oc=5" target="_blank" rel="noopener noreferrer">北朝鮮が弾道ミサイル発射 防衛省、日本のEEZ外落下と推定</a>
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
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE5VdmhXRXhrRk1lR1JiV1hZakU2Q1JRNW1iS1JOVEVGUzhjZi1BbXJIeVNRNnVFUndLZ0lOX3J2X043Q3VqbFNtTUU2ZW9oRTJsaVdjODRVMUczaDE0OGdMeXVrOGx4VDZYanJMVDZ1eUtUazM0Wmc?oc=5" target="_blank" rel="noopener noreferrer">防衛装備庁・下北試験場を捜索 青森県警、陸上自衛官が逮捕された贈収賄事件で</a>
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
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE5HdXR6OHNFZ21GWDRILTUtUjFXTWxFcXlNeHdtU0NKNmpReEl0ZHhhQS1pak5jUUlsN0V5ZWpadXU4bm1Pd2QtU2tJQTEzRERvcFBLR0phbnBXY0xVTDhPeGxMYVF1azBy?oc=5" target="_blank" rel="noopener noreferrer">防衛省「懲戒処分公表時期を調整」 自衛隊に届いた1通のメール</a>
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
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTFBheXExT2JmSVZXN011amZVbnhFdG1EZzctTUtPLWNWQjV3MXBBQTVlbzEwRmNXN1pCczlaS2FTUHVrTVF0OHBXdGFNckx5N0oxdHVvdU9fUEVRSUtWV3R0VjBfR19mOTA?oc=5" target="_blank" rel="noopener noreferrer">陸上自衛官を収賄容疑で逮捕 防衛装備庁試験場の入札めぐり 青森 [青森県]</a>
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
            <span class="source">東洋経済オンライン</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiW0FVX3lxTE1yY1AtSVRaY2NFbEt4UGxhLXJUVERaQWVrY3hnSGJvOXFPY2V1ZjNJN0hMa2NQdFBBbmhRQVoxVDJNUGZhSjR1M3Nqa0hiajVFaTctSl9xTDZBVlU?oc=5" target="_blank" rel="noopener noreferrer">｢飛べない国産哨戒機｣稼働率2～3割のP-1､なぜ失敗は放置されたのか―防衛省･経産省に欠けた航空産業を育てる能力</a>
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
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE54aGx3UkRqY1JJRjc5OERvMTRSN19ZWjZGOVBVYVFIbVdqcFdjYUdsSEM2VjZiUmtxaVBJN21fMDlTaXEzUGJQR2o2SEZSTHViY1JmRmFmQmttRzJsZTNVenZkYXBuSUU?oc=5" target="_blank" rel="noopener noreferrer">スタートアップ企業、防衛産業へ続々参入「新しい戦い方」の担い手に [高市政権の安保見直し][安全保障関連3文書]</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月25日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMib0FVX3lxTE40VGhHcFpYQ2RqOWx1RE5KNEdRYXE3anZidXpkXzBvWUk0eTEybHRuQlE5QXdCUFA3U1BYbmF2LU9FN0tNeEhhVzd4cDVIcU9JNHNjTWdzbm8zOTJ5RnZMdVVmQjFENm80ODYxUFp4Zw?oc=5" target="_blank" rel="noopener noreferrer">スタートアップ企業、防衛産業へ続々参入「新しい戦い方」の担い手に 動画</a>
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
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE55bjVZSGM5THZPWTZ3bGhVS3NtMEpvQzNxWjBzRS1IQmFGc3FkNmVzcFBDcnJjX0REQ0VGMmVqLXkyblh1eGxGakdkUUFTYnZYYkdsYWNqWWhVVHhhd1p0cWI2R0gxUVE?oc=5" target="_blank" rel="noopener noreferrer">高市首相、トルコ・エルドアン大統領と会談 防衛装備分野で協力確認</a>
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
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiXEFVX3lxTE9XVk5wOGpHTWVsQzlMNWJTYm81ODdJcGI4cmQ3eDVSTjU5cm1FRU1CakU2TXFLZXo5Z09qa2dHZ3l0SXN2T2dQdG1LRmlXSi1SNGRuQkhZQ3FXODJl?oc=5" target="_blank" rel="noopener noreferrer">（大転換期の安全保障）新しい戦い方：１ 技術が変える、戦争の形態 防衛省も攻撃型ドローンの開発急ぐ</a>
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
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE5xN3RIT19Pb2ZIb1pRZ2NVaEkzWEdvd0NuQkkwVlFwd3dQdnFHc0FUOU00N09Icmg5US1oMGx1REoxcXQtd1NWQzIxc0s4YlNKLTU2WnpSUVNSWmNINy1fdGpybEphOFFq?oc=5" target="_blank" rel="noopener noreferrer">高市政権の行方,トランプ政権：高市首相、日米同盟演出に腐心 「頭越し」の米中接近を警戒</a>
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
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE04bTFtV1d2ckh5UWxYRDlvT0xsdmFEanBCVUktYkpHWTE5Mjl1Y0MwcWN6d3UzWWR3SXl4d19EMGZXNy1tZklYQ3pFd2M0cDRVOWxCZ0JKbWdDRy16MWpzNVdDSGlnNFFP?oc=5" target="_blank" rel="noopener noreferrer">日米同盟の強化を確認へ ICC制裁への言及焦点 日米首脳会談</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月22日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE9idDJkTXVST3ozUGczdE1ySlFma0VPenNHZ1VsemF4OEkzWEo4VVhNdFZyWXlyNHBSTUJRc3pQVFotYUlqcXJyNVFDV19OSzFoN3pHR0Vya0MtcEpBMGNKRjFpUDJXQU96?oc=5" target="_blank" rel="noopener noreferrer">激動期の安保：防衛産業融資、惑う金融 業界「平和国家」信用にリスク／政府「成長戦略」盾に増す圧力</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月22日</span>
            <span class="source">Reuters</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE5NYUp1RWRrY2RZaWpxTGVYMy1WZDYwcGVDRWo1bHYzclNtVDkxUjJXOEozY0c1SVVwc0J2MFlFVm1BOWFtMlJkNGtwWFZkWnRfVVFFc0QxQTVialpZTHRaSzl6N2VwbXNJLVRCUHFvMVdadzIwTm5iV3o1c3NFZm8?oc=5" target="_blank" rel="noopener noreferrer">日米首脳が会談、高市首相「日米同盟の強さ示す」</a>
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
            <span class="date">9月21日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE1TWWplc3BtRGt3MjVWZmtYU3d5M3oydlRkUjVfMG5Ud0p0MmFyVVppcW1HOFdGT2VBdFg2eHMxRnJhTzhpZzc0aGdhTjlsbWlFak8yVDBDNDVrRTZaN290eElmRWJ2SVU2?oc=5" target="_blank" rel="noopener noreferrer">激動期の安保：防衛産業強化 政府と金融機関に温度差「融資はセンシティブ」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月20日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE1ESVo3QWhtRmlLVHViTW9EMVVqaFBHaTVDd3BwMmFaWnUzZjBSQW5IUkFuQkF0R2RLa00yR1UzZk9FYmFsTkMta20zalpzUlhud29xY2dGdGFDTnA4dmhEVGYyNl9NZw?oc=5" target="_blank" rel="noopener noreferrer">北朝鮮が「弾道ミサイル」発射、すでに日本のＥＥＺ外に落下か…防衛省発表</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月19日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE0wWEZUbFM1NkNaeGdNNFFxSS1UMUhxTmI5TnMyV0ZzVVFldi1nTGZ0QlNxeGVLcWg2NlFoVFRjUXNCWEN0YUF3SWxtUGdiVlFKRlF0QUhmZ3BxX1p2WE5aQWxzLW5DRGxv?oc=5" target="_blank" rel="noopener noreferrer">武器輸出の原則容認 国民の不安解消に政府がやるべきこと</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月18日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTFBCMkpfUE1RSExFRDdTbDRDSVZRMlZCMVZsb0xpcUwyTkFwWU5yUGo3YTktSHBVUUNNUVBzRzFVRzFXUlpTNk85aGM4aU5wcGVPdE1JSnV5Q3BTenB0RGlFNEhnMEhJSWhGcUhDWQ?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相「防衛産業の成長への一歩」 三菱UFJの融資基準新設方針</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月18日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE42SVFJWkpSRG1JNHhjMWR2dWJod3lick5tOU45TzU0M3pFX0JxY3hSNGlLd3ZxSFYyY2h0MjBVcTlVdGFBT2RQU09IeXRkdXNNdW1sdHlqZ3MybXRMWG1JWFZtVXJnVzg?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相が訓示 安保3文書改定「我が国と地域の未来を左右」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月18日</span>
            <span class="source">信濃毎日新聞デジタル</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMia0FVX3lxTFBnV1M0Vkk5Ukd6WFhUS0JlMzBQSzJnRkpsaW9oZENVRVZKUVhCVm51LWh1SndocXlCSDlDeERUTmFfUDNjU0s1RTZYOVFIaVVGbkhKZ21FNmsxRTZCZUplU1FmTnRvY29qNWY4?oc=5" target="_blank" rel="noopener noreferrer">安保3文書「未来を左右」 留任小泉氏、改定へ決意</a>
        </li>
      </ol>
    </section>
  </main>
</body>
</html>

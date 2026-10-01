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
      <div class="stat"><span>UPDATED</span><strong>2026年10月01日 16:04</strong></div>
      <div class="stat"><span>ARTICLES</span><strong>20件</strong></div>
      <div class="stat"><span>LATEST</span><strong>9月30日</strong></div>
    </section>
    <section>
      <div class="section-head">
        <h2>Latest Coverage</h2>
        <p class="note">Google News RSSから取得・フィルタリングした記事です。</p>
      </div>
      <ol class="news-list">
        <li class="news-card">
          <div class="meta">
            <span class="date">9月30日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiogFBVV95cUxObXJ0OEJBcnVLTnVGLWNtRVJkR3JlZVBYZjVidlNaRTBiRWNVc0pmQWk1MmZZR3ZRblowM1F4MVZrMXRQbHEyMnFtTFFLNjU2RVpsbVJ4WjRfaEN2cVNDdXVOS1dhaC1yUFUyUmhnaHVaN0swcTRqOHFzMUhMRjNlejFpRHFZdzJPSDBVYmpOOXpBY3dvX09ScFBORGdhZ0cwNnc?oc=5" target="_blank" rel="noopener noreferrer">防衛装備庁・下北試験場を捜索 青森県警、陸上自衛官が逮捕された贈収賄事件で（写真・画像 1/1）</a>
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
            <span class="source">東京新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiU0FVX3lxTE1lWUVXUkZ1VXE4OS1RdWhoWHQ5MXdZYnRxcUlYaDRIWFEwUkZiR3hxcWI0Yl9rQnZTUVFTbkhoRDdnUWliRnNZdG53eV9qakNjaHlj?oc=5" target="_blank" rel="noopener noreferrer">アメリカ企業の無人機「シーガーディアン」一挙大量購入計画 防衛省、2900億円超要求の「事情」</a>
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
            <span class="date">9月23日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTFA0UXB6T1Y0cnJ0em95WmlPOGtZVUxLMXdLenNpRW5Yd0VlRWtrRDRhQ1dqYjVWWmtiOW4tQkptVmJBMlNoRlFPbHlhVU84N2NVVUZuOWdiNEtEbDVWSGYwSjgwVVZDQXpLS0RwUEVkVzJabkdiUkE?oc=5" target="_blank" rel="noopener noreferrer">高市首相「日米同盟の強さを世界に示す」米中会談2日前の日米会談、対中連携で示せた収穫</a>
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
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE04bTFtV1d2ckh5UWxYRDlvT0xsdmFEanBCVUktYkpHWTE5Mjl1Y0MwcWN6d3UzWWR3SXl4d19EMGZXNy1tZklYQ3pFd2M0cDRVOWxCZ0JKbWdDRy16MWpzNVdDSGlnNFFP?oc=5" target="_blank" rel="noopener noreferrer">日米同盟の強化を確認へ ICC制裁への言及焦点 日米首脳会談</a>
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
            <span class="date">9月22日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE9idDJkTXVST3ozUGczdE1ySlFma0VPenNHZ1VsemF4OEkzWEo4VVhNdFZyWXlyNHBSTUJRc3pQVFotYUlqcXJyNVFDV19OSzFoN3pHR0Vya0MtcEpBMGNKRjFpUDJXQU96?oc=5" target="_blank" rel="noopener noreferrer">激動期の安保：防衛産業融資、惑う金融 業界「平和国家」信用にリスク／政府「成長戦略」盾に増す圧力</a>
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
            <span class="date">9月19日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE0wWEZUbFM1NkNaeGdNNFFxSS1UMUhxTmI5TnMyV0ZzVVFldi1nTGZ0QlNxeGVLcWg2NlFoVFRjUXNCWEN0YUF3SWxtUGdiVlFKRlF0QUhmZ3BxX1p2WE5aQWxzLW5DRGxv?oc=5" target="_blank" rel="noopener noreferrer">武器輸出の原則容認 国民の不安解消に政府がやるべきこと</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月18日</span>
            <span class="source">東京新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiU0FVX3lxTE8zWi1VNDZtdVVsd1ZnelRaYUZXSzNfcGxrRXY0aGVYVUJCb1U0VmVhMlNxWEl3WndubEprZFp1MlpKRXNWUDhyVHdZTlNuNnd0R0xz?oc=5" target="_blank" rel="noopener noreferrer">メガバンクも防衛産業に投資の流れ？ 高市政権に歩調を合わせ、戦争の反省から方針転換か</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月18日</span>
            <span class="source">信濃毎日新聞デジタル</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMia0FVX3lxTFBnV1M0Vkk5Ukd6WFhUS0JlMzBQSzJnRkpsaW9oZENVRVZKUVhCVm51LWh1SndocXlCSDlDeERUTmFfUDNjU0s1RTZYOVFIaVVGbkhKZ21FNmsxRTZCZUplU1FmTnRvY29qNWY4?oc=5" target="_blank" rel="noopener noreferrer">安保3文書「未来を左右」 留任小泉氏、改定へ決意</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月17日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE9IenZpQUxnM3JCeTNlcGk4SjEybmVPNVZsOXBGbDNVVExOeFRxd1lsNnBQa0xONGNSc2dMdHRER05leFI5cE5WbEtHcHJkRFBPRElna25OckZuckZCZ3A2SFVELTE4UGlm?oc=5" target="_blank" rel="noopener noreferrer">記者の目：武器輸出の「5類型」撤廃 不安視する国民 説明尽くせ＝竹内望（政治部）</a>
        </li>
      </ol>
    </section>
  </main>
</body>
</html>

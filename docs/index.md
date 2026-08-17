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
      <div class="stat"><span>UPDATED</span><strong>2026年08月17日 11:21</strong></div>
      <div class="stat"><span>ARTICLES</span><strong>36件</strong></div>
      <div class="stat"><span>LATEST</span><strong>8月17日</strong></div>
    </section>
    <section>
      <div class="section-head">
        <h2>Latest Coverage</h2>
        <p class="note">Google News RSSから取得・フィルタリングした記事です。</p>
      </div>
      <ol class="news-list">
        <li class="news-card">
          <div class="meta">
            <span class="date">8月17日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTFAyZU1fNVp3ZTYxNldZWXF3LU12RGVJYTcwYTFmT2tuUFg3NU5lbV9DZjJiWjFhR0tSZGlFN1Z1UU5ZdnlQdlM3V21tLXhBN2pDdHBrcW1TU1dlV0xoZVp4WWs1bEtLNW5Ib0VJeQ?oc=5" target="_blank" rel="noopener noreferrer">日米同盟、老いとの戦い 中国台頭がさらす安保体制の弱点</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月17日</span>
            <span class="source">東京新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiU0FVX3lxTE1lS0RyS3plbDdNbnpka3haOUFtMHV3ZmtXSkE3dDJEUE1FTF9VNFJZaHgzeTRJSm82SEtHV0xONWJwNlhHT2t5TVk2Vm85WFUtel9v?oc=5" target="_blank" rel="noopener noreferrer">武器輸出解禁が転換点…歴史学者・藤原辰史さんは「戦争はもう始まっている」と日本の無自覚を問う</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月17日</span>
            <span class="source">東京新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZEFVX3lxTE9YTERpWllpeEZuNVRrWlVQV3dYa0I5TW9RRjBIT1hvYVphX0lHRncyX1RQdW84UEk1bGs3dEJBaGYxblZkRjNKM2RFR1BoQkVTUDhudWhlUHVSUjZ0Z2ZWUmlPbEQ?oc=5" target="_blank" rel="noopener noreferrer">武器輸出解禁が転換点…歴史学者・藤原辰史さんは「戦争はもう始まっている」と日本の無自覚を問う</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月16日</span>
            <span class="source">信濃毎日新聞デジタル</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMia0FVX3lxTE50NG56N1gtOFpFazh1enBGQUNjUEFFZW9zc3lVcmstV3Y4TkZOU3IxcUZSOXhyY0lGdnpwSFk5STlBUVdINUJGaU9iWDdWc0RjbVVBZjdpT3NQMWoyRzJPa1FMaTBHZTExcXBR?oc=5" target="_blank" rel="noopener noreferrer">【高市首相初の終戦の日】防衛力強化、にじむ思い 靖国参拝、保守派は期待</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月15日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTFBldWp5TGdvcHJGX1BrM3NTMWgyMlR3VF9MSTZwQ05LWmtyWTZmQVh6NWtEd0stVFpDQlRNX2c4UkNwcXM3bGhLWjVSVzZIaHRFWjI1Tnl0SlpvQWVSa1FxVjFBVVZMeVVS?oc=5" target="_blank" rel="noopener noreferrer">揺らぐ「平和」：軍拡の時代に 防衛産業、活況と葛藤</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月14日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE1nY0txOW50Z1AxaW1jTHFBVVRkR1MzRFIzOWRYZ1FvVkw2dVFOaXktRXVPQnpfUHdUVElGZ3FTa0Z1c2NSQzhxaWVUdWIzSzB1YnBJWnJXOTZERWxvOVJCaHVuSC1EWlg1?oc=5" target="_blank" rel="noopener noreferrer">ポッドキャスト：日本の平和主義は守れるか 拡大する防衛産業の行方は</a>
        </li>
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
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTFBSWWdXcHBxLVJoR1B0QjdnamNiX2lIdHJaUXlqSGhLV3Z2SFlZeDZBWDR0amo4WG93SkZjOHNGcG40TzZoMHZiYl9Fbm9FSm55bURvOHVvRU5VWWp4NnlJdGJ5NW8zUQ?oc=5" target="_blank" rel="noopener noreferrer">【速報】防衛省関係者によると、弾道ミサイルの可能性があるものは日本のＥＥＺ外に落下したとみられる</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月12日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE1IM3NKRm1DQ3BqX195bmsxWmM5RnlYUnFiSUdDVTF6QmtUbzVqSVpXMGVMODlZeWJqdG94QW81cGJ6NTlJM1N3YXM2WkpDb0FEOExxRjA3TWRKTi1NS0tteVZjMGo4UQ?oc=5" target="_blank" rel="noopener noreferrer">【速報】防衛省によると、北朝鮮から発射された弾道ミサイルの可能性があるものは、既に落下したとみられる</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月12日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE9oWVhDVzNTbzJ6OXZRR285MjNKZ3Y1U3VyLXdXUmZvS2xBWHhoNHhlaU13X24ta1lyVzZDejRwZGpqRV9kckFPUWsxYzhEbWVqRUxPakRRQ0E5bUZVSG1TVEVIVmdQQQ?oc=5" target="_blank" rel="noopener noreferrer">【速報】防衛省は、北朝鮮から弾道ミサイルの可能性があるものが発射されたと発表した</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月11日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE13eS0tWUQ1ZkJsUHktNWlZcDV4d0Y3UFk4alc2dExUWkFPNVNaTThVYUhaMW5HMUhaTjhTTEhyZkpad0U3cUNvOTFHX1ZJS0JPQlk0b0EtVG5KU2NiS3lZQmJFbkpDd0la?oc=5" target="_blank" rel="noopener noreferrer">「平和都市」か「防衛産業」か 揺れる長崎が選択した道</a>
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
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE0zSC1jVE54Z3QwR0NRcC1vVmw2UjZGRUR0U281cUlNbjlVT3RJTUVBS2ZvN3dMUHA1b0ZKSFBlRnhSWmNHUnBVT0RTOUVKQ0xBa3ZHREFuUXllVkhOVmR6elhic0NlWDhYd1QxUw?oc=5" target="_blank" rel="noopener noreferrer">パケ駐日EU大使、日欧安保「かつてなく密接」 防衛産業の協力期待</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月10日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTFBPQzc3T2hramdaSDZic2VCN3dkbjRhRVZJdWVvYzBxQlgwajctaU9vYS12Sm5EekFMX2xtWlgwWG1zcE9DZWNkdTVvMWtBNURGOVgyWkZVLTFSVmtvSVBKakg3UWh5NWh0M0JvcA?oc=5" target="_blank" rel="noopener noreferrer">円安防止の日米同盟に組み込まれる日銀 27年春にかけ金利1.5%へ</a>
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
            <span class="date">8月9日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE8xRzhxMkdvbDFGcks1b09oYnRfdS1RazgwWlRVUklXUTR6MTNxd092Qkd3Q0x3alhVemctZ3dJdFNuQnh6aGdfdmJ3QWEyNmhnRUcteUd2aEhva2k0MXF3cldreVNlYlNIOVpxTw?oc=5" target="_blank" rel="noopener noreferrer">防衛装備品にサイバー防御ソフト 空自レーダーなど27年にも導入</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月7日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE5vUW0tU0RTLWJ6WjBmeFRWSTNuX3VfbGhSbFlBYm5ZOGl5dHB1cGRrUnVlMGFRSlZIRWU4TUozbTZ4UjFibDQtSEUtOFhaWHU3d1hMNkRMNUVWeFk0VGFGN2RfbHNJWnFnZDNtQQ?oc=5" target="_blank" rel="noopener noreferrer">護衛艦や戦闘機の取得に遅れ 防衛省、物価高で単価上昇</a>
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
          <a href="https://news.google.com/rss/articles/CBMiW0FVX3lxTE45Nm9MREtKOGZUWGFUd1hmeVBpemVrYVRLbTRyUEhOUDZKSkpSQUdHcmhnY0doN055eWlIdHdHc1dtbHBfY0NoZHNYMy1FQUxCVUNPdmx3YmpqSmc?oc=5" target="_blank" rel="noopener noreferrer">災害支援で賞賛される防衛省･自衛隊､その陰で放置された組織防衛と無謬主義という罪､防衛費を倍増すべき組織なのか</a>
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
          <a href="https://news.google.com/rss/articles/CBMiW0FVX3lxTE5uNGFDT2V6cE05ZGgzeDRJbjB2Z1pRMnNiZ3hlNzVkY29YR1pFMjFDNFE3bkFMeTVyQ2NDVnQwNnVwNVcxdXlrM1htbmZNVnQ4TmItMHZlc18tdEE?oc=5" target="_blank" rel="noopener noreferrer">災害支援で賞賛される防衛省･自衛隊､その陰で放置された組織防衛と無謬主義という罪､防衛費を倍増すべき組織なのか</a>
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
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE44VXRYc092VjRUb1drTXVNLWtFUFl3M2s3VE9JajBYRkdxT1lmc1dmaTdydG9RaFlqLV9Kc2t4NnNRVlJxTUlsUkxOU1JQMmptaFZ3SHNSRmlqbTdBMzZHRmZ6aVR6aElrcDJfUA?oc=5" target="_blank" rel="noopener noreferrer">防衛省、装備品調達数を事前通知へ 企業に設備投資促す</a>
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
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE14THowcUw2ZUxib2ZWQTJrdFcxeEduS2IxVWdzY05kZVBLR1I5MzRmT3RWTHliR1lTTlFlV2lKSzlLQmdRY28xUmZrZld3amFlVzVlYkxWdnd1MWNmbVR6WDZHRTBBQQ?oc=5" target="_blank" rel="noopener noreferrer">【速報】防衛省によると、北朝鮮から弾道ミサイルの可能性があるものが発射された</a>
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
            <span class="date">8月6日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMigAFBVV95cUxPUG1SNmQxZHJua3c1UUplSEw1b1otS0lMME55SGVkbkJDMlMzak9rWlp5eGxGWUpmVWRQUHFhejl5YzQyQzRlUXZGV3pOTFVIelFvb3ZsZkVmV0YwZURzU0JmR2lEVDJmbEtETWp5bDlzVkNrakZiRnNzOF81NXFrRQ?oc=5" target="_blank" rel="noopener noreferrer">画像・写真：防衛省「日本周辺に影響なし」 北朝鮮ミサイル：時事ドットコム</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">8月5日</span>
            <span class="source">日刊工業新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiW0FVX3lxTFBRTU5Kd1JQZmx2bXNGVkR5RHdoeFVjVVp6TGU4MFoxSk1yR2ktQ3V1b1MwbHFKSmdaa0poVFE5Q3Y5RExNbW1pWkR0SUZJcVByajVwbXRVNmNhamM?oc=5" target="_blank" rel="noopener noreferrer">防衛省幹部人事／防衛審議官に安藤敦史氏</a>
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
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE4yRUdSUjZZck5hNlBGNUFNUE5Pc3FPZEJjcUFtaEIzLXhxQjRDQ21aYWY1RFkySUVxNGdqcEpMam1pMV8wOU1QdUdpMC0wYllHY0ZlSzlzeUJoUG9ObzJYSGF4blo5YXFxUWZiWQ?oc=5" target="_blank" rel="noopener noreferrer">「経済の武器化」対抗へ同志国と連携 安保3文書改定へ有識者会議</a>
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
            <span class="date">8月3日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTFBUTERuckRMQlNKaGEwWFBHUFk3bHBwQzRMVDlBZnIzZE5BcThGMWpVOHdxRER1b3FjN1VrQ1Bld2VhT2gtNkZEV0RmSjBuQmk3eHVVdkpJN1VyQQ?oc=5" target="_blank" rel="noopener noreferrer">防衛装備、日本の政策はどう変わる？ 元統幕長・前装備庁長官に聞く</a>
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
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMia0FVX3lxTFBMNVNSbkNCa0JsX2dlQjB4V3l5R014NWJ1Q3p0bXBZNVlHNmtDZ2c0dHdxczd5VlpINDdBTE5ZRFk2T1F3MkRnSGlhTWtScjl0NkNOYzA2UzZONmliSmhrd0RwN3h1dmhHalRj?oc=5" target="_blank" rel="noopener noreferrer">［地球を読む］日米同盟 相互防衛の意思 隙間なく…ハーバート・マクマスター 元米大統領補佐官</a>
        </li>
      </ol>
    </section>
  </main>
</body>
</html>

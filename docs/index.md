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
      <div class="stat"><span>UPDATED</span><strong>2026年09月26日 15:00</strong></div>
      <div class="stat"><span>ARTICLES</span><strong>52件</strong></div>
      <div class="stat"><span>LATEST</span><strong>9月25日</strong></div>
    </section>
    <section>
      <div class="section-head">
        <h2>Latest Coverage</h2>
        <p class="note">Google News RSSから取得・フィルタリングした記事です。</p>
      </div>
      <ol class="news-list">
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
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiggFBVV95cUxPNDBSaHdublp3Nzc1eUZ0V0hidFN0MHozd1JXRGRKZHVWWjZYdWRRSVB4bEczbVhjWWJ4UkkxNmFwcklzZnlXbUZTcHVrSTk2Q3NOWTJZMmJzUE4zekUzeXFYUDBuR3FBZml5OUxQbDZuM0RzQmxEN0Ywempkc1Fyanpn?oc=5" target="_blank" rel="noopener noreferrer">無人機開発へ新興企業支援 防衛省、資金配慮の新制度</a>
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
          <a href="https://news.google.com/rss/articles/CBMikgFBVV95cUxOc2JtT0FIMWV2bGJpYXRuUXJtOTNZT2hJNUJXRFI0TFNPNURaeVd6Wk0xUjIzc2JQcENRQjJMdUxjSVJhSlFMRGtDMlZLbWlXVmpxU2lod1N0OUVHRnNKcDVYLWp3c2wyRFVmZ1BTYlpqOEc2eVZsQ2J3X2M1WXZnbVZ3OTBCbWVDX0I0Ti1SUDZuUQ?oc=5" target="_blank" rel="noopener noreferrer">スタートアップ企業、防衛産業へ続々参入「新しい戦い方」の担い手に 動画</a>
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
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiU0FVX3lxTE9EVVBxWS1SQlpjY2VKSzlabmc5X0UwaDhXSU82N0xvQUVGQ3U5amxJbnptZlFRZEVtQjNEU2EtSEFRRGVBYXRtd0ZpZkh6NFI1Qlc4?oc=5" target="_blank" rel="noopener noreferrer">日米首脳会談、高市首相「日米同盟の強さ示すことに」</a>
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
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTFA0UXB6T1Y0cnJ0em95WmlPOGtZVUxLMXdLenNpRW5Yd0VlRWtrRDRhQ1dqYjVWWmtiOW4tQkptVmJBMlNoRlFPbHlhVU84N2NVVUZuOWdiNEtEbDVWSGYwSjgwVVZDQXpLS0RwUEVkVzJabkdiUkE?oc=5" target="_blank" rel="noopener noreferrer">高市首相「日米同盟の強さを世界に示す」米中会談2日前の日米会談、対中連携で示せた収穫</a>
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
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE5yT0xta3lXTUJZdzR3RWctM1ZQR0h2NnVPLWZNRXpGS0JYaFZ1NDNiTnVERXd0enJ1cU5SWE9hU01UalNwRC1XRHdDNmhxSlpfTlhfNWlleGppcW1QSGZGc1oxWlZfdw?oc=5" target="_blank" rel="noopener noreferrer">高市首相、トランプ氏との会談「中国巡る課題でタイムリーに意見交換」「日米同盟さらに揺るぎないものに」</a>
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
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiXEFVX3lxTE9XVk5wOGpHTWVsQzlMNWJTYm81ODdJcGI4cmQ3eDVSTjU5cm1FRU1CakU2TXFLZXo5Z09qa2dHZ3l0SXN2T2dQdG1LRmlXSi1SNGRuQkhZQ3FXODJl?oc=5" target="_blank" rel="noopener noreferrer">（大転換期の安全保障）新しい戦い方：１ 技術が変える、戦争の形態 防衛省も攻撃型ドローンの開発急ぐ</a>
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
            <span class="source">Reuters</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMif0FVX3lxTE5NYUp1RWRrY2RZaWpxTGVYMy1WZDYwcGVDRWo1bHYzclNtVDkxUjJXOEozY0c1SVVwc0J2MFlFVm1BOWFtMlJkNGtwWFZkWnRfVVFFc0QxQTVialpZTHRaSzl6N2VwbXNJLVRCUHFvMVdadzIwTm5iV3o1c3NFZm8?oc=5" target="_blank" rel="noopener noreferrer">日米首脳が会談、高市首相「日米同盟の強さ示す」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月23日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE40bkJUSzlBQVlmeUo1SkRBZEpHa2paRGt2WWFqc1U5M254LWs3WlpWUDlMYTlza2NnWWRVOGZIZGtPUHhWcFNvWjVqMl85QmVWWUNFNEtidE1Ec0RucVdyVGNDVXo0dw?oc=5" target="_blank" rel="noopener noreferrer">【速報】高市首相は、日米首脳会談について「世界に向けて日米同盟の強さを示すことになる」と述べた</a>
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
            <span class="date">9月20日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE9ZUVlyMFhHT0sxUWZXM2MzYUpJU1kwVkxoamlxcnVqZk9oeWI5aUxUSkFNVGRqV2h3V0pSOU96aFdFWnJmb1JlTjhqMlZLSTJXMFU0aWx5dS1jSGFFUV8zbTNySDNHdw?oc=5" target="_blank" rel="noopener noreferrer">【速報】防衛省によると、北朝鮮から午後６時すぎに発射された弾道ミサイルの可能性があるものは日本のＥＥＺ外に落下したとみられる</a>
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
            <span class="date">9月20日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE5wNzNwd09ONmdLSDc4TEJIU0NIMVI1OENVVHFtMDNYMlVjTjNmT0E4dU5hTEJwak92TmI4QTZtbndIV0VOYnVQZ2hjOFNZb3BDNkZKMHFCeTV2bWRuR0tadmlER2JWZw?oc=5" target="_blank" rel="noopener noreferrer">【速報】防衛省によると、弾道ミサイルの可能性があるものは既に落下したとみられる</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月20日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE04T1pMeUtocm1BU0JVRndNZV9LejYzZmJvY3RGQ1hjN29IdFMtejdHa3duWTFjbnJpR3VDOE5lbEZDNUR6NEk4UFFwcERNb0RRR05sVUVfMU4wOFB4QVVzNnFjTEdFdw?oc=5" target="_blank" rel="noopener noreferrer">【速報】防衛省によると、北朝鮮から弾道ミサイルの可能性があるものが発射された</a>
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
            <span class="date">9月19日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTFBwZndqdXplZW9BMDVETjRTbnVPQXE0WG44VWM4dWdCaTF1QUZTcGhfM2dpczlPU1h0YzQxWU1iMHBPNGhWMk9PUzRRcWNxaFRBUjNTdk5OX1k1c3U0NmpCZk5ERQ?oc=5" target="_blank" rel="noopener noreferrer">日米同盟強化へ連携 防衛相電話協議：時事ドットコム</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月19日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiggFBVV95cUxQMmpheVV3QW5TSUg0NmpHaEpKLU41X1dSOUdNbHBWX1BEMDlWVU5DSzhUV1BBLU1KZmsxZ3lybVRvTlV0S0laUlljaTlSVTl5bng2MW8wUFlDZ0ppUTB4OGtWdVJVV3ZfSjBNcDNIUjE0emxqZm8zMl9ONzN4ZFdDODJn?oc=5" target="_blank" rel="noopener noreferrer">画像・写真：日米同盟強化へ連携 防衛相電話協議：時事ドットコム</a>
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
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE11X0t6NE9EMHU1VFpONUJHMTcwVFpoRmE0VDlMNEZBZVgzcXlFX05lZ2o0SDJ6QURmbWxFdFZJZjBadDRMbW95Wi1NUlE5TkJhX0VBVkx0WWphdTAxUXVaNTFGaFVBei10elQ1Mg?oc=5" target="_blank" rel="noopener noreferrer">英新興、低価格のドローン迎撃ミサイル 1発数百万円で防衛省に提案</a>
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
            <span class="source">信濃毎日新聞デジタル</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMia0FVX3lxTFBnV1M0Vkk5Ukd6WFhUS0JlMzBQSzJnRkpsaW9oZENVRVZKUVhCVm51LWh1SndocXlCSDlDeERUTmFfUDNjU0s1RTZYOVFIaVVGbkhKZ21FNmsxRTZCZUplU1FmTnRvY29qNWY4?oc=5" target="_blank" rel="noopener noreferrer">安保3文書「未来を左右」 留任小泉氏、改定へ決意</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月18日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE0wVzNQR2xmZjROQUh4aENSdG03OU1FRlhHR2JNN2RoZFNlU3JkM1AxVl90ZVd0Uk0tQ1hzSTJGTHpObWY3emtVQ19VN2tkeHV0VWpQNEt4aVNvSWZfSWptMWFTYWZndmZ2ODdOag?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相、3文書改定「日本と地域の未来を左右」 防衛省で訓示</a>
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
            <span class="date">9月17日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibkFVX3lxTE5vVmd2ZVg4ZXl6ZUpjNy13WmJFNXp6bmtPSDlVb0g0cEg3YXcwUzNjdUIzSlVMS2tEODMyMkYxNzA2MzdhYW1CdmJyM2RsTVJ1X0NaejRsVGRoRVZ2dFc2UTVLazRnSThCMk5ZeEpn?oc=5" target="_blank" rel="noopener noreferrer">安保3文書改定の有識者会議 政府横断的な取り組みや防衛費を議論</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月17日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE4wRFlYOE5zUU1mcy1vNzRCQkVybUtoU18wR3FWc29CRXdoMnVwcDVBTUpxX21QNXBuOEZFMjNodmxNRTB2M3R2eGtEcmt5WVhjMTB1bUFvM292VTRnMXR3?oc=5" target="_blank" rel="noopener noreferrer">防衛産業への投融資 全銀協・加藤会長「個別に判断」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月17日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE9TbEJ6ZVN1S2FfNlp3UWRhWG9fQlZTaENhWUFXX2NHY1BITzlRaW1pSFVua1FPTVh5MGRsdUhDUmVVUjQ5TkNWdWlPdTZQZXFPeEVjOWxERERrbjF4VnUtNF9xX0lfSmNmVHEtVQ?oc=5" target="_blank" rel="noopener noreferrer">三菱重工業など防衛関連株が高い 「防衛産業に融資」報道に期待</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月17日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTFBMLWZET0JRNHd3YzljSkx6dEtIaUMxQ0UzYVFJWE5hV0hzcFplWjlhRGJoYWJTX1l4QVFOLVpIMEFlYmQzS0pmQ2ItaDlMWW94UnU4ZTNrdmp1VjVCWmdGcWxqZmw3Sk0?oc=5" target="_blank" rel="noopener noreferrer">安保3文書改定の有識者会議 政府横断的な取り組みや防衛費を議論</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月17日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE1uR0hMbmVuVlIyaWM5ZUN6MEp1WU96bENuMmIwbGpLTm5zaTVoMHg5NUNEMkVkSW02dDc3R0ZZNzJqY2QtSlZ4bi1rYTZPTEJPS2VpRUlUbmM2SnZScGhZ?oc=5" target="_blank" rel="noopener noreferrer">安保3文書の改定に向けた有識者会議 AIの研究・開発求める意見</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月17日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE9IenZpQUxnM3JCeTNlcGk4SjEybmVPNVZsOXBGbDNVVExOeFRxd1lsNnBQa0xONGNSc2dMdHRER05leFI5cE5WbEtHcHJkRFBPRElna25OckZuckZCZ3A2SFVELTE4UGlm?oc=5" target="_blank" rel="noopener noreferrer">記者の目：武器輸出の「5類型」撤廃 不安視する国民 説明尽くせ＝竹内望（政治部）</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月16日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTFAxaWYwemF0ekxjM3JuTkVFRDVMSTIwUFU2Y1hQdGRaR0Z2b18yajBORUFITWxiTWh6SnJKSWVXRS1LejBCNlpwRWRkOVVFT0dxWGxQbjNwNDNTRnZPdUFON0VNMkR1VHo5c3QxNA?oc=5" target="_blank" rel="noopener noreferrer">三菱UFJ銀行が防衛産業に融資 慎重姿勢を転換、安保政策を軸に判断</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月16日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE9GZEtuNTV2VTJPZnNMcEpuS0QxQ0JiMGk0TkVGeGhqVGtvVzIzOEpxRXBHWEwxTi1hNzFSbkZ3RTlmdTBaZmlTMmZkX2JRRWZvRkFUczg4bFZBNlBvX1NrV19aRjRaTHV2?oc=5" target="_blank" rel="noopener noreferrer">防衛関連企業の融資、三菱UFJが慎重姿勢を転換 審査進めやすく</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月15日</span>
            <span class="source">東京新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiU0FVX3lxTE51bHdjdnlqRnAxRTlPR1JVY00wVlV3bmhUcTNZX3BwZ29wUlNva2Y0RndSMEhCbDBvQ0I3cDgzT2NFVTIzS2M2RFFwdUlzSTdCSzc0?oc=5" target="_blank" rel="noopener noreferrer">「脅威国を名指し」防衛省がつくった小中高生向け教材の偏った記述 「配布は行わない」断る教育委員会も</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月15日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE92NHFmVlJVYzh4dnJJTFFvdmt5YjVmcWRNZ3pxUlp1VXcxUzR1T2RHRktQTFBZSm81S2doSnNSMGZ1bTdWbjVtbkpNMkw3akVLb2NWRnpqZkFHM2V2a0t0akdQQy1wU3M?oc=5" target="_blank" rel="noopener noreferrer">フィンランド国防次官 防衛装備・先端技術で日本との協力深化に期待</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月14日</span>
            <span class="source">Reuters</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMigwFBVV95cUxOZ3BzcndjOEJWc3EtelI4NDBCLWFaWWttWDRvbm01ZjlVZnVvdU1BVTJBREtiUnRfZUVlWjNXNHFwRmZ4amIxb1hFdGJtUVF2Q1lXUkhaU1MwOXFETHdWRWotSVh6UGNnT1NKYWFLVEtsZ3p1UGRWWHM0MjhLTDZLX1o2cw?oc=5" target="_blank" rel="noopener noreferrer">日本への侵攻を遠方で阻止、安保3文書にドローン防衛構想＝関係者</a>
        </li>
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
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiWEFVX3lxTE1ya3pwSUZ6TjFOUnFqRktId3p0Q3F3dGN6U1FLZ0lLVHJURjVNSkF6RTJWaklXZ1VyVU10Nl9fU0ZKVEJLcnZvcEYydGJ6WEpfZm9oX29wU18?oc=5" target="_blank" rel="noopener noreferrer">呉の製鉄所跡地の「複合防衛拠点」計画 防衛省が県や市に説明</a>
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
          <a href="https://news.google.com/rss/articles/CBMiYkFVX3lxTE5vSFVEQU1yS2REM2l1ejFuUkdDdW1Rai1McFJMV2FveDVVaVRpYW1waDU2dWlSOVZ1bUo1RFFYNUJ5N3d0N1RGYUFtSmltUGJPS3A1bmxKWWNJVGxOUXAwMnVn?oc=5" target="_blank" rel="noopener noreferrer">米国防総省傘下「災害対応・人道支援センター」所長「日米同盟の絆は、一段と深まっている」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月11日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE1ROHJCZ2szRzhEdTYtZW9HOGNVcEtYTy1WTE02TURzWnJCaDhlV2o0TkZwWmJlTWV6dWQxU1NxTFFGUUdKMjBCUm9KbUM2UnVZM3R6cW5CSldtbTRjM3BSTzhKN2tzbjJoYjlQRktISVpNWHhJLXc?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相、原潜保有「あらゆる選択肢を排除せず検討」 安保3文書改定で議論</a>
        </li>
      </ol>
    </section>
  </main>
</body>
</html>

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
      <div class="stat"><span>UPDATED</span><strong>2026年09月24日 14:58</strong></div>
      <div class="stat"><span>ARTICLES</span><strong>34件</strong></div>
      <div class="stat"><span>LATEST</span><strong>9月24日</strong></div>
    </section>
    <section>
      <div class="section-head">
        <h2>Latest Coverage</h2>
        <p class="note">Google News RSSから取得・フィルタリングした記事です。</p>
      </div>
      <ol class="news-list">
        <li class="news-card">
          <div class="meta">
            <span class="date">9月24日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE55bjVZSGM5THZPWTZ3bGhVS3NtMEpvQzNxWjBzRS1IQmFGc3FkNmVzcFBDcnJjX0REQ0VGMmVqLXkyblh1eGxGakdkUUFTYnZYYkdsYWNqWWhVVHhhd1p0cWI2R0gxUVE?oc=5" target="_blank" rel="noopener noreferrer">高市首相、トルコ・エルドアン大統領と会談 防衛装備分野で協力確認</a>
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
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMihwFBVV95cUxQaklsYWhMMGZib1o0c3lUM2FhQU1CTWVJR1FZNW1HS2JubkVNTkZVN1Z1SEZJNGwxdVloR09CemxkV1RWOEZxcmQ2Ulk5WngwLVhOaklRZm9kOG9IX3JVR0xtNFd0VEJyZ292SmdSX3NRZzJTLTdLeTJ6azhGY1hwZVZRZ2NuNzg?oc=5" target="_blank" rel="noopener noreferrer">高市首相「日米同盟の強さ示す」 米中首脳会談前にトランプ氏と会談 [高市早苗首相 自民党総裁]</a>
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
            <span class="date">9月22日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTFA5UTEwaWxSSWR5OFBJQTEtSGxuLXhjVU1UV1hxNzZKaHd5eUFoN2UyUGpFMVJkcEN6UlZyUUFlbEV0cVAxNjRvUkFtNjVMODQ3NkFscF9QSlR3WWRtYjFCTGtiUHlENDJUNGVRN3VlVmVpTEVZWUE?oc=5" target="_blank" rel="noopener noreferrer">＜独自＞防衛大がAIリテラシー教育導入へ、来年度にも 安保3文書改定見据え PT設置</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月21日</span>
            <span class="source">東洋経済オンライン</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiUkFVX3lxTE96cFJxcmliSV9MZjFtWC15ZkdtY0tQdjJRVHhGUlFUUGQtOTF2YkdSZE1rb0x2em0tT0ptalVGV2lmZUxENmpyUGNSNkpfWXF5Z3c?oc=5" target="_blank" rel="noopener noreferrer">【検証･防衛記者クラブ（前編）】国民の知る権利を空洞化させる―防衛省で露呈した権力監視の放棄と当局癒着の実態</a>
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
            <span class="source">時事通信ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiVEFVX3lxTE1oR0trUnFJMU9QSWhiVFpncW1XczhQajg2N2NPMGp3ZjNmNlY2TVhRSXljUE9pNDEzQUlieHJ3aGhsRjBVblZZMXpUMzl5NVJsdXRpZQ?oc=5" target="_blank" rel="noopener noreferrer">◎日米同盟強化へ連携</a>
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
            <span class="source">信濃毎日新聞デジタル</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMia0FVX3lxTFBnV1M0Vkk5Ukd6WFhUS0JlMzBQSzJnRkpsaW9oZENVRVZKUVhCVm51LWh1SndocXlCSDlDeERUTmFfUDNjU0s1RTZYOVFIaVVGbkhKZ21FNmsxRTZCZUplU1FmTnRvY29qNWY4?oc=5" target="_blank" rel="noopener noreferrer">安保3文書「未来を左右」 留任小泉氏、改定へ決意</a>
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
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE4wRFlYOE5zUU1mcy1vNzRCQkVybUtoU18wR3FWc29CRXdoMnVwcDVBTUpxX21QNXBuOEZFMjNodmxNRTB2M3R2eGtEcmt5WVhjMTB1bUFvM292VTRnMXR3?oc=5" target="_blank" rel="noopener noreferrer">防衛産業への投融資 全銀協・加藤会長「個別に判断」</a>
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
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibkFVX3lxTE5vVmd2ZVg4ZXl6ZUpjNy13WmJFNXp6bmtPSDlVb0g0cEg3YXcwUzNjdUIzSlVMS2tEODMyMkYxNzA2MzdhYW1CdmJyM2RsTVJ1X0NaejRsVGRoRVZ2dFc2UTVLazRnSThCMk5ZeEpn?oc=5" target="_blank" rel="noopener noreferrer">安保3文書改定の有識者会議 政府横断的な取り組みや防衛費を議論</a>
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
            <span class="date">9月16日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE5VYS1kZ0NrMUgzTlVNRnBIc3FQYjhNa0lyOUpDb2RZeUlRQUJsMzBhd1l3UGhUY1JPUHNNSWlHeGhzRTdNT1FucmhublN2bnY3QURBS1Btb0FNR0tNSHZGT05MLUY4emlGNG5JMW1SYjJhT3daNHc?oc=5" target="_blank" rel="noopener noreferrer">鳥取知事、防衛省に不快感「きちんとした情報こない」 無人機墜落対応巡り</a>
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
            <span class="date">9月15日</span>
            <span class="source">東京新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiU0FVX3lxTE51bHdjdnlqRnAxRTlPR1JVY00wVlV3bmhUcTNZX3BwZ29wUlNva2Y0RndSMEhCbDBvQ0I3cDgzT2NFVTIzS2M2RFFwdUlzSTdCSzc0?oc=5" target="_blank" rel="noopener noreferrer">「脅威国を名指し」防衛省がつくった小中高生向け教材の偏った記述 「配布は行わない」断る教育委員会も</a>
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
            <span class="date">9月13日</span>
            <span class="source">ニュースイッチ by 日刊工業新聞社</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiQkFVX3lxTFAwVENtWFh1U1JNaVJLSHVMUjNkMzU1Z2ZiTGZ3V2M5YlkwRC1xa3pyV09jZXJ1akpkZUdpaXk1ZnVRZw?oc=5" target="_blank" rel="noopener noreferrer">無人機・AI「新しい戦い方」変化、防衛省が分析まとめ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月11日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE5sQ1lFQ1hJYjNkSFpmY0F0RlYwWWVOR25EdWNBWlZJYm9iSHQybXJ4aG5JWF9pZnRvVTBEUVVNQ2ZaMUY2ZXZHSHhzT2hLcWc0Z1ZzdXVfQVVWTDlKekxHcWFkeDMwTDQ?oc=5" target="_blank" rel="noopener noreferrer">防衛省「複合防衛拠点」イメージ図を提示 水上・水中無人機製造など [広島県]</a>
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
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibkFVX3lxTFBGZ1NyN2huRjcyc3ZlRFJibUthOUV1MHFMZmtTdjZTNDhGMFN1NDNQVU5FWV92VEVQMU9hVzRhS1hGY2dzc0pOYTNjZHFJcUFZejdaM211S0VZTmgzSnpSSEdJN19pNENzb2FVdTFR?oc=5" target="_blank" rel="noopener noreferrer">防衛省「複合防衛拠点」イメージ図を提示 水上・水中無人機製造など [広島県]</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月11日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE1ROHJCZ2szRzhEdTYtZW9HOGNVcEtYTy1WTE02TURzWnJCaDhlV2o0TkZwWmJlTWV6dWQxU1NxTFFGUUdKMjBCUm9KbUM2UnVZM3R6cW5CSldtbTRjM3BSTzhKN2tzbjJoYjlQRktISVpNWHhJLXc?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相、原潜保有「あらゆる選択肢を排除せず検討」 安保3文書改定で議論</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月10日</span>
            <span class="source">信濃毎日新聞デジタル</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMia0FVX3lxTE56dXhBWVo5cU1JQ2VQYWt1QlZzc0hwbi1Xa1hhbTR6cC1rX3V4M3Zqb2R1UjNEUDZjejhIZmhpQy13RzR3Z2NfQ2pld2h1YkFpNWpTOUNLdnBUNEIxV05IWXE3TWRNdFUtcXdJ?oc=5" target="_blank" rel="noopener noreferrer">消えた「反省」、にじむ防衛力強化…たった一文字で打ち出した高市カラー 終戦の日、安倍氏への共感を上回るインパクトを残した表現とは</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月9日</span>
            <span class="source">東洋経済オンライン</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE8zb1VCZ0lFRS1PVVhIZnU0cE5WQjZJdFNxNDRSY3BYc2N4QWw2NHZTeFNjWWVjbXQ3c19PYU1YUUl4U3ROYkNMcmh5OVlIN2Z5QWdTb0w0dW55SnlGSVRV?oc=5" target="_blank" rel="noopener noreferrer">防衛省による国民の目を欺く前例なき160超の事項要求､｢事項要求｣で10兆円に膨らむ防衛費と文民統制への重大な疑問</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月9日</span>
            <span class="source">ニュースイッチ by 日刊工業新聞社</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiQkFVX3lxTE1HU3N6amZ6dHFISG9jX0t4WW0xc3luQ1NCdUxSMHZUVVFkdWN2UjN1R3RBQ3dkRnJoWTM5eXQ0NnhKQQ?oc=5" target="_blank" rel="noopener noreferrer">防衛省施設にペロブスカイト太陽電池…積水化学など、防水材一体型で実証</a>
        </li>
      </ol>
    </section>
  </main>
</body>
</html>

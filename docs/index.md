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
      <div class="stat"><span>UPDATED</span><strong>2026年09月20日 14:56</strong></div>
      <div class="stat"><span>ARTICLES</span><strong>45件</strong></div>
      <div class="stat"><span>LATEST</span><strong>9月20日</strong></div>
    </section>
    <section>
      <div class="section-head">
        <h2>Latest Coverage</h2>
        <p class="note">Google News RSSから取得・フィルタリングした記事です。</p>
      </div>
      <ol class="news-list">
        <li class="news-card">
          <div class="meta">
            <span class="date">9月20日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZEFVX3lxTE4tNWRmMkN1SkJKWDJoUUtHajJEc3g5ajhIR0daYVdacVlvNXBZeVkwcnNFZnVIRW1MUWUtZjY5Xzc2TlMzYXZhSlp3VURjMTd3T3FqQjlrSXpidkxtdkV1bDJuWVY?oc=5" target="_blank" rel="noopener noreferrer">画像・写真：日米同盟強化へ連携：時事ドットコム</a>
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
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE4wRFlYOE5zUU1mcy1vNzRCQkVybUtoU18wR3FWc29CRXdoMnVwcDVBTUpxX21QNXBuOEZFMjNodmxNRTB2M3R2eGtEcmt5WVhjMTB1bUFvM292VTRnMXR3?oc=5" target="_blank" rel="noopener noreferrer">防衛産業への投融資 全銀協・加藤会長「個別に判断」 | NHKニュース | 安全保障、防衛、金融</a>
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
            <span class="date">9月17日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE9TbEJ6ZVN1S2FfNlp3UWRhWG9fQlZTaENhWUFXX2NHY1BITzlRaW1pSFVua1FPTVh5MGRsdUhDUmVVUjQ5TkNWdWlPdTZQZXFPeEVjOWxERERrbjF4VnUtNF9xX0lfSmNmVHEtVQ?oc=5" target="_blank" rel="noopener noreferrer">三菱重工業など防衛関連株が高い 「防衛産業に融資」報道に期待</a>
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
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE9GZEtuNTV2VTJPZnNMcEpuS0QxQ0JiMGk0TkVGeGhqVGtvVzIzOEpxRXBHWEwxTi1hNzFSbkZ3RTlmdTBaZmlTMmZkX2JRRWZvRkFUczg4bFZBNlBvX1NrV19aRjRaTHV2?oc=5" target="_blank" rel="noopener noreferrer">防衛関連企業の融資、三菱UFJが慎重姿勢を転換 審査進めやすく</a>
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
            <span class="source">東京新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiU0FVX3lxTE51bHdjdnlqRnAxRTlPR1JVY00wVlV3bmhUcTNZX3BwZ29wUlNva2Y0RndSMEhCbDBvQ0I3cDgzT2NFVTIzS2M2RFFwdUlzSTdCSzc0?oc=5" target="_blank" rel="noopener noreferrer">「脅威国を名指し」防衛省がつくった小中高生向け教材の偏った記述 「配布は行わない」断る教育委員会も</a>
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
            <span class="date">9月13日</span>
            <span class="source">ニュースイッチ by 日刊工業新聞社</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiQkFVX3lxTFAwVENtWFh1U1JNaVJLSHVMUjNkMzU1Z2ZiTGZ3V2M5YlkwRC1xa3pyV09jZXJ1akpkZUdpaXk1ZnVRZw?oc=5" target="_blank" rel="noopener noreferrer">無人機・AI「新しい戦い方」変化、防衛省が分析まとめ</a>
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
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE5sQ1lFQ1hJYjNkSFpmY0F0RlYwWWVOR25EdWNBWlZJYm9iSHQybXJ4aG5JWF9pZnRvVTBEUVVNQ2ZaMUY2ZXZHSHhzT2hLcWc0Z1ZzdXVfQVVWTDlKekxHcWFkeDMwTDQ?oc=5" target="_blank" rel="noopener noreferrer">防衛省「複合防衛拠点」イメージ図を提示 水上・水中無人機製造など [広島県]</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月11日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTFBKQkM5UlpSR2M5cFNxSXNVS2N2cUNVbVdyZ2dhcXY0aWVNeG03VkViaUR4b0pZUFZNSTdCelYyWE9BSGc2b2xGME00ODdGN185RTdldkp0bmVzNGZiZWdkeFhrakZfMHg2RC1nTQ?oc=5" target="_blank" rel="noopener noreferrer">ドローンや弾薬、有事増産へ設備投資を助成 防衛省が法改正検討</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月11日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE9hSXZ3MjEwX0hkUEpjWUdyUGhPcmtyU18xaWRzV0ZBVkFjZUpMS1l3cUhnSEQzNXE5V05ubDMyUEgtX0ZqLXAtdlE2c05UTWlTYVZlUTJFdkFiVXJBVmg0TXRESVlUd216NW1ORA?oc=5" target="_blank" rel="noopener noreferrer">呉の日鉄跡地に複合防衛拠点、防衛省がイメージ図 28年度以降に整備</a>
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
        <li class="news-card">
          <div class="meta">
            <span class="date">9月11日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTFBub0t1MXJWZGtfaXhUTVVQSEtKRVNOTXM1a3puNHZfZW1helJyQnI1Zng3TUpBczdpQ3Bzd0dHN1dpRG10SER6RklBSG9HVVI4R2d4S05jNjFfOERjVWNWTDJ5TGNaNXpNdnNqeA?oc=5" target="_blank" rel="noopener noreferrer">ウズベキスタンに戦闘機売却 中国、武器輸出先を拡大</a>
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
        <li class="news-card">
          <div class="meta">
            <span class="date">9月8日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE8wWVlBSF9CdGtZMl92ZDBJYmxLaFNfVGZ4XzgyNUVKN1FIVXZ4SEFreklPOHRMc3RPTEdPNFprVUxxQ1NMYVJ2N2RKRkZUUGRYczl1NEVfcE9DeXh6YVkzNnB3a2NXak0?oc=5" target="_blank" rel="noopener noreferrer">社説：防衛装備品供与 同志国との連携強化に繋げよ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月8日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMickFVX3lxTFB0aVFlbTdQUmh3Z19LQ2Z3NnVjWnRuNGhtdUUtNDh1SVNqeTZta3hrUTA1OXpQYVVtczI4NnBfcTFOVHY1aFdDalo4YkZSUkVET1BDWlY3bzNPeVNRMnBfYnNvNU04d243YU1ZWUxZQVp3QQ?oc=5" target="_blank" rel="noopener noreferrer">南西諸島の防衛力強化・南西シフトに「一定の理解」「さらなる強化は不要」…沖縄県知事選挙でも注目の争点に</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月7日</span>
            <span class="source">時事通信ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiXkFVX3lxTE12azNXMjlZOHFkd09oV3gzbkxOYVJHSWxUWWZpSkhwdTF0ekE2RU9MZUlRR19TSEpXenVIZ1JRRjN5S2VkSEtQLUV6YzJXWGhHbUFWbXpEQk5jTTh0MGc?oc=5" target="_blank" rel="noopener noreferrer">独ＶＷ工場、防衛産業に転換＝イスラエル投資会社に売却へ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月7日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE1qYWVRdEs2QjF1RFNqQ1FuUEpEeG5KUFhYaUkyNWh6OV9JRWMyYkc4N1FQREpqcVgtNEVWT3d4OTd6cGg1N0ljNzkxbUtIZ2t4Q01XR1pWNzhpWGdYSjRPLU40VQ?oc=5" target="_blank" rel="noopener noreferrer">防衛産業へ投融資、銀行が苦慮 政府が要請、政投銀は制限撤廃も</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月7日</span>
            <span class="source">日経ビジネス電子版</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE9wczZpNEpwdENvaFJ0U2ZjOXg4aURSbUJtS0NHaDUteGprZkhVRDhEczRfaW9DNEZsOHhXNGp2dkxfeVNRS1hCT2VuS2xxNTdWOWRueDlTYmk1RWxHTElNNVZNWVpxT3M?oc=5" target="_blank" rel="noopener noreferrer">笹川平和財団が提言 「防衛産業は防衛力そのもの」を具現化する法</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月7日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE5yOXFPdVR2Z3hEa28zUkg2TGxLUnczYUNQa0JNUnBNb2x1bGRwdkJheWp4N1hZcDN2RHQ5MXVQS0R3d2EtZ3czZ3AybjUzdjQ3VjMwWVdINy13dVhmeFhPZEVuRQ?oc=5" target="_blank" rel="noopener noreferrer">独ＶＷ工場、防衛産業に転換 イスラエル投資会社に売却へ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月7日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTFB2cHRVOUI0clNHV0VWT19WdE0xSjcyUTZFdnZGTmFIeVowMVZaLVozOWxKM1pBazRtQ1lQX3JIR1k2RkdkTFM4TmtzNXA1ZGtsbFluTnlQX05hRzN5eEc5VlBqWVVFSzFh?oc=5" target="_blank" rel="noopener noreferrer">「防衛」に新興企業（その2止） 「商機」に沸く防衛産業</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月7日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiggFBVV95cUxNVFVzZlpsdHFXdHlTZ3NLS1F4bE5UVzBTU1dEUnVyMXdSUnFzU1NXZTJuMkZNVE92T3UyTnNXQWt6aDJ0c1VjTk9QY1RqbzFZT1BKRVZUTnpZekRxejE3bVAtYjBYS05jTXBLOEZoR2FhQTc0V0NPWmthUlBSN3lsamdR?oc=5" target="_blank" rel="noopener noreferrer">防衛産業へ投融資、銀行が苦慮 政府が要請、政投銀は制限撤廃も</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月7日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMigAFBVV95cUxQcDFTQ044Q280OTVzM0tXYW5IOVA2SWEyZm1nY3RTb0xBWkVseFVSN0MyYTJZMjNzZVRkUVNkVTF4OXdpOGkyUXpDQVFfa0Z1Y2JZY1JaMHVVSzJ2T0w3akFBMHRFQWMya1hjRmNORjFySFBjZXd3YVNZLTZ0bXNsag?oc=5" target="_blank" rel="noopener noreferrer">独ＶＷ工場、防衛産業に転換 イスラエル投資会社に売却へ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月7日</span>
            <span class="source">東京新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiU0FVX3lxTE1faWRZcHZFdkpKMlBtODRfZzhkNUx6Z0hONDdwSlZfd2l4YUpYcEpXeXp6VU1jakdRVkU5REo2YkVpUm9mWk5VZnBPTDdZTWpxalNz?oc=5" target="_blank" rel="noopener noreferrer">政府の武器輸出政策を問う 24日、明治大で公開シンポ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月6日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTFAxcW9jMlQtOU1BMVZCOFkza05LNzI2Qm1ibU5CSGVjcGQtZnRxU21uek95dmQyLVZNbGNlZXJOTndieHk1aHNlLXpodWp4amhWT3AtMUpmRGhRSWh3b21WWGFqYThhbzg?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相を留任で調整 内閣改造、安保3文書改定を控え継続性重視</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">9月6日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE9peWFzb25jZzRreVdwOE9ocThmWFBLTmlGZWhBOHB4ajJsUThRSTlXQzZxUW41bXd2by1IeWxaZnloOFpCVlJFSWlpWlVHMFdiUUkyX1lJRUZJTktKcGZpOHZxLUp3ai1heFk3ZQ?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相を続投で調整 内閣改造で首相意向、安保3文書改定を控え</a>
        </li>
      </ol>
    </section>
  </main>
</body>
</html>

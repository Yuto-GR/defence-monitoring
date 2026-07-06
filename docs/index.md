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
      <div class="stat"><span>UPDATED</span><strong>2026年07月06日 14:17</strong></div>
      <div class="stat"><span>ARTICLES</span><strong>60件</strong></div>
      <div class="stat"><span>LATEST</span><strong>7月6日</strong></div>
    </section>
    <section>
      <div class="section-head">
        <h2>Latest Coverage</h2>
        <p class="note">Google News RSSから取得・フィルタリングした記事です。</p>
      </div>
      <ol class="news-list">
        <li class="news-card">
          <div class="meta">
            <span class="date">7月6日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE5peGp0Q0ozNzE1WktSODFuRXZ2RDBZaHUtWFpDSWo0SnVyaDZuM09pdFFIM3JGdjZYMHg2eno3MXdKUmEtWUFNbUVPX0VXM3ZfSGdmVmhPRC10TzZUc2RCbnlvNHk0VFE?oc=5" target="_blank" rel="noopener noreferrer">防衛費増の数値目標示さず 安保3文書の自民提言の裏側は……</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月6日</span>
            <span class="source">中日新聞Web</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiVEFVX3lxTFBQQkVPVmVxazlYV0N0YXAtUE5tbTRDUTFocHN0VkNlYlViU3JaSHlDR05lTGhNejhQMlVkcU82RF9XalNCRmdSVnVoYnd5Wk04V3lQdw?oc=5" target="_blank" rel="noopener noreferrer">加速する武器輸出 歯止めは？ 高山晶一・編集委員が聞く</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月6日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTFBhSHY2aG9XZjM1aWFGQ0RCS0NreGl6djZ0eEpQQjM5a0tFYlB1WkhXdmV1UmJkRjVMaE9oYmMyaGpSeHF3VDU0NWhmamdtUnpoMXBsUmlHcmNaZFJ2ek1vNFA2aUJPUQ?oc=5" target="_blank" rel="noopener noreferrer">防衛省に局増設へ、他国と防衛協力や交流する国際連携所管が有力…骨太の方針に向け政府・与党調整</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月6日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMid0FVX3lxTE9jWE1FdWNZcXlWX2lwLUpEZDBLOVJaZmNVVDUzUDZRLVA1aGNtZTl1NV93NnlaM0kzT0ZnWE52STdDOFlyLWZrTHRDajFhTDRlV2ZwNUhjb3NwTzVOTWFSeU8tczRQMjNBR1VHXzVVS250RVRmcVR3?oc=5" target="_blank" rel="noopener noreferrer">トルコ、急成長する防衛産業（上） 欧州の期待と懸念</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月4日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTFB0bWVHYmhaTUJjZDBrSWIwRkFVU3A0WnVER3h5VUp2QW85WmpDWUhSTUVaU25Xc3JjdFdFdXJTeWFNSWV0Zi1WeDQ1UVBTS0dlN2p6LXBlS0FhdDFZZWtjTDJQV1RPc0VQ?oc=5" target="_blank" rel="noopener noreferrer">次期戦闘機開発、27年末まで契約延長 英投資計画受け 防衛省</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月4日</span>
            <span class="source">中日新聞Web</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiVEFVX3lxTFBHQjJLdVJsY21KeWFYbmZzMVNuLTlyOFN0T0o5VWpmbFlmLXVjT1J1bkx0emtYN2FrQWFSRjZKeGI1MDBkQll1ZEhNNGlEeTJqMW01Tg?oc=5" target="_blank" rel="noopener noreferrer">空襲の地で感じた防衛産業展の“熱気” メ～テレのドキュメンタリーが放送文化基金賞受賞</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月4日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiXEFVX3lxTFBoMjJNaEhTRHQzZ2czTWRIdXMzNU43TzdjemJJMU5ZWHRyeXVLZk5OQWtwQUFBZkppczJFWDVkTDR5WFJvOUhaVmlXdm1DekNHUzdwSjY3b2VKdWgt?oc=5" target="_blank" rel="noopener noreferrer">防衛省、職員移動にＬｕｕｐ 東京ドーム５個分、市ケ谷庁舎で</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月4日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMimAFBVV95cUxNODRERUhsSU9NSC1WbV9ZQjZxWHBMSHdnTFU0SENVd2hjT1c4bVBkcGNNWndJUUVpZkgxTlJaXzJyUnJxbHVzYmlEeXptUDdMZERQT3FSaGFRM2JnNDktUlY1Q0NxLXBGSWFHZTZXRE1GanYxWUxsQU1CaE5BcXdxbXpnNm1lQkQwYUZHQWFkdkExTFp2WDhtTQ?oc=5" target="_blank" rel="noopener noreferrer">防衛装備の工場「国有民営」 政府、法改正へ調整 有事の緊急増産に備え</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月4日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiqAFBVV95cUxQRUlEcEp5c0dzdUpTSmFsZTlWdGdHQ3RjcndfQWVTRmdtX0J5VEtQdlNwVDNpWkd5Q2REek1GLUtMNEJwZmRvWVRlQTdUZWhxSE5IdVgzZTFzMHRmSXJVQTVrQXlfT0djV0Z6YkwtR01td0xzVms5QWIzcXkyU1VKSmFpVjczeUtQdjI4SjhsTjdpS2tWZXZjZllKNkNnVWxCaGJGZnNUbHk?oc=5" target="_blank" rel="noopener noreferrer">防衛装備の工場「国有民営」 政府、法改正へ調整 有事の緊急増産に備え</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月3日</span>
            <span class="source">東京新聞デジタル</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiU0FVX3lxTE91Q2tGX0dueVpyUHNXeUhhMHNTdk5hYVEzVmlzaF9iWG11Skd6dEJQaTlhRVRQWktZcE5MOEN2N21jeFQ2U2pjU0haMzRtV1FWTm1B?oc=5" target="_blank" rel="noopener noreferrer">「一切の武器輸出禁止を」署名約12万筆 高市政権が武器輸出ルールを緩和してから急増</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月3日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE5DbTk0dTBDU0t3eU44eUVyWktqb1hreHdIdEZ1S2dta2YxOThUMFY3dGUtejhGOUNER1dmRlc0UUwyTk8tY1VYQ0pCNzVWZnQwZ2pLODZ4a0YxdmxpWTRMbVhhdFh0clU?oc=5" target="_blank" rel="noopener noreferrer">防衛省にLuupの電動キックボード 小泉氏「情報保全上問題ない」 [高市早苗首相 自民党総裁]</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月3日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE1XQ1hMU0FJNUpNc09yMTZqalZDNllTMGtKU2NKeGFKVXA4NkxrbHhiOFdna2lxTjJHQTJDbERLVXRiUlI3N3hpY2prdXFmVFNGMlhjekU3cHIwWXc4eG4wVi1mRHp3VXpLV29veENwVDhmcXhsWmc?oc=5" target="_blank" rel="noopener noreferrer">防衛省、広い敷地移動にLuup導入 位置情報流出の懸念に小泉防衛相「保全上問題ない」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月3日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTFBzcXBYSGFqQ1ctbGNqeDl0d2o4MGtNck1PM3NoOEFMalhsRWI3SnlRa3g5cUtjTk45UG9PX1d4LUd4SzMyUFhUa1VIWlNyUFpIMUJnQ1M3RjM1UHdJSVpxT1ZFc0hGTm1E?oc=5" target="_blank" rel="noopener noreferrer">「当事者」台湾の視点を忘れるな 防衛力強化論の前にすべきこと</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月3日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTFBOaGktTERBUmpoQzI4cTdsQllIYnhyczNHZTVCN0Y1N082QVVJaXo4dW5Memo5ZkxOTGU0LVo2NnB5UXg2dEtwcllYWGI0MUZJQ0JObXF6SmZSbWdmajNpaWVCMzZUS1h4V0dzbg?oc=5" target="_blank" rel="noopener noreferrer">防衛装備の生産能力維持へ｢公設民営｣ 法改正調整、輸出促進に新法人</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月2日</span>
            <span class="source">Reuters</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMigAFBVV95cUxNSFZCX19sQ3RPaksxdm0zSjczd1RLaWs0ajluVWpNUEJLRDJqbllBdG92Wkx4eXZpNy0zeE9oa2E4ODdMQl91dmtsMHg2cFNQalJMRElaeWJBUGtVdmhwV1lHcUdFZGVqeUlIajJIbk9EZkoyY0F1QWlNazB6RTF0UQ?oc=5" target="_blank" rel="noopener noreferrer">ウクライナ、戦時中の武器輸出へ枠組み発表 一部売上高を防衛基金に</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月2日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiggFBVV95cUxNZlh5UkRxSzVSNk9HNk44ckxjZE9QVm5pZVYwWVJOTWpoWUdIUUMxLVB0eTRjellOQW95Y1NSZ3ZoMzgxNjhfTDh0ZWQwV0x0eTk0c3FJMDZMWDJ0SzBXdWdGS1BxdWtVQTJCY0lDdVkyYzBNT205M19ta3lQSGlsNGhR?oc=5" target="_blank" rel="noopener noreferrer">防衛装備協力の推進期待 武器輸出解禁「歓迎」―印国防研究所トップ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月2日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTFBGNzVaWnFxNWQ4UFlTdl9jaHI4bkZsU25QNFhiVHl2emZqMElZNGU3Nm5iSEpidXI2ZzcyR014NkZyNFJtSkVLTFp5RURIV0NLaGtHdWhpMXJYT2xUT0pDd2xkOA?oc=5" target="_blank" rel="noopener noreferrer">防衛装備協力の推進期待 武器輸出解禁「歓迎」―印国防研究所トップ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月2日</span>
            <span class="source">NHK</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMickFVX3lxTE01VnB4a2Zmd3h0Q3FIclcxTHJ6WldIR1RYVVRwUFZzTTMyQ2F2ZzZrRS04NnJHSTlnZEw3T09vMHZHSjJFT0Z1ZkkzY1pJSV8tNV9haXB2VFJLaldCR05Dd2w1VGZYd3duNFI3ZFVIdVotQQ?oc=5" target="_blank" rel="noopener noreferrer">木曜6時台後半 ニュース・気象情報/Biz「インドの防衛産業」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月2日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTFBoSWZibVhjRFVMTEdBbGoyLVo2Rkl3RGp6Z29tVEV2WEhTVmluSnpORXlacVo5cjlHRDVOT3h3b2FORjJzSlFER21uaEhldnAwVVhySTFHQXNuNVVlR25sMFVSQkdqMHpF?oc=5" target="_blank" rel="noopener noreferrer">大学祭の自衛隊ブース中止騒動 職員組合と防衛省 双方の懸念</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月2日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE1vZXJHNDNuMkFOZVNaQXFsUExwbDhvVUZELWRkMXF5LTVkTlFmS1J3S09yc0Q1SGU3amlfWVEwZjUwVWRGei1CXzg5RkpWT2xyTEpPUTRjZEhDX1d0UVd5WENPSQ?oc=5" target="_blank" rel="noopener noreferrer">英、防衛力強化へ投資計画 日伊と戦闘機開発１．８兆円</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月1日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE10VUY4eDJqdUluS2VyY1JWMXJSZk4tcEltb2oxTE5LVXhlQVBMb2pfNF9XckM2bGhIMEx3N0xBTUc4MlhHT2RSR0NpeVFvbGo1bEZ0YlYzTXNNQU1vcVVDQWE5XzJoekU?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相、防衛産業スタートアップと意見交換 技術活用に意欲 [高市早苗首相 自民党総裁]</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月1日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE96TlpzRGVYWklSM2hyUDJ2YmhiNjVMSUlBVjRNSlZNUFd4RlJzX01DVE5tSTlfZGdweEFiRWhzWnlIdHNiTENvdEc0UWJWWHlvSlpiLXc4MDBjeFhXZ0pBc2dINEpWMXp5MFMzcWFKaTV3Z0FKaWc?oc=5" target="_blank" rel="noopener noreferrer">防衛装備移転は国際社会の安定に貢献 民間の技術は国境超える必要不可欠な社会インフラ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月1日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiogFBVV95cUxNZS1nQ3l2Unh3OS1sTm15NG44OFFvcEt4X283WEFfc1BJemFPNE1rM2J1RmVMRkhNQ2RrQWZNTmJPTHNVSzBkQndsd3BFUzJHVEdTV1NaVzgtUjBibzExMEN4Nk1yd1U0bTVIeXI0NzlWc2xjakFPR2hDN09yNTRJU2Ywa042aW5WYXZxSzVmR0w0bE94QmR4TVNfM3RlMFNheEE?oc=5" target="_blank" rel="noopener noreferrer">防衛装備移転は国際社会の安定に貢献 民間の技術は国境超える必要不可欠な社会インフラ（写真・画像 7/11）</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月1日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE5venBRU3JPR290aVBsc0Zpb1dNcTVqYnFwZ09US0thZ3NMQVFYM0hNbFVoZ0JLM0VyZFFIRmNtZnB1Y1MxMjRycEZMWnk1ckZYQUx2NzEwbTFXTVgyaDBqeHFDYVhxRWdWbTVBS0hJZjdLMnowc2c?oc=5" target="_blank" rel="noopener noreferrer">防衛産業強化で戦い方を進化させ、日本企業が世界の中核で存在感発揮する基盤作りを</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月1日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiogFBVV95cUxNc2lJWk0wME1zU1BoNkpuTkN2NUVlaGZRby1fWkdCaElYRmZ4UEpLazVTUWMzN2M4VkhUMFVTS092XzU4QUhXUzRyczlIUEdpTWx4TDNsQmNSLVBmUF9fM2pDR01YTFJOZmJZdFlrZ1FKSGxPRklON21XZ2dzb2ZFWk52SDZjTzZ4RE5LYkxfdFdBNjdBMDNjeFJrU2J1aTA1S3c?oc=5" target="_blank" rel="noopener noreferrer">防衛産業強化で戦い方を進化させ、日本企業が世界の中核で存在感発揮する基盤作りを（写真・画像 1/3）</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月30日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTFBIcDVPWDk1UVhRUVYzc1JQaWtfTm83QmlMaGYyUGhoTkpwVDhGanB0cHNESzBCRXdpdDVZSmhfdF84aWNsOGIyeEt6Vnc0MEFzdnNmeFRPMWl2YVE3Rm94c1VXeVZGZXJLVC1QcGV2RTBQZVllVXc?oc=5" target="_blank" rel="noopener noreferrer">英国が無人機へ1兆円超投資 過去最大規模で防衛力強化、国防相「戦争の様相は急速変化」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月30日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE1qRlBlOWRPRnJOVHpzcDlkNXB6RjJ0aW5lQjVGamhQcHJrT3RYSy1wTGYxbUdaQ05JNlYwQkNwWGEtVEFjSXc4eTlKOWdoSEZoVXhfbXlaWFVPVVV2OU1SaHR4TmJPbnNNcWI4YQ?oc=5" target="_blank" rel="noopener noreferrer">GMやVW、米欧自動車が工場で防衛装備生産 EV向け低迷で設備活用</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月29日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiXEFVX3lxTE80cUZ2c1FJcmhIclluR3B5aXdjbjJ2YW1jS3cyd29yQ3phblNFN3JxZEd1a1RjaERQTHZrMHRGNVl3azFuZGowbUkwZTlQUTAzb3NCbExKRWxIOHdm?oc=5" target="_blank" rel="noopener noreferrer">（Ａｎｏｔｈｅｒ Ｎｏｔｅ）ご機嫌取り外交、理念失う日米同盟 藤田直央</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月29日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMijgFBVV95cUxPME11RWxHM25pN0dodjVOaUJSbENTOFVlQWYtT0V3SG80YmFXaTVCaVJEaW15TnJTcm9IUnVCeFFkWDJKVWpGYU1DblBObXQ2ejVpWGJwbGd2S2h6bTJLRHFpUGFQMENUdVktRmplZ05fdW5vQk42YmR2S3Zya2ZpeFNyRG93WFc5YnF3QnhB?oc=5" target="_blank" rel="noopener noreferrer">（Ａｎｏｔｈｅｒ Ｎｏｔｅ）ご機嫌取り外交、理念失う日米同盟 藤田直央</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月28日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE9LNUcxNXRTX2xjSnE2c3RKZmJ5aWxXOENYVXg4M3ZIemV2TFp2OG5sQVhkNWNyWVhtaUhJM0l2MG5nOFE0eDFsanEyWjZLRUNaNVgzMF9WT085X21ZV3NxTTMybHhGUQ?oc=5" target="_blank" rel="noopener noreferrer">日韓防衛相会談、防衛装備・技術協力の議論で一致…移転３原則見直し踏まえ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月28日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1zeUJSZWZpcnotbVdjOEFXRE5ZbmNoTGxwdVVWN2t3RENTWjhsUUJpNnZUTXFPTlB2TEExQ1pxT2Etakd0bEJabDg2SFJRalhfMlRPQlBXaXkxbS1zWjZtekF5U3VzVGM?oc=5" target="_blank" rel="noopener noreferrer">武器輸出で台頭する韓国、参考例にする日本 国内世論には大きな違い [高市政権の安保見直し][安全保障関連3文書]</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月28日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE1vZGlhaDdEbnZpVkNSSFZlZVZjSk9fRElFejBnR1kzaTgzLWktVEJpWGc3UE1NRzhvdG02TXRyRXY2a2NYbmNBREktbU5zOXo5V2lCNUpjQXRlRDdrRmh3?oc=5" target="_blank" rel="noopener noreferrer">中国とロシアの爆撃機 日本周辺を共同飛行 防衛省が警戒と監視</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月27日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiYkFVX3lxTE9nOVBDS0JIWnRtVXl0dHl4RFFDbG9WdmVsZU84MmRILWRGYVI5cUxKdWN1MXEtRXh3NWlQcnN6VGNHVjVSNlAwNnUwQUVpUWtFS3Mtd3JVSnQ5QjdHTE9IdTV3?oc=5" target="_blank" rel="noopener noreferrer">カナダ 防衛装備「日本と連携」 国防相 無人機、重要鉱物供給も</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月26日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTFB6cXdERE04S1ExUldGYVpST0c5eHN1ZWxYemNQX0kyaU9jWmlQUkdDa21CUFJOcG5ZRXZYZUtDQW9Rd3dXbDVxLU95ZGtGWjlsUU9BR1A3MHFBZkl2cXVmTnB0dVdSLUphUUo0Zw?oc=5" target="_blank" rel="noopener noreferrer">退職自衛官への給付金5割増 生涯設計を支援、防衛省が新組織検討</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月26日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE9JZWRvX1pWZkFsSHo5dEtsU1I2aDdraGxOTU9RcDFHai1Oc2tHZ0wyT1BnbVFnZFZoVTFFNHk1dXdDV0dZNEtuRDRCVzZ1M0FCV1U1aTFuUUhDbXpnRGZZSHRmQWhjeU0?oc=5" target="_blank" rel="noopener noreferrer">航空宇宙自衛隊、発足へ 改正防衛省設置法など成立 空自を改編</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月26日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE4ydUVtcklmQ2tSTVhLdXpIbS02NjNGNjFtQi14Y3RuU3ZKb1ZWRkpWMkFrR0thbHJIWkt3VTFEMWdLNzAtUHF3MFdvanVqTEJBYlJQd2YwRWowYkdUUjdiMG1CWQ?oc=5" target="_blank" rel="noopener noreferrer">空自を「航空宇宙自衛隊」に改編 安全保障上、宇宙領域の重要性増加で―改正防衛省設置法成立</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月26日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE13amtRX2hNeWFZUHZkam5ldDJuVTB1LUdtQmdER2dkVk9BOExESkloc1dKMjJIbG83UEk3UXZCMHBNR2xzbFhXU04xbXN1bUZQOUZHZlFfaWxmZG13NlNUd1JZZw?oc=5" target="_blank" rel="noopener noreferrer">日独防衛産業協力に期待 対中はリスク低減必要―独州首相</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月26日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTFAtd0FDLTk0dWJFbENhNXphN3RraVBwcEhKQ0xwUnMzeWtfTjVyYm9qVHlxZzJpeExzWmtkZXI0S0hscThmRV9hOGIxRmVmM1N4cTdYN05xWV9lYzY5OFdsejNuVQ?oc=5" target="_blank" rel="noopener noreferrer">政府、防衛装備工場の国有化検討 有事の増産見据え、「骨太の方針」に明記へ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月26日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiggFBVV95cUxNQnlrMTROVk9ILWVkMU1IWUE1TU1VNDlBR3UyMnFCYUhVYUtncXJDWlNKYTJPR2lmMmRWTndwZ2ZJZHFjTmg5bXh5dy1tLWRHOHVSTkFEX2drZVR1cGh3M2VCNkhwWXpYZ0ZHWUJKRG5Lb1VfNmhTN21odWhESUpRX1Jn?oc=5" target="_blank" rel="noopener noreferrer">政府、防衛装備工場の国有化検討 有事の増産見据え、「骨太の方針」に明記へ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月26日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE45M293Z1EwYURNcy1GSXlsMXJuZTRaUWJGUVlBUC1LODNpaHRVZmozeFpqcEhIaVBqaFZQeFItU2dIUFZuVkhiWlZDakRpemZDRUlaWkszVU5IWVdCdWFSenlISnRXd0E?oc=5" target="_blank" rel="noopener noreferrer">非核三原則「見直すべき」「柔軟に対応を」 安保3文書の有識者会議</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月26日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE0tMUJnZXdOWVh1eXRrYkFnQURuRUp3Si1oM1lqQUtFVFVxekFsSHpBa000SkRKWC00SDBZUzRVak1EMjduc0dxYUpaWFZBbl8wbnFVWGVmS1RkeENmRXI2RVdqUUNPYVhHVGQ1Vw?oc=5" target="_blank" rel="noopener noreferrer">「AI・無人機技術持つ新興企業育成を」 安保3文書会議の議事要旨</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月25日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE9yZ0I0WV9YaUtaVV9ia3FTbGdfX0NQX2xEZ2tZemZqYkJKRm9zUkdmYnVPZHltQXA3SHlKQlc4MV9zYjhNaUVUb25WUEppVG5PR24xMTk5SjlncmdvaDZQQUsxQQ?oc=5" target="_blank" rel="noopener noreferrer">「ＡＩや重要鉱物で協力」 対日防衛装備協定で強み結集―カナダ国防相</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月25日</span>
            <span class="source">時事通信ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiT0FVX3lxTE93SWZLSkc2UzlReFptVURtdDEyazV0ODZhSDVnbmRJRVBJVWVlXzk3bnhBQ2xUYUt0Y0lEQlpJZDR3WlE4RmRmMy1YWmJ2dms?oc=5" target="_blank" rel="noopener noreferrer">【動画】【ノーカット】「ＡＩや重要鉱物で協力」 対日防衛装備協定で強み結集 カナダ国防相</a>
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
            <span class="date">6月25日</span>
            <span class="source">信濃毎日新聞デジタル</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMia0FVX3lxTE05WFFuRGJZYXRWNVBYNWVyTHBncHNYZTczLTBYTXdDblN6ejlhQUNNS2NObjdXU3VWYzNxRVQ4X1RBZEx1aWlZSE9KRXFZMzRkc2wwRXh0WkpuZzVCTmNjY0ZFQ2ZOczdXVVk0?oc=5" target="_blank" rel="noopener noreferrer">【安保3文書改定】タカ派色似通う首相と維新 防衛増税へ強まる懸念</a>
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
          <a href="https://news.google.com/rss/articles/CBMiW0FVX3lxTE56X0t3VVIwclBWdTR1a3czU2YyZjZkUmF2SmE4bU1vZnp2bkhSZ1VsZG5nSzB4V09ldDVpYWJId1hwc25QUGFLMkJpeF8weWg3bWh6QVBTdDJqdW8?oc=5" target="_blank" rel="noopener noreferrer">税金を投じても日本の防衛産業は強くならない ｢防衛公社｣｢国営工廠｣構想が見落とす統廃合と改革への意識の欠如</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月24日</span>
            <span class="source">Reuters</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMigAFBVV95cUxPdEVwWTRGV2V2cC1VVFd2bk9jdmhoUkR6b3BLYWtGdTNmdlhVMFVxNXQ0d1ZVdGdTYTdaWlBrc1J0SVU0bHl0T0pFNEtyUW9Oc1VhN3RNWjdjTk9PV1Vic3VBRy05aEdDWU9YTERrV3llMmlxV0pqSElVYnB4bVk0dg?oc=5" target="_blank" rel="noopener noreferrer">防衛装備の増産や輸出を主導、骨太の方針に「法人の設立」明記へ＝関係者</a>
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
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTFBMQnZMQkR2YjFIZ0hOYmRXdWNGOVJheVFCaG9SeV8taGpDUUlIaTBjdy1BbDR2TTFQTGdQaWg4ZFdudHYxVVFLaGlQa3pHYmhRNUl6T2lENmtlVlRVMzUwY2lBb01HaE0?oc=5" target="_blank" rel="noopener noreferrer">安保3文書改定の提言、自民と維新が提出 首相「これからが正念場」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月24日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiqAFBVV95cUxQZnI3S0RjN05mR29tWVlHZDV1TGlJWkN5aHZpV2d2Mm9DbnBHSFNnTUNRbkd1TmRNMjFFZkpUbEdHWXhlVzRIV2o1ZElxMkFyLXNWbmV5aGo5T3d0NXUzenlGcWJTNE1uWXdjRmZLWkxvci1YUlB1eTNKM181YUVIUTRlbVZIZ1FwRmtqNWFIbUNvZzN0azVyQTVOS2RUZkpQM1VBanhKYTg?oc=5" target="_blank" rel="noopener noreferrer">自民党、安保3文書改定に向けた政府への提言全文</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月24日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE5QTGVSdHNVWkk3NEI4TWJVZDN3TEdtejFkb0UwYWVQMXFDNVBzbjF5Vl9vb3RCOEVxSmpWVDJLc25ZS0RBazlHcnRoRkVrUXl2MkI3M29SbzRsN3hwd0dwOHY0V2VtRGpVQ1N4Ukh4c3hJby1uR2c?oc=5" target="_blank" rel="noopener noreferrer">安保3文書 自民、維新が提言提出 高市首相「これからが検討の正念場」</a>
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
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiogFBVV95cUxQQ1hTT2puMU0tWU5tUzBQUjhrNXd4Slc4bVRyQTVKVkhxY0tiSWRxZ2Y4ODRNTTZELXdsREZTY0dDMGkzejZVcnlUQXJqNU00SGVrSVZhWWhUUlBTcndmY3ZQanJnVk9zb29iVHZValVhcVptZE01TE9Bc2FFNXBOZnBLQktjOVNway1wVVFhempGZjZURjFQTmw5SFBXUWhlbFE?oc=5" target="_blank" rel="noopener noreferrer">安保3文書 自民、維新が提言提出 高市首相「これからが検討の正念場」（写真・画像 1/2）</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月24日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiogFBVV95cUxPZ0loYTRLTlFoUm5DT3psSWVvQ1d5MmVPRVJBMFZkM0JRQ0lWRTFQU1hIMWFXWl81SVFIdUM5dmx4blp0b1NSa0o4N09tZ2s4Wk1ySlRGNUhmeldrZjRDbGwwaE1YVjFiQTB4NUljWk5ibHNSQ3NlWXdUZGoyb2lZeTBJMHNab0Fub2VHUVlScE9WQkxEZWVSWC1WWVpSaGRxVUE?oc=5" target="_blank" rel="noopener noreferrer">安保3文書 自民、維新が提言提出 高市首相「これからが検討の正念場」（写真・画像 2/2）</a>
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
            <span class="date">6月23日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTFBULXRhdW0yeGloQ19FUnQ2SkExd19xTTJJMUk3QWpfWnl2aGZUb2s0OC01MVJtUkNzd29VNUtmNHFKdVQ1clA4RFRraDRGZm9hZzh2dy1OYnZvanFYaTZkQVRjSkt0UHhXUWVPYg?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相、装備輸出・日米同盟を語る インタビュー全編を動画で</a>
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
            <span class="date">6月22日</span>
            <span class="source">Reuters</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMigAFBVV95cUxOREpIRWhjMGpFS1c3ZEZneVV6ZlFVQnVNUVJzQVFrZjI5QTBKb2h6M0d2TGt3cDBoTmFOOU9vMHhsWXFydzdVdzN6bENMbmRMUklsNk03VFRCZkhMQl9ONGlpSklrUU9RckZNbTkyeUJqLW1Mbk9HWV9jYTdZY3h3Yg?oc=5" target="_blank" rel="noopener noreferrer">印、ＵＡＥと防衛装備売却協議 超音速ミサイルなど＝関係筋</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月21日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiogFBVV95cUxOSGRYT3hxUUhhVDdhaEJ1NEVLazJ3d3ljZWRpbVh2djhMa1JZUER6NkFYNXdudEk1STJvandKd0xvbU9DUVRZdVFrOGFYby1jOFRFVzYycDVLSUNRZnlJbG1ISVF0ZERaUlRWcnBXSGJEdXQ0SXR3NmNBVVYzdnhGYWJMbmYzYVFVczktR1hGNTNnYl8wWFo1SXVRenJVLU1sQkE?oc=5" target="_blank" rel="noopener noreferrer">独自＞安保3文書に「新しい守り方」明記へ 無人機やAI導入…軍事色抑えた表現に（写真・画像 1/2）</a>
        </li>
      </ol>
    </section>
  </main>
</body>
</html>

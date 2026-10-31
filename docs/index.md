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
      <div class="stat"><span>UPDATED</span><strong>2026年10月31日 15:50</strong></div>
      <div class="stat"><span>ARTICLES</span><strong>77件</strong></div>
      <div class="stat"><span>LATEST</span><strong>10月31日</strong></div>
    </section>
    <section>
      <div class="section-head">
        <h2>Latest Coverage</h2>
        <p class="note">Google News RSSから取得・フィルタリングした記事です。</p>
      </div>
      <ol class="news-list">
        <li class="news-card">
          <div class="meta">
            <span class="date">10月31日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE5BeS1DR0Z6cGR1dWxwbFpMOEs0WU1tM2ZWQ1l5ancwd01OOXg5YmgxLWkyZGVnYUJFY2RQMmpObF9QUVE5RG9HYkJoNERZa0NBYnl2Q0tJRDUwR2ZVZExj?oc=5" target="_blank" rel="noopener noreferrer">安保3文書改定「防衛と経済の好循環」を重視 新法人設立も</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月31日</span>
            <span class="source">東京新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiU0FVX3lxTFBNUkFfOTRUTDNJTzNhTm9ITHlDVWV0VHJqRHRUZ2w5NkdnbktndEpWN2hXa0x0NlVJU3FVdnZmbEFOYzl0ZGNJbTBidTB5RkhWYkV3?oc=5" target="_blank" rel="noopener noreferrer">赤字路線が「防衛インフラ」に？…安保3文書改定で明記の案に透ける「国民生活の軍事化」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月30日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE5adFk0TVEwa1dyNkVidlMwb0RlRFNmSmZBTm5WdDNtcTVCQXRLSEljVFpBZE5nOXFNV0ltV1JEU3JxaEVIbDAwQXVjeTFwMjhqaU1SSVVFeXF2ZmNQX1dQNUg4NE5zNUJCZnBDUw?oc=5" target="_blank" rel="noopener noreferrer">新明和工業、神戸空港島で防衛省向け救難飛行艇製造 数十億円を投資</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月30日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE9uZHdpbURBM2xzRVZqV2ZiOGhmTUZ3ZThXTHhYOVFfSy1ueHlPdVpWOFhfRnhkWHotMEJ4dEdYZm0xUm1fbVJOb0RkS0ZMdmRRd2swVVdtTU5kbkV2VWZHdk9LdnIxWWc?oc=5" target="_blank" rel="noopener noreferrer">「イケイケ」で売り込む日本の武器輸出 足元の自衛隊からは不満も [高市政権の安保見直し][安全保障関連3文書]</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月30日</span>
            <span class="source">東京新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiU0FVX3lxTE9uZnVFbEZrWDFNN0tha0Ywd25PVmU3VzJGS1hqclpuNEZVZUR1MFIzYlFFMUU0dlM4dUhBN0ptZWlHOWJoOHFxZmxqYVFpN0xRS2Rj?oc=5" target="_blank" rel="noopener noreferrer">横浜米軍施設に新部隊 防衛省、県と市に伝達</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月30日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiXEFVX3lxTE9zVVNfUkEwakFsb1h0bGxhMDMtdC0tV0M1d2dfbXFvVkNKRGVwY0J2YlJscTlVSjAwYXdzbWl0TTJRSVBVLUdLN1FPai13TXprWERLamszbHBpWWRI?oc=5" target="_blank" rel="noopener noreferrer">防衛省ファンド、大学からの応募最多 名古屋大や大阪大など初採択</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月29日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE43Umh0RVJGZ2tpQjF5a2VJRkM3VlpTSFliZHpKZng4c08tNk1UQXFpQktIMkJTVnI0Ti1DSlRhLTR4RTRFZlNpTDBVbVNjYl85V1F5WVoxYUNhaklvM0ZiWklTX21hdlVaS0dPcg?oc=5" target="_blank" rel="noopener noreferrer">韓国、ドイツと戦略的関係を強化 AIなど先端技術・防衛産業で協力</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月29日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE5XRG8zcU1MeXFsX1BTQnpjNlV5T25pUS1nWVdoNnphazM0YUNUTDNhZ2k0M2R6ZGZubEpiV1Q4QUJUTmZiSUVTenk4YjQxUTNYUEl2dTA3WGtRVXRsYkdXeHpmRmp0RFk?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相、防衛力強化も「専守防衛は変わらず」 フィリピンで訴え</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月29日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMihgFBVV95cUxNVnYycHQxTm9oak4zQzhOVzY2czdmVGdYZVlMNlBhT2FzXzFldndKQ0cwU3VwSExfSjlCTEZ1clhDZGhoTmhNVnNJWTJhbDZRN3VpSF92N0twN1BxMUNodTcxYkQ1al9FUFFxR0x1N2RjQ095Q0tXdnNXVXUwUWtuSjV1TGlodw?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相、防衛力強化も「専守防衛は変わらず」 フィリピンで訴え</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月29日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiW0FVX3lxTE5jbGxVNVllWVB6T3JGSlVmOTlCbzRQSWU3STVqSEthSVBaMEZxZGN3ZUd1Zjg2Zzh2T2RnY1UtMXpOWXY0YjVjMlNKbXl5c1RUUk9Td0RnV2hFNnM?oc=5" target="_blank" rel="noopener noreferrer">AI・無人化で変わる防衛産業、日本企業は「次の成長市場」をどう取り込むか</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月29日</span>
            <span class="source">日経ビジネス電子版</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE5zMDI1NERHT2s1azJEb2d3TE5EaGxuT3FFZUR6WW93UHZ0em42VlZ6V2pYVVMzU0Q5aWw4WGVUdWJLZUxwX2c1bzgyamxjTDNEUUd0NzdJaVFmUQ?oc=5" target="_blank" rel="noopener noreferrer">「新しい戦い方」が呼び起こす防衛産業の地殻変動</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月29日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE0ySUc0SmlvYXJhWFpBdWZFQ19QUEE1SVU4QVJLVkFTTnI3WEhFVEhObi01cmpiV25rS3lrMnBZYVIwMUZ3WWxrRmlybUNLMTdveFE3UHFZRllYYVE1amlUWGp5SlBnZw?oc=5" target="_blank" rel="noopener noreferrer">【速報】防衛省関係者によると、弾道ミサイルの可能性があるものは日本の排他的経済水域外に落下したとみられる</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月29日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE8xcms2b3NDX1FqWUVDT21xbDJDZGI4MUJYWVNZMjBpMlNqeEZsU3duaGVGUUdONUQ4OHRGSTgzYlRCa1ZBUnp2VFBCT0JESE4zT3l4ZHk5M2UyLTdlTHJHUjJiTjFPVjFi?oc=5" target="_blank" rel="noopener noreferrer">北朝鮮が弾道ミサイル発射か、既に落下とみられる 防衛省</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月29日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE1FQUdTeUI1cjI0YlNBbnc1RVo1QkpUcHlaR3JzT3BkUmJjWlhaTmVja3c2QnoxbXc4emR5MVBVXzFuMDJHNk9RazhENGVlWjdHMXVhT1dZUzA0aGRETmcxS2kyaHJWZw?oc=5" target="_blank" rel="noopener noreferrer">【速報】防衛省によると、北朝鮮から発射された弾道ミサイルの可能性があるものは既に落下したとみられる</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月29日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMifkFVX3lxTE8xS1JFcXN3ZWNSWjlHdlpDNFZLZXNtZE9OcjhrWmNJakdfZFh3RWFKUi1Yb3ktQV9BUElyTTVaQ1drSjlYMUU2S2NOWVJ5dzIzOGFqb0ZyZjZpX2V3OHNqR0ctQTdCbm41ZTM3S1dSWXVXcFVTSFlqQXlXZnM3QQ?oc=5" target="_blank" rel="noopener noreferrer">370兆円ノルウェー基金、防衛産業に投資解禁へ 大旋回を探る - 日経ヴェリタス</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月29日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiXEFVX3lxTE1FRkoyeE84MkNQMG5zYmJQYzJMTzF4UEVNSFJPVndtR3VKVEJ2MmlqREZGM29nR01qTTEtNEg4Y3hzMXI0UjZMQlBNYnZ0cl9ZcjJjX0ZKLVItWVlw?oc=5" target="_blank" rel="noopener noreferrer">日米で防衛力強化姿勢 中国念頭、歩調合わせる 防衛相会談</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月28日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE43M1paQ3pCVlFzZVA4NVdUUl9sMmxKZEdzWGJzNHlrMlozUkkzR3lXVmRmV3FfZUpNbnpadUxxTXNpMC1JMWttZzlHYVJXQVJ0UDhfM2ZPNWR6TEdad080M0VSTk5pUQ?oc=5" target="_blank" rel="noopener noreferrer">中国の海軍艦艇と海警船、日本周辺の海峡を「同行」通過…防衛省が初公表・計４隻が大隅海峡通り太平洋へ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月28日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE9rb3FCUlNGSHBVNlNvWS0welNPTVRuZmItdFB0cWZmeW9fWEZkTzF6SDdiN3JIQzVQQ1VtaUFDODl2NVZrU2Ntc1lKOHd5S2FMQ1M0Q0s5bi1RbmtOOTlUMmw2QQ?oc=5" target="_blank" rel="noopener noreferrer">中国海警船、海軍艦艇と同行 防衛省が初公表―鹿児島県沖</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月28日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMigAFBVV95cUxOcXgwbnRxUFV3dDg5R1AxWmN4QlJSQ3lCTGEtVWZ4TXBhSmtZZ3d0OVlKektlUk9VNnJqN25ITTE5VVFOb19la2ZLXzhnRkM1NHRJTkViY2I5ZEpaRFlxUGd1YUhGcFlmanJaQk1rd3lvX1ZyeXlURnliZmQ2Ml81OQ?oc=5" target="_blank" rel="noopener noreferrer">中国海警船、海軍艦艇と同行 防衛省が初公表―鹿児島県沖</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月28日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTFBLMVRFNkRQZXQ0VDNjUERETE1mUlVaS2pXNmNsMGQ5ZHI1blFZY1hzX1M5MUluQVh4TDBZSkxfVWliME5pNTVSUFFzVEVzR1NXNU13blZxcWRsaFdkSVdj?oc=5" target="_blank" rel="noopener noreferrer">中国海軍と海警局の船が海峡を同時に通過 防衛省が初の発表</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月28日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE9tNUFyTmFaRkRvckY2TGthdUlfRVp3Nk8wWnZ1SVEzVHVUUVNrLTZnZGs2M085WWk5ZFBRd3JmSktiRkNLaFFPcWRpOGZVSXh0cWxvT3QxTS0tSWlRWDYyaGRCS1V4R0k?oc=5" target="_blank" rel="noopener noreferrer">日米防衛相が会談 安保3文書改定控え、日本の防衛力強化を議論</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月28日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMijAFBVV95cUxNVjhFMm92VFd6Zjl0bURWWlR1VVhpWFFJVGFDWFptY0dLZlI0eXZDTzJES2xFVkhwYlFGaUV2ZV9rWlRwbzk3dkNQSFQ5Y2tONXFON0Q3dzBYdk5YWG9XOU82OHF6cmpwMW1aNExlaDk2TUZPMVo0dHFUUGZDc1FtZGRPSEFHZEIyazBvYg?oc=5" target="_blank" rel="noopener noreferrer">防衛財源「不足分は増税も選択肢」 関係費拡大も 安保3文書巡る政府有識者会議</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月28日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE5iM28tV2xqRWUycUlwbUtXaTk1V1NvQmdmY0NTVS1oQmtRajlOWHVJdnhFbHBnZE5DWnNkVFktNk9fZUg5ei10cXdxOVlWRkZYZ19hMEcyRVpLUi1BOGxELVhQTQ?oc=5" target="_blank" rel="noopener noreferrer">防衛力強化、恒久財源見えず 消費減税・積極投資と奪い合い</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月28日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiggFBVV95cUxPcTdKSEtJaTVWS0ZwNFc4ellrdzJPcjd5aTZPelB0TUItelJjU0dUYndxRGNaa2NBeDdVUk5ZLVpHSk5sTFBRdHVtcFpPd09NY1FDYklyRlpONW94aUprbEc3bHFodkxKTk9DNlI3OVV4OE4xYmJnV0ZWVkpHSGdRZUln?oc=5" target="_blank" rel="noopener noreferrer">防衛力強化、恒久財源見えず 消費減税・積極投資と奪い合い</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月27日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTFB2M3FZTEFlQndBVVVnWnZyV0FVMTFQZENpTWVJQTFoZFFwdXJSMTBoaTNqZklhNGJza09OR1NibDFaZi1FNVVwVGVwdHRpbTBMYUo1MTZaOWtEakw0Wm1V?oc=5" target="_blank" rel="noopener noreferrer">安保3文書の有識者会議“増税も選択肢として排除せず”の意見 | NHKニュース | 安全保障、防衛、ＡＩ・ネット・ＩＴ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月27日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE1mcWNMbndPbWRXcGpTTmhuQllZS0tFbWE3Y3ktM0JpS2ltcHhna2dzeGhPeHdMM1p0aFZvMTdweFd4UGVHektSYURpb0dneExrSzZOY1Y4ZkV0Um9RcmFJVVFvMTQ1Ymg2?oc=5" target="_blank" rel="noopener noreferrer">笹川財団、天文学会に防衛省との連携求める 「消極的」と主張</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月27日</span>
            <span class="source">Reuters</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMihwFBVV95cUxOUXJKbWVlU210QW0wUHdvMC02X1dRRzdkQW1lcmdqemh0Qi1pTGxiN01vZUt0ek8tSFBsN0U5c0hOc0dVdUFDOEg1QnBYcmxVM1h5aHl2dGplM05LaHc4WndlUUs0S296VkZ2N2xLXzFUSW1OSWp5cndjTlZzenRUd3N0REVpQWM?oc=5" target="_blank" rel="noopener noreferrer">防衛費増強、増税排除すべきでないとの声も 安保3文書改定の有識者会議</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月27日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE42QlJxYXVQM0VfdWJOaDN3akVWSFJubHpfVlBheW9aYW1GWXZRVFM5dW5hR1BsTDRlc1o3VERXWU1vSEdkN2d3QzdBSEhTTEVwOGFoNjNIblBqYnpTaDZGZFU4WV9PT1RpVW51OA?oc=5" target="_blank" rel="noopener noreferrer">高市政権「軍民共用」で成長狙う新戦略 安保3文書・予算で財源対応</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月27日</span>
            <span class="source">中日新聞Web</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiVEFVX3lxTFBWQmNRTl9PbEJMTFE0dVRxYnV5SS1OY3dtdDhDbmJZaTZsZ2laRXd1OHNkSkdjN0dHVFpfLWh0akRRREliYnlvTGptbnlXRVZFaURlOQ?oc=5" target="_blank" rel="noopener noreferrer">【南山大＆中日新聞コラボ企画】アメリカはなぜ強いのか？ 移民問題からAI、日米安保まで大学生が国際部長に問う</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月27日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibkFVX3lxTE9IckZOU3lZZzR6TklKYWp0SFpUWGhXUmhIdkdtWXJheS1wS2lCcWJnQ3dYeE1Za0R1VU5fdXYyMEFMeUlKTE9fNV9uNWoyOC1hd0Uxcm9idjJMOEtxMzZ0WFJLRmRMZmJ1VVpDRkl3?oc=5" target="_blank" rel="noopener noreferrer">【そもそも解説】日本の武器輸出、どう変わった？ 戦争で使われる？</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月27日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTFBZeUE5bXZ1YW9iYlYxeWQ1VmpWUUE3dW5yTm5nbWJPZDRNb0VBZllmLUdZWlcwX1FXcF9DcGJiVG5qNGZQYi1EaWZ4aWlLcHdhbFlZLW1SdXNlbTF0cEFCMnhJYXBCSTM4bXRNVFM3QjFnN0NEOWc?oc=5" target="_blank" rel="noopener noreferrer">中国主催、国連本部で「東京裁判80年写真展」開催 高市政権の「防衛力強化」を牽制か</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月27日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE5wbzRfeWlNdFpjZDMySFE4U1MtZUdVR1VET1hfSXYwZ0tKdEd1d2tsaUVfbUJhSDkxc3JqN21RSnRua2czNXFEbHZ6MlVrR0xzdElsY01CSkp0MmRlbGw5N204SQ?oc=5" target="_blank" rel="noopener noreferrer">防衛装備移転 署名 フィンランドと協定</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月26日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE81SWR2X0txQ2NlTU5RY3JLSHdnM09ncXZOTXh3WTNiQUJqa2thX3ZSUUQyS3ZEcFBwZl9BX3ZQTWZoLU5VeTJSTTg1eTFKRTFhZ19ScjVjR0JXSk1NNTNV?oc=5" target="_blank" rel="noopener noreferrer">政府 OSAで完成済み防衛装備品を同志国に初供与へ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月26日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE83dXhLd2ZKYzRSS2xsN19rR0llMGpWQ0JnZWYzelBKeVJxN0d3WUtsazZqcFYtT3RxTV9FLV9ZTGFXZEhBaXFYTlB0cXhTRkMxanM2QjNFWEhTbDZvSWNWVVAxeEtQYkU?oc=5" target="_blank" rel="noopener noreferrer">日フィンランド、防衛相会談で核政策話題に 防衛装備移転の協定締結</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月26日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE03VXVwV1R6Vmpic3FPS1RVRk9OTVdnYTJtS3NIVXh0Mk00eGN6UG4tYnZRdkk3NmtwOWpQZWZ4ZW1HaElZV3JfR2VmQ3g0RzBDeGo3OHBxRFZSVzBrLUFEN1I1UF9lNTNvUjVRNg?oc=5" target="_blank" rel="noopener noreferrer">日本とフィンランド、防衛装備の移転協定を締結 対ロシアで連携拡大</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月26日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE1nclJ4WmI5eW1GRTlab0dlLTE0T0JfMDhnb2syVGFxN2RKWUtCNWdOSmx4OWczbGxVTkhHakJQN3R6Q3U1bm9RSXpLMEFTVzUwNzBoVXhDbVFfWDZER25YYW8wbTVPaXli?oc=5" target="_blank" rel="noopener noreferrer">自民2議連、安保3文書改定で防衛相に提言 無人機への対応など</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月26日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE1kNFlpVXF1bjZHWERsQ1U4RkVlVDIzUjJXblAwbFNaWC15Vk1PUG52eTlSZnZ2T0lTMUxRb1Zma3lCY2lrd1QyTkRhSFJTVnFJaktReWRUVVJPbGpjVEU0?oc=5" target="_blank" rel="noopener noreferrer">自民議連 “防衛装備品の生産力強化向け 独立行政法人新設を”</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月26日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE83ekIweEdDQWRYZ0I5bV9EM3ZjT0xyVDhSTHZoM3I4OXhURW1OLUIySkh0d000MUMzSEpYZ2Vab3NNdUNSeXRIUTlaMGVjdTVHRFMtWWVURDdrZjRLYW5IY01JQ21fV2kz?oc=5" target="_blank" rel="noopener noreferrer">防衛装備庁の研究助成、京大は応募せず 意向2件を学内審査</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月26日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiXEFVX3lxTFBUQ1RWdWhXZXZaVmNia29MV2Q5cVR3MUh0RW1OQWxWTWIzcGlfSXZrakQ4TExodDVvMHd3SmtKbVRQeFdkeXRwYXJUYVNRbE5VSFlwLXV3Mi1DcU5X?oc=5" target="_blank" rel="noopener noreferrer">（社説）防衛省ファンド 大学と軍事 危うい接近</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月25日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE0xYTlQYkptaHVDN25RZzFWeHVkVU5XNWZid0J1X25TaGVUdXNxQXRHSmRKdWhJUXlMN2FjNVl0T2Z2eEhQLW9fMjBOcy1lVW9aRmpwbVJUWnFGSnBTQnVLdHg0ZmJCQQ?oc=5" target="_blank" rel="noopener noreferrer">ＡＩなど「軍民両用」産業育成へ、政府が年内に「防衛産業基盤戦略」策定…継戦能力確保狙う</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月24日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE5YTDdFRzJraU5HWnBhRjVwa0JxaHdxMjZjcEZXaUNZQURaYVBIMzJGdkl1QmNsb2ZNRjljRVFveDFESjhaTkNXdjZpcGxMX0NGeWVUbnhJZ3RNdEpLbngzZ2VZTXI1UmoxeC1ycQ?oc=5" target="_blank" rel="noopener noreferrer">高市首相、日米同盟「平和と繁栄支える礎」 富士山会合にメッセージ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月23日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE9Na19Oc3lJMEhWTmlGMFo5ZGhYRHMxbU1pNWl5UmdyUFA4anRjbGx2QkxLcmZqdldiTWJNb0hzWW10TFNXXzdEN1IzRXZ4Tkl0UnhCZkdsVFF3SFExQ3Fv?oc=5" target="_blank" rel="noopener noreferrer">防衛省の研究費提供制度に過去最多560件の応募 根強い懸念も</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月23日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE9ZS2wxXzk2cklEc1diZmd4X2RoOVFUNFBTd1psVjRydjdIYVVoREJTRTJnWjZoNUVMZHAxZG1XVkNYQlphcjFvenR4Njl5dzNrNk5hOW9aU010dTdsaW5z?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相“防衛装備庁所管の研究所を機能別に抜本改編”</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月23日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE9qZ2NFYlFkY01sUXNtZ0VKQWFjLTBjX3BOVWFfXzkzbTM0b0JDVFk0bWppREp6ZDAwbnhZb2staE1sTmZMX1V4S21LaGdkWk1QZEl5TDJNOVJTbzFmSUk5MHhvMEpUT2diRlA2cUg3YlA2dS05ekE?oc=5" target="_blank" rel="noopener noreferrer">防衛装備庁傘下の研究所を抜本的見直しへ 小泉防衛相「機動別の体制に改編」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月23日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE1mQUJjdS0wY3ZlN3R5emV3dXYzNEI3N2R0bVZvSDRXN0hrS0F5cEs4Z3pJbHA5RG9CVUxIUGR4QzdPbTRtMW5DYXRrQmhQemFPQXYzTllwMXI4aWwzLWc2WGV6MWVWQmhz?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相、防衛装備庁の研究所体制を改編へ 機能別に再編</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月23日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTFAyV0ZoWVlHcGdJSW9DSDc5QXozYnQ4N21ORjF0alpKQk5hOTlRUDZjUGtfb3hqbVZJQXYzTm00clNQM2ZXcTlweDZWVHJ6eFY3bUcyQ0FiR3U2Vk5EenI3Mmp1LUlRLXFRdENvTGNaMjVJLU55NEE?oc=5" target="_blank" rel="noopener noreferrer">グラス駐日米大使「日米同盟の黄金時代築く象徴」 日本の高校生がハクトウワシ像を贈呈</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月23日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE9qcF9za3Y0X29QYm5mcmk0dnZ4ZE9pcWt4aHRlcDFpdzJzZE9XWHN3WG9JNUtuajMtU1J6SDRBR1dDQWFBZ1BsbWZXQVNoMTdLRWZKVWFFUlJieldGbzlF?oc=5" target="_blank" rel="noopener noreferrer">佐世保市 防衛産業振興の協議会設立に向け 初の準備会合</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月23日</span>
            <span class="source">信濃毎日新聞デジタル</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMia0FVX3lxTFBVZGxkVUtON21WMWZmNEVpWWJvbXo2QmhFY2kxQ0tESUpFdmxGbkx2YUZrcDdSeGluY2hTRmI2TUtsWm1jVmJWQlRYNU1vNDBDZXo1NmY4VkU3TTE1SHRON2ZRS0hyaTNENWxn?oc=5" target="_blank" rel="noopener noreferrer">カナダとトルコ、連携拡大 防衛産業や貿易で戦略関係</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月22日</span>
            <span class="source">信濃毎日新聞デジタル</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMia0FVX3lxTFBubkxzSDlYaG5ORnJpaHZYNGc3QXFkcG91M05oTVVtb2FUWjNSeDJaZWZmYTNHQVFuQjltV3pEVmtSc0g5WFhEMmIzSTdlUllISXVzUm9MVkI4UGlfX1JXQ2o3VHRhWEN2aDBR?oc=5" target="_blank" rel="noopener noreferrer">ドイツ、ロシア情報活動で男逮捕 軍事拠点や防衛産業標的</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月22日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTFA3VUczUjdFdzRIQk5YSXF3Wm5wbVFjcGEwMWNoY2ZzZWFETXU5M2RUTUJYRXdDZXRZTm9IX3o1RllHckVtTExlVTVSWjYzOHJheFdoQV9tVjdlYW45ZmNKZzFIcXU0OFA4WjZZTQ?oc=5" target="_blank" rel="noopener noreferrer">トルコなどイスラム教4カ国、防衛産業の協力で覚書 共同生産など</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月22日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTFBXZ0cyeVZGVXh4dVlnNGJuSElBUUZBb0Zra0RJQVpRSHA5WDE4UHN5YldHYi03LV9jdzRwQTJGRTFkSXNzV09TUnEycTVNbC1JTzdWNHQyLWVFb2pqZnRjYlRBa1pKazU4Y0JJdA?oc=5" target="_blank" rel="noopener noreferrer">「基地のまち」長崎・佐世保、防衛産業振興へ協議会 26年度内に設立</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月22日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTFBrWVU3N183elBiRHJPTkV1UjBGMG5vYnM1WktaZnBaU3J5R1oyeGZiMDVzQXJIcGpjSlZEWHR4N0J5OENqYWVCd05VRlp5dkF5M0lfV1c3V282T1pPVThjTy15Y2FPeWpR?oc=5" target="_blank" rel="noopener noreferrer">安保3文書の提言、12月に先送り 減税と増税の同時議論考慮か</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月22日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTFBPYkxEb05jekpLTUlSa3lvdktPdVhva2dfQTREZEk2QWdxaXREY2tVSUVMV2hyaVYxN0R3My03R1MxbTVxcTFqVFlSQ0Nqd1VTNVZUOGJUQ29nUFhQMnI4aFNqcERSQjN6NVJxN3phUUZqWXpJcEE?oc=5" target="_blank" rel="noopener noreferrer">＜高市政権1年＞外交ではトランプ氏と信頼構築で成果 防衛は安保3文書改定が正念場</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月21日</span>
            <span class="source">信濃毎日新聞デジタル</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMicEFVX3lxTE5KWUJsWUhiLXEybWU3RHlTa3RHcjdWYWhtLXJWQllXN3hZSzlTdy1OVjBJX1NGQkRQLUxJSko1TDJEZjlELVhOMVhyYkcwQVdnQjBIYkIzVWpsbWhiYzR0QjkzM2x2VDA2UE9qQlVXRGc?oc=5" target="_blank" rel="noopener noreferrer">信州大の安保技術研究、防衛装備庁が3件採択 応募・採択ともに初 軍事利用へ懸念の声</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月21日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE95TURzR2Y2cjhJZmpaTk5UbndwemNhQ3lVcGtfR0k0V2xGMXRmalljMEh5S3ZKWXpCaFZiOE5lRTVwYUxnUlBSUG1QS2plZ01RZ3pWbjNsa2NEWnJLWXU5ZkUwajJ4ZXYwSEUwSQ?oc=5" target="_blank" rel="noopener noreferrer">維新が原潜導入を要求、自民「歯止め役」に 安保3文書改定を協議へ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月20日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE9zNzJLREFBb0VYV2RGTlFSNVh0VE1wdDA1U0xyWUdrRzJ3bzBBczZ3bmRaeGgzVEZ1V1VmaWtHVEk3NGNZeERMOEhSakJXSWJlZGd3em1xTHVVVkUxVWltU1FhMmYyZmM?oc=5" target="_blank" rel="noopener noreferrer">防衛省の研究費に手を伸ばした教授 「学生さえ節約させてしまった」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月20日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE9jLU40ZHZRMGNkT3JFZEFOcnp0SE11akZuX0JaQWJCLTF5OEtvMjBqZi1KZ2JHT25YYzI4VkE3bC1BRjZfUzBXNTZ5S0x2TzZTUnVnUjZvTWcxRkxySEVueGhyUGVrdzg?oc=5" target="_blank" rel="noopener noreferrer">軍事との一線どう引くか 大学の防衛省ファンド応募急増、現場で何が</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月20日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE1YLUhVak43bmFqeUtvLUJjajhlREhtMGxvejdlNU5Nb0o5SHhaTW5wOWcwUDVxTVFpT215WTItQ092WGNXeFluVmJhWGpWUkxXZWFWQjBzNlprTVF2djJFWU9hX2R1ajhuU2tlV1lGUE1sM015eWc?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相「大学の姿勢が明らかに変化」防衛省の安全保障技術研究に過去最多560件応募</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月20日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1OUGtFQTNyTHYxZ3JiV2RlTFFTMGVrNzJaOUQ1UXNwNTRVdzhUcXQ1RC05bW1FVC1LdHlpOHN4N3k5SWxKaUpWdEtMVGh0UmxfUVh5TVJoRFBleU85ZkRiTklkMWFsclU?oc=5" target="_blank" rel="noopener noreferrer">応募最多の防衛省ファンディング、どんな制度？ 軍民両用研究を支援</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月20日</span>
            <span class="source">中日新聞Web</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiVEFVX3lxTE4yNmJwblIycjNMNWIzbEszMUNqOFZHQzFFZlR4UElCUkM1V1pVWmRWWUVRZkk0Y1VhOWt1NlpsQ0I5Z0c2M0xHZEVsQlhDaE5zNmpxaA?oc=5" target="_blank" rel="noopener noreferrer">名古屋大や岐阜大、信州大で初採択 防衛省の軍事技術研究費用助成制度、豊橋技術科学大の研究も</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月20日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE1zSW1SWm9zR2hKeTl2VXFZckR4UDRoc3N1OUJ2QjVMTXlfUmNsSWZUWG1Tek1yN0xrZ3dXckw2U2Y0Mk15YjRWSEZsX3Z6bWlCYURfX1JieVk1UXE2djJLTkVoNlBCQXdReUxzRw?oc=5" target="_blank" rel="noopener noreferrer">防衛装備庁の安保技術助成制度、応募が過去最多560件 11大学初採択</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月20日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE5EUkwyYW05SHZ5ZTFqS0ptcHlMQ3VHYlJTQUhvcHhSR1ZyR2IyelAtZVJuclFrZjh6UnU5Q0hEZ2lvelRXc0ZrbTFLVU42WTBLalc4ODRWRHo3M05EWm9sbHlpLXBJNElPY0dYWUpfVTF0V3dzOUE?oc=5" target="_blank" rel="noopener noreferrer">防衛装備庁下北試験場の入札巡り接待受けたか 収賄罪で陸上自衛官を起訴 青森地検</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月20日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiogFBVV95cUxPQ0pFZGh4ZUpxRUNCSkh0TzRuMzVDOWozcW54VnI3Uzd3WXlPZ3Z6dzM0aEVvLVRMcjBfX3NfdVZsNW9sS3p5UmhBSURwR2Z5VjhyZTNkc1FzbFVMQVlzREtkX211YVFvTWRmOWN0Y1VMbjVpMUZlOXdvZmVoRkFyekJZMngxSWMybDhsNzJuY0s5Vm83TEdOcnhvTjNqcmVUNXc?oc=5" target="_blank" rel="noopener noreferrer">防衛装備庁下北試験場の入札巡り接待受けたか 収賄罪で陸上自衛官を起訴 青森地検（写真・画像 1/1）</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月20日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE9YcGhkNXhFLVFFeDFFYV9lVGlJTWNtb2hKWlYtSVkxOVkxZVJyZThyZGVjZ3JLTWx0VHllUG9QRy1INkxLODRRazRtTDQ3OVlyX29LTFBicThra1hrLXRScUZfU3ZrU0dv?oc=5" target="_blank" rel="noopener noreferrer">安保3文書改定の与党協議、11月開催へ 防衛費の増額など論点に</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月20日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTFB4U1hSM181SThJX195ZUpWc0RrWWVJMjlUREtNX0ZSYUNQeS1IWUoxR2JQdEY5UkNtX1hfUHhDRGVVd0JGWGhRYkc2TF8tQ2NvRTBoT2Zhai1xejlKdGtKTUZ5X2lXU0U?oc=5" target="_blank" rel="noopener noreferrer">安保3文書改定、自民と維新が与党協議へ 11月中旬にも</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月20日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTFAxdm1PekFGZ3BONWxVTVRvbkpBc1psZDBWRXJEaGJiZGhqZHFXS0lPUFdVeVNvZ3pDSkRHQmJZRzhFN1NVMXRKYVhYVGVibzRyY1loQnNHVldDSC0xYlZRbmJIYnhsRlJJUjhJdw?oc=5" target="_blank" rel="noopener noreferrer">自民・維新、年内の安保3文書改定に向けた実務者協議へ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月19日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE1rMWM4QTRtUk1uWmVaLURldS1XSm00dC0yZVI1eHV2ODBxS3B2VklyN1ZxbUxCOFNXUGlHQkJBb3dtQU96dXJ0eV8yLUdDcGpVRWthVlBSNllYT0FDWm5KWHlSMkhpQWVCVUt2Yw?oc=5" target="_blank" rel="noopener noreferrer">防衛省のAI基本方針、「見直し必要」小泉防衛相</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月18日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiXEFVX3lxTE42UUxERG1BSXIyMDlrbkhwUVNNRk9HSjB4SFZCNGRZcHNkQ0pvUGZyRU5sRXo2bW9IR1E2OXV0cEJGYng2cDFkYi1STV90UFlFRTBPWFE4bW1CWktI?oc=5" target="_blank" rel="noopener noreferrer">（フロントライン 政治）小泉進次郎防衛相 防衛力強化・積極発信、「将来の首相候補」が向かう先は</a>
        </li>
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
            <span class="date">10月17日</span>
            <span class="source">ニュースイッチ by 日刊工業新聞社</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiR0FVX3lxTE9xd2RSRUtmNXd1ZE4tYUY5Y2J2aFY3MUpaOVpaMDA1RjhZdWloaWVNS3U0OFd2NTNxUlJvcG9MSjBzeno3ZmlN?oc=5" target="_blank" rel="noopener noreferrer">防衛装備品にスタートアップ技術取り込む、始動した新たな調達制度「防衛省版SBIR」の全容</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月17日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTFBORGZ0cjUxUmNLczNkR2xMS2NVb0VtaVkyMnF1Y1JYZXB5SG1rbHpZWHZaOTY3ZEEteGdlOVdTZGZhTlZSN0tMR2FmSWRIeUFaaVBpVVZKdmtlRktkZ1dseEU1cDQ4dTU4enZZUmdZQXZoNHNld2c?oc=5" target="_blank" rel="noopener noreferrer">防衛財源に法人増税浮上 年間10兆円超へ膨張公算 安保3文書の改定巡り、財界反発も</a>
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
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE9KUldnelAyemluZkl3dzZKZGNwZzZ6WUhOaVhDbVdEekgxdHpDVk12djI5UWNkaEpWRVFnSG9Ud3c5eWJGTjFZOHNwNzZvdVNlZURmSkFZTU1GQjZrZHl5QW5qcDlmUlhSNktqbA?oc=5" target="_blank" rel="noopener noreferrer">マクニカ、UAEのサイバー防衛関連企業を子会社化 事業拡大へ</a>
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
      </ol>
    </section>
  </main>
</body>
</html>

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
      <div class="stat"><span>UPDATED</span><strong>2026年07月09日 13:58</strong></div>
      <div class="stat"><span>ARTICLES</span><strong>68件</strong></div>
      <div class="stat"><span>LATEST</span><strong>7月9日</strong></div>
    </section>
    <section>
      <div class="section-head">
        <h2>Latest Coverage</h2>
        <p class="note">Google News RSSから取得・フィルタリングした記事です。</p>
      </div>
      <ol class="news-list">
        <li class="news-card">
          <div class="meta">
            <span class="date">7月9日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiXEFVX3lxTE9xS0JQejVmWjZJdUFycDBlNDh0eGdkTE5KYlY4Y0FCOTNlRFM2WThIeUpoVHMtNTN1SDd0bHVqQjA4RVhUOHJtdUFUNnNkbWRKQXQzcG1FaUdwTEpO?oc=5" target="_blank" rel="noopener noreferrer">防衛力強化、必要性訴え ゼレンスキー氏、トランプ氏と会談</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月9日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMid0FVX3lxTE1fcmlDdGtncW5EMDJuRDQ4QWdlNDJDUF8tSzJIY3AyWVVxclNBZWMtMXNhbDd4NTNUcGdtMTlDRTNyeWt2aWRoY1ZjZkJuRXljUWczTnBtTk9GekllOFR4SDVCUjZjQ1FPcW5ncWhWdDZ1NzJJTFpR?oc=5" target="_blank" rel="noopener noreferrer">防衛産業、新たなフロンティアは海中に（Lex）</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月8日</span>
            <span class="source">信濃毎日新聞デジタル</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMicEFVX3lxTE9Lall2RGJRUjM3VkdqZFFmM1NtTy11Y0pmakkyZVB3dFpnXzJhSURndlE4SURQdGR4RHhhQ05hUGFMMWY1cFpRaE00VGVDTjg3WWdmb0NWVXcybGY1YVYyMk9NWHFzMDNIZVlJRTNBaTg?oc=5" target="_blank" rel="noopener noreferrer">殺傷能力ある武器輸出の解禁 長野県弁護士会が反対声明</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月8日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE1PUnRabzM3ci1lRzhpNVBpdFRoUzlHbVl0cXJwRnZXY0MzOUlfNVNld2ZDRGRyUGEtUUxfdXBqTmNpU1k3cjFuZDBGZmJfa0FOalZXR3lsUGdPRkJnQVhCanpCTQ?oc=5" target="_blank" rel="noopener noreferrer">韓国、防衛産業で欧州食い込み図る ＮＡＴＯの壁克服へ「パートナー」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月8日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiggFBVV95cUxNUUY0OFBXbERVTnZ1cF9jUGJsSWh6UjU4dU1WbFJqZ1l5bjBGX2V5WGhXaHllaS1GaF9RZENkeF82dUlIcG9xOHVFZFd0b1lGTjhKZ0RhcWJDTlFZb3d2Ui04aFUwMFRXbXRPYnFWR1pRNlkzdGItLVVfN3BWRDlkcVVR?oc=5" target="_blank" rel="noopener noreferrer">韓国、防衛産業で欧州食い込み図る ＮＡＴＯの壁克服へ「パートナー」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月8日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZkFVX3lxTE9RUVc0VkR1WGR3Yi1Ldm9Ta1RaQnN2OHF0a2g5Wmt3S21sTk9raFV2bjVIamFybWtXa2ZkbEZzMkFkU1VET1N6QWRZZThuM1BBbmVFM3owNE5HRGZleFc3VHpUcHpFQQ?oc=5" target="_blank" rel="noopener noreferrer">防衛省幹部が相次ぎＸアカウント開設、中国との「認知戦」に備え…小泉防衛相「黙っているだけではウソも本当に」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月8日</span>
            <span class="source">ニュースイッチ by 日刊工業新聞社</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiR0FVX3lxTE53X1FMaEpiUy1EWTdEUVdNN3JFY0xGSmUtcjBua1M0ZzhUbVg0Y1ZPTmhFUTFRNE9nZi1Vd0pQXzZubVNUV0s0?oc=5" target="_blank" rel="noopener noreferrer">三菱重工が引き渡し、防衛省向け護衛艦「ながら」の仕様</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月8日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiXEFVX3lxTFBFTDZ1QmtzcHZJb1FXb2pMRkJ1X1RVdGhwaXBpbmdYZTJkS1p1aXp5WTBRbnVjWm1weFpNcDVBUnJ3elFtaFYxbjNMRlY2RnUyY0d3SFl5SVdaMGty?oc=5" target="_blank" rel="noopener noreferrer">欧州防衛、負担増応じる構え 米から圧力 防衛産業と大型契約発表 ＮＡＴＯサミット</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月8日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE9kRGNHYmhQMUVzQ0JONFh6bWx4eFNjRGVuVFF3Y091WFA3TWd6VWtEUFlkYkptWGRjRnVFUWZoQm55ZVphYV9wSUZRazJmY3NxNWhfMUloYVlEd3hFbzR3VVhNdFZIRUVLREZpTQ?oc=5" target="_blank" rel="noopener noreferrer">「NATO＋インド太平洋」会合 防衛産業・サイバー分野で協力確認</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月7日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE9ObzQtcFhxckVNaXZwN01EUWpaVTR0QWlqQThrbWhNc1hpQ3MtWnp5SHBrYUlScFRMSUtySU9mYjR6SE5ESWdkYkNvUG80VkZrVUtrN1RYWGtiNXdQZlREN09CZ1V3bTlTS0xfbA?oc=5" target="_blank" rel="noopener noreferrer">防衛省、局の増設を要求へ 骨太方針に「組織の抜本強化」明記</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月7日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTFA2ei1IdDVtZ2k0ZFkwc180eWc1Mk1ocjBsT2pjaGNnU01MV3U1NlNpRUozRTJ4NkRBNXJ5OURxMVQ4Nl92cjNNbHFLZlNkMzZZMUlDQ0x0dHZzSFU0c0JKV0owWQ?oc=5" target="_blank" rel="noopener noreferrer">ＮＡＴＯ、防衛産業を前面に 首脳会議開幕、増産へ官民結集</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月7日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiggFBVV95cUxNOEYyZmtDRnFzdmlaLUQ4bHlwdVFaTnFHMEZRVEtKSXc5a3BhVVNQWXQwUTdta3YzOTVsanNIYjh1SmVnbVVFaUJMVTNlWkZpTFdSbVduU1NwcmVqZWZGWl9WMEw2NDZJVlBGRTlnWDV5X1AtM2lvaTJpZ28zWWs1OEpR?oc=5" target="_blank" rel="noopener noreferrer">ＮＡＴＯ、防衛産業を前面に 首脳会議開幕、増産へ官民結集</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月7日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiggFBVV95cUxONHBmR2xXekdUZndxWnB0dVY0YU5iSGlrM21vOUt5b0x4TE9NbUxVMXEyeDl6YnQwM19QUC1HSlc5N1pQYkNsTzVqV056M3NEUFZ6Y1R5aE4yN1pJNGxHSUI4aWNkcWV5cTNjMktxeTBBSXlvVTJfRU9mNmwtOV9Eak5R?oc=5" target="_blank" rel="noopener noreferrer">ＮＡＴＯ、防衛産業を前面に 首脳会議開幕、増産へ官民結集</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月7日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE5ldHhrODBsUjlwVTJwWFk4V2ZpZ1F2d3AtX0RUV2twSDdWenMzMnZDZVpCTFN5OHNNaDBVcndzbTctY1A3NUswRE1ZTDRYQ09ER0tSdlp2T2wyYU8zWGE3T2YxQQ?oc=5" target="_blank" rel="noopener noreferrer">防衛省の「局」、増設検討 国際協力所管、ＯＢ支援庁も</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月7日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE9oejlBdnVrVk44YmpqREozUVdtT0toTlNhdnNUS01hWWlMdmN2b3FBeTBKc0dfdHhXZlk1RGxuZjAtVVlRNzRLRFJNV1M0WHJwLXk3Z0oycWdTUWl5YjBMRGwyR2R0MFE?oc=5" target="_blank" rel="noopener noreferrer">防衛省報道官がX開設、「表のホットライン」中国主張に反論の狙いも [高市政権の安保見直し][安全保障関連3文書]</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月7日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE5HeW8yZnZPUUZUeDdGNldzbE5jY1lBTWtkVFJjaFNFcHlWMFUyQnl6YVRkSlFMTThSVzRxUE9Gc3F6T3BOMjV1X2hBSDVhY24yZXo3a3ZRMFEyUG80VkQzdy1GZ2pvRzg?oc=5" target="_blank" rel="noopener noreferrer">防衛省、新たな局の増設検討 骨太の方針に組織の「抜本的強化」 [高市政権の安保見直し][安全保障関連3文書]</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月7日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiXEFVX3lxTFA1RDhmZ3FFbjR3cXB4NFJsVEpHdmxqbk9KMVNrdEp1OHBzbHM0el9MTnpkTU1MVUhDTGlocUJCVDRfMllhVGh3Uno4OW1SeFpQSXIxanY5bUVrMHRH?oc=5" target="_blank" rel="noopener noreferrer">武器輸出、台頭韓国・追う日本 韓…安くて早い、対北朝鮮で発展 日…高性能で高価、国民は抵抗感</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月6日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE1ubDdJaGhhSTZzOFlvWThCVmFXbVRnOVNjV1pwb1h0b0ZnR195MXByS1p5UW1XT01mVEZMQ2N3SWVpaFFDdlI4OHVfYzloanRnZzJaVUxiRzM4UWJ5TnFfWTNBcXZUTmlFaUlwaQ?oc=5" target="_blank" rel="noopener noreferrer">三菱重工業の株価、午後一段高 「防衛装備の工場『国有民営』」報道で</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月6日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTFBfWUFoOGUzNXU0X3ZydWZYZFRad2F5cmdWWGRZcml6aWMyU2Z1Y1NQWTRoNDRiNXZHalFfX0dTVWpOQloyNlRySEQyeUlxUE9aZkFkbllna3JFRjd1dUhVSExUOA?oc=5" target="_blank" rel="noopener noreferrer">防衛省「ＬＵＵＰ」を導入 市ケ谷庁舎に、ＳＮＳで懸念</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">7月6日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiggFBVV95cUxQc3FPRHhTTlowZXJwNmZBaGxhckYxTHNaOWJ4Wmd6VUdER3Uxcndrdkd0V0sxaXlCU2xUTGJsZW5vaHJnQmNpdVJEZ1NDbTN2WXhoUlRnbnlxNUJGcW03UUJsdlJmenh6WmdCWHE2X3NWUVd1WEpBT3F5UHQ2UGpWSFBB?oc=5" target="_blank" rel="noopener noreferrer">防衛省「ＬＵＵＰ」を導入 市ケ谷庁舎に、ＳＮＳで懸念</a>
        </li>
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
          <a href="https://news.google.com/rss/articles/CBMiqAFBVV95cUxPOHByZzJ4TkR2T0h2djFoZnNlSnE1SmVoSEllamVpYkZMc0ZHODY4dmJYUjRkV09YYXZ3RWY5dFpCWHhvMmU0b2xpaGtEd0RxSnhUYmxTOFFiMEg3TUtuWmN4cy1ER0JGZUN4OWlNamJUVFdYdk12ZUtZcUtpWVl3aWJLcmp4eXA1T0FwZWJDemg2ZlJWX0hHMUt1RFB1MXRDSzBWaTRkTlk?oc=5" target="_blank" rel="noopener noreferrer">防衛装備の工場「国有民営」 政府、法改正へ調整 有事の緊急増産に備え</a>
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
            <span class="source">ロイター</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMigAFBVV95cUxNSFZCX19sQ3RPaksxdm0zSjczd1RLaWs0ajluVWpNUEJLRDJqbllBdG92Wkx4eXZpNy0zeE9oa2E4ODdMQl91dmtsMHg2cFNQalJMRElaeWJBUGtVdmhwV1lHcUdFZGVqeUlIajJIbk9EZkoyY0F1QWlNazB6RTF0UQ?oc=5" target="_blank" rel="noopener noreferrer">ウクライナ、戦時中の武器輸出へ枠組み発表 一部売上高を防衛基金に</a>
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
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiggFBVV95cUxNZlh5UkRxSzVSNk9HNk44ckxjZE9QVm5pZVYwWVJOTWpoWUdIUUMxLVB0eTRjellOQW95Y1NSZ3ZoMzgxNjhfTDh0ZWQwV0x0eTk0c3FJMDZMWDJ0SzBXdWdGS1BxdWtVQTJCY0lDdVkyYzBNT205M19ta3lQSGlsNGhR?oc=5" target="_blank" rel="noopener noreferrer">防衛装備協力の推進期待 武器輸出解禁「歓迎」―印国防研究所トップ</a>
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
          <a href="https://news.google.com/rss/articles/CBMiYkFVX3lxTE9KeDlxYjNCMlk3U2pxMlhuejVGTGZ6UjY5Ylp4dnNZVGFMRUJkT0ZnSC1TMG1Sb0x4SEdwdWViaHl5aS1qa3dNWDhwWmFoRGptRHhrRldicDRaQ19tQUdVMmx3?oc=5" target="_blank" rel="noopener noreferrer">英、防衛力強化へ投資計画 日伊と戦闘機開発１・８兆円</a>
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
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE1qRlBlOWRPRnJOVHpzcDlkNXB6RjJ0aW5lQjVGamhQcHJrT3RYSy1wTGYxbUdaQ05JNlYwQkNwWGEtVEFjSXc4eTlKOWdoSEZoVXhfbXlaWFVPVVV2OU1SaHR4TmJPbnNNcWI4YQ?oc=5" target="_blank" rel="noopener noreferrer">GMやVW、米欧自動車が工場で防衛装備生産 EV向け低迷で設備活用</a>
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
            <span class="date">6月29日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiXEFVX3lxTE80cUZ2c1FJcmhIclluR3B5aXdjbjJ2YW1jS3cyd29yQ3phblNFN3JxZEd1a1RjaERQTHZrMHRGNVl3azFuZGowbUkwZTlQUTAzb3NCbExKRWxIOHdm?oc=5" target="_blank" rel="noopener noreferrer">（Ａｎｏｔｈｅｒ Ｎｏｔｅ）ご機嫌取り外交、理念失う日米同盟 藤田直央</a>
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
            <span class="date">6月27日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiYkFVX3lxTE9nOVBDS0JIWnRtVXl0dHl4RFFDbG9WdmVsZU84MmRILWRGYVI5cUxKdWN1MXEtRXh3NWlQcnN6VGNHVjVSNlAwNnUwQUVpUWtFS3Mtd3JVSnQ5QjdHTE9IdTV3?oc=5" target="_blank" rel="noopener noreferrer">カナダ 防衛装備「日本と連携」 国防相 無人機、重要鉱物供給も</a>
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
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiUEFVX3lxTE91a3dOR2ZBVlZydlRETFc2bllmcHE3TUJoSEI4dHY4WkdnUXVId0pSWmI4M0JPQmpJM3drSkM2ZFd5X3lvSjVVYV9SV2hxUnhT?oc=5" target="_blank" rel="noopener noreferrer">「ＡＩや重要鉱物で協力」 対日防衛装備協定で強み結集 カナダ国防相：ニュース動画：時事ドットコム</a>
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
          <a href="https://news.google.com/rss/articles/CBMiW0FVX3lxTE10elVHb3dzM29XRlRlcUVzc3hoQ2xZQWxTQ2JNcEdCMFdXVzcwNk5pVHlfRzNfNlJ1bkNiZnZHQS1LQ2ZNZzVRVS1hb3Q1b2t6WWtRTmFwa3ctY1U?oc=5" target="_blank" rel="noopener noreferrer">税金を投じても日本の防衛産業は強くならない ｢防衛公社｣｢国営工廠｣構想が見落とす統廃合と改革への意識の欠如</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月24日</span>
            <span class="source">東洋経済オンライン</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiV0FVX3lxTFB2VzZzYmFPQlJobGJkc2gyZzFMM2dYczFDZ0RVS1pjczJkTWhTZWJId3FKVkZhSnFsUWlXZnY4NEd0QjdoaEs5XzBVQWpCbDFFVzRIeENsWQ?oc=5" target="_blank" rel="noopener noreferrer">画像 | 税金を投じても日本の防衛産業は強くならない ｢防衛公社｣｢国営工廠｣構想が見落とす統廃合と改革への意識の欠如</a>
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
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTE82UWxPWXJYNW5PMjlLVUd1dlVpaVhKd2p2bDZQQlY3UExsbDE5ZjR5ZUp3MFJhRUZIeVRaUXFvb0RjZUdqVFdxZjdaSXI1b2ZfWW44bHFqT1g3MHBRSHRCaDdhTk85bXRv?oc=5" target="_blank" rel="noopener noreferrer">首相に自民、維新が安保3文書改定提言提出 両党の溝浮き彫りに</a>
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
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiogFBVV95cUxQMldKbVFQLTItdjFUcFJMTlJxNWl0a3A4UUZ1X19aU0RNMkx3blV5YVozQWlQTHdTZGhQR2VJb0lQbEJieVFPX3pVRVpPSzNRcW51MWNRY0o3cXhucF9HV1RGTkFBVE44N013TktybjJ6YXByeGl0ZEd6NUZ6aHFwa1dfOFIxdEwwMVAxeVF4SW1mb2owMmd2ZWl3aXVveXQyVVE?oc=5" target="_blank" rel="noopener noreferrer">安保3文書与党提言、核政策の見解相違埋まらず 自民は難題先送り 維新は現実的検討（写真・画像 2/2）</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">6月24日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1yWEZ6Y2VuSGV2ckdDejFmVlNNR0VIUHo5TTgxNDRFaF9vSjRQcnNwdU5YUzJKaE9ld2pmQ2FOcDlSNnZzQzN4d0pRMkZwOXYyRUdWeEdOV0o4OFVlRi1lMkxXX3l6QTA?oc=5" target="_blank" rel="noopener noreferrer">武器輸出の推進に新組織を設置へ 「継戦能力」確保でGOCOを検討</a>
        </li>
      </ol>
    </section>
  </main>
</body>
</html>

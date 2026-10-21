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
      <div class="stat"><span>UPDATED</span><strong>2026年10月21日 14:51</strong></div>
      <div class="stat"><span>ARTICLES</span><strong>51件</strong></div>
      <div class="stat"><span>LATEST</span><strong>10月21日</strong></div>
    </section>
    <section>
      <div class="section-head">
        <h2>Latest Coverage</h2>
        <p class="note">Google News RSSから取得・フィルタリングした記事です。</p>
      </div>
      <ol class="news-list">
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
            <span class="source">信濃毎日新聞デジタル</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMicEFVX3lxTE9fMEROTV9aUkstMllaamdWSHk0eEFQMzhHQ19jRjhqY0t6LXdfQ1RKbHc1STV1SXNIOVRwNkl3cnN0bUptektkYzBCVmVhbVlYMXlWWTFjR2w0WTNoVHMyNUVhTjJLaklTZEhjQktkRkY?oc=5" target="_blank" rel="noopener noreferrer">防衛省の研究費助成への応募、厳しさ増す研究資金の確保が背景に</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月21日</span>
            <span class="source">東京新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiU0FVX3lxTE93VGlpS3RVNzNSQVBWODhuRzlDcjVlQWR5SjNXMWJJNU9fWVVrLTNCcUNXbndXOE80aW9pLVhvYmU5TGc5N1RoQ1FfOTh2aktoajdB?oc=5" target="_blank" rel="noopener noreferrer">「軍事研究には従わない」はずの象牙の塔が防衛省の支援をアテにするなんて…識者は警鐘「責任持てるか」</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月21日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE5Id19DOW9vb2d5bWVva0tIUXB5RjdxX2RJamFUWTVSVjhMRHpsRnBuMFUyR0UyWXV3cnBxZUpwWUVSakJseG5KWXRSLU5WTVdNUkFmcVNFd1JoQTl4YlBJ?oc=5" target="_blank" rel="noopener noreferrer">高市内閣発足1年 消費税減税法案成立に全力 安保3文書取り組む | NHKニュース | 高市内閣、国会、消費税</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月21日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMib0FVX3lxTE9JZWNEaHdVRGk5dzNfTFlmTWJ5dUkzOF9oTGlVWWJGZXY1ckFzNG9lZjhKMk51OFlURHd4UnZaS1R1c1pzZjdIdnphYl9UWkdzcUdfcDRxMGw4LU8zV01YUktmcTFMbmdOb0RvSXpKTQ?oc=5" target="_blank" rel="noopener noreferrer">「軍事研究」応募最多 防衛省・計560件 11大学が初採択</a>
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
            <span class="date">10月20日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTFB4U1hSM181SThJX195ZUpWc0RrWWVJMjlUREtNX0ZSYUNQeS1IWUoxR2JQdEY5UkNtX1hfUHhDRGVVd0JGWGhRYkc2TF8tQ2NvRTBoT2Zhai1xejlKdGtKTUZ5X2lXU0U?oc=5" target="_blank" rel="noopener noreferrer">安保3文書改定、自民と維新が与党協議へ 11月中旬にも</a>
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
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE8xRnNoMUVYZjVfT25tUFRtWkdTTERQTDcycXhfdk4zNVdFTW9wYjJqOFFMZ0NyTHBhMnNPMklsemRVc2JqaHdLaDhyWVBlbFoxLVZtejhKT2p5dVhDakhB?oc=5" target="_blank" rel="noopener noreferrer">防衛装備庁の贈収賄疑い 陸曹長と建設会社元社長ら3人起訴</a>
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
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE1zSW1SWm9zR2hKeTl2VXFZckR4UDRoc3N1OUJ2QjVMTXlfUmNsSWZUWG1Tek1yN0xrZ3dXckw2U2Y0Mk15YjRWSEZsX3Z6bWlCYURfX1JieVk1UXE2djJLTkVoNlBCQXdReUxzRw?oc=5" target="_blank" rel="noopener noreferrer">防衛装備庁の安保技術助成制度、応募が過去最多560件 11大学初採択</a>
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
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1OUGtFQTNyTHYxZ3JiV2RlTFFTMGVrNzJaOUQ1UXNwNTRVdzhUcXQ1RC05bW1FVC1LdHlpOHN4N3k5SWxKaUpWdEtMVGh0UmxfUVh5TVJoRFBleU85ZkRiTklkMWFsclU?oc=5" target="_blank" rel="noopener noreferrer">応募最多の防衛省ファンディング、どんな制度？ 軍民両用研究を支援</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月20日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTFB6TkRQQ2FkWVpCR2NLVWRfT0ZkQlE1Q1ViTXZvdjRqbGxTc2kycEV2aVVvY2VtN1NLWTBMV3p0MC1sS0NzcURxNHBJMFJhalZfZHpEVklHWUVmdmRtdkUwV2VxeHRSdlk?oc=5" target="_blank" rel="noopener noreferrer">防衛省ファンド、大学からの応募最多 名古屋大や大阪大など初採択</a>
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
            <span class="source">中日新聞Web</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiVEFVX3lxTE4yNmJwblIycjNMNWIzbEszMUNqOFZHQzFFZlR4UElCUkM1V1pVWmRWWUVRZkk0Y1VhOWt1NlpsQ0I5Z0c2M0xHZEVsQlhDaE5zNmpxaA?oc=5" target="_blank" rel="noopener noreferrer">名古屋大や岐阜大、信州大で初採択 防衛省の軍事技術研究費用助成制度、豊橋技術科学大の研究も</a>
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
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTFBORGZ0cjUxUmNLczNkR2xMS2NVb0VtaVkyMnF1Y1JYZXB5SG1rbHpZWHZaOTY3ZEEteGdlOVdTZGZhTlZSN0tMR2FmSWRIeUFaaVBpVVZKdmtlRktkZ1dseEU1cDQ4dTU4enZZUmdZQXZoNHNld2c?oc=5" target="_blank" rel="noopener noreferrer">防衛財源に法人増税浮上 年間10兆円超へ膨張公算 安保3文書の改定巡り、財界反発も</a>
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
            <span class="date">10月16日</span>
            <span class="source">毎日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiaEFVX3lxTFB1SUhFZ2w3YjVZN09tcDh2S05XYXNtcWplc0RHTnQ1RlRBNUpUdkhWQUx4aW1oTzRVNXIxVmJtb2tVeEVJcVdXZk5pZHNLVl9mcGdzd0R1RE1MbDJzNHVjODRmRFNzWThx?oc=5" target="_blank" rel="noopener noreferrer">自衛隊に原子力潜水艦導入検討、安保3文書改定で盛り込む方針</a>
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
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE9JZVNoMkpsTktSSm9LZkpocFptZVhOaHVsRGI3WjlrMWhSeVVVbWVLRlJMZi1YNUVRQVU3MVF3SGlLMzUtUVJTQnladzh2aGl5U1c3aXJ3SDBMMUtDWjNSMTNfNzhmdldDT1p6bQ?oc=5" target="_blank" rel="noopener noreferrer">SHIFT、安保でのAI利用プロジェクトを開始 防衛装備庁の事業</a>
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
        <li class="news-card">
          <div class="meta">
            <span class="date">10月15日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE85aElrRDROUTVtcTZkMHFZN09LWWlrVkxCRjQ0SWtsYlJjRkx2NlcyZ255RkRRRlhjdTh6MmpjWktJaUg2eU1WZTdWeDk5VklndDNmUl9QWFI5Sk54b0lwWXV3eENpdGRyMlRBaA?oc=5" target="_blank" rel="noopener noreferrer">中国軍の空母「遼寧」が南シナ海へ航行 防衛省発表</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月15日</span>
            <span class="source">東京新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiU0FVX3lxTE14bTFWUEZLaWpiQWk5S2tETlU2NllfVGQ3WWdyQzY1ZFV6NEJSX1hkNm1wdEpobWt0ZEt4RUZqNUNtYXA3V3RCYV9SbklwcDB6VGpn?oc=5" target="_blank" rel="noopener noreferrer">核が持ち込まれたら「攻撃誘発の危険もある」…安保3文書改定でシンクタンクが警鐘</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月15日</span>
            <span class="source">読売新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiYkFVX3lxTE9CcDZjcHRsVm9BVlRsSGREcnFxMDlnekFRZWFXTXpnQm0wWFdfVVdUaV90NXBzdW1rZzNPNzlzVUNHNDlxX3RERG1kWVJXcmpWUFIxRFBfR0VSRXRubUNZdjR3?oc=5" target="_blank" rel="noopener noreferrer">北朝鮮、国連委で日本の防衛力強化を批判「敗戦国から好戦国に」…日本抑止のために「戦力を強化」とも</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月15日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE5tZjQteW1mV3p5U21lSTlhRmdZaTgwbHZmcXhibDVqVUhzaFZiRmVsVUFpc0hyWTBDNnR4c0hZamw2Njd5RVlBWW5LX2pZVXQxR2hiVU5LbnJXNVQwQUt0bFZOMF9WcmloRGJLTA?oc=5" target="_blank" rel="noopener noreferrer">安保3文書改定で非核三原則「表現検討」 首相が言及、環境変化で</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月14日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTFBJWWZwdFFrTE5YTUNMNmZmdVJiZmlrQ0U4M0NXd3JKZGZlLWQ5S2JSZE14ZW53QmxXZFI1bUdkcFVFWDRLczlrMklkY0FEWGg5Z25hZ09ZcEJxU2c2c1JqNXhWd28tQ0F1TGlPTQ?oc=5" target="_blank" rel="noopener noreferrer">原子力潜水艦、安保3文書に導入の明記求める意見 有識者会議</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月14日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE9jWFBQLVNrTFl6MnRVTnlfTHJpM2tBc3Q0bkxhdW9BLWg1YTdEdnBteTlHVHdsc1ctT1RDdFdOVUJTOElTQlM2Nml3aG82MmsxNEg1UHJaY2w1ekZSRjYyTjBGcVZDenc?oc=5" target="_blank" rel="noopener noreferrer">原潜「導入」「検討」の明記求める声 安保3文書の有識者会議で</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月14日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTE80THJ1b1hwR3pfSDVTaXlCOGtXaEw2LWw0TzVLLV9OcnNXQXNyc2x5X3FLVnhiQVg5TWNmN2ZIVllzSHQyLUpNWEdkTmN2NFA3WHF3NGZ4Y1FCN3ViZjBDb21fVzN0VUk0MC1FSA?oc=5" target="_blank" rel="noopener noreferrer">安保3文書改定、原潜保有の「調査」明記論 建造1兆円の見方</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月14日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE9RWUxxUDhyTjdjZ2prdVpOM041a2F4eUl1WlhCR2x2SXVzYkNSS0laRUJvM1pCdHNmQjFMTG4wVmdpaWxmY2tmb0VXM1dVaTcyeDFKaEplZ09qMzZ1SUxvQ1lhb3hzcng0OXZXNkJEVC1Wam9DeEE?oc=5" target="_blank" rel="noopener noreferrer">非核三原則の例外規定「検討の余地ある」 高市首相、安保3文書改定をめぐり答弁</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月14日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTFAyb3dOQ19IS29ibnIwRlBZbDRWRm5YS1gtcGVxdXZqUDNRMkJsazZ6cUtnU194Q1lZR0dSc3BUcy1RUGo1TTJYZG1yRlNBM0tMODA4azV1bXd2dkltQndEakQtdlMtS05aeHlpYw?oc=5" target="_blank" rel="noopener noreferrer">高市首相、非核三原則「表現ぶりに検討の余地」 安保3文書改定で</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月13日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE5uQXpEcUppcG8zb0dLNnFJbTRPbUFseks4SG95VE5FX1E1d2FtLUYyQmttS3BvYzRHbDd2NFV4OEl5R0RnVlZtQ3Y1VzFmSmVxb01kNnN5S1NYUWxlaVpwVV91ZDlESTJJTUx3RjZrNjlIMnRkX3c?oc=5" target="_blank" rel="noopener noreferrer">退職自衛官の再就職支援、自民議連が設立総会 安保3文書改定に向けて提言へ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月13日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiogFBVV95cUxQMEZqaTU2TUdaWHNNRGVPdnppNjZpY2lvTFprdklmMVhpOE1JSkFuN1laQWNHVDBOM1VZWl9obVlCQVVLY3VTM3VMel9UYW9nNUVDV25jbGd4c0o2VUZrUGtGN0ZWUlBHT0lJRmlWNUJVZjRHQ2lTYTNzdGxnUGc3UzhpdTNoblpIeVUxenJIZ3FpVW44NV9lNlJSZFFJeXdSNlE?oc=5" target="_blank" rel="noopener noreferrer">退職自衛官の再就職支援、自民議連が設立総会 安保3文書改定に向けて提言へ（写真・画像 1/1）</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月10日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE1TT3E2X0tMWFVBWUIxUWFwWUk0TzBxZEZWaF9BZ25fZl9BS3ZxXzZfQnNwalFQeFdsazQ1Sl9tWmpyTDdZaXRYRm53MUJxaVZXZ2hpckVVd3NjTWFhRXZJ?oc=5" target="_blank" rel="noopener noreferrer">台湾総統「中国が現状変更」 防衛力強化強調し連携呼びかけ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月10日</span>
            <span class="source">東京新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiU0FVX3lxTE5iQlhLOTNOT3EwdVNCbzJIZ0NIaFdpWDJKelNSWHlxVjNoNzZ0OFR5MlRpYi10aTg0VnFsSnZYV3NCUWZ3MXpMRGRhNWhOemlKS3Jr?oc=5" target="_blank" rel="noopener noreferrer">台湾総統、防衛力強化を訴え 中国に対抗、双十節で演説</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月9日</span>
            <span class="source">時事ドットコム</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiY0FVX3lxTE5jMTJsYk9hYkNXYWVUcktBSTlDSXZraVJ4SFhJc0R2anFOS3k4clJDZFh0dFZ3T1dpU0R4dUs3UzhKS3dTaVp2VkxLdVRhcU1UazhHWTJNR1pyNGhpd253ZThNWQ?oc=5" target="_blank" rel="noopener noreferrer">ロケット打ち上げ、迅速化研究 防衛省、衛星攻撃に備え</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月9日</span>
            <span class="source">朝日新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1rcEpsNlowVHNjY2J5RDRvOUw1QzVEd1hGVEVEOVVrdFJ5SU9zRnkzZEo4aGwwVEdNVWtrUGg4MW5ucmdRU1AtS2xzeWRKbm5XQVB2QW5PekswempnUlJrRVhuLUZvMkU?oc=5" target="_blank" rel="noopener noreferrer">防衛力強化へ特定利用空港じわり増加 都市部近接の神戸、懸念の声も [兵庫県]</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月9日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE5tdmdJQ21vdnV0V1V0WHJpMWRwY3Byb0lha2d1U0U5bHN3cGNaa1VEQjR4djE5eU12QjYxZlZqT0xQcmdlNHJ3S2tvMWFnanJrOG9OUmJxLV93MTRlMFNhbmowRHZISlk0ZjUzZkdpMFEwTGdwSnc?oc=5" target="_blank" rel="noopener noreferrer">小泉進次郎防衛相、原潜保有「議論の必要性は国民も理解」 安保3文書改定</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月8日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE1kUzgxazZETTF1c2s4NU5waWJHSGV6WkhzeUVoN04xTGtpeW5SVDhyRU5OQ3MxRG1lUUdfRHg5Z0NqYTFaT3h0RTJOTnpKdDZETGd4T2NCbWhXRVpCT1l0Z3ZnTlhBV3NaMVRubjZKT0V1VUkycUE?oc=5" target="_blank" rel="noopener noreferrer">＜独自＞核持ち込み、緊急時の例外記載案浮上 安保3文書改定、非核三原則は維持へ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月8日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE5jeEFnSXdHV0FSVXRXRXY2cmt3N3BSQXFiZnR0XzdmbDVlaDRncjJJMkZtVmtjbXFaR0tIR0hBOXJjSUNxSXFQc2tkWmUwYkgxbGtDZVkxWjhKR2dJNHRrS0FXUU5tV1ZuR2t6Z04wMnY0SC1raVE?oc=5" target="_blank" rel="noopener noreferrer">安保3文書改定は「本質論で丁寧に議論進めたい」 自民・小林政調会長が記者会見</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月7日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMibEFVX3lxTFB1eEtYU2NvZXIyYUhNNlBmcVpIYThjaHVVc2MwZm5RcDBGa2YyTkkxc0dmcjBOclF6TjQ5OU9nV0o0b2tXQ1gyS2ZEWnJiREp0dlM0RW5wRG12aWdfdFBOZ2dKOVRIWFFXQ0pKTw?oc=5" target="_blank" rel="noopener noreferrer">スタートアップ参入促進へ5000億円 自民の防衛産業議連が提言案</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月7日</span>
            <span class="source">NHKニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiX0FVX3lxTE96Uk1PRS1JUTJseFdGN2FKcnFmdGFlSlV1LTdyY1RqLU16TXJXdjc0dGowV1dxdUdmVE90X0VycTZzR1pldzc1T2MxdE9RM3BlOGk0b09zVFd1OHB4SlJV?oc=5" target="_blank" rel="noopener noreferrer">小泉防衛相 スタートアップ企業に防衛産業への参入呼びかけ</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月7日</span>
            <span class="source">Reuters</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMihAFBVV95cUxPRzYwUThaOTNBWHgwYlVTcS1zbDBFaEpweHZqdFVGd2FkRDNFX044dnVLLVc5bWdLd29lM3dpZWl5TG9IRTZJa2VjUzA4VFN2MkdjeFZZcWs0UmVjTi11OERkUmpNWHhLVmlGWUNrbkJOODhSR0pWLXJEUFhPdDg1eHI4bEk?oc=5" target="_blank" rel="noopener noreferrer">米台関係、米中首脳会談後も強固 防衛装備の適時引き渡し重要＝駐米代表 | ロイター</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月7日</span>
            <span class="source">日本経済新聞</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMiWkFVX3lxTE9mQURRSXVJYmFlVFdmRVFXT2tEZjY5OGY5UGFtR1N4SGozbDhZaWhyV2tHQW5RaVZzUW5waHFqNUZpQlBocmFDakVrd0prelpXQkpvUF9JOVNyZw?oc=5" target="_blank" rel="noopener noreferrer">中国軍とどう向き合うか 安保3文書改定、日本の選択を専門家と解説</a>
        </li>
        <li class="news-card">
          <div class="meta">
            <span class="date">10月7日</span>
            <span class="source">産経ニュース</span>
          </div>
          <a href="https://news.google.com/rss/articles/CBMidkFVX3lxTE1VeXhwZGdpd25MSXVONzhqMGtYY1VLSWdMb0ZUU2xPY3lEQXU2aF9odXlXTHZwdnZOdUNGX2NrVHEzZEhLMEpZV0pQTThJTEZKSTRNRm5wRHRIU2dzTURxVUlWWlZlVFh6T24tNUp4aTdua0JmU2c?oc=5" target="_blank" rel="noopener noreferrer">防衛産業推進へ「独法」新設要求 自民議連、安保3文書改定への提言了承 予算規模数兆円</a>
        </li>
      </ol>
    </section>
  </main>
</body>
</html>

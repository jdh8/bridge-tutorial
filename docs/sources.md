# 資料來源

## Bridge World Standard 2017

完整的制度原文在 <https://www.bridgeworld.com/pages/readingroom/bws/bwscompletesystem.html>，一頁大約 90 KB 的 HTML。用 curl 抓的時候要帶瀏覽器的 User-Agent。舊的 `indexphp.php?page=...` 和 `default.asp?...` 網址都是 404（2026-10-04 查過）。2026-10-11 直連被 Cloudflare 的驗證頁擋住，改從 Wayback Machine 抓：`https://web.archive.org/web/2024id_/<原網址>`。

制度上的事實要對照原文再寫進書裡，不要憑記憶。一個容易踩的坑：BWS 2017 的 1NT - 2NT 是轉換到方塊，不是自然的邀請；邀請要走 2♠ 問範圍，或是 Stayman 之後再叫 2NT。

本書和 BWS 不同的地方，見[點數範圍](ranges.md)和[強牌 2♣](strong-2c.md)。

## 二蓋一的各家打法

[二蓋一的風格](two-over-one.md)用到的資料：

- Max Hardy 的制度摘要：<https://bridge-tips.co.il/wp-content/uploads/2016/09/2_1-Hardy-Max.pdf>。
- Kokish–Kraft 的制度筆記（2008）：<https://bridgewithdan.com/wp-content/uploads/2019/07/WEAK-NOTRUMP-SYSTEM-Kokish-Kraft-Jan-2008.pdf>。
- Larry Cohen 的文章：<https://www.larryco.com/bridge-articles/unifying-21-gf>。
- Bridge Winners 在 2018 年的 BW 2/1 投票系列：<https://bridgewinners.com/article/series/bridge-winners-standard-21/>。定案在 `bw-21-final-conclusions`，其中的表格是一張圖。
- kwbridge 的整理：<https://kwbridge.com/2over1.htm>。

Bridge Winners 的得票率要登入才看得到。留言不必登入：文章的 HTML 裡有 `pk: <數字>`，留言在 `/bwcomments/list/Article/<pk>/`，回傳 JSON。

Lawrence 和 Bergen 的打法目前只查到二手的整理，沒有對照原書。

## 賭倍者的扣叫

[第五部的數字](part5.md#賭倍者的扣叫)用到的資料：

- La Jolla 的 bidding handbook，10-9 節〈Cue Bids in Takeout Double Situations〉：<https://lajollabridge.com/French/biddinghandbook/10-09.pdf>。
- Pete Matthews 的〈Doubler's Cue Bid〉：<https://bridgewinners.com/article/view/doublers-cue-bid/>。他的扣叫通常是三張支持、加叫的牌力，和本書的總入口不同。
- Steve Robinson 的專家問卷〈Forcing Bids after a Takeout Double〉：<https://csbnews.org/en/forcing-bids-after-a-takeout-double/>。只讀過摘要，沒有逐句對照。

## 負性賭倍

[第五部的數字](part5.md#迫叫)查開叫者能不能放掉負性賭倍時用到的資料：

- Larry Cohen 的〈Double Trouble〉：<https://www.larryco.com/uploaded/pdf/pdfup_24.pdf>。PDF，沒有 pdftotext 時可以用 Swift 的 PDFKit 取出文字。
- Marty Bergen《Negative Doubles》的摘錄：<https://www.bridgewebs.com/richmondba/negdoub_bergen.pdf>。只有高線位的部分，全書沒有查到。
- Robert Todd 的〈Opener's Rebids After a Negative Double〉：<https://www.advinbridge.com/this-week-in-bridge/343>。
- Karen Walker：<https://kwbridge.com/negdbl.htm>；Richard Pavlicek：<https://www.rpbridge.net/5a00.htm>。
- ACBL 的 SAYC System Booklet：<https://www.bridgehands.com/Conventions/SAYC_System_Notes.pdf>。字型把花色符號編成別的字，抽出來的文字少了 ♠。
- 英文維基百科的 Negative double 條目，歷史的部分引 Official Encyclopedia of Bridge 第七版第 303 頁。

## 歷史

Bryant McCampbell 的《Auction Tactics》（Dodd, Mead，1915）在 archive.org 有全文和掃描：<https://archive.org/details/auctiontactics00mcca>，1917 年的印本是 `auctiontactics00mcca_0`。純文字在 `https://archive.org/download/<id>/<id>_djvu.txt`，單頁掃描在 `https://archive.org/download/<id>/page/n<leaf>_w1000.jpg`，書上的第 62 頁是 leaf 65。迫伴賭倍的考證見[第五部的數字](part5.md#歷史)。

## 雙夢家統計

作者自己的雙夢家統計（大約一億副牌）寫在 `../pons/docs/`：

| 檔案 | 主題 |
|---|---|
| `notrump-game-threshold.md` | 3NT 的門檻 |
| `major-game-threshold.md` | 高花成局的門檻 |
| `minor-game-threshold.md` | 低花成局的門檻 |
| `notrump-slam.md` | 無王滿貫 |
| `suit-slam.md` | 王牌滿貫 |
| `nltc.md`、`zar.md`、`binky-points.md` | 其他的牌力評估法 |

每一篇都按牌力尺度（大牌點、只有夢家算支持點、兩手都算支持點）和王牌張數，列出損益兩平的點數。

書裡的統計說法，例如成局或滿貫要幾點、一張王牌或一個短門值多少，先查這些文件再引用；文件沒有涵蓋的問題才另外模擬。這些研究用的尺度和書裡的表格略有不同，例如短門一律算 3、2、1 點，兩門合計十張以上再加 1 點，所以引用時要說明是哪一種尺度。

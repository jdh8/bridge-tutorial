// 實戰篇的揭曉模式：一次只看輪到的那一家，叫完一個叫品再對答案。
// 資料全部取自頁面上的表格：第一張表是四家的牌，<details> 裡是叫牌過程和解說。
// 表格的欄位順序是西北東南。
"use strict";

document.querySelectorAll(".deal").forEach(deal => {
	const details = deal.querySelector("details");
	const hands = deal.querySelectorAll(".table-wrapper")[0].querySelectorAll("td");
	const answer = details.querySelector(".table-wrapper");
	const bullets = [...details.querySelectorAll("li")];

	// 每個叫品：誰叫的、叫什麼、在答案表裡是哪一格
	const calls = [...answer.querySelectorAll("td")]
		.map((td, i) => ({ seat: i % 4, text: td.textContent.trim(), i }))
		.filter(call => call.text);

	// 解說照叫牌順序排，粗體是「北 1NT」或「東、南、西 Pass」。
	// 有些叫品沒有解說，合寫的那條要留給後面的人。
	let p = 0;
	for (const call of calls) {
		for (const q of [p, p + 1]) {
			const bold = bullets[q]?.querySelector("strong").textContent ?? "";
			if (bold.includes("西北東南"[call.seat]) && bold.endsWith(" " + call.text)) {
				call.bullet = bullets[q];
				p = bold.includes("、") ? q : q + 1;
				break;
			}
		}
	}

	const start = document.createElement("button");
	const step = document.createElement("button");
	start.textContent = "一次看一家";
	deal.prepend(start);

	let table, notes, k, shown;

	const show = seat => hands.forEach((td, i) => {
		td.style.visibility = seat === undefined || i === seat ? "" : "hidden";
	});

	const finish = () => {
		table.remove();
		notes.remove();
		step.remove();
		show();
		details.hidden = false;
		details.open = true;
		start.textContent = "一次看一家";
		table = null;
	};

	start.onclick = () => {
		if (table) return finish();
		table = answer.cloneNode(true);
		table.querySelectorAll("td").forEach(td => td.style.visibility = "hidden");
		notes = document.createElement("ul");
		details.hidden = true;
		details.after(table, notes, step);
		start.textContent = "攤開四家";
		k = 0;
		shown = false;
		show(calls[0].seat);
		step.textContent = "對答案";
	};

	step.onclick = () => {
		if (shown) {
			show(calls[k].seat);
			step.textContent = "對答案";
		} else {
			const call = calls[k++];
			table.querySelectorAll("td")[call.i].style.visibility = "";
			// 合寫的解說只放一次
			if (call.bullet && call.bullet !== calls[k - 2]?.bullet)
				notes.append(call.bullet.cloneNode(true));
			if (k === calls.length) return finish();
			step.textContent = "下一家";
		}
		shown = !shown;
	};
});

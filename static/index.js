const left = document.querySelector(".left");
const center = document.querySelector(".center");
const bigImg = center.querySelector("div");
const table = document.querySelector(".table").querySelectorAll("table")[1];
console.log("fdfd");
const tableData = [
  [
    { no: 0, type: "QRCODE", content: "0gsfsa" },
    { no: 1, type: "CODE", content: "1gsfsa" },
    { no: 2, type: "EN13", content: "2gsfsa" },
    { no: 3, type: "EN8", content: "3gsfsa" },
    { no: 4, type: "QRCODE", content: "4gsfsa" },
    { no: 5, type: "error", content: "" },
    { no: 6, type: "QRCODE", content: "6gsfsa" },
    { no: 7, type: "QRCODE", content: "7gsfsa" },
  ],
  [
    { no: 0, type: "QRCODE", content: "0gsfsa" },
    { no: 1, type: "CODE", content: "1gsfsa" },
    { no: 2, type: "EN13", content: "2gsfsa" },
    { no: 3, type: "EN8", content: "3gsfsa" },
    { no: 4, type: "QRCODE", content: "4gsfsa" },
    { no: 5, type: "error", content: "" },
    { no: 6, type: "QRCODE", content: "6gsfsa" },
    { no: 7, type: "QRCODE", content: "7gsfsa" },
    { no: 8, type: "error", content: "" },
    { no: 9, type: "error", content: "" },
    { no: 10, type: "error", content: "" },
    { no: 11, type: "error", content: "" },
    { no: 12, type: "error", content: "" },
    { no: 13, type: "error", content: "" },
    { no: 14, type: "error", content: "" },
    { no: 15, type: "error", content: "" },
    { no: 16, type: "error", content: "" },
    { no: 17, type: "error", content: "" },
  ],
  [
    { no: 0, type: "QRCODE", content: "0gsfsa" },
    { no: 1, type: "CODE", content: "1gsfsa" },
    { no: 2, type: "EN13", content: "2gsfsa" },
    { no: 3, type: "EN8", content: "3gsfsa" },
    { no: 4, type: "QRCODE", content: "4gsfsa" },
    { no: 5, type: "error", content: "" },
  ],
  [
    { no: 0, type: "QRCODE", content: "0gsfsa" },
    { no: 1, type: "CODE", content: "1gsfsa" },
    { no: 2, type: "EN13", content: "2gsfsa" },
    { no: 3, type: "EN8", content: "3gsfsa" },
    { no: 4, type: "QRCODE", content: "4gsfsa" },
    { no: 5, type: "error", content: "" },
    { no: 6, type: "QRCODE", content: "6gsfsa" },
    { no: 7, type: "QRCODE", content: "7gsfsa" },
  ],
  [
    { no: 0, type: "QRCODE", content: "0gsfsa" },
    { no: 1, type: "CODE", content: "1gsfsa" },
    { no: 2, type: "EN13", content: "2gsfsa" },
    { no: 3, type: "EN8", content: "3gsfsa" },
    { no: 4, type: "QRCODE", content: "4gsfsa" },
    { no: 5, type: "error", content: "" },
    { no: 6, type: "QRCODE", content: "6gsfsa" },
    { no: 7, type: "QRCODE", content: "7gsfsa" },
    { no: 8, type: "error", content: "" },
    { no: 9, type: "error", content: "" },
    { no: 10, type: "error", content: "" },
    { no: 11, type: "error", content: "" },
    { no: 12, type: "error", content: "" },
    { no: 13, type: "error", content: "" },
    { no: 14, type: "error", content: "" },
    { no: 15, type: "error", content: "" },
    { no: 16, type: "error", content: "" },
    { no: 17, type: "error", content: "" },
  ],
  [
    { no: 0, type: "QRCODE", content: "0gsfsa" },
    { no: 1, type: "CODE", content: "1gsfsa" },
    { no: 2, type: "EN13", content: "2gsfsa" },
    { no: 3, type: "EN8", content: "3gsfsa" },
    { no: 4, type: "QRCODE", content: "4gsfsa" },
    { no: 5, type: "error", content: "" },
    { no: 6, type: "QRCODE", content: "6gsfsa" },
    { no: 7, type: "QRCODE", content: "7gsfsa" },
  ],
  [
    { no: 0, type: "QRCODE", content: "0gsfsa" },
    { no: 1, type: "CODE", content: "1gsfsa" },
    { no: 2, type: "EN13", content: "2gsfsa" },
    { no: 3, type: "EN8", content: "3gsfsa" },
    { no: 4, type: "QRCODE", content: "4gsfsa" },
    { no: 5, type: "error", content: "" },
    { no: 6, type: "QRCODE", content: "6gsfsa" },
    { no: 7, type: "QRCODE", content: "7gsfsa" },
    { no: 8, type: "error", content: "" },
    { no: 9, type: "error", content: "" },
    { no: 10, type: "error", content: "" },
    { no: 11, type: "error", content: "" },
    { no: 12, type: "error", content: "" },
    { no: 13, type: "error", content: "" },
    { no: 14, type: "error", content: "" },
    { no: 15, type: "error", content: "" },
    { no: 16, type: "error", content: "" },
    { no: 17, type: "error", content: "" },
  ],
];
window.onload = function () {
  console.log("fdfd");
  const server = "http://192.168.1.105:5000"
  const footer = document.querySelector(".footer"),
    year = new Date().getFullYear();
  footer.textContent = `©2021-${year} 上海指象智能科技有限公司 Powered by EIM`;
  // 首次渲染以第一个数据、图片为准
  // 左边图片渲染
  //获取数据
  $.ajax({
            type: "get",
            url: server,
            dataType: "json",
            success: function(data){
                console.log(data);
            }
        });
  for (let i = 1; i < 7; i++) {
    const img = document.createElement("img");
    if (i === 1) {
      img.className = "choose-img";
    }
    img.src = `./image/${i}.png`;
    img.setAttribute("data-no", i);
    img.addEventListener("click", chooseImg);
    left.appendChild(img);
  }
  // 中间图片渲染
  const centerImg = document.createElement("img");
  centerImg.src = `./image/1.png`;
  bigImg.appendChild(centerImg);
  // 表格渲染
  changeTableData(tableData[0]);
};

function chooseImg(e) {
  const no = parseInt(e.target.getAttribute("data-no"));
  const imgs = left.querySelectorAll("img");
  // 更换缩略图选中效果
  imgs.forEach((img) => {
    img.className = "";
  });
  imgs[no - 1].className = "choose-img";
  // 更换图片
  changeCenterImg(`./image/${no}.png`);
  // 更新表格数据
  changeTableData(tableData[no - 1]);
}

// 更换中间图片，参数为图片地址
function changeCenterImg(src) {
  const img = center.querySelector("div").querySelector("img");
  img.src = src;
}

// 渲染表格数据，参数为数据数组
function changeTableData(arr) {
  table.innerHTML = "";
  // 表头
  arr.forEach((item) => {
    const tr = document.createElement("tr");
    for (let i in item) {
      let td = document.createElement("td");
      if (i === "type" && item.type === "error") {
        td.style.color = "red";
      }
      td.textContent = item[i];
      tr.appendChild(td);
    }
    table.appendChild(tr);
  });
}

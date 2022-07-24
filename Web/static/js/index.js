// 获取输入的权柄
let input = document.querySelector(".first");
// 获取运行的权柄
let run = document.querySelector("button");
// 获取输出的权柄
let output = document.querySelector(".second");

// 定义函数
function func() {
    let num = 3.1415926;
    console.log(num.toFixed(5));
}

// 将函数暴露出去
export {
    func,
}

let main = function() {
    // 获取权柄
    let $div = $('div');
    $div.on("click", () => {
        // 将属性age的值由18改20
        $div.attr('age', 20);
        console.log($div.attr('age'));
    });
};

export {
    main,
}

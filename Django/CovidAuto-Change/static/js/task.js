// function popWindow(e) {
//     var targ = e.target;
//     console.log(targ);
// }

function popWindow(obj) {
    // ele1:task标号
    // ele2:task标题
    // ele3:task省份
    // ele4:task城市
    // ele5:task是否启用
    var ele1 = obj.childNodes[1].childNodes[0].innerHTML;
    var ele2 = obj.childNodes[1].innerHTML.split(':')[1];
    var ele3 = obj.childNodes[3].childNodes[1].innerHTML.split(':')[1];
    var ele4 = obj.childNodes[3].childNodes[3].innerHTML.split(':')[1];
    var ele5 = obj.childNodes[3].childNodes[5].innerHTML.split(':')[1];
    var ele6 = obj.childNodes[3].childNodes[9].innerHTML.split(':')[1];
    console.log(ele1, ele2, ele3, ele4, ele5, ele6);
    var window = document.getElementById('window-background');
    window.style.display = 'block';
    console.log(window);
    // 设置弹窗内的input中的value
    var pop_window_title = document.getElementsByClassName('pop-window-title')[0];
    var pop_window_province = document.getElementsByClassName('pop-window-province')[0];
    var pop_window_city = document.getElementsByClassName('pop-window-city')[0];
    var pop_window_coordinate = document.getElementsByClassName('pop-window-coordinate')[0];

    var checkbox_input = document.getElementsByClassName('pop-window-on-or-off')[0];

    pop_window_title.setAttribute('value', ele2);
    pop_window_province.setAttribute('value', ele3);
    pop_window_city.setAttribute('value', ele4);
    pop_window_coordinate.setAttribute('value', ele6);
    // 判断checkbox是否勾选
    if(ele5 == 'True') {
        checkbox_input.checked = true;
    }
    else if(ele5 == 'False') {
        checkbox_input.checked = false;
    }

    var task_id = document.getElementsByClassName('task-id')[0];
    // console.log(task_id.getAttribute('value'));
    task_id.setAttribute('value', ele1);
    
    // var close_window = getElementsByClassName('close-window')[0];
}

function closeWindow() {
    var window = document.getElementById('window-background');
    window.style.display = 'none';
}

function createWindow() {
    var window = document.getElementById('window-background');
    window.style.display = 'block';
    // 去掉删除task
    var delete_btn = document.getElementsByClassName('pop-window-delete')[0];
    delete_btn.remove();
    // 更改表单提交action
    var submit_btn = document.getElementsByClassName('pop-window-submit')[0];
    submit_btn.setAttribute('formaction', "create_tasks/");
}
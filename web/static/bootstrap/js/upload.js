$(document).ready(function () {

    $("#btnSubmit").click(function (event) {
        event.preventDefault();
        upload_keywords();

    });

});

function upload_keywords() {
    // Get form
    var form = $('#uploadKeywords')[0];
    var data = new FormData(form);
    console.log(data.get("key"));
    console.log(data.get("words_group"));

    $.ajax({
        type: "POST",
        enctype: 'multipart/form-data',
        url: "/import_keywords",
        data: data,
        processData: false,
        contentType: false,
        cache: false,
        timeout: 600000,
        success: function (data) {
            console.log("SUCCESS : ", data);

            if (data.status == true) {
                bootbox.alert(data.msg);
                console.log("info", "关键词上传成功");
                $('#key').val("");
                $('#words_group').val("");

            } else if (data.status == false) {
                bootbox.alert(data.msg);
                console.log("error", "导入数据失败");
            }

        },
        error: function (e) {
            bootbox.alert("错误");
            console.log("ERROR : ", e.responseText);
        }
    });
}

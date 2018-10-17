var dataController = {}
dataController.delete = function (dataId) {
    var form = new FormData();
    form.append("id",dataId);
    $.ajax({
        type: "POST",
        enctype: 'multipart/form-data',
        url: "/delete",
        data: form,
        processData: false,
        contentType: false,
        cache: false,
        timeout: 60000,
        success: function (data) {
            console.log("SUCCESS : ", data);
            if (data.status == true) {
                //$("#delcfmOverhaul").modal("hide");
                bootbox.alert("数据删除成功",function () {
                    window.location.reload();
                });
            } else if (data.status == false) {
                bootbox.alert("数据删除失败");
            }
        },
        error: function (e) {
            bootbox.alert("错误");
            console.log("ERROR : ", e.responseText);
        }
    });
}

dataController.confirm_delete = function (id) {
    bootbox.confirm({
        title: "提示",
        message: "是否确定删除该条信息？",
        buttons: {
            cancel: {
                label: '<i class="fa fa-times"></i> 取消'
            },
            confirm: {
                label: '<i class="fa fa-check"></i> 确定'
            }
        },
        callback: function (result) {
            if (result){
                dataController.delete(id)
            }
        }

    });
}

dataController.updateKeywords = function (obj) {
    var id = obj["id"];
    var keyword = obj["keyword"];
    var group = obj["group"];
    $("#update_id").val(id);
    $("#update_key").val(keyword);
    $("#update_words_group").val(group.join("\r\n\r\n"));
    $("#updateModal").modal();
}

dataController.submitChange = function () {
    var form = new FormData();
    var id = $("#update_id").val();
    var keyword = $("#update_key").val();
    var group = $("#update_words_group").val();
    form.append("id", id);
    form.append("keyword", keyword);
    form.append("group", group);
    $.ajax({
        type: "POST",
        enctype: 'multipart/form-data',
        url: "/update",
        data: form,
        processData: false,
        contentType: false,
        cache: false,
        timeout: 60000,
        success: function (data) {
            $("#updateModal").modal();
            console.log("SUCCESS : ", data);
            if (data.status == true) {
                bootbox.alert("数据更新成功",function () {
                    window.location.reload();
                });
            } else if (data.status == false) {
                bootbox.alert("数据更新失败");
            }
        },
        error: function (e) {
            $("#updateModal").modal();
            bootbox.alert("错误");
            console.log("ERROR : ", e.responseText);
        }
    });

}

getResponse = function (url, method, data) {
    $.ajax({
        type: method,
        enctype: 'multipart/form-data',
        url: url,
        data: data,
        processData: false,
        contentType: false,
        cache: false,
        timeout: 60000,
        success: function (data) {
            console.log("SUCCESS : ", data);
            return data;
        },
        error: function (e) {
            alert("错误");
            console.log("ERROR : ", e.responseText);
        }
    });
}

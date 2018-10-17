<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>新闻采集平台数据导入</title>
    <link href="static/bootstrap/css/bootstrap.css" rel="stylesheet">
    <link href="static/bootstrap/css/bootstrap-theme.css" rel="stylesheet">
    <link href="static/assets/css/ie10-viewport-bug-workaround.css" rel="stylesheet">
    <link href="static/assets/css/grid.css" rel="stylesheet">
    <script src="static/assets/js/ie-emulation-modes-warning.js"></script>
    <script src="static/bootstrap/js/jquery-2.1.1.js"></script>
    <script src="static/bootstrap/js/bootstrap.js"></script>
    <script src="static/bootstrap/js/bootbox.min.js"></script>


    <link href="../static/bootstrap/css/bootstrap.css" rel="stylesheet">
    <link href="../static/bootstrap/css/bootstrap-theme.css" rel="stylesheet">
    <link href="../static/assets/css/ie10-viewport-bug-workaround.css" rel="stylesheet">
    <link href="../static/assets/css/grid.css" rel="stylesheet">
    <script src="../static/assets/js/ie-emulation-modes-warning.js"></script>
    <script src="../static/bootstrap/js/jquery-2.1.1.js"></script>
    <script src="../static/bootstrap/js/bootstrap.js"></script>
    <script src="../static/bootstrap/js/bootbox.min.js"></script>
</head>
<body>
<!-- 信息修改 -->
<div class="modal fade" id="updateModal">
    <div class="modal-dialog">
        <div class="modal-content message_align">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span
                        aria-hidden="true">×</span></button>
                <h4 class="modal-title">修改数据</h4>
            </div>
            <div class="modal-body">
                <form id="uploadKeywords">
                    <div class="form-group">
                        <input type="hidden" id="update_id" />
                        <label for="update_key" class="col">代表词</label>
                        <input type="text" class="form-control" name="key" id="update_key"/>
                    </div>
                    <div class="form-group">
                        <label for="update_words_group">关键词组</label>
                        <textarea class="form-control" rows="3" name="words_group" id="update_words_group"></textarea>
                    </div>
                </form>
            </div>
            <div class="modal-footer">
                <input type="hidden" id="url"/>
                <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
                <a onclick="dataController.submitChange()" class="btn btn-success">确定</a>
            </div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div><!-- /.modal -->
<div class="container-fluid">

    <div class="page-header">
        <h1>数据查看</h1>
        <p class="lead">数据查看</p>
    </div>

    <table class="table">
        <thead>
        <tr>
            <th class="col-sm-1">ID</th>
            <th class="col-sm-2">代表词</th>
            <th class="col-sm-7">关键词组</th>
            <th class="col-sm-2">操作</th>
        </tr>
        </thead>
        <tbody>
        %for item in data:
        <tr>
            <th scope="row" class="col-sm-1">{{item["id"]}}</th>
            <td class="col-sm-2">{{item["keyword"]}}</td>
            <td class="col-sm-7">
                %for line in item["group"]:
                    <p><span class="glyphicon glyphicon-chevron-left"></span>{{line}}<span class="glyphicon glyphicon-chevron-right"></span></p>
                %end
            </td>
            <td class="col-sm-2">
                <a href="#" onclick='dataController.updateKeywords({{item}})'><span class="glyphicon glyphicon-pencil"></span>修改数据</a>&nbsp;
                <a href="#" onclick='dataController.confirm_delete({{item["id"]}})'><span class="glyphicon glyphicon-remove"></span>删除数据</a>
                <!--<a href="#" onclick="showDeleteModal({{item["id"]}})"><span class="glyphicon glyphicon-remove"></span>删除数据</a>-->
            </td>
        </tr>
        %end
        </tbody>
    </table>

</div> <!-- /container -->
<script src="../static/bootstrap/js/data.js"></script>
<script src="/static/bootstrap/js/data.js"></script>
</body>
</html>
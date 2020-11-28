<html>

<head>
    <meta charset="UTF-8" />
    <title>專案修改</title>
    <script src="jquery-3.4.1.min.js"></script>
    <script src="bootstrap.min.js"></script>
    
</head>
<script>
        $(function () {
            $(".face_add").click(function () {
                if ($(".face_div").children().length == 10) {
                    alert("超過上限");
                } else {
                    $.ajax({
                        url: 'aaa.html',
                        type: 'get',
                        success: function (data){
                            $(".face_div").append(data);
                        }
                    })
                }
            })
        })
        
</script>
<body>
    <p>
        <h1>
            <center><b>專案修改</b></center>
        </h1>
    </p>
    <?php
    include("db_connect.php");
    $id = $_GET["id"];
    $res = sql_query("SELECT * FROM `project` WHERE `id` = $id")[0];
    $direction = sql_query("SELECT * FROM `direction` WHERE `direction_id` = $id");
    ?>
    <form action="db_project_update.php" method="post" name="form1">

        <center>
            <h1>
                <p>
                    <input type="button" value="回到專案管理" onclick="location.href='project.php'">
                </p>
                <p>
                    專案名稱:<input type="text" name="name" value="<?= $res["name"] ?>"><br>
                    專案說明:<input type="text" name="description" value="<?= $res["description"] ?>"><br>
                    <input type="hidden" name="id" value="<?= $res["id"] ?>">
                    <p><input type="button" class="btn face_add" value="新增面向"></p>
                    
                    <div class="face_div">
                        <?php
                        foreach($direction as $d){
                        ?>
                        <p>
                            面向名稱：<input type="text" value="<?=$d['name']?>" name="direction_name[]" required>
                            面向說明：<input type="text" value="<?=$d['description']?>" name="direction_description[]" required>
                            <input type="hidden" value="<?=$d['id']?>" name="direction_id[]">
                            <input type="button" class="btn btn-danger" value="X" data-dismiss="alert">
                        </p>
                        <?php
                        }
                        ?>
                    </div>
                    <input type="submit" value="修改資料"><input type="reset" value="重新輸入">
                </p>
                <h1>
        </center>

    </form>
</body>

</html>
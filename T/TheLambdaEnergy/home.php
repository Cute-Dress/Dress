<?php
include_once('mysql.php');



session_start();
if (isset($_SESSION['id']) && !empty($_SESSION['id'])) {
    // session 值不为空
    session_start();
    $id=$_SESSION['id'];


// 执行查询
    $sql = "SELECT * FROM user_root WHERE id = $id";
    $result = $mysqli->query($sql);
    $email='不存在';




// 检查查询结果
    if ($result->num_rows > 0) {
        // 登录成功，将用户重定向到另一个页面
        $row = $result->fetch_assoc();
        $name=$row['name'];
        $phone=$row['phone'];
        $wechat=$row['wechat'];
        $email=$row['email'];
        session_start();
        $_SESSION['teacher']=$name;
        //读取html文件
        $html = file_get_contents('home.html');
        //替换占位符
        $html = str_replace("{name}",$name,$html);
        $html = str_replace("{email}",$email,$html);
        $html = str_replace("{wechat}",$wechat,$html);
        $html = str_replace("{phone}",$phone,$html);

        //显示html
        echo $html;


    } else {
        // 登录失败，显示错误消息
        echo "Invalid username or password";
        header("Location: loginerror.html");
        $mysqli->close();

    }

} else {
    // session 值为空
    header("Location: loginerror.html");
}
// 获取表单提交数据

// 关闭数据库连接
$mysqli->close();


?>
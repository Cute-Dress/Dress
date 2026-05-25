<?php
include_once('mysql.php');

// 获取表单提交数据
$username = $_POST['username'];
$password = $_POST['password'];

// 执行查询
$sql = "SELECT id FROM user_root WHERE username = '$username' AND password = '$password'";
$result = $mysqli->query($sql);

// 检查查询结果
if ($result->num_rows > 0) {
    // 登录成功，将用户重定向到另一个页面
    $row = $result->fetch_assoc();
    $id = $row['id'];

    // 保存POST数据到$_SESSION中
    session_start();
    $_SESSION['id'] = $id;

    // 重定向到下一页
    header("Location: home.php");

} else {
    // 登录失败，显示错误消息
    echo "Invalid username or password";
    header("Location: loginerror.html");
}

// 关闭数据库连接
$mysqli->close();
?>
<?php
// 定义 MySQL 服务器信息
$mysqlserveraddress = '[CENSORED]';  // 服务器地址
$mysqlusername = 'root';  // 服务器登录用户名
$mysqlpassword = '[CENSORED]';  // 服务器登录密码
$mysqldatabase = 'EXAMPLE';  // 数据库名称
$mysqlport = '3306';  // 服务器端口号

// 连接数据库
$mysqli = new mysqli($mysqlserveraddress, $mysqlusername, $mysqlpassword, $mysqldatabase, $mysqlport);
// 检查连接状态
if ($mysqli->connect_error) {
    die("Connection failed: " . $mysqli->connect_error);
    echo '数据库连接失败';
}
?>
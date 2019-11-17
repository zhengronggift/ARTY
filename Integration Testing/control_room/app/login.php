<?php
include('connect.php'); 
$test=$_POST['username'];
$test1=$_POST['password'];
if($test == "" || $test1 == "")
{
echo "Username and password cannot be empty";
}
if(ctype_alnum($test)){ 
//echo "<br>username accept";
//check to see if username in use
$query="SELECT `uname`, `password` FROM `rzheng`.`user` WHERE `uname` = '$test'";
$result=mysqli_query($conn, $query);
$num=mysqli_num_rows($result);
if ($num != 0)
{
$row = $result->fetch_assoc();
if ($row["password"] == $test1)
{
echo "You are connected";
}
else
{
echo "Sorry, password not correct.";
echo "<br><a href=https://lamp.cse.fau.edu/~rzheng/login.php>Go Back</a>";
echo "<br><a href=https://lamp.cse.fau.edu/~rzheng/test.php>Register</a>";
//echo "<br><a href=https://lamp.cse.fau.edu/~rzheng/.php>Change Password</a>";
}
}
else
{
echo "No user found";
echo "<br><a href=https://lamp.cse.fau.edu/~rzheng/login.php>Go Back</a>";
echo "<br><a href=https://lamp.cse.fau.edu/~rzheng/test.php>Register</a>";
}
}
?>

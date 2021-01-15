<?php 
  // Headers
  header('Access-Control-Allow-Origin: *');
  header('Content-Type: application/json');

  include_once '../../config/Database.php';
  include_once '../../models/User.php';

  // Instantiate DB & connect
  $database = new Database();
  $db = $database->connect();

  // Instantiate user object
  $user = new User($db);

  // Get ID
  $user->username = isset($_GET['username']) ? $_GET['username'] : die();

  // Get post
  $user->read_single();

  // Create array
  $user_arr = array(
    'id' => $user->id,
    'username' => $user->username,
    'password' => $user->password
  );

  // Make JSON
  print_r(json_encode($user_arr));
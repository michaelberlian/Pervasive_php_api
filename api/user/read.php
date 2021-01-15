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

  // user query
  $result = $user->read();
  // Get row count
  $num = $result->rowCount();

  // Check if any posts
  if($num > 0) {
    // Post array
    $users_arr = array();
    // $users_arr['data'] = array();

    while($row = $result->fetch(PDO::FETCH_ASSOC)) {
      extract($row);

      $post_item = array(
        'username' => $username
      );

      // Push to "data"
      array_push($users_arr, $post_item);
      // array_push($users_arr['data'], $post_item);
    }

    // Turn to JSON & output
    echo json_encode($users_arr);

  } else {
    // No Posts
    echo json_encode(
      array('message' => 'No Users Found')
    );
  }
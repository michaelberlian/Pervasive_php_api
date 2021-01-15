<?php 
  // Headers
  header('Access-Control-Allow-Origin: *');
  header('Content-Type: application/json');

  include_once '../../config/Database.php';
  include_once '../../models/Setting.php';

  // Instantiate DB & connect
  $database = new Database();
  $db = $database->connect();

  // Instantiate setting object
  $setting = new Setting($db);

  // settings query
  $result = $setting->read();
  // Get row count
  $num = $result->rowCount();

  // Check if any settingss
  if($num > 0) {
    // settings array
    $settings_arr = array();
    // $settings_arr['data'] = array();

    while($row = $result->fetch(PDO::FETCH_ASSOC)) {
      extract($row);

      $settings_item = array(
        'id' => $id,
        'brightness' => $brightness,
        'switch' => $switch
      );

      // Push to "data"
      array_push($settings_arr, $settings_item);
      // array_push($settings_arr['data'], $settings_item);
    }

    // Turn to JSON & output
    echo json_encode($settings_arr);

  } else {
    // No settingss
    echo json_encode(
      array('message' => 'No Users Found')
    );
  }
<?php 
  // Headers
  header('Access-Control-Allow-Origin: *');
  header('Content-Type: application/json');
  header('Access-Control-Allow-Methods: PUT');
  header('Access-Control-Allow-Headers: Access-Control-Allow-Headers,Content-Type,Access-Control-Allow-Methods, Authorization, X-Requested-With');

  include_once '../../config/Database.php';
  include_once '../../models/Setting.php';

  // Instantiate DB & connect
  $database = new Database();
  $db = $database->connect();

  // Instantiate setting object
  $setting = new Setting($db);

  // Get raw setting data
  $data = json_decode(file_get_contents("php://input"));

  // Set ID to update
  $setting->id = $data->id;

  $setting->brightness = $data->brightness;
  $setting->function = $data->function;

  // Update setting
  if($setting->update()) {
    echo json_encode(
      array('message' => 'setting Updated')
    );
  } else {
    echo json_encode(
      array('message' => 'setting Not Updated')
    );
  }
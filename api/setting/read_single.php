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

  // Get ID
  $setting->id = isset($_GET['id']) ? $_GET['id'] : die();

  // Get setting
  $setting->read_single();

  // Create array
  $setting_arr = array(
    'id' => $setting->id,
    'switch' => $setting->switch,
    'function' => $setting->function
  );

  // Make JSON
  print_r(json_encode($setting_arr));
<?php 
    // Headers
    header('Access-Control-Allow-Origin: *');
    header('Content-Type: application/json');
    header('Access-Control-Allow-Methods: POST');
    header('Access-Control-Allow-Headers: Access-Control-Allow-Headers,Content-Type,Access-Control-Allow-Methods, Authorization, X-Requested-With');

    include_once '../../config/Database.php';
    include_once '../../models/Setting.php';

    // Instantiate DB & connect
    $database = new Database();
    $db = $database->connect();

    // Instantiate setting object
    $setting = new Setting($db);

    // Get raw posted data
    $data = json_decode(file_get_contents("php://input"));

    $setting->brightness = $data->brightness;
    $setting->function = $data->function;

    // Create post
    if($setting->create()) {
        echo json_encode(
        array('message' => 'setting Created')
        );
    } else {
        echo json_encode(
        array('message' => 'setting Not Created')
        );
}
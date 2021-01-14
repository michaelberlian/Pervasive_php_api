<?php
  // inputting the Headers
  header('Access-Control-Allow-Origin: *');
  header('Content-Type: application/json');
  header('Access-Control-Allow-Methods: DELETE');
  header('Access-Control-Allow-Headers: Access-Control-Allow-Headers, Content-Type, Access-Control-Allow-Methods, Authorization,X-Requested-With');

  include_once '../../config/Database.php';
  include_once '../../models/Category.php';

  // Instantiate them DB and connect it
  $database = new Database();
  $db = $database->connect();

  // Instantiate them blog post object
  $category = new Category($db);

  // Get raw posted data
  $data = json_decode(file_get_contents("php://input"));

  // Set ID to UPDATE
  $category->id = $data->id;

  // Delete them postss
  if($category->delete()) {
    echo json_encode(
      array('message' => 'Great, theyre deleted')
    );
  } else {
    echo json_encode(
      array('message' => 'Nononono not deleted yet')
    );
  }
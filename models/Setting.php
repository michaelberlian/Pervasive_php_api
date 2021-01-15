<?php 
  class Setting{
    // DB stuff
    private $conn;
    private $table = 'settings';

    // Post Properties
    public $id;
    public $brightness;
    public $switch;
    public $created_at;

    // Constructor with DB
    public function __construct($db) {
      $this->conn = $db;
    }

    // Get Posts
    public function read() {
      // Create query
      $query = 'SELECT * FROM ' . $this->table;
      
      // Prepare statement
      $stmt = $this->conn->prepare($query);

      // Execute query
      $stmt->execute();

      return $stmt;
    }

    // Get Single Post
    public function read_single() {
          // Create query
          $query = 'SELECT * FROM ' . $this->table . ' WHERE id =?';

          // Prepare statement
          $stmt = $this->conn->prepare($query);

          // Bind ID
          $stmt->bindParam(1, $this->id);

          // Execute query
          $stmt->execute();

          $row = $stmt->fetch(PDO::FETCH_ASSOC);

          // Set properties
          $this->id = $row['id'];
          $this->brightness = $row['brightness'];
          $this->switch = $row['switch'];
    }

    // Create Post
    public function create() {
          // Create query
          $query = 'INSERT INTO ' . $this->table . ' SET brightness = :brightness, switch = :switch';

          // Prepare statement
          $stmt = $this->conn->prepare($query);
      
          // Clean data
          $this->brightness = htmlspecialchars(strip_tags($this->brightness));
          $this->switch = htmlspecialchars(strip_tags($this->switch));

          // Bind data
          $stmt->bindParam(':brightness', $this->brightness);
          $stmt->bindParam(':switch', $this->switch);

          // Execute query
          if($stmt->execute()) {
            return true;
      }

      // Print error if something goes wrong
      printf("Error: %s.\n", $stmt->error);

      return false;
    }

    // Update Post
    public function update() {
          // Create query
          $query = 'UPDATE ' . $this->table . '
                                SET brightness = :brightness, switch = :switch
                                WHERE id =:id';

          // Prepare statement
          $stmt = $this->conn->prepare($query);

          // Clean data
          $this->brightness = htmlspecialchars(strip_tags($this->brightness));
          $this->switch = htmlspecialchars(strip_tags($this->switch));
          $this->id = htmlspecialchars(strip_tags($this->id));

          // Bind data
          $stmt->bindParam(':brightness', $this->brightness);
          $stmt->bindParam(':switch', $this->switch);
          $stmt->bindParam(':id', $this->id);

          // Execute query
          if($stmt->execute()) {
            return true;
          }

          // Print error if something goes wrong
          printf("Error: %s.\n", $stmt->error);

          return false;
    }

    // Delete Post
    public function delete() {
          // Create query
          $query = 'DELETE FROM ' . $this->table . ' WHERE id = :id';

          // Prepare statement
          $stmt = $this->conn->prepare($query);

          // Clean data
          $this->id = htmlspecialchars(strip_tags($this->id));

          // Bind data
          $stmt->bindParam(':id', $this->id);

          // Execute query
          if($stmt->execute()) {
            return true;
          }

          // Print error if something goes wrong
          printf("Error: %s.\n", $stmt->error);

          return false;
    }
    
  }
<?php
    class Database {
        // params
        private $host = 'localhost';
        private $db_name = 'myblog';
        private $username = 'root';
        private $password = '';
        private $conn;

        // DB connect
        public function connect(){
            $this->conn = null; 

            try{

            } catch (PDOException $e){
                echo 'Connection Error: ' . $e->getMessage();
            }
        }
    }
?>
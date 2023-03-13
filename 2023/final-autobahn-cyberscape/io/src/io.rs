use std::path::Path;

use crate::{utils, constant};

pub struct Storage {
    dir: String,
}

impl Storage {
    pub fn new(dir: String) -> Storage {
        Storage { dir }
    }

    pub fn list(&self) -> Vec<String> {
        let path = Path::new(&self.dir);
        utils::entries(path)
    }

    pub fn users(&self) -> Vec<String> {
        let path = Path::new(&self.dir);
        let parent = path.parent().unwrap();
        utils::entries(parent)
    }

    pub fn get(&self, key: &str) -> String {
        if !utils::is_valid_key(key) { return constant::ERROR.to_string() }
        let path = Path::new(&self.dir);
        let path = path.join(key);
        if !path.exists() { return constant::ERROR.to_string() }
        utils::read_file(path.as_path())
    }

    pub fn set(&self, key: &str, value: &str) -> String {
        if !utils::is_valid_key(key) { return constant::ERROR.to_string() }
        let path = Path::new(&self.dir);
        let path = path.join(key);
        utils::create_file(path.as_path(), value);
        constant::OK.to_string()
    }
}
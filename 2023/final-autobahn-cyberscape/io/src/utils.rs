use std::io::Write;
use std::path::Path;
use uuid::Uuid;
use std::fs::File;
use std::fs;
use crate::constant;

pub fn create_file(path: &Path, value: &str) {
    let mut file = File::create(path).unwrap();
    file.write_all(value.as_bytes()).unwrap();
}

pub fn read_file(path: &Path) -> String {
    let content = fs::read_to_string(path).unwrap();
    content
}


pub fn create_dir(path: &Path) {
    fs::create_dir(path).unwrap();
}

pub fn dir_exist(dir: &str) -> bool {
    let path = Path::new(dir);
    path.exists() && path.is_dir()
}

pub fn is_valid_key(key: &str) -> bool {
    let key = key.trim();
    if key.len() == 0 {
        return false;
    }
    
    for c in constant::INVALID_CHARS.chars() {
        if key.contains(c) {
            return false;
        }
    }
    
    true
}

pub fn generate_token() -> String {
    let uuid = Uuid::new_v4();
    uuid.to_string()
}

pub fn entries(path: &Path) -> Vec<String> {
    let mut result = Vec::new();
    if path.exists() && path.is_dir() {
            let entries = fs::read_dir(path).unwrap();
            for entry in entries {
                let entry = entry.unwrap();
                let path = entry.path();
                result.push(
                    path.into_iter()
                    .last()
                    .unwrap()
                    .to_str()
                    .unwrap()
                    .to_string());
            }
        }
    result
}

pub fn init() {
    if !dir_exist(constant::STORAGE_PATH) {
        create_dir(Path::new(constant::STORAGE_PATH));
    }
    if !dir_exist(constant::TOKEN_PATH) {
        create_dir(Path::new(constant::TOKEN_PATH));
    }
}
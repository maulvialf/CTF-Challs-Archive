use crate::{utils, constant};

use std::path::Path;


pub fn register(username: &str) -> String {
    if !utils::is_valid_key(username) { return constant::ERROR.to_string() }
    let workdir = constant::STORAGE_PATH.to_string() + username;
    if utils::dir_exist(workdir.as_str()) { return constant::ERROR.to_string() }
    
    let token = utils::generate_token();
    let user_token = constant::TOKEN_PATH.to_string() + token.as_str();
    
    utils::create_dir(Path::new(workdir.as_str()));
    utils::create_file(Path::new(user_token.as_str()), &workdir);
    
    token
}

pub fn get_workdir(token: &str) -> String {
    let user_token = constant::TOKEN_PATH.to_string() + token;
    let path = Path::new(user_token.as_str());
    
    if !path.exists() { return constant::ERROR.to_string() }
    let workdir = utils::read_file(path);

    workdir
}


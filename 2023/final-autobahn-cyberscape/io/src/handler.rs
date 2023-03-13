use std::vec;

use serde::{Deserialize, Serialize};
use actix_web::{get, post, delete, web, Responder, HttpRequest};
use crate::{constant, service, io};

#[derive(Deserialize, Serialize)]
pub struct Register {
    username: String,
}

#[derive(Deserialize, Serialize)]
pub struct Data {
    data: String,
}

#[derive(Deserialize, Serialize)]
pub struct Response {
    message: String,
    data: Vec<String>,
}

pub fn get_auth_header(req: &actix_web::HttpRequest) -> Option<String> {
    let auth_header = req.headers().get("X-IO-Auth-Token");
    if auth_header.is_none() { return None }
    let auth_header = auth_header.unwrap().to_str().unwrap();
    let auth_header = auth_header.trim();
    if auth_header.len() == 0 { return None }
    let auth_header = auth_header.to_string();
    Some(auth_header)
}

#[get("/")]
pub async fn index() -> impl Responder {
    web::Json(Response { message: constant::OK.to_string(), data: vec![] })
}

#[post("/register")]
pub async fn register(form: web::Json<Register>) -> impl Responder {
    let message = service::register(form.username.as_str());
    web::Json(Response { message, data: vec![] })
}

#[get("/users")]
pub async fn users(req: HttpRequest) -> impl Responder {
    let auth_header = match get_auth_header(&req) {
        Some(auth_header) => auth_header,
        None => return web::Json(Response { message: constant::ERROR.to_string(), data: vec![] }),
    };

    let workdir = service::get_workdir(auth_header.as_str());
    if workdir == constant::ERROR { return web::Json(Response { message: constant::ERROR.to_string(), data: vec![] }) }

    let storage = io::Storage::new(workdir);
    let data = storage.users();
    web::Json(Response { message: constant::OK.to_string(), data })
}

#[get("/storage")]
pub async fn list(req: HttpRequest) -> impl Responder {
    let auth_header = match get_auth_header(&req) {
        Some(auth_header) => auth_header,
        None => return web::Json(Response { message: constant::ERROR.to_string(), data: vec![] }),
    };

    let workdir = service::get_workdir(auth_header.as_str());
    if workdir == constant::ERROR { return web::Json(Response { message: constant::ERROR.to_string(), data: vec![] }) }

    let storage = io::Storage::new(workdir);
    let data = storage.list();
    web::Json(Response { message: constant::OK.to_string(), data })

}

#[get("/storage/{key}")]
pub async fn get(req: HttpRequest, key: web::Path<String>) -> impl Responder {
    let auth_header = match get_auth_header(&req) {
        Some(auth_header) => auth_header,
        None => return web::Json(Response { message: constant::ERROR.to_string(), data: vec![] }),
    };

    let workdir = service::get_workdir(auth_header.as_str());
    if workdir == constant::ERROR { return web::Json(Response { message: constant::ERROR.to_string(), data: vec![] }) }

    let storage = io::Storage::new(workdir);
    let data = vec![storage.get(key.as_str())];
    web::Json(Response { message: constant::OK.to_string(), data })
}

#[post("/storage/{key}")]
pub async fn set(req: HttpRequest, key: web::Path<String>, form: web::Json<Data>) -> impl Responder {
    let auth_header = match get_auth_header(&req) {
        Some(auth_header) => auth_header,
        None => return web::Json(Response { message: constant::ERROR.to_string(), data: vec![] }),
    };

    let workdir = service::get_workdir(auth_header.as_str());
    if workdir == constant::ERROR { return web::Json(Response { message: constant::ERROR.to_string(), data: vec![] }) }

    let storage = io::Storage::new(workdir);
    let message = storage.set(key.as_str(), form.data.as_str());
    web::Json(Response { message, data: vec![] })
}
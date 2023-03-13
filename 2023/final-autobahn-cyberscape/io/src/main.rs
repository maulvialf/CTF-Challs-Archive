use actix_web::{App, HttpServer};


mod constant;
mod handler;
mod io;
mod service;
mod utils;


#[actix_web::main]
async fn main() -> std::io::Result<()> {
    utils::init();
    HttpServer::new(|| {
        App::new()
            .service(handler::index)
            .service(handler::register)
            .service(handler::users)
            .service(handler::get)
            .service(handler::set)
            .service(handler::list)
    })
    .bind(("0.0.0.0", 8000))?
    .run()
    .await
}


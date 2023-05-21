package routes

import (
	. "gone-wrong/users/controllers"
	. "gone-wrong/users/repository"

	. "gone-wrong/utils/session"

	"github.com/gofiber/fiber/v2"
	"gorm.io/gorm"
)

func RegisterRoutes(app *fiber.App, db *gorm.DB) {
	userRepo := NewUserRepo(db)
	handler := NewBaseHandler(userRepo)
	userRepo.UpdateAdminUser()
	routes := app.Group("/user")

	routes.Post("/login", handler.LoginCheck)
	routes.Post("/register", handler.AddUser)

	routes.Get("/flag", AdminAuthorizationCheck, handler.GetFlag)
}

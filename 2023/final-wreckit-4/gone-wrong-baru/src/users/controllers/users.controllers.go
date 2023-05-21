package controllers

import (
	"bytes"
	"encoding/json"
	"errors"
	. "gone-wrong/users/models"
	session "gone-wrong/utils/session"

	"github.com/gofiber/fiber/v2"
)

type BaseHandler struct {
	userRepo UserRepository
}

func NewBaseHandler(userRepo UserRepository) *BaseHandler {
	return &BaseHandler{
		userRepo: userRepo,
	}
}

func validateBody(c *fiber.Ctx) error {
	dst := make(map[string]string)
	dec := json.NewDecoder(bytes.NewReader(c.Body()))
	dec.DisallowUnknownFields()

	err := dec.Decode(&dst)
	if err != nil {
		return err
	}

	email, ok := dst["email"]
	if ok && len(email) == 0 {
		return errors.New("Email cannot be empty")
	}

	pwd, ok := dst["password"]
	if ok && len(pwd) == 0 {
		return errors.New("Password cannot be empty")
	}

	return nil
}

func (h *BaseHandler) LoginCheck(c *fiber.Ctx) error {
	if err := validateBody(c); err != nil {
		return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{
			"error": true,
			"msg":   err.Error(),
		})
	}

	user := &LoginUser{}

	if err := c.BodyParser(user); err != nil {
		return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{
			"error": true,
			"msg":   err.Error(),
		})
	}

	userData, err := h.userRepo.LoginCheck(user.Email, user.Password)
	if err != nil {
		return c.Status(fiber.StatusForbidden).JSON(fiber.Map{
			"error": true,
			"msg":   err.Error(),
		})
	}

	token, exp, err := session.GenerateToken(userData.ID, userData.Name, userData.IsAdmin)
	if err != nil {
		return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{
			"error": true,
			"msg":   err.Error(),
		})
	}
	return c.Status(fiber.StatusOK).JSON(fiber.Map{
		"success": true,
		"data":    map[string]interface{}{"token": token, "exp": exp},
	})
}

func (h *BaseHandler) AddUser(c *fiber.Ctx) error {
	user := &User{}

	if err := c.BodyParser(user); err != nil {
		return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{
			"error": true,
			"msg":   err.Error(),
		})
	}

	user.IsAdmin = false

	err := h.userRepo.AddUser(user)
	if err != nil {
		return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{
			"error": true,
			"msg":   err.Error(),
		})
	}

	user.Password = ""

	return c.Status(fiber.StatusCreated).JSON(fiber.Map{
		"success": true,
		"data":    user,
	})
}

func (h *BaseHandler) GetFlag(c *fiber.Ctx) error {
	return c.SendFile("/flag.txt")
}

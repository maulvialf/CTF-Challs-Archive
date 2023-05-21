package models

import (
	"gorm.io/gorm"
)

type LoginUser struct {
	Email    string `json:"email,omitempty" gorm:"type:varchar(255);unique;index;not null;default:null"`
	Password string `json:"password,omitempty" gorm:"type:varchar(255);not null;default:null"`
}

type User struct {
	gorm.Model `json:"-"`
	ID         int    `json:"id" gorm:"primary_key"`
	Name       string `json:"name,omitempty" gorm:"type:varchar(255);unique;index;not null;default:null"`
	LoginUser
	IsAdmin bool `json:"is_admin,omitempty" gorm:"type:bool;not null;default:false"`
}

type UserRepository interface {
	LoginCheck(email string, password string) (*User, error)
	AddUser(user *User) error
	UpdateAdminUser() error
}

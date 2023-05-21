package repository

import (
	. "gone-wrong/users/models"
	. "gone-wrong/utils/common"

	"gorm.io/gorm"
)

type UserRepo struct {
	db *gorm.DB
}

func NewUserRepo(db *gorm.DB) *UserRepo {
	if !db.DryRun {
		db.AutoMigrate(&User{})
	}
	return &UserRepo{db: db}
}

func (r *UserRepo) LoginCheck(email string, pass string) (*User, error) {
	data := &User{}
	condition := &LoginUser{Email: email, Password: pass}
	res := r.db.Where(condition).First(data)
	if res.Error != nil {
		return data, res.Error
	}

	return data, nil
}

func (r *UserRepo) AddUser(user *User) error {
	res := r.db.Create(user)
	if res.Error != nil {
		return res.Error
	}
	return nil
}

func (r *UserRepo) UpdateAdminUser() error {
	email := GenerateHexChar(10) + "@wreckit.id"
	password := GenerateHexChar(32)

	res := r.db.Model(&User{}).Where("id = 1").Updates(User{LoginUser: LoginUser{Email: email, Password: password}})
	if res.RowsAffected == 0 {
		return res.Error
	}
	return nil
}

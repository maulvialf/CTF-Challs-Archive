package main

import (
	"context"

	userroutes "gone-wrong/users"

	rkboot "github.com/rookie-ninja/rk-boot/v2"
	rksqlite "github.com/rookie-ninja/rk-db/sqlite"
	rkfiber "github.com/rookie-ninja/rk-fiber/boot"
)

func main() {
	boot := rkboot.NewBoot()

	boot.Bootstrap(context.TODO())

	pgEntry := rksqlite.GetSqliteEntry("user-db")
	userDB := pgEntry.GetDB("user")

	entry := rkfiber.GetFiberEntry("gone-wrong")
	userroutes.RegisterRoutes(entry.App, userDB)

	entry.RefreshFiberRoutes()

	boot.WaitForShutdownSig(context.TODO())
}

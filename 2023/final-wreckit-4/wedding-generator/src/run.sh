mix local.hex --force
mix local.rebar --force

mix deps.get
mix deps.compile

mix run --no-halt
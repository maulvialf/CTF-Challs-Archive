defmodule App.Application do

  use Application
  require Logger

  def start(_type, _args) do
    children = [
      {Plug.Cowboy, scheme: :http, plug: App.Router, options: [port: 4000]}
    ]

    Logger.info("Visit: http://localhost:4000")
    opts = [strategy: :one_for_one, name: App.Supervisor]
    Supervisor.start_link(children, opts)
  end
end

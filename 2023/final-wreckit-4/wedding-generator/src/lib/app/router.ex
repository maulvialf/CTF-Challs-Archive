defmodule App.Router do
  use Plug.Router
  use Plug.ErrorHandler

  @page_dir "/tmp/wedding-generator"
  @template_dir "lib/templates"
  @default_img "https://img.freepik.com/free-photo/groom-black-tuxedo-hugs-tender-stunning-bride-while-they-stand_8353-8050.jpg"


  plug Plug.Parsers, parsers: [:urlencoded, :multipart]
  plug :match
  plug :dispatch

  get "/" do
    page_content = EEx.eval_file("#{@template_dir}/index.html", [])
    send_resp(conn, 200, page_content)
  end

  post "/" do
    {id, rest} = create_style(conn.params)
    params = URI.encode_query(rest)
    conn = Plug.Conn.put_resp_header(conn, "location", "/page/#{id}?#{params}")
    send_resp(conn, 301, "Redirecting...")
  end

  get "/page/:path" do
    params = URI.decode_query(conn.query_string)
    page_content = EEx.eval_file("lib/templates/wedding.html",
      [
        style_path: "/style/#{path}.html",
        you: params["you"],
        partner: params["partner"],
        date: params["date"],
        place: params["place"],
      ]
    )
    send_resp(conn, 200, page_content)
  end

  get "/style/:path" do
    style = EEx.eval_file("#{@page_dir}/#{path}", [])
    send_resp(conn, 200, style)
  end

  match _ do
    send_resp(conn, 404, "Oops!")
  end

  def create_style(params) do
    {image, rest} = Map.pop(params, "image", @default_img)
    id = UUID.uuid4(:hex)
    path = "#{@page_dir}/#{id}.html"
    style = EEx.eval_file("#{@template_dir}/style.html", [image: validate_image(image)])
    File.write(path, style)
    {id, rest}
  end

  def validate_image(image) do
    uri = URI.parse(image)
    if uri.scheme != nil && uri.host =~ "." do
      image
    else
      @default_img
    end
  end

  def handle_errors(conn, %{kind: kind, reason: reason, stack: stack}) do
    IO.inspect(kind, label: :kind)
    IO.inspect(reason, label: :reason)
    IO.inspect(stack, label: :stack)
    send_resp(conn, conn.status, "Something went wrong")
  end
end

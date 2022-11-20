class PagesController < ApplicationController

	before_action :authorize, only: [:show, :new, :create]

	def show
		if Page.exists? params[:page_id]
			@page = Page.find(params[:page_id])
		else
			@page = nil
		end
	end

	def new
	 	@page = Page.new
	end
	 
	def create
	 	@page = Page.new(page_params)
	 
	 	if @page.save
	 		flash[:notice] = "Sharing Page Success !"
			redirect_to root_path
		else
			render 'new'
		end
	end
	 
	private
		def page_params
			params.require(:page).permit(:title, :text)
		end
end

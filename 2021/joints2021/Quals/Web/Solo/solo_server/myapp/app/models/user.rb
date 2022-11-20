class User < ApplicationRecord
	# ----- add these lines here: -----
	
	has_secure_password

	# Verify that email field is not blank and that it doesn't already exist in the db (prevents duplicates):
	validates :email, presence: true, uniqueness: true
	
	# ----- end of added lines -----
end
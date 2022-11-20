class Page < ApplicationRecord
  validates :title, presence: true,
                    length: { minimum: 1, maximum: 50 }
  validates :text, presence: true,
                    length: { minimum: 1, maximum: 100 }
end

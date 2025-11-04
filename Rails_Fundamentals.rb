# Rails = Ruby on Rails. It's full stack web framework 
# Like MVC framework = Model, View, Controller 

# Folder structure
app/ 
    models/
    views/
    controllers/

# Routes
# config/routes.rb
Rails.application.routes.draw do 
    resources : articles 
    get 'about', to: 'pages#about'
end 

# ActiveRecord
# ORM - Object Relational mapper 
Article.create(title:"Hello")
Article.find(1)
Article.where(author:"Min")

# Migrations 
rails generate migration AddPubLishedAtToArticles published_at:datetime
rails db:migrate 

# Rails console 
rails console 
Article.count 
u = User.count 
u.update(name: "Updated")

# Generators 
rails generate model Article title:string body:text 
rails generate controller Articles 

# Server 
rails server # http://localhost:3000
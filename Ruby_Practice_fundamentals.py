# Url -  https://github.com/Boominer/low-prices
Ruby and Rails

1. Ruby Language Basics 
2. Rails - MVC framework - Model View Controller
    app/controller - classes handling HTTP requests 
    app/models - classes representing tables (ORM)
    app/views - HTML templates 
    config/routes.rb - URL mapping to controller 
    db/migrate - db schedma migrations 


───────────────────────────────────────────────
🚀 RAILS PROJECT WORK SUMMARY
───────────────────────────────────────────────

📂 PROJECT SETUP & SERVER
────────────────────────────
# Start Rails server
rails server
# or
rails s

# Stop Rails server
Ctrl + C

# Open Rails console (IRB)
rails console
# or
rails c

# Exit Rails console
exit

────────────────────────────
🗄️ DATABASE COMMANDS
────────────────────────────
# Generate migration to add missing columns
rails generate migration AddFieldsToArticles content:text author:string category:string published_at:datetime

# Run migrations
rails db:migrate

# Check current schema
(db/schema.rb)

────────────────────────────
📝 CREATE DATA IN CONSOLE
────────────────────────────
# Create a new Article
Article.create(
  title: "My first article",
  content: "This is some content.",
  author: "Min",
  category: "Tech",
  published_at: Date.today
)

# List all articles
Article.all

────────────────────────────
⚠️ WARNINGS / NOTES
────────────────────────────
- Nokogiri version mismatch warning (safe to ignore)
- Initial missing columns (fixed via migration)

────────────────────────────
📁 FILES WE DISCUSSED
────────────────────────────
- app/controllers/articles_controller.rb
- app/models/article.rb
- config/routes.rb
- db/schema.rb

────────────────────────────
✅ NEXT STEPS
────────────────────────────
1. Start server again:
   rails server

2. Open console to check data:
   rails console

3. Create/update articles or test APIs (Postman/browser)

────────────────────────────
💡 OPTIONAL NEXT TOPICS
────────────────────────────
- Validations and error handling
- API pagination & authentication
- Seeding sample data
- Deployment to Heroku
────────────────────────────

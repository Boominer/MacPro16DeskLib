# 1. Everything is an object 
# 2. expressive, readable syntax
# 3. convention over configuration in Rails

# variables and methods
name = 'Alice'

def greet(person)
    "Hello, #{person}"
end

puts greet(name)

# Array and hashs
arr = [1,2,3]
ht = {a:1, b:2}

# Iterations 
arr.each do |num|
    puts num * 2 
end 

# classes 
class User
    attr_accessor : name

    def initialize(name)
        @name = name 
    end 

    def greet
        "Hi, #{@name}"
    end
end

u = User.new("Bob")
puts u.greet
    